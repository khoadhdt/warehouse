import re


class SizeHandler:
    """Xử lý kích thước (Dài x Rộng x Cao)."""

    @staticmethod
    def to_string(length_widget, width_widget, height_widget):
        """Chuyển 3 giá trị từ QLineEdit thành chuỗi."""
        length = length_widget.text().strip()
        width = width_widget.text().strip()
        height = height_widget.text().strip()
        if length and width and height:
            return f"{length} x {width} x {height}"
        return ""

    @staticmethod
    def to_fields(size_str, length_widget, width_widget, height_widget):
        """Tách chuỗi kích thước và điền vào 3 QLineEdit."""
        size_parts = size_str.split(" x ") if size_str else ["", "", ""]
        length_widget.setText(size_parts[0].strip())
        width_widget.setText(
            size_parts[1].strip() if len(size_parts) > 1 else "")
        height_widget.setText(
            size_parts[2].strip() if len(size_parts) > 2 else "")

    @staticmethod
    def build_size_regex(length, width, height):
        # Hàm build regex cho size lọc theo kiểu 3 chiều

        def part_to_regex(val):
            if val == '' or val == '?':
                # phần này có thể là bất kỳ số (integer hoặc float)
                return r'\d+(\.\d+)?'
            else:
                # Escape dấu chấm nếu có, để regex hiểu đúng số
                val_escaped = re.escape(val)
                return val_escaped

        regex_pattern = f"^{part_to_regex(length)} x {part_to_regex(width)} x {part_to_regex(height)}$"
        return regex_pattern
