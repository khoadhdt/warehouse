# warehouse_app/modules/ui/multiselect_dropdown.py
from typing import List
from PySide6.QtWidgets import (
    QWidget, QListWidget, QListWidgetItem, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout, QApplication
)
from PySide6.QtCore import Qt, QRect, QEvent
from PySide6.QtGui import QKeyEvent, QMouseEvent


# ====================== DANH SÁCH CHỌN NHIỀU ======================

class MultiSelectListWidget(QListWidget):
    """List hiển thị dropdown có thể chọn nhiều mục."""

    def __init__(self, parent=None, dropdown_widget=None):
        super().__init__(parent)
        self.dropdown_widget = dropdown_widget
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setSelectionMode(QListWidget.MultiSelection)
        self.itemClicked.connect(self.handle_item_clicked)

        self.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 2px;
                color: #1e3a8a;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:selected {
                background-color: #0078d4;
                color: white;
            }
        """)

    def handle_item_clicked(self, item: QListWidgetItem):
        """Cập nhật dropdown khi click item."""
        if self.dropdown_widget:
            self.dropdown_widget.update_selected_items()

    def leaveEvent(self, event: QEvent):
        """Tự ẩn list khi di chuột ra ngoài."""
        self.hide()
        super().leaveEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        """Hỗ trợ Enter và Esc."""
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.dropdown_widget.update_selected_items()
            self.hide()
        elif event.key() == Qt.Key_Escape:
            self.hide()
        else:
            super().keyPressEvent(event)


# ====================== DROPDOWN CHỌN NHIỀU ======================

class MultiSelectDropdown(QWidget):
    """Widget cho phép chọn nhiều mục với chip hiển thị."""

    def __init__(self, parent: QWidget, items: List[str], object_name: str):
        super().__init__(parent)
        self.parent = parent
        self.items = items
        self.object_name = object_name
        self.selected_items: List[str] = []
        self.init_ui()

    def init_ui(self):
        """Khởi tạo giao diện chính."""
        self.setObjectName(self.object_name)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(6, 6, 6, 6)
        self.main_layout.setSpacing(6)

        # Khu vực chứa chip
        self.chips_container = QWidget()
        self.chips_layout = QHBoxLayout(self.chips_container)
        self.chips_layout.setContentsMargins(0, 0, 0, 0)
        self.chips_layout.setSpacing(6)
        self.chips_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addWidget(self.chips_container)

        # Nút mở danh sách
        self.dropdown_button = QPushButton("▼")
        self.dropdown_button.setFixedSize(26, 28)
        self.dropdown_button.setStyleSheet("""
            QPushButton {
                border: 1px solid #d1d5db;
                background-color: #f3f4f6;
                border-radius: 6px;
                font-size: 14px;
                color: #374151;
            }
            QPushButton:hover { background-color: #e5e7eb; }
            QPushButton:pressed { background-color: #d1d5db; }
        """)
        self.dropdown_button.clicked.connect(self.toggle_list_widget)
        self.main_layout.addWidget(
            self.dropdown_button, alignment=Qt.AlignRight)

        # List hiển thị item
        self.list_widget = MultiSelectListWidget(self.parent, self)
        self.list_widget.addItems(self.items)
        self.list_widget.hide()

        self.setStyleSheet("""
            QWidget {
                border: 1px solid #d1d5db;
                background-color: #ffffff;
                border-radius: 6px;
                padding: 6px;
            }
            QWidget:focus {
                border: 2px solid #3b82f6;
            }
        """)
        self.setFocusPolicy(Qt.StrongFocus)

    # --------------------------------------------------
    def toggle_list_widget(self):
        """Mở hoặc đóng danh sách."""
        if self.list_widget.isVisible():
            self.list_widget.hide()
        else:
            self.load_items()
            pos = self.mapToGlobal(self.rect().bottomLeft())
            self.list_widget.setGeometry(
                QRect(pos.x(), pos.y(), self.width(),
                      min(220, len(self.items) * 32))
            )
            self.list_widget.show()
            self.list_widget.setFocus()

    def load_items(self):
        """Tải lại danh sách và chọn lại item cũ."""
        self.list_widget.clear()
        self.list_widget.addItems(self.items)
        for i in range(self.list_widget.count()):
            if self.list_widget.item(i).text() in self.selected_items:
                self.list_widget.item(i).setSelected(True)

    def update_selected_items(self):
        """Cập nhật chip khi người dùng chọn."""
        self.selected_items = [i.text()
                               for i in self.list_widget.selectedItems()]
        self.update_chips()

    def update_chips(self):
        """Tạo lại các chip hiển thị."""
        # Xóa chip cũ
        while self.chips_layout.count() > 0:
            item = self.chips_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Tạo chip mới
        for item_text in self.selected_items:
            chip_widget = QWidget()
            chip_layout = QHBoxLayout(chip_widget)
            chip_layout.setContentsMargins(4, 2, 4, 2)
            chip_layout.setSpacing(4)

            chip_label = QLabel(item_text)
            chip_label.setStyleSheet("""
                QLabel {
                    background-color: #dbeafe;
                    color: #1e3a8a;
                    border-radius: 12px;
                    padding: 4px 8px;
                    font-size: 13px;
                    font-weight: 500;
                }
            """)
            chip_layout.addWidget(chip_label)

            remove_btn = QPushButton("✕")
            remove_btn.setFixedSize(20, 20)
            remove_btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-color: #ef4444;
                    color: white;
                    border-radius: 10px;
                    font-size: 12px;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #dc2626; }
                QPushButton:pressed { background-color: #b91c1c; }
            """)
            remove_btn.clicked.connect(
                lambda _, t=item_text: self.remove_item(t))
            chip_layout.addWidget(remove_btn)

            self.chips_layout.addWidget(chip_widget)

        self.chips_layout.addStretch()

    def remove_item(self, text: str):
        """Xóa item khỏi danh sách chọn."""
        for i in range(self.list_widget.count()):
            if self.list_widget.item(i).text() == text:
                self.list_widget.item(i).setSelected(False)
        self.update_selected_items()

    # --------------------------------------------------
    def get_selected_items(self) -> List[str]:
        """Lấy danh sách item đã chọn."""
        return self.selected_items

    def set_selected_items(self, items: List[str]):
        """Thiết lập danh sách đã chọn."""
        self.selected_items = [i for i in items if i in self.items]
        self.load_items()
        self.update_chips()

    def mousePressEvent(self, event: QMouseEvent):
        if self.list_widget.isVisible() and not self.list_widget.geometry().contains(event.globalPos()):
            self.list_widget.hide()
        super().mousePressEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Down:
            self.toggle_list_widget()
        super().keyPressEvent(event)
