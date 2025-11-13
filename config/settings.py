# warehouse_app/config/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# warehouse_app/config/settings.py
DB_HOST = "172.23.8.153"
DB_PORT = 5432
DB_NAME = "warehouse_db"
DB_USER = "postgres"
DB_PASS = "wsepc"

# ❌ KHÔNG thêm ?sslmode=disable
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = "host=172.23.8.153 dbname=warehouse_db user=postgres password=wsepc port=5432 sslmode=disable"
# print(DATABASE_URL)

# Đường dẫn ảnh (nếu vẫn dùng folder mạng)
IMAGES_USER = os.getenv(
    "WM_IMAGES_BASE", r"D:\Backup data all\Managementdata\Other\inventory_management_images_EOL")

# Table names/constants (giữ tương đồng với code cũ)
TABLE_INPUT = "inventory_entries"
TABLE_USERS = "users"
TABLE_TEAMS = "teams"
SOFTWARE_TITLE = "Warehouse Manager"

# Dùng như hằng số
DEFAULT_IMAGE = "default.jpg"
# === THÊM 2 DÒNG NÀY (BẮT BUỘC) ===
IMAGE_LABEL_SIZE = (200, 200)           # Kích thước hiển thị ảnh trong QLabel
DEFAULT_IMAGE_PATH = "resources/default_image.jpg"  # Đảm bảo file này tồn tại!
