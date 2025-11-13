# warehouse_app/modules/ui/input_tab.py
import os
import shutil
from typing import List, Optional, Dict, Any
import pandas as pd
import asyncio

from PySide6.QtWidgets import (
    QFileDialog, QMessageBox, QVBoxLayout, QCompleter,
    QTableView
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QStringListModel, Qt, QObject, QEvent

from modules.inventory import add_entry, delete_entry, refresh_current_stock, update_entry, generate_next_cid
from modules.options import get_all_categories
from modules.search import search_entries
from modules.ui.multiselect_dropdown import MultiSelectDropdown
from modules.image import display_image_async  # SỬA: loại bỏ asyncio
from modules.image_hover_preview import HoverPreviewLabel
from config.global_vars import get_folders
from config.settings import DEFAULT_IMAGE_PATH

import logging
logging.disable(logging.CRITICAL)


class InputTabController(QObject):
    def __init__(self, ui, team_id, user_id, username, db_handler):
        super().__init__()
        self.ui = ui
        self.team_id = team_id
        self.user_id = user_id
        self.username = username
        self.db_handler = db_handler

        self.is_new = False
        self.is_editing = False
        self.editing_entry_id = None
        self.image_folder, self.invoice_folder = get_folders()
        self.selected_image_path_input = None

        # Cache tên linh kiện (load 1 lần)
        self.name_suggestions_cache = []
        self.name_completer = QCompleter()
        self.name_model = QStringListModel()
        self.name_completer.setModel(self.name_model)
        self.name_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.name_completer.setFilterMode(Qt.MatchContains)
        self.ui.input_component_name_lineedit.setCompleter(self.name_completer)
        self.ui.input_component_name_lineedit.textChanged.connect(
            self.on_name_text_changed)

        # Table
        self.col_indices: Dict[str, int] = {}
        self.table_model = QStandardItemModel()
        self.ui.input_data_tableView.setModel(self.table_model)
        self.ui.input_data_tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.ui.input_data_tableView.setSelectionBehavior(
            QTableView.SelectRows)
        self.ui.input_data_tableView.setSelectionMode(
            QTableView.SingleSelection)
        self.ui.input_data_tableView.verticalHeader().setVisible(False)

        # Hover preview
        self.replace_image_label_with_hover()

        # Khởi tạo
        self.setup_dropdowns()
        self.setup_connections()
        self.load_name_suggestions_cache()
        self.load_table_data_once()  # ← LOAD 1 LẦN DUY NHẤT

    # =========================================================
    # THAY THẾ LABEL
    # =========================================================
    def replace_image_label_with_hover(self):
        self.hover_preview = HoverPreviewLabel(self.ui.tabInput)
        self.hover_preview.setFixedSize(200, 200)
        self.hover_preview.setStyleSheet("""
            QLabel {
                background-color: #ffffff; border: 2px solid #e0e0e0;
                border-radius: 10px; padding: 6px;
            }
            QLabel:hover { background-color: #f7faff; }
        """)
        self.hover_preview.setAttribute(Qt.WA_StyledBackground, True)

        old_label = self.ui.input_images_label
        parent_layout = old_label.parent().layout()
        if parent_layout:
            parent_layout.replaceWidget(old_label, self.hover_preview)
        old_label.deleteLater()
        self.ui.input_images_label = self.hover_preview
        self.ui.input_images_label.installEventFilter(self)
        self.ui.input_images_label.hide_zoom()

    def eventFilter(self, watched, event):
        if watched == self.ui.input_images_label and event.type() == QEvent.MouseButtonDblClick:
            self.select_image()
            return True
        return super().eventFilter(watched, event)

    # =========================================================
    # DROPDOWNS
    # =========================================================
    def setup_dropdowns(self):
        try:
            self.options = asyncio.run(get_all_categories(self.team_id))
            self.groups_selector = MultiSelectDropdown(
                self.ui.tabInput, self.options.get("groups", []), "groupsSelector")
            self.process_selector = MultiSelectDropdown(
                self.ui.tabInput, self.options.get("process", []), "processSelector")
            self.model_selector = MultiSelectDropdown(
                self.ui.tabInput, self.options.get("model", []), "modelSelector")
            self.material_selector = MultiSelectDropdown(
                self.ui.tabInput, self.options.get("material", []), "materialSelector")

            for widget, dropdown in [
                (self.ui.input_groups_widget, self.groups_selector),
                (self.ui.input_process_widget, self.process_selector),
                (self.ui.input_model_widget, self.model_selector),
                (self.ui.input_material_widget, self.material_selector),
            ]:
                if widget.layout() is None:
                    widget.setLayout(QVBoxLayout())
                widget.layout().addWidget(dropdown)

            self.ui.input_unit_combobox.addItems(self.options.get("unit", []))
            self.ui.input_storage_location_combobox.addItems(
                self.options.get("storage_location", []))
            self.ui.input_status_combobox.addItems(
                self.options.get("status", []))
        except Exception as e:
            QMessageBox.critical(None, "Lỗi dropdown", str(e))

    # =========================================================
    # KẾT NỐI
    # =========================================================
    def setup_connections(self):
        self.ui.input_check_id_auto_checkBox.stateChanged.connect(
            self.on_auto_cid_changed)
        self.ui.input_new_button.clicked.connect(self.add_new_item)
        self.ui.input_edit_button.clicked.connect(self.edit_selected_item)
        self.ui.input_delete_button.clicked.connect(self.delete_selected_item)
        self.ui.input_search_button.clicked.connect(self.search_items)
        self.ui.input_export_button.clicked.connect(self.export_to_excel)

        self.ui.input_data_tableView.selectionModel(
        ).selectionChanged.connect(self.on_row_selected)

    # =========================================================
    # LOAD DỮ LIỆU 1 LẦN DUY NHẤT
    # =========================================================
    def load_table_data_once(self):
        """Chỉ gọi 1 lần khi mở tab"""
        try:
            data = asyncio.run(search_entries(
                team_id=self.team_id, filters={"movement_type": "in"}))
            self.update_table_model(data)
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", str(e))

    def update_table_model(self, data: List[Dict[str, Any]]):
        """Cập nhật bảng từ dữ liệu (dùng chung cho load và search)"""
        self.table_model.clear()
        if not data:
            self.clear_form()
            return

        headers = list(data[0].keys())
        self.table_model.setHorizontalHeaderLabels(headers)
        self.col_indices = {h: i for i, h in enumerate(headers)}

        for row_data in data:
            items = []
            for key in headers:
                value = row_data.get(key, "")
                if isinstance(value, list):
                    value = ", ".join(str(v) for v in value)
                item = QStandardItem(str(value))
                item.setEditable(False)
                items.append(item)
            self.table_model.appendRow(items)

        self.ui.input_data_tableView.resizeColumnsToContents()
        self.ui.input_data_tableView.horizontalHeader().setStretchLastSection(True)

        if self.table_model.rowCount() > 0:
            idx = self.table_model.index(0, 0)
            self.ui.input_data_tableView.setCurrentIndex(idx)

    # =========================================================
    # TÌM KIẾM → CHỈ QUERY KHI SEARCH
    # =========================================================
    def search_items(self):
        filters = {"movement_type": "in"}
        # ... (giữ nguyên logic lọc)
        if self.ui.input_search_component_id_checkBox.isChecked():
            cid = self.ui.input_component_id_lineedit.text().strip().upper()
            if cid:
                filters["component_id"] = cid
        if self.ui.input_search_component_name_checkBox.isChecked():
            name = self.ui.input_component_name_lineedit.text().strip()
            if name:
                filters["component_name"] = name
        # ... các filter khác

        data = asyncio.run(search_entries(self.team_id, filters=filters))
        self.update_table_model(data)  # ← Cập nhật bảng

    # =========================================================
    # CHỌN DÒNG → LẤY DỮ LIỆU TỪ BẢNG, KHÔNG QUERY DB
    # =========================================================
    def on_row_selected(self, selected=None, deselected=None):
        indexes = self.ui.input_data_tableView.selectedIndexes()
        if not indexes:
            self.clear_form()
            return

        row = indexes[0].row()
        self.block_form_signals(True)

        def get_value(col_name, default=""):
            col = self.col_indices.get(col_name)
            if col is None:
                return default
            item = self.table_model.item(row, col)
            return item.text() if item else default

        component_id = get_value("component_id")
        component_name = get_value("component_name")
        group_name = get_value("group_name")

        # Gán form
        self.ui.input_component_id_lineedit.setText(component_id)
        self.ui.input_component_name_lineedit.setText(component_name)
        self.ui.input_size_lineedit.setText(get_value("size"))
        self.ui.input_quantity_lineedit.setText(get_value("quantity"))
        self.ui.input_unit_combobox.setCurrentText(get_value("unit"))
        self.ui.input_status_combobox.setCurrentText(get_value("status"))
        self.ui.input_invoice_lineedit.setText(get_value("invoice"))
        self.ui.input_desinvoice_lineedit.setText(get_value("modinvoice"))
        self.ui.input_note_textedit.setPlainText(get_value("note"))
        self.ui.input_storage_location_combobox.setCurrentText(
            get_value("storage_location"))

        # Multi-select
        def parse_list(text):
            return [x.strip() for x in text.split(",") if x.strip()] if text else []

        for sel, field in [
            (self.groups_selector, "group_name"),
            (self.process_selector, "process"),
            (self.model_selector, "model"),
            (self.material_selector, "material")
        ]:
            sel.blockSignals(True)
            sel.set_selected_items(parse_list(get_value(field)))
            sel.blockSignals(False)

        self.block_form_signals(False)

        # === ẢNH: DỮ LIỆU ĐÃ CÓ → GỌI ASYNC KHÔNG BLOCK ===
        display_image_async(
            component_id=component_id,
            label=self.ui.input_images_label
        )
    # =========================================================
    # GỢI Ý TÊN (CACHE + KHÔNG DÙNG TIMER)
    # =========================================================

    def load_name_suggestions_cache(self):
        try:
            df = self.db_handler.read_data(
                "inventory_entries", ["component_name", "team_id"])
            df = df[df["team_id"] == self.team_id]
            self.name_suggestions_cache = sorted(
                set(df["component_name"].dropna().astype(
                    str).str.strip().unique())
            )
        except Exception as e:
            self.name_suggestions_cache = []

    def on_name_text_changed(self, text: str):
        if len(text) < 2:
            self.name_model.setStringList([])
            return
        filtered = [
            v for v in self.name_suggestions_cache if text.lower() in v.lower()][:20]
        self.name_model.setStringList(filtered)
        if filtered:
            self.name_completer.complete()

    # =========================================================
    # THÊM / SỬA / XÓA
    # =========================================================
    def add_new_item(self):
        if self.is_new:
            self.save_new_item()
            return
        if self.is_editing:
            self.save_edit_item()
            return
        self.clear_form()
        self.is_new = True
        self.ui.input_new_button.setText("Save")
        self.ui.input_delete_button.setText("Cancel")
        self.ui.input_edit_button.setEnabled(False)

    def save_image(self, component_id: str):
        if not self.selected_image_path_input:
            return None

        image_folder, _ = get_folders()
        target_path = os.path.join(image_folder, f"{component_id}.jpg")
        os.makedirs(image_folder, exist_ok=True)

        try:
            if self.selected_image_path_input.lower().endswith(('.jpg', '.jpeg')):
                if self.selected_image_path_input != target_path:
                    shutil.copy2(self.selected_image_path_input, target_path)
            else:
                from PIL import Image
                img = Image.open(self.selected_image_path_input).convert('RGB')
                img.save(target_path, "JPEG", quality=90)

            self.ui.input_images_label.set_image(target_path)
            return target_path
        except Exception as e:
            print(f"[SAVE IMAGE] Lỗi: {e}")
            return None

    def edit_selected_item(self):
        indexes = self.ui.input_data_tableView.selectedIndexes()
        if not indexes:
            QMessageBox.warning(None, "Lỗi", "Chọn dòng để sửa.")
            return
        if self.is_new:
            return

        row = indexes[0].row()
        self.editing_entry_id = int(self.table_model.item(
            row, self.col_indices.get("id", 0)).text())
        self.is_editing = True
        self.ui.input_new_button.setText("Save Edit")
        self.ui.input_delete_button.setText("Cancel")
        self.ui.input_edit_button.setEnabled(False)

    def save_edit_item(self):
        try:
            if not self.editing_entry_id:
                return

            component_id = self.ui.input_component_id_lineedit.text().strip().upper()
            if not component_id:
                QMessageBox.warning(None, "Lỗi", "Vui lòng nhập mã linh kiện.")
                return

            image_path = self.save_image(
                component_id) if self.selected_image_path_input else None

            data = {
                "id": self.editing_entry_id,
                "component_id": component_id,
                "component_name": self.ui.input_component_name_lineedit.text().strip(),
                "group_name": self.groups_selector.get_selected_items(),
                "process": self.process_selector.get_selected_items(),
                "model": self.model_selector.get_selected_items(),
                "size": self.ui.input_size_lineedit.text().strip(),
                "unit": self.ui.input_unit_combobox.currentText(),
                "team_id": self.team_id,
                "material": self.material_selector.get_selected_items(),
                "storage_location": self.ui.input_storage_location_combobox.currentText(),
                "invoice": self.ui.input_invoice_lineedit.text().strip(),
                "modinvoice": self.ui.input_desinvoice_lineedit.text().strip(),
                "status": self.ui.input_status_combobox.currentText(),
                "note": self.ui.input_note_textedit.toPlainText(),
                "quantity": float(self.ui.input_quantity_lineedit.text() or 0),
                "created_by": self.user_id,
            }

            asyncio.run(update_entry(**data))
            asyncio.run(refresh_current_stock())
            self.finish_edit_mode()
            self.load_table_data_once()
            QMessageBox.information(None, "Thành công", "Đã cập nhật.")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", str(e))

    def delete_selected_item(self):
        if self.ui.input_delete_button.text() == "Cancel":
            self.finish_edit_mode()
            return

        indexes = self.ui.input_data_tableView.selectedIndexes()
        if not indexes:
            return

        row = indexes[0].row()
        entry_id = int(self.table_model.item(
            row, self.col_indices.get("id", 0)).text())
        if QMessageBox.question(None, "Xác nhận", f"Xóa ID={entry_id}?") == QMessageBox.Yes:
            asyncio.run(delete_entry(entry_id, self.user_id))
            asyncio.run(refresh_current_stock())
            self.load_table_data_once()

    def finish_edit_mode(self):
        self.is_new = self.is_editing = False
        self.editing_entry_id = None
        self.ui.input_new_button.setText("New")
        self.ui.input_delete_button.setText("Delete")
        self.ui.input_edit_button.setEnabled(True)
        self.clear_form()

    # =========================================================
    # HỖ TRỢ
    # =========================================================
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Chọn ảnh", "", "Images (*.jpg *.jpeg *.png)")
        if file_path:
            self.selected_image_path_input = file_path
            self.ui.input_images_label.set_image(file_path)

    def save_image(self, component_id: str):
        if not self.selected_image_path_input:
            return None
        target_path = os.path.join(self.image_folder, f"{component_id}.jpg")
        os.makedirs(self.image_folder, exist_ok=True)
        try:
            if self.selected_image_path_input.lower().endswith(('.jpg', '.jpeg')):
                if self.selected_image_path_input != target_path:
                    shutil.copy2(self.selected_image_path_input, target_path)
            else:
                from PIL import Image
                img = Image.open(self.selected_image_path_input).convert('RGB')
                img.save(target_path, "JPEG", quality=90)
            self.ui.input_images_label.set_image(target_path)
            return target_path
        except Exception as e:
            print(f"[IMAGE][LỖI lưu]: {e}")
            return None

    def clear_form(self):
        self.ui.input_images_label.current_loader = None
        for w in [
            self.ui.input_component_id_lineedit, self.ui.input_component_name_lineedit,
            self.ui.input_size_lineedit, self.ui.input_invoice_lineedit,
            self.ui.input_desinvoice_lineedit, self.ui.input_note_textedit,
            self.ui.input_quantity_lineedit
        ]:
            w.clear()
        for cb in [self.ui.input_unit_combobox, self.ui.input_storage_location_combobox, self.ui.input_status_combobox]:
            cb.setCurrentIndex(-1)
        for sel in [self.groups_selector, self.process_selector, self.model_selector, self.material_selector]:
            sel.set_selected_items([])
        self.ui.input_images_label.set_image("")
        self.ui.input_images_label.hide_zoom()

    def on_auto_cid_changed(self, state):
        if state == 2:
            self.generate_and_set_cid()

    def generate_and_set_cid(self):
        storage = self.ui.input_storage_location_combobox.currentText()
        if not storage:
            QMessageBox.warning(None, "Lỗi", "Chọn Storage Location.")
            self.ui.input_check_id_auto_checkBox.setChecked(False)
            return
        new_cid = asyncio.run(generate_next_cid(storage))
        if new_cid:
            self.ui.input_component_id_lineedit.setText(new_cid)
        else:
            self.ui.input_check_id_auto_checkBox.setChecked(False)

    def block_form_signals(self, block=True):
        for w in [
            self.ui.input_component_id_lineedit, self.ui.input_component_name_lineedit,
            self.ui.input_size_lineedit, self.ui.input_quantity_lineedit,
            self.ui.input_unit_combobox, self.ui.input_status_combobox,
            self.ui.input_invoice_lineedit, self.ui.input_desinvoice_lineedit,
            self.ui.input_note_textedit, self.ui.input_storage_location_combobox,
        ]:
            w.blockSignals(block)

    def export_to_excel(self):
        # path, _ = QFileDialog.getSaveFileName(
        #     None, "Xuất Excel", "", "Excel Files (*.xlsx)")
        # if not path:
        #     return
        # try:
        #     headers = [self.table_model.horizontalHeaderItem(
        #         c).text() for c in range(self.table_model.columnCount())]
        #     data = []
        #     for r in range(self.table_model.rowCount()):
        #         row = [self.table_model.item(r, c).text() if self.table_model.item(r, c) else "" for c in range(self`self.table_model.columnCount())]
        #         data.append(row)
        #     pd.DataFrame(data, columns=headers).to_excel(path, index=False)
        #     QMessageBox.information(None, "Xuất Excel", f"Đã lưu: {path}")
        # except Exception as e:
        #     QMessageBox.critical(None, "Lỗi", str(e))
        pass
