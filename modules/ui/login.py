import asyncio
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import Signal, QThread, QObject
from modules.auth import verify_user


class LoginWorker(QObject):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        try:
            result = asyncio.run(verify_user(self.username, self.password))
            self.finished.emit(result or {})
        except Exception as e:
            self.error.emit(str(e))


class LoginScreen(QWidget):
    login_success = Signal(dict)  # 👉 phát tín hiệu khi đăng nhập thành công

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập hệ thống kho")
        self.resize(320, 180)

        layout = QVBoxLayout()
        self.txt_user = QLineEdit()
        self.txt_user.setPlaceholderText("Username")

        self.txt_pass = QLineEdit()
        self.txt_pass.setPlaceholderText("Password")
        self.txt_pass.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Đăng nhập")
        self.btn_login.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("Tên đăng nhập:"))
        layout.addWidget(self.txt_user)
        layout.addWidget(QLabel("Mật khẩu:"))
        layout.addWidget(self.txt_pass)
        layout.addWidget(self.btn_login)
        self.setLayout(layout)

    def handle_login(self):
        username = self.txt_user.text().strip()
        password = self.txt_pass.text().strip()
        if not username or not password:
            QMessageBox.warning(self, "Thiếu thông tin",
                                "Nhập đủ username và password.")
            return

        self.btn_login.setEnabled(False)
        self.thread = QThread()
        self.worker = LoginWorker(username, password)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_login_result)
        self.worker.error.connect(self.on_login_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def on_login_result(self, user):
        self.btn_login.setEnabled(True)
        if user:
            # QMessageBox.information(
            #     self, "Đăng nhập thành công", f"Xin chào {user['username']}")
            self.login_success.emit(user)
        else:
            QMessageBox.critical(self, "Sai thông tin",
                                 "Tên đăng nhập hoặc mật khẩu sai!")

    def on_login_error(self, err):
        self.btn_login.setEnabled(True)
        QMessageBox.critical(self, "Lỗi", f"Lỗi khi đăng nhập:\n{err}")
