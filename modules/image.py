# warehouse_app/modules/image.py
import os
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Qt
from config.settings import IMAGE_LABEL_SIZE, DEFAULT_IMAGE_PATH
from config.global_vars import get_folders  # ← DÙNG CHUNG

# Cache ảnh
_image_cache = {}


class ImageLoader(QThread):
    finished = Signal(str, QPixmap)

    def __init__(self, image_path, size=IMAGE_LABEL_SIZE, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.size = size

    def run(self):
        try:
            if not os.path.isfile(self.image_path):
                raise FileNotFoundError()

            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():
                raise ValueError("Invalid image")

            scaled = pixmap.scaled(
                *self.size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.finished.emit(self.image_path, scaled)

        except Exception:
            # ẨN LỖI "KHÔNG TÌM THẤY" → DÙNG DEFAULT
            default = QPixmap(DEFAULT_IMAGE_PATH)
            if default.isNull():
                default = QPixmap(*self.size)
                default.fill(Qt.lightGray)
            scaled = default.scaled(
                *self.size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.finished.emit(self.image_path, scaled)


def display_image_async(component_id: str, label, size=IMAGE_LABEL_SIZE):
    """
    CHỈ DÙNG component_id → TẤT CẢ ẢNH NẰM CHUNG image_folder
    """
    if not component_id:
        label.clear()
        return

    image_folder, _ = get_folders()  # ← LẤY TỪ CẤU HÌNH
    image_path = os.path.join(image_folder, f"{component_id}.jpg")

    # Cache
    if image_path in _image_cache:
        label.setPixmap(_image_cache[image_path])
        return

    # Hủy loader cũ
    if hasattr(label, 'current_loader') and label.current_loader:
        old = label.current_loader
        if old.isRunning():
            old.quit()
            old.wait(1000)
        old.deleteLater()

    # Tải mới
    loader = ImageLoader(image_path, size=size)
    label.current_loader = loader

    def on_finished(path, pixmap):
        if not pixmap.isNull():
            _image_cache[path] = pixmap
            label.setPixmap(pixmap)
        if hasattr(label, 'current_loader') and label.current_loader == loader:
            label.current_loader = None
        loader.deleteLater()

    loader.finished.connect(on_finished)
    loader.start()
