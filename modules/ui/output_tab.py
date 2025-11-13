# warehouse_app/modules/ui/output_tab.py → SỬA TOÀN BỘ (CẬP NHẬT MỚI NHẤT)

import os
import asyncio
from PySide6.QtWidgets import (
    QMessageBox, QTableWidgetItem, QFileDialog, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QObject, Qt, QEvent
from modules.inventory import add_entry, refresh_current_stock, get_component_info_from_stock
from modules.search import search_entries
from modules.ui.multiselect_dropdown import MultiSelectDropdown
from modules.image_hover_preview import HoverPreviewLabel  # ← THÊM IMPORT
import logging


class OutputTabController(QObject):
    def __init__(self, ui, team_id, user_id, username, db_handler, input_controller):
        super().__init__()
        self.ui = ui
        self.team_id = team_id
        self.user_id = user_id
        self.username = username
        self.db_handler = db_handler
        self.input_controller = input_controller  # ← THAM CHIẾU INPUT

        self.current_entry = None
        self.is_new = False  # ← TRẠNG THÁI TẠO MỚI

        self.col_indices = {}  # BẮT BUỘC

        # === TẠO MULTISELECT CHO OUTPUT (GIỐNG INPUT) ===
        self.setup_multiselect_widgets()

        # === THAY THẾ output_images_label BẰNG HoverPreviewLabel ===
        self.replace_image_label_with_hover()

        self.setup_connections()
        self.clear_form()

    # =========================================================
    # TẠO MULTISELECT CHO OUTPUT (GIỐNG INPUT)
    # =========================================================
    def setup_multiselect_widgets(self):
        # Dùng options từ input_controller
        options = self.input_controller.options

        self.output_groups_selector = MultiSelectDropdown(
            self.ui.tabOutput, options.get("groups", []), "output_groups")
        self.output_process_selector = MultiSelectDropdown(
            self.ui.tabOutput, options.get("process", []), "output_process")
        self.output_model_selector = MultiSelectDropdown(
            self.ui.tabOutput, options.get("model", []), "output_model")
        self.output_material_selector = MultiSelectDropdown(
            self.ui.tabOutput, options.get("material", []), "output_material")

        for widget, dropdown in [
            (self.ui.output_groups_widget, self.output_groups_selector),
            (self.ui.output_process_widget, self.output_process_selector),
            (self.ui.output_model_widget, self.output_model_selector),
            (self.ui.output_material_widget, self.output_material_selector),
        ]:
            if widget.layout() is None:
                widget.setLayout(QVBoxLayout())
            widget.layout().addWidget(dropdown)

    # =========================================================
    # THAY THẾ output_images_label → HoverPreviewLabel (ZOOM KHI HOVER)
    # =========================================================
    def replace_image_label_with_hover(self):
        self.hover_preview = HoverPreviewLabel(self.ui.tabOutput)
        self.hover_preview.setFixedSize(200, 200)

        # Giữ style giống input
        self.hover_preview.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                padding: 6px;
                color: #444444;
            }
            QLabel:hover {
                background-color: #f7faff;
            }
        """)
        self.hover_preview.setAttribute(Qt.WA_StyledBackground, True)

        # Thay thế widget cũ
        old_label = self.ui.output_images_label
        parent_layout = old_label.parent().layout()
        if parent_layout:
            parent_layout.replaceWidget(old_label, self.hover_preview)
        old_label.deleteLater()
        self.ui.output_images_label = self.hover_preview

        self.hover_preview.setMouseTracking(True)
        self.hover_preview.installEventFilter(self)

        # Ẩn zoom ban đầu
        self.ui.output_images_label.hide_zoom()

    def eventFilter(self, watched, event):
        if watched == self.ui.output_images_label and event.type() == QEvent.MouseButtonDblClick:
            self.select_image()  # ← CHO PHÉP CHỌN ẢNH (TÙY CHỌN)
            return True
        return super().eventFilter(watched, event)

    # =========================================================
    # HIỂN THỊ ẢNH (DÙNG HoverPreviewLabel)
    # =========================================================
    def display_image(self, image_path: str):
        default = "images/default.jpg"
        path = image_path if os.path.exists(
            image_path) and os.path.getsize(image_path) > 0 else default
        self.ui.output_images_label.set_image(path)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Chọn ảnh", "", "Images (*.jpg *.jpeg *.png)")
        if file_path:
            self.ui.output_images_label.set_image(file_path)

    # =========================================================
    # KẾT NỐI
    # =========================================================
    def setup_connections(self):
        self.ui.output_check_id_auto_checkBox.stateChanged.connect(
            self.on_auto_fill_from_input)
        self.ui.output_new_button.clicked.connect(
            self.on_new_button_clicked)  # ← SỬA
        self.ui.output_delete_button.clicked.connect(
            self.on_delete_or_cancel)  # ← SỬA
        self.ui.output_export_button.clicked.connect(self.export_to_excel)
        self.ui.output_search_button.clicked.connect(self.search_output_items)
        self.ui.output_data_tablewidget.currentCellChanged.connect(
            self.on_output_row_selected)

    # =========================================================
    # NÚT NEW → CHUYỂN SANG SAVE / CANCEL
    # =========================================================
    def on_new_button_clicked(self):
        if self.is_new:
            self.save_new_output()  # ← LƯU
        else:
            self.start_new_output()  # ← TẠO MỚI

    def start_new_output(self):
        self.clear_form()
        self.is_new = True
        self.ui.output_new_button.setText("💾 Save")
        self.ui.output_delete_button.setText("❌ Cancel")

    def on_delete_or_cancel(self):
        if self.is_new:
            # HỦY TẠO MỚI
            self.is_new = False
            self.ui.output_new_button.setText("➕ New")
            self.ui.output_delete_button.setText("Delete")
            self.clear_form()
        else:
            # XÓA DÒNG ĐƯỢC CHỌN TRONG BẢNG
            self.delete_selected_output()

    # =========================================================
    # LƯU XUẤT KHO MỚI
    # =========================================================
    def save_new_output(self):
        if not self.current_entry:
            QMessageBox.warning(None, "Lỗi", "Không có linh kiện để xuất.")
            return

        try:
            qty_out = int(self.ui.output_quantity_lineedit.text() or 0)
            if qty_out <= 0:
                QMessageBox.warning(None, "Lỗi", "Số lượng > 0.")
                return
            if qty_out > self.current_entry["current_quantity"]:
                QMessageBox.warning(None, "Lỗi", "Vượt tồn kho.")
                return

            data = {
                "component_id": self.current_entry["component_id"],
                "component_name": self.current_entry["component_name"],
                "group_name": self.output_groups_selector.get_selected_items(),
                "process": self.output_process_selector.get_selected_items(),
                "model": self.output_model_selector.get_selected_items(),
                "size": self.current_entry["size"],
                "unit": self.current_entry["unit"],
                "team_id": self.team_id,
                "material": self.output_material_selector.get_selected_items(),
                "storage_location": self.current_entry["storage_location"],
                "invoice": self.current_entry["invoice"],
                "modinvoice": self.current_entry["modinvoice"],
                "status": self.current_entry["status"],
                "note": self.ui.output_note_textedit.toPlainText(),
                "quantity": qty_out,
                "movement_type": "out",
                "created_by": self.user_id,
            }

            entry_id = asyncio.run(add_entry(**data))
            asyncio.run(refresh_current_stock())

            QMessageBox.information(
                None, "Thành công", f"Đã xuất {qty_out} cái (ID={entry_id}).")

            # THOÁT CHẾ ĐỘ TẠO MỚI
            self.is_new = False
            self.ui.output_new_button.setText("➕ New")
            self.ui.output_delete_button.setText("Delete")
            self.ui.output_check_id_auto_checkBox.setEnabled(True)
            self.clear_form()
            self.load_output_table()

        except Exception as e:
            print(str(e))
            QMessageBox.critical(None, "Lỗi", str(e))

    # =========================================================
    # XÓA DÒNG XUẤT KHO TRONG BẢNG
    # =========================================================
    def delete_selected_output(self):
        row = self.ui.output_data_tablewidget.currentRow()
        if row < 0:
            QMessageBox.warning(None, "Lỗi", "Vui lòng chọn dòng để xóa.")
            return

        entry_id = int(self.ui.output_data_tablewidget.item(row, 0).text())
        if QMessageBox.question(None, "Xác nhận", f"Xóa phiếu xuất ID={entry_id}?") == QMessageBox.Yes:
            from modules.inventory import delete_entry
            asyncio.run(delete_entry(entry_id, self.user_id))
            asyncio.run(refresh_current_stock())
            self.load_output_table()
            QMessageBox.information(None, "Xóa", f"Đã xóa ID={entry_id}")

    # =========================================================
    # XÓA FORM
    # =========================================================
    def clear_form(self):
        self.ui.output_component_id_lineedit.clear()
        self.ui.output_quantity_lineedit.clear()
        self.ui.output_note_textedit.clear()
        self.ui.output_invoice_lineedit.clear()
        self.ui.output_desinvoice_lineedit.clear()

        self.ui.output_component_name_label.setText("-")
        self.ui.output_size_label.setText("-")
        self.ui.output_unit_label.setText("-")
        self.ui.output_storage_location_label.setText("-")
        self.ui.output_status_label.setText("-")
        self.ui.output_inventory_label.setText("-")

        self.output_groups_selector.set_selected_items([])
        self.output_process_selector.set_selected_items([])
        self.output_model_selector.set_selected_items([])
        self.output_material_selector.set_selected_items([])

        self.ui.output_images_label.set_image("images/default.jpg")
        self.ui.output_images_label.hide_zoom()

        self.current_entry = None

    # =========================================================
    # TẢI BẢNG XUẤT
    # =========================================================

    def load_output_table(self, data=None):
        try:
            # DỮ LIỆU ĐÃ CÓ → DÙNG NGAY
            if data is None:
                data = asyncio.run(
                    search_entries(team_id=self.team_id, filters={
                                   "movement_type": "out"})
                )

            table = self.ui.output_data_tablewidget
            if not data:
                table.setRowCount(0)
                self.clear_form()
                return

            headers = list(data[0].keys())
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)
            table.setRowCount(len(data))

            # LƯU INDEX CỘT
            self.col_indices = {}
            for c, h in enumerate(headers):
                self.col_indices[h] = c

            # ĐỔ DỮ LIỆU
            for r, row in enumerate(data):
                for c, key in enumerate(headers):
                    value = row.get(key, "")
                    if isinstance(value, list):
                        value = ", ".join([str(v)
                                          for v in value]) if value else ""
                    table.setItem(r, c, QTableWidgetItem(str(value)))

            table.resizeColumnsToContents()

            # TỰ ĐỘNG CHỌN DÒNG ĐẦU
            if table.rowCount() > 0:
                table.selectRow(0)
                self.on_output_row_selected(0, 0)

        except Exception as e:
            QMessageBox.critical(None, "Lỗi tải dữ liệu xuất", str(e))

    def search_output_items(self):
        filters = {"movement_type": "out"}
        if self.ui.output_search_component_id_checkBox.isChecked():
            cid = self.ui.output_component_id_lineedit.text().strip()
            if cid:
                filters["component_id"] = cid
        if self.ui.output_search_note_checkBox.isChecked():
            note = self.ui.output_note_textedit.toPlainText().strip()
            if note:
                filters["note_contains"] = note
        self.load_output_table(asyncio.run(
            search_entries(self.team_id, filters=filters)))

    def export_to_excel(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Xuất Excel", "", "Excel Files (*.xlsx)")
        if not path:
            return
        try:
            import pandas as pd
            table = self.ui.output_data_tablewidget
            headers = [table.horizontalHeaderItem(
                c).text() for c in range(table.columnCount())]
            data = [[table.item(r, c).text() if table.item(r, c) else "" for c in range(table.columnCount())]
                    for r in range(table.rowCount())]
            pd.DataFrame(data, columns=headers).to_excel(path, index=False)
            QMessageBox.information(None, "Xuất Excel", f"Đã lưu: {path}")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", str(e))

    # =========================================================
    # KHI CHỌN DÒNG TRONG BẢNG XUẤT
    # =========================================================
    def on_output_row_selected(self, row, col):
        if row < 0 or not hasattr(self, 'col_indices'):
            self.clear_form()
            return

        try:
            table = self.ui.output_data_tablewidget

            def get_value(col_name):
                col = self.col_indices.get(col_name)
                if col is None:
                    return ""
                item = table.item(row, col)
                return item.text() if item else ""

            # === LẤY DỮ LIỆU ===
            component_id = get_value("component_id")
            qty_text = get_value("quantity")
            note = get_value("note")

            # === GÁN ===
            self.ui.output_component_id_lineedit.setText(component_id)
            self.ui.output_component_name_label.setText(
                get_value("component_name") or "-")
            self.ui.output_size_label.setText(get_value("size") or "-")
            self.ui.output_unit_label.setText(get_value("unit") or "-")
            self.ui.output_storage_location_label.setText(
                get_value("storage_location") or "-")
            self.ui.output_status_label.setText(get_value("status") or "-")
            self.ui.output_invoice_lineedit.setText(get_value("invoice"))
            self.ui.output_desinvoice_lineedit.setText(get_value("modinvoice"))
            self.ui.output_note_textedit.setPlainText(note)

            # === SỐ LƯỢNG XUẤT (âm → dương) ===
            try:
                qty = abs(int(qty_text)) if qty_text and qty_text.lstrip(
                    '-').isdigit() else 0
                self.ui.output_quantity_lineedit.setText(str(qty))
            except:
                self.ui.output_quantity_lineedit.setText("0")

            # === MULTISELECT ===
            def parse_list(text):
                return [x.strip() for x in text.split(",") if x.strip()] if text else []

            self.output_groups_selector.set_selected_items(
                parse_list(get_value("group_name")))
            self.output_process_selector.set_selected_items(
                parse_list(get_value("process")))
            self.output_model_selector.set_selected_items(
                parse_list(get_value("model")))
            self.output_material_selector.set_selected_items(
                parse_list(get_value("material")))

            # === ẢNH ===
            image_path = os.path.join(
                self.input_controller.image_folder, f"{component_id}.jpg")
            self.display_image(image_path)

            # === CHECKBOX AUTO FILL ===
            self.ui.output_check_id_auto_checkBox.blockSignals(True)
            self.ui.output_check_id_auto_checkBox.setChecked(True)
            self.ui.output_check_id_auto_checkBox.blockSignals(False)

            self.current_entry = {"component_id": component_id}  # nếu cần

        except Exception as e:
            print(f"[OUTPUT] on_output_row_selected lỗi: {e}")
    # =========================================================
    # TỰ ĐỘNG ĐIỀN KHI CHECKBOX
    # =========================================================

    def on_auto_fill_from_input(self, state):
        if state != 2:  # unchecked
            self.ui.output_inventory_label.setText("?")
            return

        cid = self.ui.output_component_id_lineedit.text().strip().upper()
        if not cid:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập mã linh kiện.")
            self.ui.output_check_id_auto_checkBox.setChecked(False)
            return

        try:
            info = asyncio.run(
                get_component_info_from_stock(self.team_id, cid))
            if not info:
                QMessageBox.warning(None, "Không tồn kho",
                                    f"Không có mã: {cid}")
                self.ui.output_check_id_auto_checkBox.setChecked(False)
                return

            self.current_entry = info
            current_stock = info["current_quantity"]

            # === ĐỔ DỮ LIỆU ===
            self.ui.output_component_id_lineedit.setText(cid)
            self.ui.output_component_name_label.setText(
                info.get("component_name", "-"))
            self.ui.output_size_label.setText(info.get("size", "-"))
            self.ui.output_unit_label.setText(info.get("unit", "-"))
            self.ui.output_storage_location_label.setText(
                info.get("storage_location", "-"))
            self.ui.output_status_label.setText(info.get("status", "-"))
            self.ui.output_invoice_lineedit.setText(info.get("invoice", ""))
            self.ui.output_desinvoice_lineedit.setText(
                info.get("modinvoice", ""))
            self.ui.output_inventory_label.setText(str(current_stock))

            # MultiSelect
            self.output_groups_selector.set_selected_items(
                info.get("group_name", []))
            self.output_process_selector.set_selected_items(
                info.get("process", []))
            self.output_model_selector.set_selected_items(
                info.get("model", []))
            self.output_material_selector.set_selected_items(
                info.get("material", []))

            # Ảnh
            image_path = os.path.join(
                self.input_controller.image_folder, f"{cid}.jpg")
            self.display_image(image_path)

            self.ui.output_quantity_lineedit.setFocus()

        except Exception as e:
            print(f"[OUTPUT] auto fill lỗi: {e}")
            self.ui.output_check_id_auto_checkBox.setChecked(False)
            QMessageBox.critical(None, "Lỗi", str(e))

    # =========================================================
    # TÍNH TỒN KHO (KHÔNG DÙNG TRONG UI)
    # =========================================================
    def calculate_current_stock(self, component_id: str) -> float:
        try:
            all_entries = asyncio.run(search_entries(
                team_id=self.team_id,
                filters={"component_id_exact": component_id}
            ))
            total = sum(row.get("quantity", 0) for row in all_entries)
            return max(0, total)
        except Exception as e:
            print(f"[STOCK] Lỗi tính tồn: {e}")
            return 0.0
