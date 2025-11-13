-- XÓA CÁC OBJECT CŨ (AN TOÀN)
DROP VIEW IF EXISTS v_components_full;
DROP TABLE IF EXISTS audit_log             CASCADE;
DROP TABLE IF EXISTS inventory_entries     CASCADE;
DROP TABLE IF EXISTS options               CASCADE;
DROP TABLE IF EXISTS teams                CASCADE;
DROP TABLE IF EXISTS users					CASCADE;
DROP MATERIALIZED VIEW IF EXISTS current_stock;

-- Tạo extension (idempotent)
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;

-- Tạo hàm IMMUTABLE wrapper cho unaccent + text
CREATE OR REPLACE FUNCTION immutable_unaccent(text) 
RETURNS text AS $$
BEGIN
    RETURN unaccent($1);
EXCEPTION WHEN OTHERS THEN
    RETURN $1;  -- fallback nếu lỗi
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Hàm tạo search_vector (gọi từ trigger)
CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
DECLARE
    -- Dùng để nối các giá trị mảng thành chuỗi (nếu có)
    process_text TEXT;
    model_text TEXT;
    material_text TEXT;
    group_text TEXT;
BEGIN
    -- Xử lý các cột mảng: ghép phần tử mảng thành chuỗi cách nhau bởi dấu cách
    process_text := array_to_string(NEW.process, ' ');
    model_text := array_to_string(NEW.model, ' ');
    material_text := array_to_string(NEW.material, ' ');
    group_text := array_to_string(NEW.group_name, ' ');

    -- Tạo search_vector với đầy đủ các trường
    NEW.search_vector := to_tsvector('simple',
        COALESCE(immutable_unaccent(NEW.component_id), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.component_name), '') || ' ' ||
        COALESCE(immutable_unaccent(group_text), '') || ' ' ||
        COALESCE(immutable_unaccent(process_text), '') || ' ' ||
        COALESCE(immutable_unaccent(model_text), '') || ' ' ||
        COALESCE(immutable_unaccent(material_text), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.storage_location), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.invoice), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.modinvoice), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.status), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.note), '')
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Tạo bảng teams
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'teams') THEN
        CREATE TABLE teams (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL,           -- EOL, FOL, TEST, SMT
            display_name VARCHAR(100),                  -- Tên hiển thị
            image_folder TEXT NOT NULL,                 -- Đường dẫn ảnh linh kiện
            invoice_folder TEXT NOT NULL,               -- Đường dẫn invoice
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    END IF;
END $$;

-- Index
CREATE INDEX IF NOT EXISTS idx_teams_name ON teams(name);
CREATE INDEX IF NOT EXISTS idx_teams_active ON teams(is_active);

-- Tạo dữ liệu nhóm
INSERT INTO teams (name, display_name, image_folder, invoice_folder) VALUES
('EOL', 'End of Line', 
 $$\\172.23.10.230\map-eng\8. BAO CAO THIET BI EOL\2.SOFTWARE\Data\Images_EOL$$,
 $$\\172.23.10.230\map-eng\8. BAO CAO THIET BI EOL\2.SOFTWARE\Data\Invoices_EOL$$),

('FOL', 'First of Line', 
 $$\\172.23.10.230\map-eng\FOL\Images_FOL$$,
 $$\\172.23.10.230\map-eng\FOL\Invoices_FOL$$)

ON CONFLICT (name) DO NOTHING;

-- Hàm lấy đường dẫn folder hình ảnh và invoice theo tên team
CREATE OR REPLACE FUNCTION get_team_folders(team_name TEXT)
RETURNS TABLE (
    image_folder TEXT,
    invoice_folder TEXT
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        t.image_folder,
        t.invoice_folder
    FROM teams t
    WHERE LOWER(t.name) = LOWER(team_name)
      AND t.is_active = TRUE
    LIMIT 1;
END;
$$ LANGUAGE plpgsql STABLE;



-- Tạo bảng users (đã đồng bộ với code Python)
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'users') THEN
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(255),
            password VARCHAR(255) NOT NULL,  -- Đổi từ password_hash → password
            role VARCHAR(20) NOT NULL DEFAULT 'viewer'
                CHECK (role IN ('admin', 'manager', 'user', 'viewer')),
            team_id INTEGER REFERENCES teams(id) ON DELETE SET NULL,  -- THÊM: nhóm (EOL, FOL,...)
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMPTZ
        );
    END IF;
END $$;

-- Index cho tìm kiếm nhanh
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'idx_users_username') THEN
        CREATE INDEX idx_users_username ON users(username);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'idx_users_role') THEN
        CREATE INDEX idx_users_role ON users(role);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'idx_users_team') THEN
        CREATE INDEX idx_users_team ON users(team_id);
    END IF;
END $$;


-- Tạo bảng options (DANH SÁCH GỢI Ý THEO NHÓM) – ĐÃ SỬA TỐI ƯU
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'options') THEN
        CREATE TABLE options (
            id SERIAL PRIMARY KEY,
            team_id INTEGER NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
            category VARCHAR(50) NOT NULL,
            value TEXT NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            created_by INTEGER REFERENCES users(id),
            updated_at TIMESTAMPTZ,
            updated_by INTEGER REFERENCES users(id),
            UNIQUE(team_id, category, value)
        );
    END IF;
END $$;

-- Index hiệu suất cao
DROP INDEX IF EXISTS idx_options_team_category;
CREATE INDEX idx_options_team_category ON options(team_id, category) WHERE is_active = TRUE;

-- Hàm lấy tất cả list theo team
CREATE OR REPLACE FUNCTION get_all_team_options(team_name TEXT)
RETURNS JSONB AS $$
DECLARE
    team_id INT;
    result JSONB;
BEGIN
    SELECT id INTO team_id
    FROM teams
    WHERE LOWER(name) = LOWER(team_name)
      AND is_active = TRUE
    LIMIT 1;

    IF team_id IS NULL THEN
        RETURN '{}'::JSONB;
    END IF;

    SELECT jsonb_build_object(
        'group_name', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='groups'), '{}'),
        'process', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='process'), '{}'),
        'model', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='model'), '{}'),
        'unit', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='unit'), '{}'),
        'material', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='material'), '{}'),
        'status', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='status'), '{}'),
        'storage_location', COALESCE(ARRAY_AGG(value) FILTER (WHERE category='storage_location'), '{}')
    )
    INTO result
    FROM options
    WHERE team_id = team_id
      AND is_active = TRUE;

    RETURN result;
END;
$$ LANGUAGE plpgsql STABLE;


-- Tạo bảng inventory_entries + cột search_vector (thường)
DO $$ 
BEGIN
    CREATE TABLE IF NOT EXISTS inventory_entries (
        id BIGSERIAL PRIMARY KEY,
        component_id VARCHAR(100) NOT NULL,
        component_name TEXT NOT NULL,
        group_name TEXT[] DEFAULT '{}',
        process TEXT[] DEFAULT '{}',
        model TEXT[] DEFAULT '{}',
        size TEXT,
        unit TEXT,
        team_id INTEGER NOT NULL REFERENCES teams(id),
        material TEXT[] DEFAULT '{}',
        storage_location TEXT,
        invoice TEXT,
        modinvoice TEXT,
        status TEXT,
        note TEXT,
        quantity NUMERIC(12, 3) NOT NULL CHECK (quantity > 0),
        movement_type VARCHAR(20) NOT NULL DEFAULT 'adjustment'
            CHECK (movement_type IN ('in', 'out', 'adjustment')),
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        created_by INTEGER NOT NULL REFERENCES users(id),
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_by INTEGER REFERENCES users(id),
        search_vector TSVECTOR
    );
END $$;

-- Trigger cập nhật search_vector
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_trigger WHERE tgname = 'trig_update_search_vector') THEN
        CREATE TRIGGER trig_update_search_vector
        BEFORE INSERT OR UPDATE ON inventory_entries
        FOR EACH ROW EXECUTE FUNCTION update_search_vector();
    END IF;
END $$;

-- Tạo bảng audit_log
DO $$ 
BEGIN
    CREATE TABLE IF NOT EXISTS audit_log (
        id BIGSERIAL PRIMARY KEY,
        table_name TEXT NOT NULL,
        record_id BIGINT,
        action TEXT NOT NULL CHECK (action IN ('I', 'U', 'D')),
        old_row_data JSONB,
        new_row_data JSONB,
        changed_by INTEGER REFERENCES users(id),
        changed_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
END $$;

-- Index audit_log
DO $$ BEGIN CREATE INDEX IF NOT EXISTS idx_audit_changed_by ON audit_log(changed_by); EXCEPTION WHEN OTHERS THEN END $$;
DO $$ BEGIN CREATE INDEX IF NOT EXISTS idx_audit_changed_at ON audit_log(changed_at DESC); EXCEPTION WHEN OTHERS THEN END $$;

-- === TẠO INDEXES (CONCURRENTLY + FALLBACK) ===
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_component_id ON inventory_entries(component_id); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_component_id ON inventory_entries(component_id); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_team_id ON inventory_entries(team_id); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_team_id ON inventory_entries(team_id); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_movement_type ON inventory_entries(movement_type); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_movement_type ON inventory_entries(movement_type); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_status ON inventory_entries(status); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_status ON inventory_entries(status); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_created_at ON inventory_entries(created_at DESC); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_created_at ON inventory_entries(created_at DESC); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_created_by ON inventory_entries(created_by); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_created_by ON inventory_entries(created_by); END $$;

-- GIN cho array
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_group_gin ON inventory_entries USING GIN(group_name); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_group_gin ON inventory_entries USING GIN(group_name); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_process_gin ON inventory_entries USING GIN(process); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_process_gin ON inventory_entries USING GIN(process); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_material_gin ON inventory_entries USING GIN(material); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_material_gin ON inventory_entries USING GIN(material); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_model_gin ON inventory_entries USING GIN(model); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_model_gin ON inventory_entries USING GIN(model); END $$;


-- Trigram cho autocomplete
DO $$
BEGIN
    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_name_trgm ON inventory_entries USING GIN(component_name gin_trgm_ops);
EXCEPTION WHEN OTHERS THEN
    CREATE INDEX IF NOT EXISTS idx_entries_name_trgm ON inventory_entries USING GIN(component_name gin_trgm_ops);
END $$;
-- Trigram cho component_id (hỗ trợ tìm kiếm nhanh theo mã linh kiện)
DO $$
BEGIN
    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_component_id_trgm
    ON inventory_entries USING GIN(component_id gin_trgm_ops);
EXCEPTION WHEN OTHERS THEN
    CREATE INDEX IF NOT EXISTS idx_entries_component_id_trgm
    ON inventory_entries USING GIN(component_id gin_trgm_ops);
END $$;


-- Full-text search
DO $$
BEGIN
    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_search_gin ON inventory_entries USING GIN(search_vector);
EXCEPTION WHEN OTHERS THEN
    CREATE INDEX IF NOT EXISTS idx_entries_search_gin ON inventory_entries USING GIN(search_vector);
END $$;

-- Composite
DO $$
BEGIN
    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_stock_query ON inventory_entries (team_id, component_id, created_at);
EXCEPTION WHEN OTHERS THEN
    CREATE INDEX IF NOT EXISTS idx_entries_stock_query ON inventory_entries (team_id, component_id, created_at);
END $$;

-- === MATERIALIZED VIEW current_stock ===
CREATE MATERIALIZED VIEW IF NOT EXISTS current_stock AS
WITH latest_attrs AS (
    SELECT DISTINCT ON (component_id)
        component_id, component_name, group_name, process, model, size, unit,
        team_id, material, storage_location, invoice, modinvoice, status, note,
        created_by, created_at
    FROM inventory_entries
    ORDER BY component_id, created_at DESC
)
SELECT 
    la.*,
    COALESCE(SUM(CASE WHEN ie.movement_type = 'out' THEN -ie.quantity ELSE ie.quantity END), 0) AS current_quantity
FROM latest_attrs la
JOIN inventory_entries ie ON ie.component_id = la.component_id
GROUP BY la.component_id, la.component_name, la.group_name, la.process, 
         la.model, la.size, la.unit, la.team_id, la.material, la.storage_location,
         la.invoice, la.modinvoice, la.status, la.note, la.created_by, la.created_at
HAVING SUM(CASE WHEN ie.movement_type = 'out' THEN -ie.quantity ELSE ie.quantity END) > 0;

-- ✅ BẮT BUỘC: tạo unique index để có thể REFRESH CONCURRENTLY
-- (chỉ gọi 1 lần, dùng CONCURRENTLY + IF NOT EXISTS)
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_current_stock_unique
ON current_stock (team_id, component_id);

-- Xoa bang options va reset id
TRUNCATE TABLE inventory_entries RESTART IDENTITY CASCADE;
TRUNCATE TABLE audit_log RESTART IDENTITY CASCADE;
TRUNCATE TABLE teams RESTART IDENTITY CASCADE;
TRUNCATE TABLE options RESTART IDENTITY CASCADE;
TRUNCATE TABLE users RESTART IDENTITY CASCADE;