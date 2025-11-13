# warehouse_app/modules/image_hover_preview.py
from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PySide6.QtGui import QPixmap, QWheelEvent, QImage
from PySide6.QtCore import Qt, QPropertyAnimation, Signal, QObject
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL)  # ← TẮT TẤT CẢ LOG TRONG TOÀN BỘ APP


class ImageHoverController(QObject):
    """
    Controller trung gian để điều khiển HoverPreviewLabel từ bên ngoài
    (ví dụ: khi chọn dòng trong bảng)
    """
    image_changed = Signal(str)  # Phát tín hiệu khi ảnh mới được chọn


class HoverPreviewLabel(QLabel):
    """
    Hiển thị ảnh nhỏ + zoom lớn khi hover, hỗ trợ:
    - Tải ảnh từ path
    - Cập nhật ảnh khi chọn dòng mới (qua signal)
    - Zoom bằng bánh xe
    - Hiệu ứng fade in/out
    """

    def __init__(self, parent=None, controller: ImageHoverController = None):
        super().__init__(parent)
        logger.debug("[HoverPreviewLabel] __init__ called")
        self.setMouseTracking(True)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(80, 80)
        self.setMaximumSize(300, 300)
        self.setStyleSheet("border: 1px solid #ccc; background: #f0f0f0;")

        self.image_path = None
        self.original_image = None
        self.controller = controller or ImageHoverController()

        # ZOOM LABEL
        self.zoom_label = QLabel(parent)
        self.zoom_label.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        self.zoom_label.setAttribute(Qt.WA_TranslucentBackground)
        self.zoom_label.setAttribute(
            Qt.WA_StyledBackground, True)  # ← BẬT STYLE
        self.zoom_label.setAlignment(Qt.AlignCenter)
        self.zoom_label.setStyleSheet("""
            background-color: rgba(15, 15, 15, 240);
            border: 3px solid #3B82F6;
            border-radius: 14px;
            padding: 10px;
        """)
        self.zoom_label.hide()
        logger.debug(
            f"[HoverPreviewLabel] zoom_label created, visible: {self.zoom_label.isVisible()}")

        # Zoom config
        self.base_size = (600, 600)
        self.current_scale = 1.0
        self.min_scale = 0.5
        self.max_scale = 5.0

        self.setScaledContents(False)
        self.setAlignment(Qt.AlignCenter)

        # Kết nối signal từ controller
        self.controller.image_changed.connect(self.update_image_from_path)

    # === Cập nhật ảnh từ path (gọi từ bảng) ===
    def update_image_from_path(self, path: str):
        if not path or path == self.image_path:
            return
        self.image_path = path
        self._load_and_display_thumbnail()

    # === Tải và hiển thị thumbnail ===
    def _load_and_display_thumbnail(self):
        if not self.image_path:
            self.clear()
            self.original_image = None
            return

        img = QImage(self.image_path)
        if img.isNull():
            self.clear()
            self.original_image = None
            # self.setToolTip("Không tải được ảnh")
            return

        self.original_image = img
        scaled = img.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.setPixmap(QPixmap.fromImage(scaled))
        # self.setToolTip(self.image_path)

    # === Resize thumbnail khi widget thay đổi kích thước ===
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.original_image:
            self._load_and_display_thumbnail()

    # === Zoom bằng bánh xe ===
    def wheelEvent(self, event: QWheelEvent):
        if not self.original_image:
            return
        delta = event.angleDelta().y()
        if delta == 0:
            return
        factor = 1.15 if delta > 0 else 1 / 1.15
        new_scale = self.current_scale * factor
        if self.min_scale <= new_scale <= self.max_scale:
            self.current_scale = new_scale
            self.show_zoom()
        event.accept()

    def set_image(self, path: str):
        """Load ảnh + CẬP NHẬT ZOOM NGAY LẬP TỨC nếu đang hover"""
        self.image_path = path
        img = QImage(path)
        if img.isNull():
            self.original_image = None
            self.clear()
            self.hide_zoom()  # Ẩn nếu đang zoom
            return

        self.original_image = img

        # Hiển thị ảnh nhỏ
        scaled = img.scaled(
            self.width(), self.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.setPixmap(QPixmap.fromImage(scaled))

        # === TỰ ĐỘNG CẬP NHẬT ZOOM NẾU ĐANG HOVER ===
        if self.underMouse():
            self.show_zoom()
    # === Hiển thị ảnh phóng to ===

    def show_zoom(self):
        logger.debug("[HoverPreviewLabel] show_zoom called")
        if not self.original_image:
            return

        screen = self.screen().availableGeometry()
        max_w, max_h = int(screen.width() * 0.9), int(screen.height() * 0.9)
        w = min(int(self.base_size[0] * self.current_scale), max_w)
        h = min(int(self.base_size[1] * self.current_scale), max_h)

        zoomed = self.original_image.scaled(
            w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap = QPixmap.fromImage(zoomed)
        self.zoom_label.setPixmap(pixmap)
        self.zoom_label.adjustSize()
        logger.debug(
            f"[HoverPreviewLabel] zoom_label shown, visible: {self.zoom_label.isVisible()}")
        # Căn giữa màn hình
        size = self.zoom_label.sizeHint()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.zoom_label.move(x, y)

        self._fade_in(self.zoom_label)

    def _fade_in(self, widget):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        widget.show()
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(250)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.start()
        self.anim = anim

    def _fade_out(self, widget):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(180)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.finished.connect(widget.hide)
        anim.start()
        self.anim = anim

    def enterEvent(self, event):
        logger.debug("[HoverPreviewLabel] enterEvent triggered")
        if self.original_image:
            self.show_zoom()
        super().enterEvent(event)  # ← BẮT BUỘC GỌI

    def leaveEvent(self, event):
        logger.debug("[HoverPreviewLabel] leaveEvent triggered")
        logger.debug(
            f"[HoverPreviewLabel] zoom_label visible before hide: {self.zoom_label.isVisible()}")
        self.hide_zoom()
        logger.debug(
            f"[HoverPreviewLabel] zoom_label visible after hide: {self.zoom_label.isVisible()}")
        super().leaveEvent(event)

    def hide_zoom(self):
        logger.debug("[HoverPreviewLabel] hide_zoom called")
        if self.zoom_label.isVisible():
            self.zoom_label.hide()
        logger.debug(
            f"[HoverPreviewLabel] zoom_label hidden, visible: {self.zoom_label.isVisible()}")

    def clear_and_hide(self):
        self.clear()
        self.hide_zoom()
