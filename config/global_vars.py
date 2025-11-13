# warehouse_app/config/global_vars.py
"""
BIẾN TOÀN CỤC – DÙNG CHUNG TOÀN ỨNG DỤNG
"""

# config/global_vars.py
_LINK_IMAGE: str = "images/default/"
_LINK_INVOICE: str = "invoices/default/"


def update_folders(image_folder: str, invoice_folder: str):
    global _LINK_IMAGE, _LINK_INVOICE
    _LINK_IMAGE = image_folder or "images/default/"
    _LINK_INVOICE = invoice_folder or "invoices/default/"


def get_folders() -> tuple[str, str]:
    """Trả về (image_folder, invoice_folder) hiện tại"""
    return _LINK_IMAGE, _LINK_INVOICE
