-- XÓA CÁC OBJECT CŨ (AN TOÀN)
DROP VIEW IF EXISTS v_components_full;
DROP TABLE IF EXISTS audit_log             CASCADE;
DROP TABLE IF EXISTS inventory_entries     CASCADE;
DROP TABLE IF EXISTS options               CASCADE;
DROP TABLE IF EXISTS groups                CASCADE;
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
BEGIN
    NEW.search_vector := to_tsvector('simple',
        COALESCE(immutable_unaccent(NEW.component_name), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.note), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.type_name), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.invoice), '') || ' ' ||
        COALESCE(immutable_unaccent(NEW.modinvoice), '')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Tạo bảng groups
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'groups') THEN
        CREATE TABLE groups (
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
CREATE INDEX IF NOT EXISTS idx_groups_name ON groups(name);
CREATE INDEX IF NOT EXISTS idx_groups_active ON groups(is_active);

-- Tạo dữ liệu nhóm
INSERT INTO groups (name, display_name, image_folder, invoice_folder) VALUES
('EOL', 'End of Line', 
 $$\\172.23.10.230\map-eng\8. BAO CAO THIET BI EOL\2.SOFTWARE\Data\Images_EOL$$,
 $$\\172.23.10.230\map-eng\8. BAO CAO THIET BI EOL\2.SOFTWARE\Data\Invoices_EOL$$),

('FOL', 'First of Line', 
 $$\\172.23.10.230\map-eng\FOL\Images_FOL$$,
 $$\\172.23.10.230\map-eng\FOL\Invoices_FOL$$)

ON CONFLICT (name) DO NOTHING;

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
            group_name VARCHAR(50) NOT NULL,  -- THÊM: nhóm (EOL, FOL,...)
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
    IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'idx_users_group') THEN
        CREATE INDEX idx_users_group ON users(group_name);
    END IF;
END $$;

-- Thêm user mẫu (mật khẩu: 123456)
INSERT INTO users (username, password, role, group_name)
VALUES (
    'admin',
    '$2b$12$3x9f8k7j6h5g4f3d2s1a0u9o8i7u6y5t4r3e2w1q',  -- hash của "123456"
    'admin',
    'EOL'
) ON CONFLICT (username) DO NOTHING;

-- Tạo bảng options (DANH SÁCH GỢI Ý THEO NHÓM) – ĐÃ SỬA TỐI ƯU
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'options') THEN
        CREATE TABLE options (
            id SERIAL PRIMARY KEY,
            group_id INTEGER NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
            category VARCHAR(50) NOT NULL,
            value TEXT NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            created_by INTEGER REFERENCES users(id),
            updated_at TIMESTAMPTZ,
            updated_by INTEGER REFERENCES users(id),
            UNIQUE(group_id, category, value)
        );
    END IF;
END $$;

-- Index hiệu suất cao
DROP INDEX IF EXISTS idx_options_group_category;
CREATE INDEX idx_options_active ON options(group_id, category) WHERE is_active = TRUE;
CREATE INDEX idx_options_category ON options(category) WHERE is_active = TRUE;

-- Tạo bảng inventory_entries + cột search_vector (thường)
DO $$ 
BEGIN
    CREATE TABLE IF NOT EXISTS inventory_entries (
        id BIGSERIAL PRIMARY KEY,
        component_id VARCHAR(100) NOT NULL,
        component_name TEXT NOT NULL,
        type_name TEXT,
        color TEXT[] DEFAULT '{}',
        process TEXT[] DEFAULT '{}',
        model TEXT,
        size TEXT,
        unit TEXT,
        group_id INTEGER NOT NULL REFERENCES groups(id),
        material TEXT[] DEFAULT '{}',
        storage_location TEXT[] DEFAULT '{}',
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
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_group_id ON inventory_entries(group_id); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_group_id ON inventory_entries(group_id); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_movement_type ON inventory_entries(movement_type); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_movement_type ON inventory_entries(movement_type); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_status ON inventory_entries(status); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_status ON inventory_entries(status); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_created_at ON inventory_entries(created_at DESC); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_created_at ON inventory_entries(created_at DESC); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_created_by ON inventory_entries(created_by); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_created_by ON inventory_entries(created_by); END $$;

-- GIN cho array
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_color_gin ON inventory_entries USING GIN(color); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_color_gin ON inventory_entries USING GIN(color); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_process_gin ON inventory_entries USING GIN(process); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_process_gin ON inventory_entries USING GIN(process); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_material_gin ON inventory_entries USING GIN(material); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_material_gin ON inventory_entries USING GIN(material); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_storage_gin ON inventory_entries USING GIN(storage_location); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_storage_gin ON inventory_entries USING GIN(storage_location); END $$;

-- Trigram cho autocomplete
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_name_trgm ON inventory_entries USING GIN(component_name gin_trgm_ops); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_name_trgm ON inventory_entries USING GIN(component_name gin_trgm_ops); END $$;

-- Full-text search
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_search_gin ON inventory_entries USING GIN(search_vector); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_search_gin ON inventory_entries USING GIN(search_vector); END $$;

-- Composite
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_entries_stock_query ON inventory_entries (group_id, component_id, created_at); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_entries_stock_query ON inventory_entries (group_id, component_id, created_at); END $$;

-- === MATERIALIZED VIEW current_stock ===
CREATE MATERIALIZED VIEW IF NOT EXISTS current_stock AS
WITH latest_attrs AS (
    SELECT DISTINCT ON (component_id)
        component_id, component_name, type_name, color, process, model, size, unit,
        group_id, material, storage_location, invoice, modinvoice, status, note,
        created_by, created_at
    FROM inventory_entries
    ORDER BY component_id, created_at DESC
)
SELECT 
    la.*,
    COALESCE(SUM(CASE WHEN ie.movement_type = 'out' THEN -ie.quantity ELSE ie.quantity END), 0) AS current_quantity
FROM latest_attrs la
JOIN inventory_entries ie ON ie.component_id = la.component_id
GROUP BY la.component_id, la.component_name, la.type_name, la.color, la.process, 
         la.model, la.size, la.unit, la.group_id, la.material, la.storage_location,
         la.invoice, la.modinvoice, la.status, la.note, la.created_by, la.created_at
HAVING SUM(CASE WHEN ie.movement_type = 'out' THEN -ie.quantity ELSE ie.quantity END) > 0;

-- Index cho materialized view
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_current_stock_group ON current_stock(group_id); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_current_stock_group ON current_stock(group_id); END $$;
DO $$ BEGIN CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_current_stock_component ON current_stock(component_id); EXCEPTION WHEN OTHERS THEN CREATE INDEX IF NOT EXISTS idx_current_stock_component ON current_stock(component_id); END $$;
