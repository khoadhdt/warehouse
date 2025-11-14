# warehouse_app/modules/ui/main_window.py
from PySide6.QtWidgets import QMainWindow, QStatusBar, QPushButton, QMessageBox, QInputDialog, QHBoxLayout, QWidget, QLabel, QTabWidget
from PySide6.QtGui import QPixmap, QDesktopServices, QImage, QGuiApplication, QPainter, QColor, QPen, QMouseEvent, QKeyEvent
from PySide6.QtCore import QStringListModel, Qt, QThread, QTimer, QUrl, QObject, QEvent
from ui.screen_InventoryManager import Ui_MainWindow
from modules.ui.input_tab import InputTabController
from modules.ui.output_tab import OutputTabController
from modules.ui.inventory_tab import InventoryTabController
from db.database import DatabaseHandler
from config.settings import SOFTWARE_TITLE
import os
from config.global_vars import get_folders
import subprocess
import asyncio
from modules.options import get_all_categories  # ← Đảm bảo import

_OPTIONS_CACHE: dict = {}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_info: dict):
        super().__init__()
        self.setupUi(self)

        self.image_folder, self.invoice_folder = get_folders()  # ← LẤY MỚI NHẤT

        self.user_info = user_info

        username = user_info.get("username", "")
        role = user_info.get("role", "")
        team_display = user_info.get("team_display_name", "")
        self.setWindowTitle(f"{SOFTWARE_TITLE}")

        # === 1. LABEL USER INFO BÊN TRÁI ===
        user_label = QLabel(f"User: {username} | Team: {team_display}")
        user_label.setStyleSheet("color: #555; padding: 0 10px;")
        self.statusBar.addWidget(user_label)  # ← TRÁI

        # === 2. TẠO BUTTON BÊN PHẢI ===
        btn_open_invoice = QPushButton("Mở Invoice")
        btn_open_invoice.setFixedSize(100, 22)
        btn_open_invoice.clicked.connect(self.open_invoice)  # ← GỌI HÀM

        # Tạo widget chứa button + layout
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addStretch()
        layout.addWidget(btn_open_invoice)
        layout.setContentsMargins(0, 0, 10, 0)

        self.statusBar.addPermanentWidget(btn_open_invoice)  # ← PHẢI

        # === 3. TẠO LABEL ZOOM ẢNH Ở GIỮA MÀN HÌNH ===
        # centralwidget là widget trung tâm
        self.images_zoom_label = QLabel(self.centralwidget)
        self.images_zoom_label.setObjectName("images_zoom_label")
        self.images_zoom_label.setAlignment(Qt.AlignCenter)
        self.images_zoom_label.setScaledContents(True)  # Tự động co giãn ảnh
        self.images_zoom_label.setMinimumSize(300, 300)
        self.images_zoom_label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid #3B82F6;
                border-radius: 10px;
                padding: 6px;
            }
        """)
        # self.images_zoom_label.hide()  # Ẩn ban đầu

        # === 2. ẨN TAB THEO ROLE ===
        tab_widget: QTabWidget = self.tabWidget_main  # ← tên tabWidget trong .ui

        # Danh sách tab hiển thị theo role
        role_tabs = {
            "admin":   [0, 1, 2, 3, 4, 5, 6, 7, 8],     # Tất cả
            "manager": [1, 2, 5, 6],                # Chỉ 1,2,5,6
            "user":    [1, 5, 6],                  # Chỉ 1,5,6
            "viewer":  [5, 6],                    # Chỉ 5,6
        }

        allowed_tabs = role_tabs.get(role, [5, 6])  # mặc định viewer
        for i in range(tab_widget.count()):
            if i not in allowed_tabs:
                tab_widget.setTabVisible(i, False)  # ẨN TAB
            else:
                tab_widget.setTabVisible(i, True)   # HIỆN TAB

        db_handler = DatabaseHandler()

        team_id = user_info.get("team_id")
        user_id = user_info.get("id")

        # === LOAD OPTIONS 1 LẦN DUY NHẤT ===
        try:
            loop = asyncio.get_event_loop()
            self.options = loop.run_until_complete(
                self.load_categories_once(team_id))
        except Exception as e:
            print(f"[ERROR] Không thể load options: {e}")
            self.options = {}

        # === KHỞI TẠO INPUT TAB VỚI OPTIONS ===
        self.input_tab_controller = InputTabController(
            ui=self,
            team_id=team_id,
            user_id=user_id,
            username=username,
            db_handler=DatabaseHandler(),
            options=self.options  # ← TRUYỀN VÀO
        )
        self.input_tab_controller.search_items()

        # TẠO OUTPUT TAB VỚI THAM CHIẾU INPUT
        # self.output_tab_controller = OutputTabController(
        #     ui=self,
        #     team_id=team_id,
        #     user_id=user_id,
        #     username=username,
        #     db_handler=db_handler,
        #     input_controller=self.input_tab_controller  # ← TRUYỀN QUA
        # )
        # self.output_tab_controller.load_output_table()

        # TẠO INVENTORY
        # self.inventory_controller = InventoryTabController(
        #     ui=self,
        #     team_id=team_id,
        #     user_id=user_id,
        #     username=username,
        #     db_handler=db_handler
        # )
    # MỞ INVOICE TỪ invoice_folder
    # =========================================================

    def open_invoice(self):
        clipboard = QGuiApplication.clipboard()
        copied_text = clipboard.text().strip()

        if not copied_text:
            QMessageBox.warning(
                self, "Lỗi", "Không có dữ liệu trong clipboard!")
            return

        # Bước 2: Xử lý chuỗi bằng CAT_CHUOI_INVOICE
        invoice_name = self.cat_chuoi_invoice(copied_text)

        # Bước 3: Tạo đường dẫn file
        file_path = os.path.join(self.invoice_folder, f"{invoice_name}.xlsx")
        print("Đường dẫn thử:", file_path)

        # Bước 4: Kiểm tra tồn tại
        if not os.path.exists(file_path):
            # Hiển thị hộp thoại nhập nếu file từ clipboard không tồn tại
            text, ok = QInputDialog.getText(self, "Nhập tên hóa đơn",
                                            f"Không tìm thấy file: {invoice_name}.xlsx\nVui lòng nhập tên khác:")
            if ok and text.strip():
                invoice_name = self.cat_chuoi_invoice(text.strip())
                file_path = os.path.join(
                    self.link_invoice, f"{invoice_name}.xlsx")
            else:
                return  # Người dùng hủy

        # Bước 5: Mở file nếu tồn tại
        if os.path.exists(file_path):
            # self.load_invoice_data(file_path)
            subprocess.Popen(['start', '', file_path], shell=True)
        else:
            QMessageBox.warning(self, "Không tìm thấy",
                                f"Không tìm thấy file invoice chi tiết: {invoice_name}")

    def cat_chuoi_invoice(self, text: str) -> str:
        # Bước 1: Chuẩn hóa các dấu gạch
        text = text.replace("\u2010", "-").replace("\u2013",
                                                   "-").replace("\u2014", "-").strip()

        # Bước 2: Nếu có dấu "_", xử lý theo phần sau
        if "_" in text:
            parts = text.split("_")
            # Ưu tiên tìm phần bắt đầu bằng "CBW"
            for part in parts:
                if part.upper().startswith("CBW"):
                    return part.strip()
            # Nếu không có phần bắt đầu bằng CBW, trả về phần cuối cùng
            return parts[-1].strip()

        # Bước 3: Nếu không có dấu "_", lấy chuỗi trước dấu "-" cuối cùng
        dash_pos = text.rfind("-")
        if dash_pos > 0:
            return text[:dash_pos].strip()

        # Bước 4: Trường hợp không có "-" hoặc "_", trả về nguyên chuỗi đã được strip
        return text.strip()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'images_zoom_label'):
            # Căn giữa label theo centralwidget
            self.center_zoom_label()

    def center_zoom_label(self):
        if not self.images_zoom_label.isVisible():
            return
        rect = self.centralwidget.geometry()
        label_size = self.images_zoom_label.sizeHint()
        x = (rect.width() - label_size.width()) // 2
        y = (rect.height() - label_size.height()) // 2
        self.images_zoom_label.move(x, y)

    def show_zoomed_image(self, image_path: str):
        if not os.path.exists(image_path):
            return

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            return

        # Tính kích thước tối đa (80% màn hình)
        max_size = self.centralwidget.size() * 0.8
        scaled_pixmap = pixmap.scaled(
            max_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        self.images_zoom_label.setPixmap(scaled_pixmap)
        self.images_zoom_label.resize(scaled_pixmap.size())
        self.images_zoom_label.show()
        self.center_zoom_label()

        # Click để đóng
        self.images_zoom_label.mousePressEvent = lambda e: self.hide_zoomed_image()

    def hide_zoomed_image(self):
        self.images_zoom_label.hide()
        self.images_zoom_label.clear()

    async def load_categories_once(self, team_id: int):
        """Chỉ query DB 1 lần duy nhất cho mỗi team"""
        global _OPTIONS_CACHE
        if team_id not in _OPTIONS_CACHE:
            try:
                _OPTIONS_CACHE[team_id] = await get_all_categories(team_id)
            except Exception as e:
                print(f"[ERROR] load_categories_once: {e}")
                _OPTIONS_CACHE[team_id] = {}
        return _OPTIONS_CACHE[team_id]
