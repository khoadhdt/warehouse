# warehouse_app/main.py
# ====== FORCE IMPORTS FOR PYINSTALLER ======
# Hỗ trợ PyInstaller gom đủ thư viện bên ngoài khi build exe
import os
import sys
import re
import json
import asyncio
import logging
import warnings
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional, Dict, Any

# --- Third-party libraries (ngoài thư viện chuẩn Python) ---
import pandas as pd
import asyncpg
import bcrypt
from passlib.context import CryptContext
from PIL import Image

# SQLAlchemy async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# Pydantic
from pydantic import BaseModel

# PySide6 (GUI)
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel, QTabWidget, QListWidget,
    QListWidgetItem, QStatusBar, QInputDialog, QTableWidgetItem, QGraphicsOpacityEffect
)
from PySide6.QtGui import (
    QPixmap, QDesktopServices, QImage, QWheelEvent, QGuiApplication, QPainter,
    QColor, QPen, QMouseEvent, QKeyEvent
)
from PySide6.QtCore import (
    Qt, QThread, QTimer, QUrl, QObject, QEvent, QRect, QStringListModel,
    QPropertyAnimation, Signal
)
# ===========================================
# SỬA: Thêm giới hạn kích thước theo màn hình
# import sys
# import asyncio
# from PySide6.QtWidgets import QApplication
# from PySide6.QtCore import QTimer, Qt
# from PySide6.QtGui import QPixmap
from modules.ui.login import LoginScreen
from modules.ui.main_window import MainWindow
from modules.teams import get_team_by_id
from config.global_vars import update_folders, get_folders


async def build_user_with_team(user: dict):
    team_id = user.get("team_id")
    if not team_id:
        return user

    team = await get_team_by_id(team_id)
    if team:
        user["team_display_name"] = team["display_name"]
        user["image_folder"] = team.get("image_folder") or "images/default/"
        user["invoice_folder"] = team.get(
            "invoice_folder") or "invoices/default/"
    return user


def main():
    app = QApplication(sys.argv)

    # === CHỐT: GIỚI HẠN KÍCH THƯỚC TỐI ĐA ===
    screen = app.primaryScreen().availableGeometry()
    # max_w = screen.width() - 100
    # max_h = screen.height() - 100

    login = LoginScreen()

    def on_login_success(user_info):
        user_info = asyncio.run(build_user_with_team(user_info))
        update_folders(
            user_info.get("image_folder"),
            user_info.get("invoice_folder")
        )
        get_folders()

        window = MainWindow(user_info)
        window.showMaximized()
        login.close()

    login.login_success.connect(on_login_success)
    login.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
