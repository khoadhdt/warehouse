# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'screen_InventoryManager.ui'
##
# Created by: Qt User Interface Compiler version 6.8.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
                               QFrame, QGridLayout, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
                               QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
                               QTextEdit, QVBoxLayout, QWidget)
import ui.lib_icon_InventoryManagement_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1451, 816)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.MyWidget = QWidget(self.centralwidget)
        self.MyWidget.setObjectName(u"MyWidget")
        self.verticalLayout_3 = QVBoxLayout(self.MyWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_main = QTabWidget(self.MyWidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget_main.setFont(font)
        self.tabWidget_main.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_main.setAutoFillBackground(False)
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tabWidget_main.setTabShape(QTabWidget.Rounded)
        self.tabWidget_main.setIconSize(QSize(32, 32))
        self.tabWidget_main.setElideMode(Qt.ElideLeft)
        self.tabWidget_main.setTabsClosable(False)
        self.tabWidget_main.setTabBarAutoHide(False)
        self.tabLogin = QWidget()
        self.tabLogin.setObjectName(u"tabLogin")
        self.verticalLayout_21 = QVBoxLayout(self.tabLogin)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        icon = QIcon()
        icon.addFile(u":/icon/images/icon/login_logo.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabLogin, icon, "")
        self.tabInput = QWidget()
        self.tabInput.setObjectName(u"tabInput")
        self.verticalLayout_5 = QVBoxLayout(self.tabInput)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabin = QWidget(self.tabInput)
        self.widget_nhap_tabin.setObjectName(u"widget_nhap_tabin")
        self.gridLayout_NhapKho = QGridLayout(self.widget_nhap_tabin)
        self.gridLayout_NhapKho.setSpacing(5)
        self.gridLayout_NhapKho.setObjectName(u"gridLayout_NhapKho")
        self.gridLayout_NhapKho.setContentsMargins(5, 5, 5, 5)
        self.input_status_labels = QLabel(self.widget_nhap_tabin)
        self.input_status_labels.setObjectName(u"input_status_labels")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.input_status_labels.sizePolicy().hasHeightForWidth())
        self.input_status_labels.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.input_status_labels.setFont(font1)
        self.input_status_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_status_labels, 2, 0, 1, 1)

        self.input_groups_labels = QLabel(self.widget_nhap_tabin)
        self.input_groups_labels.setObjectName(u"input_groups_labels")
        sizePolicy.setHeightForWidth(
            self.input_groups_labels.sizePolicy().hasHeightForWidth())
        self.input_groups_labels.setSizePolicy(sizePolicy)
        self.input_groups_labels.setFont(font1)
        self.input_groups_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_groups_labels, 3, 6, 1, 1)

        self.input_search_process_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_process_checkBox.setObjectName(
            u"input_search_process_checkBox")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.input_search_process_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_process_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_process_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_process_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_process_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                         "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                         "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:unchecked {\n"
                                                         "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:checked {\n"
                                                         "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                         "}\n"
                                                         "")
        self.input_search_process_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_process_checkBox, 2, 8, 1, 1)

        self.input_model_labels = QLabel(self.widget_nhap_tabin)
        self.input_model_labels.setObjectName(u"input_model_labels")
        sizePolicy.setHeightForWidth(
            self.input_model_labels.sizePolicy().hasHeightForWidth())
        self.input_model_labels.setSizePolicy(sizePolicy)
        self.input_model_labels.setFont(font1)
        self.input_model_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_model_labels, 4, 6, 1, 1)

        self.input_search_model_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_model_checkBox.setObjectName(
            u"input_search_model_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_model_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_model_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_model_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_model_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_model_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                       "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                       "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QCheckBox::indicator:unchecked {\n"
                                                       "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QCheckBox::indicator:checked {\n"
                                                       "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                       "}\n"
                                                       "")
        self.input_search_model_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_model_checkBox, 4, 8, 1, 1)

        self.input_material_labels = QLabel(self.widget_nhap_tabin)
        self.input_material_labels.setObjectName(u"input_material_labels")
        sizePolicy.setHeightForWidth(
            self.input_material_labels.sizePolicy().hasHeightForWidth())
        self.input_material_labels.setSizePolicy(sizePolicy)
        self.input_material_labels.setFont(font1)
        self.input_material_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(
            self.input_material_labels, 3, 0, 1, 1)

        self.input_search_groups_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_groups_checkBox.setObjectName(
            u"input_search_groups_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_groups_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_groups_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_groups_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_groups_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_groups_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                        "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                        "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:unchecked {\n"
                                                        "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:checked {\n"
                                                        "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                        "}\n"
                                                        "")
        self.input_search_groups_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_groups_checkBox, 3, 8, 1, 1)

        self.input_desinvoice_labels = QLabel(self.widget_nhap_tabin)
        self.input_desinvoice_labels.setObjectName(u"input_desinvoice_labels")
        sizePolicy.setHeightForWidth(
            self.input_desinvoice_labels.sizePolicy().hasHeightForWidth())
        self.input_desinvoice_labels.setSizePolicy(sizePolicy)
        self.input_desinvoice_labels.setFont(font1)
        self.input_desinvoice_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(
            self.input_desinvoice_labels, 5, 6, 1, 1)

        self.input_search_material_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_material_checkBox.setObjectName(
            u"input_search_material_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_material_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_material_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_material_checkBox.setMinimumSize(QSize(22, 22))
        self.input_search_material_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_material_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                          "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                          "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:unchecked {\n"
                                                          "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:checked {\n"
                                                          "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                          "}\n"
                                                          "")
        self.input_search_material_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_material_checkBox, 3, 1, 1, 1)

        self.input_desinvoice_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_desinvoice_lineedit.setObjectName(
            u"input_desinvoice_lineedit")
        self.input_desinvoice_lineedit.setEnabled(True)
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.input_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.input_desinvoice_lineedit.setSizePolicy(sizePolicy2)
        self.input_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                     "    background-color: #f0f0f0;\n"
                                                     "    border: 1px solid #ccc;\n"
                                                     "    border-radius: 4px;\n"
                                                     "    padding: 4px;\n"
                                                     "    font-size: 14px;\n"
                                                     "    color: #3333FF;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                     "}")
        self.input_desinvoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(
            self.input_desinvoice_lineedit, 5, 11, 1, 1)

        self.input_search_desinvoice_checkBox = QCheckBox(
            self.widget_nhap_tabin)
        self.input_search_desinvoice_checkBox.setObjectName(
            u"input_search_desinvoice_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_desinvoice_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_desinvoice_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_desinvoice_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_desinvoice_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_desinvoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                            "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                            "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:unchecked {\n"
                                                            "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:checked {\n"
                                                            "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                            "}\n"
                                                            "")
        self.input_search_desinvoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_desinvoice_checkBox, 5, 8, 1, 1)

        self.input_invoice_labels = QLabel(self.widget_nhap_tabin)
        self.input_invoice_labels.setObjectName(u"input_invoice_labels")
        sizePolicy.setHeightForWidth(
            self.input_invoice_labels.sizePolicy().hasHeightForWidth())
        self.input_invoice_labels.setSizePolicy(sizePolicy)
        self.input_invoice_labels.setFont(font1)
        self.input_invoice_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(
            self.input_invoice_labels, 5, 0, 1, 1)

        self.input_search_invoice_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_invoice_checkBox.setObjectName(
            u"input_search_invoice_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_invoice_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_invoice_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_invoice_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_invoice_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_invoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                         "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                         "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:unchecked {\n"
                                                         "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:checked {\n"
                                                         "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                         "}\n"
                                                         "")
        self.input_search_invoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_invoice_checkBox, 5, 1, 1, 1)

        self.input_invoice_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_invoice_lineedit.setObjectName(u"input_invoice_lineedit")
        self.input_invoice_lineedit.setEnabled(True)
        self.input_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                  "    background-color: #f0f0f0;\n"
                                                  "    border: 1px solid #ccc;\n"
                                                  "    border-radius: 4px;\n"
                                                  "    padding: 4px;\n"
                                                  "    font-size: 14px;\n"
                                                  "    color: #3333FF;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus {\n"
                                                  "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                  "}")
        self.input_invoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(
            self.input_invoice_lineedit, 5, 3, 1, 1)

        self.input_component_name_labels = QLabel(self.widget_nhap_tabin)
        self.input_component_name_labels.setObjectName(
            u"input_component_name_labels")
        sizePolicy.setHeightForWidth(
            self.input_component_name_labels.sizePolicy().hasHeightForWidth())
        self.input_component_name_labels.setSizePolicy(sizePolicy)
        self.input_component_name_labels.setFont(font1)
        self.input_component_name_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(
            self.input_component_name_labels, 1, 6, 1, 1)

        self.input_size_horizontalLayout = QHBoxLayout()
        self.input_size_horizontalLayout.setSpacing(0)
        self.input_size_horizontalLayout.setObjectName(
            u"input_size_horizontalLayout")
        self.input_size_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_size_lineedit.setObjectName(u"input_size_lineedit")
        self.input_size_lineedit.setEnabled(True)
        self.input_size_lineedit.setStyleSheet(u"QLineEdit {\n"
                                               "    background-color: #f0f0f0;\n"
                                               "    border: 1px solid #ccc;\n"
                                               "    border-radius: 4px;\n"
                                               "    padding: 4px;\n"
                                               "    font-size: 14px;\n"
                                               "    color: #3333FF;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:focus {\n"
                                               "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                               "}")
        self.input_size_lineedit.setMaxLength(32767)
        self.input_size_lineedit.setAlignment(Qt.AlignCenter)

        self.input_size_horizontalLayout.addWidget(self.input_size_lineedit)

        self.input_size_label_2 = QLabel(self.widget_nhap_tabin)
        self.input_size_label_2.setObjectName(u"input_size_label_2")
        sizePolicy.setHeightForWidth(
            self.input_size_label_2.sizePolicy().hasHeightForWidth())
        self.input_size_label_2.setSizePolicy(sizePolicy)
        self.input_size_label_2.setFont(font1)
        self.input_size_label_2.setMargin(7)

        self.input_size_horizontalLayout.addWidget(self.input_size_label_2)

        self.gridLayout_NhapKho.addLayout(
            self.input_size_horizontalLayout, 4, 3, 1, 1)

        self.input_storage_location_labels = QLabel(self.widget_nhap_tabin)
        self.input_storage_location_labels.setObjectName(
            u"input_storage_location_labels")
        sizePolicy.setHeightForWidth(
            self.input_storage_location_labels.sizePolicy().hasHeightForWidth())
        self.input_storage_location_labels.setSizePolicy(sizePolicy)
        self.input_storage_location_labels.setFont(font1)

        self.gridLayout_NhapKho.addWidget(
            self.input_storage_location_labels, 1, 0, 1, 1)

        self.input_search_storage_location_checkBox = QCheckBox(
            self.widget_nhap_tabin)
        self.input_search_storage_location_checkBox.setObjectName(
            u"input_search_storage_location_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_storage_location_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_storage_location_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_storage_location_checkBox.setMinimumSize(
            QSize(22, 20))
        self.input_search_storage_location_checkBox.setMaximumSize(
            QSize(22, 24))
        self.input_search_storage_location_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                  "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                  "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:unchecked {\n"
                                                                  "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:checked {\n"
                                                                  "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                  "}\n"
                                                                  "")
        self.input_search_storage_location_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_storage_location_checkBox, 1, 1, 1, 1)

        self.input_images_label = QLabel(self.widget_nhap_tabin)
        self.input_images_label.setObjectName(u"input_images_label")
        self.input_images_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.input_images_label.sizePolicy().hasHeightForWidth())
        self.input_images_label.setSizePolicy(sizePolicy1)
        self.input_images_label.setMinimumSize(QSize(280, 200))
        self.input_images_label.setMaximumSize(QSize(280, 16777215))
        self.input_images_label.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_images_label.setStyleSheet(u"/* QLabel styling */\n"
                                              "QLabel {\n"
                                              "    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
                                              "    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
                                              "    border-radius: 10px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
                                              "    padding: 6px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
                                              "    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
                                              "}\n"
                                              "/* Hi\u1ec7u \u1ee9ng khi hover */\n"
                                              "QLabel:hover {\n"
                                              "    background-color: #f7faff; /* Thay \u0111\u1ed5i n\u1ec1n nh\u1eb9 khi hover */\n"
                                              "}\n"
                                              "\n"
                                              "")
        self.input_images_label.setFrameShape(QFrame.StyledPanel)
        self.input_images_label.setPixmap(
            QPixmap(u":/icon/images/icon/no_image.png"))
        self.input_images_label.setScaledContents(True)
        self.input_images_label.setAlignment(Qt.AlignCenter)
        self.input_images_label.setWordWrap(False)
        self.input_images_label.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse)

        self.gridLayout_NhapKho.addWidget(self.input_images_label, 1, 17, 5, 1)

        self.input_note_textedit = QTextEdit(self.widget_nhap_tabin)
        self.input_note_textedit.setObjectName(u"input_note_textedit")
        self.input_note_textedit.setStyleSheet(u"QTextEdit {\n"
                                               "	background-color: rgb(255, 255, 255);\n"
                                               "    border: 2px solid #ccc;\n"
                                               "    border-radius: 6px;\n"
                                               "    padding: 5px;\n"
                                               "    color: #3333FF;\n"
                                               "}\n"
                                               "\n"
                                               "QTextEdit:focus {\n"
                                               "    border: 2px solid #4a90e2;\n"
                                               "}")
        self.input_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.input_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_NhapKho.addWidget(
            self.input_note_textedit, 2, 15, 4, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.input_note_labels = QLabel(self.widget_nhap_tabin)
        self.input_note_labels.setObjectName(u"input_note_labels")
        sizePolicy.setHeightForWidth(
            self.input_note_labels.sizePolicy().hasHeightForWidth())
        self.input_note_labels.setSizePolicy(sizePolicy)
        self.input_note_labels.setFont(font1)
        self.input_note_labels.setTextFormat(Qt.AutoText)
        self.input_note_labels.setScaledContents(False)
        self.input_note_labels.setWordWrap(False)
        self.input_note_labels.setMargin(7)

        self.horizontalLayout_8.addWidget(self.input_note_labels)

        self.input_search_note_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_note_checkBox.setObjectName(
            u"input_search_note_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_note_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_note_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_note_checkBox.setMinimumSize(QSize(22, 24))
        self.input_search_note_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                      "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                      "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                      "}\n"
                                                      "\n"
                                                      "QCheckBox::indicator:unchecked {\n"
                                                      "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                      "}\n"
                                                      "\n"
                                                      "QCheckBox::indicator:checked {\n"
                                                      "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                      "}\n"
                                                      "")
        self.input_search_note_checkBox.setChecked(False)

        self.horizontalLayout_8.addWidget(self.input_search_note_checkBox)

        self.input_note_fillter_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.setObjectName(
            u"input_note_fillter_combobox")
        font2 = QFont()
        self.input_note_fillter_combobox.setFont(font2)
        self.input_note_fillter_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_note_fillter_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                       "QComboBox {\n"
                                                       "    background-color: #f0f0f0;\n"
                                                       "    border: 1px solid #ccc;\n"
                                                       "    border-radius: 4px;\n"
                                                       "    padding: 4px;\n"
                                                       "    font-size: 12px;\n"
                                                       "    color: #ff3907;\n"
                                                       "}\n"
                                                       "\n"
                                                       "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                       "QComboBox:focus {\n"
                                                       "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QComboBox::drop-down {\n"
                                                       "    border-left: 1px solid #ccc;\n"
                                                       "    width: 20px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QComboBox::down-arrow {\n"
                                                       "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                       "}")
        self.input_note_fillter_combobox.setEditable(False)

        self.horizontalLayout_8.addWidget(self.input_note_fillter_combobox)

        self.input_paste_button = QPushButton(self.widget_nhap_tabin)
        self.input_paste_button.setObjectName(u"input_paste_button")
        self.input_paste_button.setSizeIncrement(QSize(0, 40))
        self.input_paste_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_paste_button.setStyleSheet(u"/* QPushButton styling */\n"
                                              "QPushButton {\n"
                                              "    background-color: #4a90e2;\n"
                                              "    border: none;\n"
                                              "    border-radius: 10px;\n"
                                              "    color: #fff;\n"
                                              "    padding: 6px 12px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: #157117;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: #2a6cae;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:disabled {\n"
                                              "    background-color: #ccc;\n"
                                              "    color: #666;\n"
                                              "}")
        self.input_paste_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.input_paste_button)

        self.gridLayout_NhapKho.addLayout(self.horizontalLayout_8, 1, 15, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, -1, -1)
        self.input_storage_location_combobox = QComboBox(
            self.widget_nhap_tabin)
        self.input_storage_location_combobox.setObjectName(
            u"input_storage_location_combobox")
        self.input_storage_location_combobox.setMinimumSize(QSize(60, 0))
        self.input_storage_location_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_storage_location_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                           "QComboBox {\n"
                                                           "    background-color: #f0f0f0;\n"
                                                           "    border: 1px solid #ccc;\n"
                                                           "    border-radius: 4px;\n"
                                                           "    padding: 4px;\n"
                                                           "    font-size: 14px;\n"
                                                           "    color: #3333FF;\n"
                                                           "}\n"
                                                           "\n"
                                                           "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                           "QComboBox:focus {\n"
                                                           "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                           "}\n"
                                                           "\n"
                                                           "QComboBox::drop-down {\n"
                                                           "    border-left: 1px solid #ccc;\n"
                                                           "    width: 20px;\n"
                                                           "}\n"
                                                           "\n"
                                                           "QComboBox::down-arrow {\n"
                                                           "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                           "}")
        self.input_storage_location_combobox.setEditable(False)

        self.horizontalLayout_34.addWidget(
            self.input_storage_location_combobox)

        self.input_search_component_id_checkBox = QCheckBox(
            self.widget_nhap_tabin)
        self.input_search_component_id_checkBox.setObjectName(
            u"input_search_component_id_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_component_id_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_component_id_checkBox.setMinimumSize(QSize(22, 24))
        self.input_search_component_id_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                              "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                              "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:unchecked {\n"
                                                              "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:checked {\n"
                                                              "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                              "}\n"
                                                              "")
        self.input_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_34.addWidget(
            self.input_search_component_id_checkBox)

        self.input_component_id_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_component_id_lineedit.setObjectName(
            u"input_component_id_lineedit")
        self.input_component_id_lineedit.setMinimumSize(QSize(150, 0))
        self.input_component_id_lineedit.setFont(font2)
        self.input_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                       "    background-color: #f0f0f0;\n"
                                                       "    border: 1px solid #ccc;\n"
                                                       "    border-radius: 4px;\n"
                                                       "    padding: 4px;\n"
                                                       "    font-size: 14px;\n"
                                                       "    color: #3333FF;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QLineEdit:focus {\n"
                                                       "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                       "}")
        self.input_component_id_lineedit.setMaxLength(8)
        self.input_component_id_lineedit.setAlignment(Qt.AlignCenter)
        self.input_component_id_lineedit.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.input_component_id_lineedit)

        self.input_check_id_auto_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_check_id_auto_checkBox.setObjectName(
            u"input_check_id_auto_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_check_id_auto_checkBox.sizePolicy().hasHeightForWidth())
        self.input_check_id_auto_checkBox.setSizePolicy(sizePolicy1)
        self.input_check_id_auto_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                        "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                        "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:unchecked {\n"
                                                        "    image: url(:/icon/images/icon/check_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:checked {\n"
                                                        "    image: url(:/icon/images/icon/check_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                        "}\n"
                                                        "")
        self.input_check_id_auto_checkBox.setIconSize(QSize(16, 16))
        self.input_check_id_auto_checkBox.setChecked(False)

        self.horizontalLayout_34.addWidget(self.input_check_id_auto_checkBox)

        self.gridLayout_NhapKho.addLayout(self.horizontalLayout_34, 1, 3, 1, 1)

        self.input_qty_horizontalLayout = QHBoxLayout()
        self.input_qty_horizontalLayout.setSpacing(0)
        self.input_qty_horizontalLayout.setObjectName(
            u"input_qty_horizontalLayout")
        self.input_status_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_status_combobox.setObjectName(u"input_status_combobox")
        self.input_status_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_status_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_status_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                 "QComboBox {\n"
                                                 "    background-color: #f0f0f0;\n"
                                                 "    border: 1px solid #ccc;\n"
                                                 "    border-radius: 4px;\n"
                                                 "    padding: 4px;\n"
                                                 "    font-size: 14px;\n"
                                                 "    color: #3333FF;\n"
                                                 "}\n"
                                                 "\n"
                                                 "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                 "QComboBox:focus {\n"
                                                 "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::drop-down {\n"
                                                 "    border-left: 1px solid #ccc;\n"
                                                 "    width: 20px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::down-arrow {\n"
                                                 "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                 "}")
        self.input_status_combobox.setEditable(False)

        self.input_qty_horizontalLayout.addWidget(self.input_status_combobox)

        self.input_quantity_labels = QLabel(self.widget_nhap_tabin)
        self.input_quantity_labels.setObjectName(u"input_quantity_labels")
        sizePolicy.setHeightForWidth(
            self.input_quantity_labels.sizePolicy().hasHeightForWidth())
        self.input_quantity_labels.setSizePolicy(sizePolicy)
        self.input_quantity_labels.setFont(font1)
        self.input_quantity_labels.setMargin(7)

        self.input_qty_horizontalLayout.addWidget(self.input_quantity_labels)

        self.input_quantity_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_quantity_lineedit.setObjectName(u"input_quantity_lineedit")
        sizePolicy2.setHeightForWidth(
            self.input_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.input_quantity_lineedit.setSizePolicy(sizePolicy2)
        self.input_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                   "    background-color: #f0f0f0;\n"
                                                   "    border: 1px solid #ccc;\n"
                                                   "    border-radius: 4px;\n"
                                                   "    padding: 4px;\n"
                                                   "    font-size: 14px;\n"
                                                   "    color: #3333FF;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:focus {\n"
                                                   "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                   "}")
        self.input_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.input_qty_horizontalLayout.addWidget(self.input_quantity_lineedit)

        self.input_unit_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_unit_combobox.setObjectName(u"input_unit_combobox")
        sizePolicy1.setHeightForWidth(
            self.input_unit_combobox.sizePolicy().hasHeightForWidth())
        self.input_unit_combobox.setSizePolicy(sizePolicy1)
        self.input_unit_combobox.setMinimumSize(QSize(60, 0))
        self.input_unit_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_unit_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_unit_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                               "QComboBox {\n"
                                               "    background-color: #f0f0f0;\n"
                                               "    border: 1px solid #ccc;\n"
                                               "    border-radius: 4px;\n"
                                               "    padding: 4px;\n"
                                               "    font-size: 14px;\n"
                                               "    color: #3333FF;\n"
                                               "}\n"
                                               "\n"
                                               "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                               "QComboBox:focus {\n"
                                               "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox::drop-down {\n"
                                               "    border-left: 1px solid #ccc;\n"
                                               "    width: 20px;\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox::down-arrow {\n"
                                               "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                               "}")
        self.input_unit_combobox.setEditable(False)

        self.input_qty_horizontalLayout.addWidget(self.input_unit_combobox)

        self.gridLayout_NhapKho.addLayout(
            self.input_qty_horizontalLayout, 2, 3, 1, 1)

        self.input_process_labels = QLabel(self.widget_nhap_tabin)
        self.input_process_labels.setObjectName(u"input_process_labels")
        sizePolicy.setHeightForWidth(
            self.input_process_labels.sizePolicy().hasHeightForWidth())
        self.input_process_labels.setSizePolicy(sizePolicy)
        self.input_process_labels.setFont(font1)
        self.input_process_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(
            self.input_process_labels, 2, 6, 1, 1)

        self.input_search_component_name_checkBox = QCheckBox(
            self.widget_nhap_tabin)
        self.input_search_component_name_checkBox.setObjectName(
            u"input_search_component_name_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_component_name_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_component_name_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_component_name_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_component_name_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_component_name_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QCheckBox::indicator:unchecked {\n"
                                                                "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QCheckBox::indicator:checked {\n"
                                                                "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                "}\n"
                                                                "")
        self.input_search_component_name_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_component_name_checkBox, 1, 8, 1, 1)

        self.input_component_name_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_component_name_lineedit.setObjectName(
            u"input_component_name_lineedit")
        self.input_component_name_lineedit.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.input_component_name_lineedit.sizePolicy().hasHeightForWidth())
        self.input_component_name_lineedit.setSizePolicy(sizePolicy2)
        self.input_component_name_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                         "    background-color: #f0f0f0;\n"
                                                         "    border: 1px solid #ccc;\n"
                                                         "    border-radius: 4px;\n"
                                                         "    padding: 4px;\n"
                                                         "    font-size: 14px;\n"
                                                         "    color: #3333FF;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:focus {\n"
                                                         "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                         "}")
        self.input_component_name_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(
            self.input_component_name_lineedit, 1, 11, 1, 1)

        self.input_process_widget = QWidget(self.widget_nhap_tabin)
        self.input_process_widget.setObjectName(u"input_process_widget")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.input_process_widget.sizePolicy().hasHeightForWidth())
        self.input_process_widget.setSizePolicy(sizePolicy3)
        self.input_storage_location_widget_4 = QHBoxLayout(
            self.input_process_widget)
        self.input_storage_location_widget_4.setSpacing(0)
        self.input_storage_location_widget_4.setObjectName(
            u"input_storage_location_widget_4")
        self.input_storage_location_widget_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(
            self.input_process_widget, 2, 11, 1, 1)

        self.input_groups_widget = QWidget(self.widget_nhap_tabin)
        self.input_groups_widget.setObjectName(u"input_groups_widget")
        self.input_storage_location_widget_10 = QHBoxLayout(
            self.input_groups_widget)
        self.input_storage_location_widget_10.setSpacing(0)
        self.input_storage_location_widget_10.setObjectName(
            u"input_storage_location_widget_10")
        self.input_storage_location_widget_10.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(
            self.input_groups_widget, 3, 11, 1, 1)

        self.input_model_widget = QWidget(self.widget_nhap_tabin)
        self.input_model_widget.setObjectName(u"input_model_widget")
        self.input_storage_location_widget_8 = QHBoxLayout(
            self.input_model_widget)
        self.input_storage_location_widget_8.setSpacing(0)
        self.input_storage_location_widget_8.setObjectName(
            u"input_storage_location_widget_8")
        self.input_storage_location_widget_8.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(self.input_model_widget, 4, 11, 1, 1)

        self.input_material_widget = QWidget(self.widget_nhap_tabin)
        self.input_material_widget.setObjectName(u"input_material_widget")
        self.input_material_widget.setStyleSheet(u"")
        self.input_storage_location_widget_5 = QHBoxLayout(
            self.input_material_widget)
        self.input_storage_location_widget_5.setSpacing(0)
        self.input_storage_location_widget_5.setObjectName(
            u"input_storage_location_widget_5")
        self.input_storage_location_widget_5.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(
            self.input_material_widget, 3, 3, 1, 1)

        self.input_search_status_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_status_checkBox.setObjectName(
            u"input_search_status_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_status_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_status_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_status_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_status_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_status_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                        "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                        "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:unchecked {\n"
                                                        "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QCheckBox::indicator:checked {\n"
                                                        "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                        "}\n"
                                                        "")
        self.input_search_status_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_status_checkBox, 2, 1, 1, 1)

        self.input_size_labels = QLabel(self.widget_nhap_tabin)
        self.input_size_labels.setObjectName(u"input_size_labels")
        sizePolicy.setHeightForWidth(
            self.input_size_labels.sizePolicy().hasHeightForWidth())
        self.input_size_labels.setSizePolicy(sizePolicy)
        self.input_size_labels.setFont(font1)
        self.input_size_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_size_labels, 4, 0, 1, 1)

        self.input_search_size_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_size_checkBox.setObjectName(
            u"input_search_size_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_search_size_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_size_checkBox.setSizePolicy(sizePolicy1)
        self.input_search_size_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_size_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_size_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                      "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                      "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                      "}\n"
                                                      "\n"
                                                      "QCheckBox::indicator:unchecked {\n"
                                                      "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                      "}\n"
                                                      "\n"
                                                      "QCheckBox::indicator:checked {\n"
                                                      "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                      "}\n"
                                                      "")
        self.input_search_size_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(
            self.input_search_size_checkBox, 4, 1, 1, 1)

        self.input_images_label.raise_()
        self.input_note_textedit.raise_()
        self.input_search_storage_location_checkBox.raise_()
        self.input_storage_location_labels.raise_()
        self.input_size_labels.raise_()
        self.input_search_size_checkBox.raise_()
        self.input_component_name_labels.raise_()
        self.input_search_component_name_checkBox.raise_()
        self.input_component_name_lineedit.raise_()
        self.input_process_labels.raise_()
        self.input_search_process_checkBox.raise_()
        self.input_process_widget.raise_()
        self.input_groups_labels.raise_()
        self.input_search_groups_checkBox.raise_()
        self.input_groups_widget.raise_()
        self.input_model_labels.raise_()
        self.input_search_model_checkBox.raise_()
        self.input_model_widget.raise_()
        self.input_material_labels.raise_()
        self.input_search_material_checkBox.raise_()
        self.input_desinvoice_labels.raise_()
        self.input_search_desinvoice_checkBox.raise_()
        self.input_desinvoice_lineedit.raise_()
        self.input_invoice_labels.raise_()
        self.input_search_invoice_checkBox.raise_()
        self.input_invoice_lineedit.raise_()
        self.input_status_labels.raise_()
        self.input_search_status_checkBox.raise_()
        self.input_material_widget.raise_()

        self.verticalLayout_5.addWidget(self.widget_nhap_tabin)

        self.widget_button_tabin = QWidget(self.tabInput)
        self.widget_button_tabin.setObjectName(u"widget_button_tabin")
        self.inputButtonLayout = QHBoxLayout(self.widget_button_tabin)
        self.inputButtonLayout.setSpacing(5)
        self.inputButtonLayout.setObjectName(u"inputButtonLayout")
        self.inputButtonLayout.setContentsMargins(5, 5, 5, 5)
        self.input_filter_component_id_checkBox = QCheckBox(
            self.widget_button_tabin)
        self.input_filter_component_id_checkBox.setObjectName(
            u"input_filter_component_id_checkBox")
        sizePolicy1.setHeightForWidth(
            self.input_filter_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.input_filter_component_id_checkBox.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setBold(False)
        self.input_filter_component_id_checkBox.setFont(font3)
        self.input_filter_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                              "    width: 32px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                              "    height: 32px; /* Chi\u1ec1u cao icon */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:unchecked {\n"
                                                              "    image: url(:/icon/images/icon/filter_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:checked {\n"
                                                              "    image: url(:/icon/images/icon/filter_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                              "}\n"
                                                              "")
        self.input_filter_component_id_checkBox.setChecked(False)

        self.inputButtonLayout.addWidget(
            self.input_filter_component_id_checkBox)

        self.input_new_button = QPushButton(self.widget_button_tabin)
        self.input_new_button.setObjectName(u"input_new_button")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.input_new_button.sizePolicy().hasHeightForWidth())
        self.input_new_button.setSizePolicy(sizePolicy4)
        self.input_new_button.setMinimumSize(QSize(0, 40))
        self.input_new_button.setMaximumSize(QSize(16777215, 40))
        self.input_new_button.setSizeIncrement(QSize(0, 40))
        self.input_new_button.setFont(font1)
        self.input_new_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_new_button.setStyleSheet(u"/* QPushButton styling */\n"
                                            "QPushButton {\n"
                                            "    background-color: #4a90e2;\n"
                                            "    border: none;\n"
                                            "    border-radius: 10px;\n"
                                            "    color: #fff;\n"
                                            "    font-size: 12px;\n"
                                            "	font-weight: bold;\n"
                                            "    padding: 6px 12px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #357ab7;\n"
                                            "	font-size: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #2a6cae;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:disabled {\n"
                                            "    background-color: #ccc;\n"
                                            "    color: #666;\n"
                                            "}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icon/New.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.input_new_button.setIcon(icon1)
        self.input_new_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_new_button)

        self.input_edit_button = QPushButton(self.widget_button_tabin)
        self.input_edit_button.setObjectName(u"input_edit_button")
        sizePolicy4.setHeightForWidth(
            self.input_edit_button.sizePolicy().hasHeightForWidth())
        self.input_edit_button.setSizePolicy(sizePolicy4)
        self.input_edit_button.setMinimumSize(QSize(0, 40))
        self.input_edit_button.setMaximumSize(QSize(16777215, 40))
        self.input_edit_button.setSizeIncrement(QSize(0, 40))
        self.input_edit_button.setFont(font2)
        self.input_edit_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_edit_button.setStyleSheet(u"/* QPushButton - Modern style */\n"
                                             "QPushButton {\n"
                                             "    background-color: #ffd700;        /* M\u00e0u v\u00e0ng m\u1ec1m h\u01a1n */\n"
                                             "    border: 1px solid #e6c200;        /* Vi\u1ec1n nh\u1eb9 \u0111\u1ec3 t\u1ea1o chi\u1ec1u s\u00e2u */\n"
                                             "    border-radius: 8px;               /* Bo g\u00f3c nh\u1eb9 nh\u00e0ng */\n"
                                             "    color: #222;                      /* M\u00e0u ch\u1eef t\u1ed1i h\u01a1n \u0111\u1ec3 d\u1ec5 \u0111\u1ecdc */\n"
                                             "    font-size: 12px;\n"
                                             "    padding: 8px 16px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: #ffc400;        /* V\u00e0ng \u0111\u1eadm khi hover */\n"
                                             "    font-size: 15px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #e6b800;        /* M\u00e0u nh\u1ea5n m\u1ea1nh h\u01a1n */\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "    background-color: #f0f0f0;\n"
                                             "    border: 1px solid #ccc;\n"
                                             "    color: #aaa;\n"
                                             "}\n"
                                             "")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icon/Edit.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.input_edit_button.setIcon(icon2)
        self.input_edit_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_edit_button)

        self.input_delete_button = QPushButton(self.widget_button_tabin)
        self.input_delete_button.setObjectName(u"input_delete_button")
        sizePolicy4.setHeightForWidth(
            self.input_delete_button.sizePolicy().hasHeightForWidth())
        self.input_delete_button.setSizePolicy(sizePolicy4)
        self.input_delete_button.setMinimumSize(QSize(0, 40))
        self.input_delete_button.setMaximumSize(QSize(16777215, 40))
        self.input_delete_button.setSizeIncrement(QSize(0, 40))
        self.input_delete_button.setFont(font1)
        self.input_delete_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_delete_button.setStyleSheet(u"/* QPushButton - Red alert style */\n"
                                               "QPushButton {\n"
                                               "    background-color: #e53935;       /* \u0110\u1ecf c\u1ea3nh b\u00e1o hi\u1ec7n \u0111\u1ea1i */\n"
                                               "    border: none;\n"
                                               "    border-radius: 8px;\n"
                                               "    color: white;\n"
                                               "    font-size: 12px;\n"
                                               "    font-weight: bold;\n"
                                               "    padding: 8px 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: #d32f2f;       /* \u0110\u1ecf \u0111\u1eadm h\u01a1n khi hover */\n"
                                               "	font-size: 15px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: #b71c1c;       /* \u0110\u1ecf t\u1ed1i khi nh\u1ea5n */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:disabled {\n"
                                               "    background-color: #e0e0e0;\n"
                                               "    color: #999;\n"
                                               "}\n"
                                               "")
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/icon/Delete.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.input_delete_button.setIcon(icon3)
        self.input_delete_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_delete_button)

        self.input_export_button = QPushButton(self.widget_button_tabin)
        self.input_export_button.setObjectName(u"input_export_button")
        sizePolicy4.setHeightForWidth(
            self.input_export_button.sizePolicy().hasHeightForWidth())
        self.input_export_button.setSizePolicy(sizePolicy4)
        self.input_export_button.setMinimumSize(QSize(0, 40))
        self.input_export_button.setMaximumSize(QSize(16777215, 40))
        self.input_export_button.setSizeIncrement(QSize(0, 40))
        self.input_export_button.setFont(font1)
        self.input_export_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_export_button.setStyleSheet(u"/* QPushButton styling */\n"
                                               "QPushButton {\n"
                                               "    background-color: #4a90e2;\n"
                                               "    border: none;\n"
                                               "    border-radius: 10px;\n"
                                               "    color: #fff;\n"
                                               "    font-size: 12px;\n"
                                               "	font-weight: bold;\n"
                                               "    padding: 6px 12px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: #357ab7;\n"
                                               "	font-size: 14px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: #2a6cae;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:disabled {\n"
                                               "    background-color: #ccc;\n"
                                               "    color: #666;\n"
                                               "}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/icon/export_excel.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_export_button.setIcon(icon4)
        self.input_export_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_export_button)

        self.input_down_button = QPushButton(self.widget_button_tabin)
        self.input_down_button.setObjectName(u"input_down_button")
        sizePolicy4.setHeightForWidth(
            self.input_down_button.sizePolicy().hasHeightForWidth())
        self.input_down_button.setSizePolicy(sizePolicy4)
        self.input_down_button.setMinimumSize(QSize(0, 40))
        self.input_down_button.setMaximumSize(QSize(16777215, 40))
        self.input_down_button.setSizeIncrement(QSize(0, 40))
        self.input_down_button.setFont(font1)
        self.input_down_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_down_button.setStyleSheet(u"/* QPushButton styling */\n"
                                             "QPushButton {\n"
                                             "    background-color: #08e7f6;\n"
                                             "    border: none;\n"
                                             "    border-radius: 10px;\n"
                                             "    font-size: 12px;\n"
                                             "	font-weight: bold;\n"
                                             "    padding: 6px 12px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: #08d1f6;\n"
                                             "	font-size: 14px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #08d1f6;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "    background-color: #ccc;\n"
                                             "    color: #666;\n"
                                             "}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/images/icon/down_image.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_down_button.setIcon(icon5)
        self.input_down_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_down_button)

        self.input_search_button = QPushButton(self.widget_button_tabin)
        self.input_search_button.setObjectName(u"input_search_button")
        sizePolicy4.setHeightForWidth(
            self.input_search_button.sizePolicy().hasHeightForWidth())
        self.input_search_button.setSizePolicy(sizePolicy4)
        self.input_search_button.setMinimumSize(QSize(0, 40))
        self.input_search_button.setMaximumSize(QSize(16777215, 40))
        self.input_search_button.setSizeIncrement(QSize(0, 40))
        self.input_search_button.setFont(font1)
        self.input_search_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
                                               "QPushButton {\n"
                                               "    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
                                               "    border: none;\n"
                                               "    border-radius: 8px;\n"
                                               "    color: white;\n"
                                               "    font-size: 12px;\n"
                                               "    font-weight: bold;\n"
                                               "    padding: 8px 16px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
                                               "    font-size: 15px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:disabled {\n"
                                               "    background-color: #d3d3d3;\n"
                                               "    color: #888;\n"
                                               "}\n"
                                               "")
        icon6 = QIcon()
        icon6.addFile(u":/icon/images/icon/Search.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.input_search_button.setIcon(icon6)
        self.input_search_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_search_button)

        self.verticalLayout_5.addWidget(self.widget_button_tabin)

        self.input_data_tableView = QTableView(self.tabInput)
        self.input_data_tableView.setObjectName(u"input_data_tableView")
        self.input_data_tableView.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.input_data_tableView.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.input_data_tableView.setSelectionBehavior(
            QAbstractItemView.SelectRows)

        self.verticalLayout_5.addWidget(self.input_data_tableView)

        icon7 = QIcon()
        icon7.addFile(u":/icon/images/icon/stock_entry_logo.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabInput, icon7, "")
        self.tabOutput = QWidget()
        self.tabOutput.setObjectName(u"tabOutput")
        self.verticalLayout_6 = QVBoxLayout(self.tabOutput)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabout = QWidget(self.tabOutput)
        self.widget_nhap_tabout.setObjectName(u"widget_nhap_tabout")
        self.widget_nhap_tabout.setMaximumSize(QSize(16777215, 220))
        self.gridLayout_4 = QGridLayout(self.widget_nhap_tabout)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.output_quantity_label = QLabel(self.widget_nhap_tabout)
        self.output_quantity_label.setObjectName(u"output_quantity_label")
        self.output_quantity_label.setFont(font1)

        self.gridLayout_4.addWidget(self.output_quantity_label, 4, 0, 1, 1)

        self.output_note_textedit = QTextEdit(self.widget_nhap_tabout)
        self.output_note_textedit.setObjectName(u"output_note_textedit")
        self.output_note_textedit.setMinimumSize(QSize(250, 0))
        self.output_note_textedit.setFont(font3)
        self.output_note_textedit.setStyleSheet(u"QTextEdit {\n"
                                                "	background-color: rgb(255, 255, 255);\n"
                                                "    border: 2px solid #ccc;\n"
                                                "    border-radius: 6px;\n"
                                                "    padding: 5px;\n"
                                                "    color: #3333FF;\n"
                                                "}\n"
                                                "\n"
                                                "QTextEdit:focus {\n"
                                                "    border: 2px solid #4a90e2;\n"
                                                "}")
        self.output_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.output_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.output_note_textedit, 2, 8, 4, 1)

        self.output_images_label = QLabel(self.widget_nhap_tabout)
        self.output_images_label.setObjectName(u"output_images_label")
        sizePolicy1.setHeightForWidth(
            self.output_images_label.sizePolicy().hasHeightForWidth())
        self.output_images_label.setSizePolicy(sizePolicy1)
        self.output_images_label.setMinimumSize(QSize(280, 200))
        self.output_images_label.setMaximumSize(QSize(280, 16777215))
        self.output_images_label.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.output_images_label.setStyleSheet(u"/* QLabel styling */\n"
                                               "QLabel {\n"
                                               "    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
                                               "    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
                                               "    border-radius: 10px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
                                               "    padding: 5px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
                                               "    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
                                               "}")
        self.output_images_label.setFrameShape(QFrame.StyledPanel)
        self.output_images_label.setPixmap(
            QPixmap(u":/icon/images/icon/no_image.png"))
        self.output_images_label.setScaledContents(True)
        self.output_images_label.setWordWrap(False)

        self.gridLayout_4.addWidget(self.output_images_label, 1, 9, 5, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.output_storage_location_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_storage_location_label_2.setObjectName(
            u"output_storage_location_label_2")
        self.output_storage_location_label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.output_storage_location_label_2)

        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.output_storage_location_label = QLabel(self.widget_nhap_tabout)
        self.output_storage_location_label.setObjectName(
            u"output_storage_location_label")
        sizePolicy1.setHeightForWidth(
            self.output_storage_location_label.sizePolicy().hasHeightForWidth())
        self.output_storage_location_label.setSizePolicy(sizePolicy1)
        self.output_storage_location_label.setMinimumSize(QSize(120, 38))
        self.output_storage_location_label.setMaximumSize(QSize(120, 38))
        self.output_storage_location_label.setFont(font1)
        self.output_storage_location_label.setStyleSheet(u"QLabel {\n"
                                                         "    background-color: #f0f0f0;\n"
                                                         "    border: 1px solid #ccc;\n"
                                                         "    border-radius: 4px;\n"
                                                         "    padding: 4px;\n"
                                                         "    color: #333;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLabel:focus {\n"
                                                         "    border: 1px solid #4a90e2;\n"
                                                         "}")
        self.output_storage_location_label.setAlignment(Qt.AlignCenter)
        self.output_storage_location_label.setMargin(7)

        self.horizontalLayout_5.addWidget(self.output_storage_location_label)

        self.output_search_component_id_checkBox = QCheckBox(
            self.widget_nhap_tabout)
        self.output_search_component_id_checkBox.setObjectName(
            u"output_search_component_id_checkBox")
        sizePolicy1.setHeightForWidth(
            self.output_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.output_search_component_id_checkBox.setSizePolicy(sizePolicy1)
        self.output_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                               "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                               "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                               "}\n"
                                                               "\n"
                                                               "QCheckBox::indicator:unchecked {\n"
                                                               "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                               "}\n"
                                                               "\n"
                                                               "QCheckBox::indicator:checked {\n"
                                                               "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                               "}\n"
                                                               "")
        self.output_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_5.addWidget(
            self.output_search_component_id_checkBox)

        self.output_component_id_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_component_id_lineedit.setObjectName(
            u"output_component_id_lineedit")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.output_component_id_lineedit.sizePolicy().hasHeightForWidth())
        self.output_component_id_lineedit.setSizePolicy(sizePolicy5)
        self.output_component_id_lineedit.setFont(font2)
        self.output_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                        "    background-color: #f0f0f0;\n"
                                                        "    border: 1px solid #ccc;\n"
                                                        "    border-radius: 4px;\n"
                                                        "    padding: 4px;\n"
                                                        "    font-size: 14px;\n"
                                                        "    color: #3333FF;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:focus {\n"
                                                        "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                        "}")
        self.output_component_id_lineedit.setMaxLength(8)
        self.output_component_id_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.output_component_id_lineedit)

        self.output_check_id_auto_checkBox = QCheckBox(self.widget_nhap_tabout)
        self.output_check_id_auto_checkBox.setObjectName(
            u"output_check_id_auto_checkBox")
        sizePolicy1.setHeightForWidth(
            self.output_check_id_auto_checkBox.sizePolicy().hasHeightForWidth())
        self.output_check_id_auto_checkBox.setSizePolicy(sizePolicy1)
        self.output_check_id_auto_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                         "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                         "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:unchecked {\n"
                                                         "    image: url(:/icon/images/icon/load_off.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCheckBox::indicator:checked {\n"
                                                         "    image: url(:/icon/images/icon/load_on.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                         "}\n"
                                                         "")
        self.output_check_id_auto_checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.output_check_id_auto_checkBox)

        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        self.output_desinvoice_labels_2 = QLabel(self.widget_nhap_tabout)
        self.output_desinvoice_labels_2.setObjectName(
            u"output_desinvoice_labels_2")
        self.output_desinvoice_labels_2.setFont(font1)
        self.output_desinvoice_labels_2.setMargin(7)

        self.gridLayout_4.addWidget(
            self.output_desinvoice_labels_2, 5, 4, 1, 1)

        self.output_desinvoice_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_desinvoice_lineedit.setObjectName(
            u"output_desinvoice_lineedit")
        sizePolicy3.setHeightForWidth(
            self.output_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.output_desinvoice_lineedit.setSizePolicy(sizePolicy3)
        self.output_desinvoice_lineedit.setFont(font2)
        self.output_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                      "    background-color: #f0f0f0;\n"
                                                      "    border: 1px solid #ccc;\n"
                                                      "    border-radius: 4px;\n"
                                                      "    padding: 4px;\n"
                                                      "    font-size: 14px;\n"
                                                      "    color: #3333FF;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:focus {\n"
                                                      "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                      "}")
        self.output_desinvoice_lineedit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(
            self.output_desinvoice_lineedit, 5, 5, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.output_note_label = QLabel(self.widget_nhap_tabout)
        self.output_note_label.setObjectName(u"output_note_label")
        self.output_note_label.setFont(font1)
        self.output_note_label.setTextFormat(Qt.AutoText)
        self.output_note_label.setScaledContents(False)
        self.output_note_label.setWordWrap(False)
        self.output_note_label.setMargin(0)

        self.horizontalLayout_32.addWidget(self.output_note_label)

        self.output_search_note_checkBox = QCheckBox(self.widget_nhap_tabout)
        self.output_search_note_checkBox.setObjectName(
            u"output_search_note_checkBox")
        sizePolicy1.setHeightForWidth(
            self.output_search_note_checkBox.sizePolicy().hasHeightForWidth())
        self.output_search_note_checkBox.setSizePolicy(sizePolicy1)
        self.output_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                       "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                       "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QCheckBox::indicator:unchecked {\n"
                                                       "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QCheckBox::indicator:checked {\n"
                                                       "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                       "}\n"
                                                       "")
        self.output_search_note_checkBox.setChecked(False)

        self.horizontalLayout_32.addWidget(self.output_search_note_checkBox)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer)

        self.gridLayout_4.addLayout(self.horizontalLayout_32, 1, 8, 1, 1)

        self.output_component_name_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_component_name_label_2.setObjectName(
            u"output_component_name_label_2")
        self.output_component_name_label_2.setFont(font1)
        self.output_component_name_label_2.setMargin(7)

        self.gridLayout_4.addWidget(
            self.output_component_name_label_2, 1, 4, 1, 1)

        self.output_process_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_process_label_2.setObjectName(u"output_process_label_2")
        self.output_process_label_2.setFont(font1)
        self.output_process_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_process_label_2, 2, 4, 1, 1)

        self.output_process_widget = QWidget(self.widget_nhap_tabout)
        self.output_process_widget.setObjectName(u"output_process_widget")
        self.output_process_widget.setSizeIncrement(QSize(0, 0))
        self.output_process_widget.setStyleSheet(u"")
        self.input_storage_location_widget_9 = QHBoxLayout(
            self.output_process_widget)
        self.input_storage_location_widget_9.setSpacing(0)
        self.input_storage_location_widget_9.setObjectName(
            u"input_storage_location_widget_9")
        self.input_storage_location_widget_9.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.output_process_widget, 2, 5, 1, 1)

        self.output_groups_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_groups_label_2.setObjectName(u"output_groups_label_2")
        self.output_groups_label_2.setFont(font1)
        self.output_groups_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_groups_label_2, 3, 4, 1, 1)

        self.output_groups_widget = QWidget(self.widget_nhap_tabout)
        self.output_groups_widget.setObjectName(u"output_groups_widget")
        self.output_groups_widget.setSizeIncrement(QSize(0, 0))
        self.output_groups_widget.setStyleSheet(u"")
        self.input_storage_location_widget_11 = QHBoxLayout(
            self.output_groups_widget)
        self.input_storage_location_widget_11.setSpacing(0)
        self.input_storage_location_widget_11.setObjectName(
            u"input_storage_location_widget_11")
        self.input_storage_location_widget_11.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.output_groups_widget, 3, 5, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.output_quantity_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_quantity_lineedit.setObjectName(
            u"output_quantity_lineedit")
        sizePolicy.setHeightForWidth(
            self.output_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.output_quantity_lineedit.setSizePolicy(sizePolicy)
        self.output_quantity_lineedit.setFont(font2)
        self.output_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                    "    background-color: #f0f0f0;\n"
                                                    "    border: 1px solid #ccc;\n"
                                                    "    border-radius: 4px;\n"
                                                    "    padding: 4px;\n"
                                                    "    font-size: 14px;\n"
                                                    "    color: #3333FF;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:focus {\n"
                                                    "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                    "}")
        self.output_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.output_quantity_lineedit)

        self.output_inventory_label = QLabel(self.widget_nhap_tabout)
        self.output_inventory_label.setObjectName(u"output_inventory_label")
        sizePolicy2.setHeightForWidth(
            self.output_inventory_label.sizePolicy().hasHeightForWidth())
        self.output_inventory_label.setSizePolicy(sizePolicy2)
        self.output_inventory_label.setMinimumSize(QSize(0, 38))
        self.output_inventory_label.setMaximumSize(QSize(16777215, 38))
        self.output_inventory_label.setStyleSheet(u"QLabel {\n"
                                                  "    background-color: #f0f0f0;\n"
                                                  "    border: 1px solid #ccc;\n"
                                                  "    border-radius: 4px;\n"
                                                  "    padding: 4px;\n"
                                                  "    color: #333;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel:focus {\n"
                                                  "    border: 1px solid #4a90e2;\n"
                                                  "}")
        self.output_inventory_label.setAlignment(Qt.AlignCenter)
        self.output_inventory_label.setMargin(7)

        self.horizontalLayout.addWidget(self.output_inventory_label)

        self.output_unit_label = QLabel(self.widget_nhap_tabout)
        self.output_unit_label.setObjectName(u"output_unit_label")
        sizePolicy1.setHeightForWidth(
            self.output_unit_label.sizePolicy().hasHeightForWidth())
        self.output_unit_label.setSizePolicy(sizePolicy1)
        self.output_unit_label.setMinimumSize(QSize(40, 38))
        self.output_unit_label.setMaximumSize(QSize(40, 38))
        self.output_unit_label.setFont(font3)
        self.output_unit_label.setStyleSheet(u"QLabel {\n"
                                             "    background-color: #f0f0f0;\n"
                                             "    border: 1px solid #ccc;\n"
                                             "    border-radius: 4px;\n"
                                             "    padding: 4px;\n"
                                             "    color: #333;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel:focus {\n"
                                             "    border: 1px solid #4a90e2;\n"
                                             "}")
        self.output_unit_label.setAlignment(Qt.AlignCenter)
        self.output_unit_label.setMargin(0)

        self.horizontalLayout.addWidget(self.output_unit_label)

        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 2, 1, 1)

        self.output_invoice_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_invoice_label_2.setObjectName(u"output_invoice_label_2")
        self.output_invoice_label_2.setFont(font1)
        self.output_invoice_label_2.setMargin(0)

        self.gridLayout_4.addWidget(self.output_invoice_label_2, 5, 0, 1, 1)

        self.output_invoice_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_invoice_lineedit.setObjectName(u"output_invoice_lineedit")
        sizePolicy3.setHeightForWidth(
            self.output_invoice_lineedit.sizePolicy().hasHeightForWidth())
        self.output_invoice_lineedit.setSizePolicy(sizePolicy3)
        self.output_invoice_lineedit.setFont(font2)
        self.output_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                   "    background-color: #f0f0f0;\n"
                                                   "    border: 1px solid #ccc;\n"
                                                   "    border-radius: 4px;\n"
                                                   "    padding: 4px;\n"
                                                   "    font-size: 14px;\n"
                                                   "    color: #3333FF;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:focus {\n"
                                                   "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                   "}")
        self.output_invoice_lineedit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.output_invoice_lineedit, 5, 2, 1, 1)

        self.output_model_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_model_label_2.setObjectName(u"output_model_label_2")
        self.output_model_label_2.setFont(font1)
        self.output_model_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_model_label_2, 4, 4, 1, 1)

        self.output_model_widget = QWidget(self.widget_nhap_tabout)
        self.output_model_widget.setObjectName(u"output_model_widget")
        self.output_model_widget.setSizeIncrement(QSize(0, 0))
        self.output_model_widget.setStyleSheet(u"")
        self.input_storage_location_widget_6 = QHBoxLayout(
            self.output_model_widget)
        self.input_storage_location_widget_6.setSpacing(0)
        self.input_storage_location_widget_6.setObjectName(
            u"input_storage_location_widget_6")
        self.input_storage_location_widget_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.output_model_widget, 4, 5, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output_status_label = QLabel(self.widget_nhap_tabout)
        self.output_status_label.setObjectName(u"output_status_label")
        sizePolicy2.setHeightForWidth(
            self.output_status_label.sizePolicy().hasHeightForWidth())
        self.output_status_label.setSizePolicy(sizePolicy2)
        self.output_status_label.setMinimumSize(QSize(0, 38))
        self.output_status_label.setMaximumSize(QSize(16777215, 38))
        self.output_status_label.setStyleSheet(u"QLabel {\n"
                                               "    background-color: #f0f0f0;\n"
                                               "    border: 1px solid #ccc;\n"
                                               "    border-radius: 4px;\n"
                                               "    padding: 4px;\n"
                                               "    color: #333;\n"
                                               "}\n"
                                               "\n"
                                               "QLabel:focus {\n"
                                               "    border: 1px solid #4a90e2;\n"
                                               "}")
        self.output_status_label.setAlignment(Qt.AlignCenter)
        self.output_status_label.setMargin(7)

        self.horizontalLayout_2.addWidget(self.output_status_label)

        self.output_size_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_size_label_2.setObjectName(u"output_size_label_2")
        sizePolicy.setHeightForWidth(
            self.output_size_label_2.sizePolicy().hasHeightForWidth())
        self.output_size_label_2.setSizePolicy(sizePolicy)
        self.output_size_label_2.setFont(font1)
        self.output_size_label_2.setMargin(7)

        self.horizontalLayout_2.addWidget(self.output_size_label_2)

        self.output_size_label = QLabel(self.widget_nhap_tabout)
        self.output_size_label.setObjectName(u"output_size_label")
        sizePolicy2.setHeightForWidth(
            self.output_size_label.sizePolicy().hasHeightForWidth())
        self.output_size_label.setSizePolicy(sizePolicy2)
        self.output_size_label.setMinimumSize(QSize(0, 38))
        self.output_size_label.setMaximumSize(QSize(16777215, 38))
        font4 = QFont()
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setStyleStrategy(QFont.NoAntialias)
        self.output_size_label.setFont(font4)
        self.output_size_label.setStyleSheet(u"QLabel {\n"
                                             "    background-color: #f0f0f0;\n"
                                             "    border: 1px solid #ccc;\n"
                                             "    border-radius: 4px;\n"
                                             "    padding: 4px;\n"
                                             "    color: #333;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel:focus {\n"
                                             "    border: 1px solid #4a90e2;\n"
                                             "}")
        self.output_size_label.setAlignment(Qt.AlignCenter)
        self.output_size_label.setMargin(7)

        self.horizontalLayout_2.addWidget(self.output_size_label)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)

        self.output_component_name_label = QLabel(self.widget_nhap_tabout)
        self.output_component_name_label.setObjectName(
            u"output_component_name_label")
        self.output_component_name_label.setMaximumSize(QSize(16777215, 38))
        self.output_component_name_label.setStyleSheet(u"QLabel {\n"
                                                       "    background-color: #f0f0f0;\n"
                                                       "    border: 1px solid #ccc;\n"
                                                       "    border-radius: 4px;\n"
                                                       "    padding: 4px;\n"
                                                       "    color: #333;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QLabel:focus {\n"
                                                       "    border: 1px solid #4a90e2;\n"
                                                       "}")
        self.output_component_name_label.setMargin(7)

        self.gridLayout_4.addWidget(
            self.output_component_name_label, 1, 5, 1, 1)

        self.output_material_widget = QWidget(self.widget_nhap_tabout)
        self.output_material_widget.setObjectName(u"output_material_widget")
        self.output_material_widget.setSizeIncrement(QSize(0, 0))
        self.output_material_widget.setStyleSheet(u"")
        self.input_storage_location_widget_7 = QHBoxLayout(
            self.output_material_widget)
        self.input_storage_location_widget_7.setSpacing(0)
        self.input_storage_location_widget_7.setObjectName(
            u"input_storage_location_widget_7")
        self.input_storage_location_widget_7.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.output_material_widget, 2, 2, 1, 1)

        self.output_status_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_status_label_2.setObjectName(u"output_status_label_2")
        self.output_status_label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.output_status_label_2, 3, 0, 1, 1)

        self.output_material_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_material_label_2.setObjectName(u"output_material_label_2")
        self.output_material_label_2.setFont(font1)
        self.output_material_label_2.setMargin(0)

        self.gridLayout_4.addWidget(self.output_material_label_2, 2, 0, 1, 1)

        self.output_images_label.raise_()
        self.output_quantity_label.raise_()
        self.output_note_textedit.raise_()
        self.output_desinvoice_labels_2.raise_()
        self.output_desinvoice_lineedit.raise_()
        self.output_component_name_label_2.raise_()
        self.output_process_label_2.raise_()
        self.output_process_widget.raise_()
        self.output_groups_label_2.raise_()
        self.output_groups_widget.raise_()
        self.output_invoice_label_2.raise_()
        self.output_invoice_lineedit.raise_()
        self.output_model_label_2.raise_()
        self.output_model_widget.raise_()
        self.output_component_name_label.raise_()
        self.output_material_widget.raise_()
        self.output_status_label_2.raise_()
        self.output_material_label_2.raise_()

        self.verticalLayout_6.addWidget(self.widget_nhap_tabout)

        self.widget_button_tabout = QWidget(self.tabOutput)
        self.widget_button_tabout.setObjectName(u"widget_button_tabout")
        self.widget_button_tabout.setMaximumSize(QSize(16777215, 60))
        self.outputButtonLayout = QHBoxLayout(self.widget_button_tabout)
        self.outputButtonLayout.setSpacing(5)
        self.outputButtonLayout.setObjectName(u"outputButtonLayout")
        self.outputButtonLayout.setContentsMargins(5, 5, 5, 5)
        self.output_new_button = QPushButton(self.widget_button_tabout)
        self.output_new_button.setObjectName(u"output_new_button")
        sizePolicy4.setHeightForWidth(
            self.output_new_button.sizePolicy().hasHeightForWidth())
        self.output_new_button.setSizePolicy(sizePolicy4)
        self.output_new_button.setMinimumSize(QSize(0, 40))
        self.output_new_button.setFont(font2)
        self.output_new_button.setStyleSheet(u"/* QPushButton styling */\n"
                                             "QPushButton {\n"
                                             "    background-color: #4a90e2;\n"
                                             "    border: none;\n"
                                             "    border-radius: 10px;\n"
                                             "    color: #fff;\n"
                                             "    font-size: 12px;\n"
                                             "    padding: 6px 12px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: #357ab7;\n"
                                             "	font: 75 14pt;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #2a6cae;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "    background-color: #ccc;\n"
                                             "    color: #666;\n"
                                             "}")
        self.output_new_button.setIcon(icon1)
        self.output_new_button.setIconSize(QSize(36, 32))

        self.outputButtonLayout.addWidget(self.output_new_button)

        self.output_delete_button = QPushButton(self.widget_button_tabout)
        self.output_delete_button.setObjectName(u"output_delete_button")
        sizePolicy4.setHeightForWidth(
            self.output_delete_button.sizePolicy().hasHeightForWidth())
        self.output_delete_button.setSizePolicy(sizePolicy4)
        self.output_delete_button.setMinimumSize(QSize(0, 40))
        self.output_delete_button.setFont(font1)
        self.output_delete_button.setStyleSheet(u"/* QPushButton - Red alert style */\n"
                                                "QPushButton {\n"
                                                "    background-color: #e53935;       /* \u0110\u1ecf c\u1ea3nh b\u00e1o hi\u1ec7n \u0111\u1ea1i */\n"
                                                "    border: none;\n"
                                                "    border-radius: 8px;\n"
                                                "    color: white;\n"
                                                "    font-size: 13px;\n"
                                                "    font-weight: bold;\n"
                                                "    padding: 8px 16px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #d32f2f;       /* \u0110\u1ecf \u0111\u1eadm h\u01a1n khi hover */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #b71c1c;       /* \u0110\u1ecf t\u1ed1i khi nh\u1ea5n */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #e0e0e0;\n"
                                                "    color: #999;\n"
                                                "}\n"
                                                "")
        self.output_delete_button.setIcon(icon3)
        self.output_delete_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_delete_button)

        self.output_export_button = QPushButton(self.widget_button_tabout)
        self.output_export_button.setObjectName(u"output_export_button")
        sizePolicy4.setHeightForWidth(
            self.output_export_button.sizePolicy().hasHeightForWidth())
        self.output_export_button.setSizePolicy(sizePolicy4)
        self.output_export_button.setMinimumSize(QSize(0, 40))
        self.output_export_button.setFont(font2)
        self.output_export_button.setStyleSheet(u"/* QPushButton styling */\n"
                                                "QPushButton {\n"
                                                "    background-color: #4a90e2;\n"
                                                "    border: none;\n"
                                                "    border-radius: 10px;\n"
                                                "    color: #fff;\n"
                                                "    font-size: 12px;\n"
                                                "    padding: 6px 12px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #357ab7;\n"
                                                "	font: 75 14pt;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #2a6cae;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #ccc;\n"
                                                "    color: #666;\n"
                                                "}")
        self.output_export_button.setIcon(icon4)
        self.output_export_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_export_button)

        self.output_search_button = QPushButton(self.widget_button_tabout)
        self.output_search_button.setObjectName(u"output_search_button")
        sizePolicy4.setHeightForWidth(
            self.output_search_button.sizePolicy().hasHeightForWidth())
        self.output_search_button.setSizePolicy(sizePolicy4)
        self.output_search_button.setMinimumSize(QSize(0, 40))
        self.output_search_button.setFont(font1)
        self.output_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
                                                "QPushButton {\n"
                                                "    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
                                                "    border: none;\n"
                                                "    border-radius: 8px;\n"
                                                "    color: white;\n"
                                                "    font-size: 12px;\n"
                                                "    font-weight: bold;\n"
                                                "    padding: 8px 16px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
                                                "    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #d3d3d3;\n"
                                                "    color: #888;\n"
                                                "}\n"
                                                "")
        self.output_search_button.setIcon(icon6)
        self.output_search_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_search_button)

        self.verticalLayout_6.addWidget(self.widget_button_tabout)

        self.output_data_tablewidget = QTableWidget(self.tabOutput)
        if (self.output_data_tablewidget.columnCount() < 3):
            self.output_data_tablewidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(
            0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(
            1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(
            2, __qtablewidgetitem2)
        self.output_data_tablewidget.setObjectName(u"output_data_tablewidget")
        self.output_data_tablewidget.setStyleSheet(u"/* QTableWidget styling */\n"
                                                   "QTableWidget {\n"
                                                   "    background-color: #f9fbfd; /* N\u1ec1n b\u1ea3ng xanh nh\u1ea1t */\n"
                                                   "    border: 1px solid #d3d9e3; /* \u0110\u01b0\u1eddng vi\u1ec1n nh\u1eb9 */\n"
                                                   "    font-size: 12px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
                                                   "    color: #333333; /* M\u00e0u ch\u1eef ch\u00ednh */\n"
                                                   "    gridline-color: #e7edf3; /* M\u00e0u \u0111\u01b0\u1eddng l\u01b0\u1edbi nh\u1ea1t */\n"
                                                   "    selection-background-color: #3b82cc; /* M\u00e0u n\u1ec1n khi ch\u1ecdn */\n"
                                                   "    selection-color: #ffffff; /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
                                                   "    outline: none; /* Lo\u1ea1i b\u1ecf vi\u1ec1n s\u00e1ng khi focus */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Ti\u00eau \u0111\u1ec1 c\u1ed9t */\n"
                                                   "QHeaderView::section {\n"
                                                   "    background-color: #e5effb; /* N\u1ec1n ti\u00eau \u0111\u1ec1 xanh nh\u1ea1t */\n"
                                                   "    color: #4a4a4a; /* M\u00e0u ch\u1eef ti\u00eau \u0111\u1ec1 */\n"
                                                   "    padding: 10px;\n"
                                                   "    border: 1px solid #d3d9e3; /* Vi\u1ec1n gi\u1eefa c\u00e1c ti\u00eau \u0111\u1ec1 */\n"
                                                   "    font-size"
                                                   ": 12px;\n"
                                                   "    font-weight: bold;\n"
                                                   "    text-align: center;\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* C\u00e1c \u00f4 */\n"
                                                   "QTableWidget::item {\n"
                                                   "    background-color: #ffffff; /* N\u1ec1n \u00f4 m\u1eb7c \u0111\u1ecbnh */\n"
                                                   "    border: none;\n"
                                                   "    padding: 8px;\n"
                                                   "    font-size: 13px;\n"
                                                   "    color: #333333; /* M\u00e0u ch\u1eef */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* \u00d4 xen k\u1ebd */\n"
                                                   "QTableWidget::item:alternate {\n"
                                                   "    background-color: #f4f8fc; /* N\u1ec1n xen k\u1ebd xanh nh\u1eb9 */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Hi\u1ec7u \u1ee9ng hover */\n"
                                                   "QTableWidget::item:hover {\n"
                                                   "    background-color: #dceaf7; /* M\u00e0u hover xanh nh\u1ea1t */\n"
                                                   "    color: #333333; /* Ch\u1eef v\u1eabn d\u1ec5 \u0111\u1ecdc */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Hi\u1ec7u \u1ee9ng hover n\u1ed5i b\u1eadt to\u00e0n d\u00f2ng */\n"
                                                   "QTableWidget::row:hover {\n"
                                                   "    background-color: #cce1f4; /* N\u1ec1n hover n\u1ed5i b\u1eadt c\u1ea3 d\u00f2ng */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Hi\u1ec7u \u1ee9ng khi ch\u1ecdn */\n"
                                                   "QTableWidget::item:selected {\n"
                                                   "    background-color: #3b82cc; /* M"
                                                   "\u00e0u n\u1ec1n xanh \u0111\u1eadm khi ch\u1ecdn */\n"
                                                   "    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng khi ch\u1ecdn */\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Scrollbar */\n"
                                                   "QScrollBar:vertical {\n"
                                                   "    border: none;\n"
                                                   "    background: #f4f8fc; /* N\u1ec1n thanh cu\u1ed9n xanh nh\u1ea1t */\n"
                                                   "    width: 12px;\n"
                                                   "    margin: 2px 0;\n"
                                                   "    border-radius: 6px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QScrollBar::handle:vertical {\n"
                                                   "    background: #3b82cc; /* Thanh tr\u01b0\u1ee3t xanh \u0111\u1eadm */\n"
                                                   "    min-height: 20px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QScrollBar::handle:vertical:hover {\n"
                                                   "    background: #2f6fa5; /* Thanh tr\u01b0\u1ee3t khi hover */\n"
                                                   "}\n"
                                                   "\n"
                                                   "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
                                                   "    background: none;\n"
                                                   "    border: none;\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* G\u00f3c cu\u1ed9n */\n"
                                                   "QScrollBar::corner {\n"
                                                   "    background: #ffffff;\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Hi\u1ec7u \u1ee9ng khi focus */\n"
                                                   "QTableWidget:focus {\n"
                                                   "    border: 1px solid #3b82cc; /* Vi\u1ec1n xanh \u0111\u1eadm khi focus */\n"
                                                   "}\n"
                                                   "")
        self.output_data_tablewidget.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.output_data_tablewidget.setSelectionBehavior(
            QAbstractItemView.SelectRows)

        self.verticalLayout_6.addWidget(self.output_data_tablewidget)

        icon8 = QIcon()
        icon8.addFile(u":/icon/images/icon/stock_release_logo.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabOutput, icon8, "")
        self.tabLayout = QWidget()
        self.tabLayout.setObjectName(u"tabLayout")
        self.verticalLayout_7 = QVBoxLayout(self.tabLayout)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.widget_search_tablayout = QWidget(self.tabLayout)
        self.widget_search_tablayout.setObjectName(u"widget_search_tablayout")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_search_tablayout)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.layout_process_label = QLabel(self.widget_search_tablayout)
        self.layout_process_label.setObjectName(u"layout_process_label")
        sizePolicy.setHeightForWidth(
            self.layout_process_label.sizePolicy().hasHeightForWidth())
        self.layout_process_label.setSizePolicy(sizePolicy)
        self.layout_process_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.layout_process_label)

        self.layout_search_process_radio = QRadioButton(
            self.widget_search_tablayout)
        self.layout_search_process_radio.setObjectName(
            u"layout_search_process_radio")
        sizePolicy1.setHeightForWidth(
            self.layout_search_process_radio.sizePolicy().hasHeightForWidth())
        self.layout_search_process_radio.setSizePolicy(sizePolicy1)
        self.layout_search_process_radio.setStyleSheet(u"QRadioButton::indicator {\n"
                                                       "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                       "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QRadioButton::indicator:unchecked {\n"
                                                       "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QRadioButton::indicator:checked {\n"
                                                       "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                       "}\n"
                                                       "")

        self.horizontalLayout_3.addWidget(self.layout_search_process_radio)

        self.layout_process_combobox = QComboBox(self.widget_search_tablayout)
        self.layout_process_combobox.setObjectName(u"layout_process_combobox")
        sizePolicy2.setHeightForWidth(
            self.layout_process_combobox.sizePolicy().hasHeightForWidth())
        self.layout_process_combobox.setSizePolicy(sizePolicy2)
        self.layout_process_combobox.setMaximumSize(QSize(300, 16777215))
        self.layout_process_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_process_combobox.setLayoutDirection(Qt.LeftToRight)
        self.layout_process_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                   "QComboBox {\n"
                                                   "    background-color: #f0f0f0;\n"
                                                   "    border: 1px solid #ccc;\n"
                                                   "    border-radius: 4px;\n"
                                                   "    padding: 4px;\n"
                                                   "    font-size: 14px;\n"
                                                   "    color: #333;\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                   "QComboBox:focus {\n"
                                                   "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox::drop-down {\n"
                                                   "    border-left: 1px solid #ccc;\n"
                                                   "    width: 20px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox::down-arrow {\n"
                                                   "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                   "}")
        self.layout_process_combobox.setEditable(False)

        self.horizontalLayout_3.addWidget(self.layout_process_combobox)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.layout_storage_location_label = QLabel(
            self.widget_search_tablayout)
        self.layout_storage_location_label.setObjectName(
            u"layout_storage_location_label")
        sizePolicy.setHeightForWidth(
            self.layout_storage_location_label.sizePolicy().hasHeightForWidth())
        self.layout_storage_location_label.setSizePolicy(sizePolicy)
        self.layout_storage_location_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.layout_storage_location_label)

        self.layout_search_storage_location_radio = QRadioButton(
            self.widget_search_tablayout)
        self.layout_search_storage_location_radio.setObjectName(
            u"layout_search_storage_location_radio")
        sizePolicy1.setHeightForWidth(
            self.layout_search_storage_location_radio.sizePolicy().hasHeightForWidth())
        self.layout_search_storage_location_radio.setSizePolicy(sizePolicy1)
        self.layout_search_storage_location_radio.setStyleSheet(u"QRadioButton::indicator {\n"
                                                                "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator:unchecked {\n"
                                                                "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator:checked {\n"
                                                                "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                "}\n"
                                                                "")

        self.horizontalLayout_3.addWidget(
            self.layout_search_storage_location_radio)

        self.layout_storage_location_combobox = QComboBox(
            self.widget_search_tablayout)
        self.layout_storage_location_combobox.setObjectName(
            u"layout_storage_location_combobox")
        sizePolicy2.setHeightForWidth(
            self.layout_storage_location_combobox.sizePolicy().hasHeightForWidth())
        self.layout_storage_location_combobox.setSizePolicy(sizePolicy2)
        self.layout_storage_location_combobox.setMaximumSize(
            QSize(300, 16777215))
        self.layout_storage_location_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_storage_location_combobox.setFocusPolicy(Qt.WheelFocus)
        self.layout_storage_location_combobox.setLayoutDirection(
            Qt.LeftToRight)
        self.layout_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                            "QComboBox {\n"
                                                            "    background-color: #f0f0f0;\n"
                                                            "    border: 1px solid #ccc;\n"
                                                            "    border-radius: 4px;\n"
                                                            "    padding: 4px;\n"
                                                            "    font-size: 14px;\n"
                                                            "    color: #333;\n"
                                                            "}\n"
                                                            "\n"
                                                            "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                            "QComboBox:focus {\n"
                                                            "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QComboBox::drop-down {\n"
                                                            "    border-left: 1px solid #ccc;\n"
                                                            "    width: 20px;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QComboBox::down-arrow {\n"
                                                            "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                            "}")
        self.layout_storage_location_combobox.setEditable(False)

        self.horizontalLayout_3.addWidget(
            self.layout_storage_location_combobox)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.verticalLayout_7.addWidget(self.widget_search_tablayout)

        self.layout_search_button = QPushButton(self.tabLayout)
        self.layout_search_button.setObjectName(u"layout_search_button")
        self.layout_search_button.setMinimumSize(QSize(0, 40))
        self.layout_search_button.setMaximumSize(QSize(16777215, 40))
        self.layout_search_button.setSizeIncrement(QSize(0, 40))
        self.layout_search_button.setFont(font1)
        self.layout_search_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
                                                "QPushButton {\n"
                                                "    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
                                                "    border: none;\n"
                                                "    border-radius: 8px;\n"
                                                "    color: white;\n"
                                                "    font-size: 12px;\n"
                                                "    font-weight: bold;\n"
                                                "    padding: 8px 16px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
                                                "    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #d3d3d3;\n"
                                                "    color: #888;\n"
                                                "}\n"
                                                "")
        self.layout_search_button.setIcon(icon6)
        self.layout_search_button.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.layout_search_button)

        self.widget_box_tablayout = QWidget(self.tabLayout)
        self.widget_box_tablayout.setObjectName(u"widget_box_tablayout")
        self.gridLayout_boxs = QGridLayout(self.widget_box_tablayout)
        self.gridLayout_boxs.setSpacing(5)
        self.gridLayout_boxs.setObjectName(u"gridLayout_boxs")
        self.gridLayout_boxs.setContentsMargins(5, 5, 5, 5)
        self.layout_label = QLabel(self.widget_box_tablayout)
        self.layout_label.setObjectName(u"layout_label")
        font5 = QFont()
        font5.setPointSize(22)
        font5.setBold(True)
        self.layout_label.setFont(font5)
        self.layout_label.setFrameShape(QFrame.NoFrame)
        self.layout_label.setScaledContents(False)
        self.layout_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_boxs.addWidget(self.layout_label, 0, 0, 1, 1)

        self.verticalLayout_7.addWidget(self.widget_box_tablayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        icon9 = QIcon()
        icon9.addFile(u":/icon/images/icon/layout_logo.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabLayout, icon9, "")
        self.tabOther = QWidget()
        self.tabOther.setObjectName(u"tabOther")
        self.verticalLayout_4 = QVBoxLayout(self.tabOther)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.tabWidget_main.addTab(self.tabOther, "")
        self.tabInventory = QWidget()
        self.tabInventory.setObjectName(u"tabInventory")
        self.verticalLayout_10 = QVBoxLayout(self.tabInventory)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabinventory = QWidget(self.tabInventory)
        self.widget_nhap_tabinventory.setObjectName(
            u"widget_nhap_tabinventory")
        self.gridLayout_NhapKho_2 = QGridLayout(self.widget_nhap_tabinventory)
        self.gridLayout_NhapKho_2.setSpacing(5)
        self.gridLayout_NhapKho_2.setObjectName(u"gridLayout_NhapKho_2")
        self.gridLayout_NhapKho_2.setContentsMargins(5, 5, 5, 5)
        self.inventory_search_material_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_material_checkBox.setObjectName(
            u"inventory_search_material_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_material_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_material_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_material_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                              "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                              "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:unchecked {\n"
                                                              "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                              "}\n"
                                                              "\n"
                                                              "QCheckBox::indicator:checked {\n"
                                                              "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                              "}\n"
                                                              "")
        self.inventory_search_material_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_material_checkBox, 3, 2, 1, 1)

        self.inventory_status_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_status_label.setObjectName(u"inventory_status_label")
        sizePolicy.setHeightForWidth(
            self.inventory_status_label.sizePolicy().hasHeightForWidth())
        self.inventory_status_label.setSizePolicy(sizePolicy)
        self.inventory_status_label.setFont(font1)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_status_label, 2, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.inventory_status_combobox = QComboBox(
            self.widget_nhap_tabinventory)
        self.inventory_status_combobox.setObjectName(
            u"inventory_status_combobox")
        sizePolicy1.setHeightForWidth(
            self.inventory_status_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_status_combobox.setSizePolicy(sizePolicy1)
        self.inventory_status_combobox.setMinimumSize(QSize(65, 0))
        self.inventory_status_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_status_combobox.setLayoutDirection(Qt.LeftToRight)
        self.inventory_status_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                     "QComboBox {\n"
                                                     "    background-color: #f0f0f0;\n"
                                                     "    border: 1px solid #ccc;\n"
                                                     "    border-radius: 4px;\n"
                                                     "    padding: 4px;\n"
                                                     "    font-size: 14px;\n"
                                                     "    color: #3333FF;\n"
                                                     "}\n"
                                                     "\n"
                                                     "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                     "QComboBox:focus {\n"
                                                     "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::drop-down {\n"
                                                     "    border-left: 1px solid #ccc;\n"
                                                     "    width: 20px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::down-arrow {\n"
                                                     "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                     "}")
        self.inventory_status_combobox.setEditable(False)

        self.horizontalLayout_29.addWidget(self.inventory_status_combobox)

        self.inventory_quantity_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_quantity_label.setObjectName(
            u"inventory_quantity_label")
        sizePolicy.setHeightForWidth(
            self.inventory_quantity_label.sizePolicy().hasHeightForWidth())
        self.inventory_quantity_label.setSizePolicy(sizePolicy)
        self.inventory_quantity_label.setFont(font1)
        self.inventory_quantity_label.setMargin(7)

        self.horizontalLayout_29.addWidget(self.inventory_quantity_label)

        self.inventory_quantity_lineedit = QLineEdit(
            self.widget_nhap_tabinventory)
        self.inventory_quantity_lineedit.setObjectName(
            u"inventory_quantity_lineedit")
        sizePolicy2.setHeightForWidth(
            self.inventory_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_quantity_lineedit.setSizePolicy(sizePolicy2)
        self.inventory_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                       "    background-color: #f0f0f0;\n"
                                                       "    border: 1px solid #ccc;\n"
                                                       "    border-radius: 4px;\n"
                                                       "    padding: 4px;\n"
                                                       "    font-size: 14px;\n"
                                                       "    color: #3333FF;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QLineEdit:focus {\n"
                                                       "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                       "}")
        self.inventory_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.inventory_quantity_lineedit)

        self.inventory_unit_combobox = QComboBox(self.widget_nhap_tabinventory)
        self.inventory_unit_combobox.setObjectName(u"inventory_unit_combobox")
        sizePolicy1.setHeightForWidth(
            self.inventory_unit_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_unit_combobox.setSizePolicy(sizePolicy1)
        self.inventory_unit_combobox.setMinimumSize(QSize(65, 0))
        self.inventory_unit_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_unit_combobox.setLayoutDirection(Qt.LeftToRight)
        self.inventory_unit_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                   "QComboBox {\n"
                                                   "    background-color: #f0f0f0;\n"
                                                   "    border: 1px solid #ccc;\n"
                                                   "    border-radius: 4px;\n"
                                                   "    padding: 4px;\n"
                                                   "    font-size: 14px;\n"
                                                   "    color: #3333FF;\n"
                                                   "}\n"
                                                   "\n"
                                                   "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                   "QComboBox:focus {\n"
                                                   "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox::drop-down {\n"
                                                   "    border-left: 1px solid #ccc;\n"
                                                   "    width: 20px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox::down-arrow {\n"
                                                   "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                   "}")
        self.inventory_unit_combobox.setEditable(False)

        self.horizontalLayout_29.addWidget(self.inventory_unit_combobox)

        self.gridLayout_NhapKho_2.addLayout(
            self.horizontalLayout_29, 2, 3, 1, 1)

        self.inventory_search_size_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_size_checkBox.setObjectName(
            u"inventory_search_size_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_size_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_size_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_size_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                          "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                          "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:unchecked {\n"
                                                          "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:checked {\n"
                                                          "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                          "}\n"
                                                          "")
        self.inventory_search_size_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_size_checkBox, 4, 2, 1, 1)

        self.inventory_search_storage_location_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_storage_location_checkBox.setObjectName(
            u"inventory_search_storage_location_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_storage_location_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_storage_location_checkBox.setSizePolicy(
            sizePolicy1)
        self.inventory_search_storage_location_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                      "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                      "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QCheckBox::indicator:unchecked {\n"
                                                                      "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QCheckBox::indicator:checked {\n"
                                                                      "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                      "}\n"
                                                                      "")
        self.inventory_search_storage_location_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_storage_location_checkBox, 1, 2, 1, 1)

        self.inventory_note_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_note_label.setObjectName(u"inventory_note_label")
        sizePolicy.setHeightForWidth(
            self.inventory_note_label.sizePolicy().hasHeightForWidth())
        self.inventory_note_label.setSizePolicy(sizePolicy)
        self.inventory_note_label.setFont(font1)
        self.inventory_note_label.setTextFormat(Qt.AutoText)
        self.inventory_note_label.setScaledContents(False)
        self.inventory_note_label.setWordWrap(False)
        self.inventory_note_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_note_label, 1, 12, 1, 1)

        self.inventory_images_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_images_label.setObjectName(u"inventory_images_label")
        self.inventory_images_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.inventory_images_label.sizePolicy().hasHeightForWidth())
        self.inventory_images_label.setSizePolicy(sizePolicy1)
        self.inventory_images_label.setMinimumSize(QSize(280, 200))
        self.inventory_images_label.setMaximumSize(QSize(280, 16777215))
        self.inventory_images_label.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_images_label.setStyleSheet(u"/* QLabel styling */\n"
                                                  "QLabel {\n"
                                                  "    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
                                                  "    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
                                                  "    border-radius: 15px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
                                                  "    padding: 6px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
                                                  "    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
                                                  "}\n"
                                                  "/* Hi\u1ec7u \u1ee9ng khi hover */\n"
                                                  "QLabel:hover {\n"
                                                  "    background-color: #f7faff; /* Thay \u0111\u1ed5i n\u1ec1n nh\u1eb9 khi hover */\n"
                                                  "}\n"
                                                  "\n"
                                                  "")
        self.inventory_images_label.setFrameShape(QFrame.StyledPanel)
        self.inventory_images_label.setPixmap(
            QPixmap(u":/icon/images/icon/no_image.png"))
        self.inventory_images_label.setScaledContents(True)
        self.inventory_images_label.setAlignment(Qt.AlignCenter)
        self.inventory_images_label.setWordWrap(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_images_label, 1, 14, 5, 1)

        self.inventory_storage_location_label = QLabel(
            self.widget_nhap_tabinventory)
        self.inventory_storage_location_label.setObjectName(
            u"inventory_storage_location_label")
        sizePolicy.setHeightForWidth(
            self.inventory_storage_location_label.sizePolicy().hasHeightForWidth())
        self.inventory_storage_location_label.setSizePolicy(sizePolicy)
        self.inventory_storage_location_label.setFont(font1)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_storage_location_label, 1, 0, 1, 1)

        self.inventory_note_textedit = QTextEdit(self.widget_nhap_tabinventory)
        self.inventory_note_textedit.setObjectName(u"inventory_note_textedit")
        self.inventory_note_textedit.setStyleSheet(u"QTextEdit {\n"
                                                   "	background-color: rgb(255, 255, 255);\n"
                                                   "    border: 2px solid #ccc;\n"
                                                   "    border-radius: 6px;\n"
                                                   "    padding: 5px;\n"
                                                   "    color: #3333FF;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QTextEdit:focus {\n"
                                                   "    border: 2px solid #4a90e2;\n"
                                                   "}")
        self.inventory_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.inventory_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_note_textedit, 2, 12, 4, 2)

        self.inventory_search_note_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_note_checkBox.setObjectName(
            u"inventory_search_note_checkBox")
        self.inventory_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                          "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                          "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:unchecked {\n"
                                                          "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCheckBox::indicator:checked {\n"
                                                          "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                          "}\n"
                                                          "")
        self.inventory_search_note_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_note_checkBox, 1, 13, 1, 1)

        self.inventory_desinvoice_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_desinvoice_label.setObjectName(
            u"inventory_desinvoice_label")
        sizePolicy.setHeightForWidth(
            self.inventory_desinvoice_label.sizePolicy().hasHeightForWidth())
        self.inventory_desinvoice_label.setSizePolicy(sizePolicy)
        self.inventory_desinvoice_label.setFont(font1)
        self.inventory_desinvoice_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_desinvoice_label, 5, 6, 1, 1)

        self.inventory_search_desinvoice_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_desinvoice_checkBox.setObjectName(
            u"inventory_search_desinvoice_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_desinvoice_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_desinvoice_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_desinvoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QCheckBox::indicator:unchecked {\n"
                                                                "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                "}\n"
                                                                "\n"
                                                                "QCheckBox::indicator:checked {\n"
                                                                "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                "}\n"
                                                                "")
        self.inventory_search_desinvoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_desinvoice_checkBox, 5, 7, 1, 1)

        self.inventory_desinvoice_lineedit = QLineEdit(
            self.widget_nhap_tabinventory)
        self.inventory_desinvoice_lineedit.setObjectName(
            u"inventory_desinvoice_lineedit")
        self.inventory_desinvoice_lineedit.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.inventory_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_desinvoice_lineedit.setSizePolicy(sizePolicy2)
        self.inventory_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                         "    background-color: #f0f0f0;\n"
                                                         "    border: 1px solid #ccc;\n"
                                                         "    border-radius: 4px;\n"
                                                         "    padding: 4px;\n"
                                                         "    font-size: 14px;\n"
                                                         "    color: #3333FF;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:focus {\n"
                                                         "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                         "}")
        self.inventory_desinvoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_desinvoice_lineedit, 5, 8, 1, 1)

        self.inventory_size_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_size_label.setObjectName(u"inventory_size_label")
        sizePolicy.setHeightForWidth(
            self.inventory_size_label.sizePolicy().hasHeightForWidth())
        self.inventory_size_label.setSizePolicy(sizePolicy)
        self.inventory_size_label.setFont(font1)
        self.inventory_size_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_size_label, 4, 0, 1, 1)

        self.inventory_material_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_material_label.setObjectName(
            u"inventory_material_label")
        sizePolicy.setHeightForWidth(
            self.inventory_material_label.sizePolicy().hasHeightForWidth())
        self.inventory_material_label.setSizePolicy(sizePolicy)
        self.inventory_material_label.setFont(font1)
        self.inventory_material_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_material_label, 3, 0, 1, 1)

        self.output_size_horizontalLayout = QHBoxLayout()
        self.output_size_horizontalLayout.setObjectName(
            u"output_size_horizontalLayout")
        self.inventory_size_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_size_lineedit.setObjectName(u"inventory_size_lineedit")
        self.inventory_size_lineedit.setEnabled(True)
        self.inventory_size_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_size_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                   "    background-color: #f0f0f0;\n"
                                                   "    border: 1px solid #ccc;\n"
                                                   "    border-radius: 4px;\n"
                                                   "    padding: 4px;\n"
                                                   "    font-size: 14px;\n"
                                                   "    color: #3333FF;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:focus {\n"
                                                   "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                   "}")
        self.inventory_size_lineedit.setMaxLength(32767)
        self.inventory_size_lineedit.setAlignment(Qt.AlignCenter)

        self.output_size_horizontalLayout.addWidget(
            self.inventory_size_lineedit)

        self.input_size_label_7 = QLabel(self.widget_nhap_tabinventory)
        self.input_size_label_7.setObjectName(u"input_size_label_7")
        sizePolicy.setHeightForWidth(
            self.input_size_label_7.sizePolicy().hasHeightForWidth())
        self.input_size_label_7.setSizePolicy(sizePolicy)
        self.input_size_label_7.setFont(font1)
        self.input_size_label_7.setMargin(7)

        self.output_size_horizontalLayout.addWidget(self.input_size_label_7)

        self.gridLayout_NhapKho_2.addLayout(
            self.output_size_horizontalLayout, 4, 3, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.inventory_storage_location_combobox = QComboBox(
            self.widget_nhap_tabinventory)
        self.inventory_storage_location_combobox.setObjectName(
            u"inventory_storage_location_combobox")
        sizePolicy2.setHeightForWidth(
            self.inventory_storage_location_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_storage_location_combobox.setSizePolicy(sizePolicy2)
        self.inventory_storage_location_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_storage_location_combobox.setLayoutDirection(
            Qt.LeftToRight)
        self.inventory_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                               "QComboBox {\n"
                                                               "    background-color: #f0f0f0;\n"
                                                               "    border: 1px solid #ccc;\n"
                                                               "    border-radius: 4px;\n"
                                                               "    padding: 4px;\n"
                                                               "    font-size: 14px;\n"
                                                               "    color: #3333FF;\n"
                                                               "}\n"
                                                               "\n"
                                                               "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                               "QComboBox:focus {\n"
                                                               "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                               "}\n"
                                                               "\n"
                                                               "QComboBox::drop-down {\n"
                                                               "    border-left: 1px solid #ccc;\n"
                                                               "    width: 20px;\n"
                                                               "}\n"
                                                               "\n"
                                                               "QComboBox::down-arrow {\n"
                                                               "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                               "}")
        self.inventory_storage_location_combobox.setEditable(False)

        self.horizontalLayout_33.addWidget(
            self.inventory_storage_location_combobox)

        self.inventory_component_id_label = QLabel(
            self.widget_nhap_tabinventory)
        self.inventory_component_id_label.setObjectName(
            u"inventory_component_id_label")
        sizePolicy.setHeightForWidth(
            self.inventory_component_id_label.sizePolicy().hasHeightForWidth())
        self.inventory_component_id_label.setSizePolicy(sizePolicy)
        self.inventory_component_id_label.setFont(font1)
        self.inventory_component_id_label.setMargin(7)

        self.horizontalLayout_33.addWidget(self.inventory_component_id_label)

        self.inventory_search_component_id_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_component_id_checkBox.setObjectName(
            u"inventory_search_component_id_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_component_id_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                  "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                  "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:unchecked {\n"
                                                                  "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:checked {\n"
                                                                  "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                  "}\n"
                                                                  "")
        self.inventory_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_33.addWidget(
            self.inventory_search_component_id_checkBox)

        self.inventory_component_id_lineedit = QLineEdit(
            self.widget_nhap_tabinventory)
        self.inventory_component_id_lineedit.setObjectName(
            u"inventory_component_id_lineedit")
        sizePolicy2.setHeightForWidth(
            self.inventory_component_id_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_component_id_lineedit.setSizePolicy(sizePolicy2)
        self.inventory_component_id_lineedit.setFont(font2)
        self.inventory_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                           "    background-color: #f0f0f0;\n"
                                                           "    border: 1px solid #ccc;\n"
                                                           "    border-radius: 4px;\n"
                                                           "    padding: 4px;\n"
                                                           "    font-size: 14px;\n"
                                                           "    color: #3333FF;\n"
                                                           "}\n"
                                                           "\n"
                                                           "QLineEdit:focus {\n"
                                                           "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                           "}")
        self.inventory_component_id_lineedit.setMaxLength(8)
        self.inventory_component_id_lineedit.setAlignment(Qt.AlignCenter)
        self.inventory_component_id_lineedit.setClearButtonEnabled(True)

        self.horizontalLayout_33.addWidget(
            self.inventory_component_id_lineedit)

        self.gridLayout_NhapKho_2.addLayout(
            self.horizontalLayout_33, 1, 3, 1, 1)

        self.inventory_invoice_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_invoice_label.setObjectName(u"inventory_invoice_label")
        sizePolicy.setHeightForWidth(
            self.inventory_invoice_label.sizePolicy().hasHeightForWidth())
        self.inventory_invoice_label.setSizePolicy(sizePolicy)
        self.inventory_invoice_label.setFont(font1)
        self.inventory_invoice_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_invoice_label, 5, 0, 1, 1)

        self.inventory_search_groups_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_groups_checkBox.setObjectName(
            u"inventory_search_groups_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_groups_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_groups_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_groups_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                            "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                            "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:unchecked {\n"
                                                            "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:checked {\n"
                                                            "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                            "}\n"
                                                            "")
        self.inventory_search_groups_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_groups_checkBox, 3, 7, 1, 1)

        self.inventory_search_invoice_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_invoice_checkBox.setObjectName(
            u"inventory_search_invoice_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_invoice_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_invoice_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_invoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                             "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                             "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                             "}\n"
                                                             "\n"
                                                             "QCheckBox::indicator:unchecked {\n"
                                                             "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                             "}\n"
                                                             "\n"
                                                             "QCheckBox::indicator:checked {\n"
                                                             "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                             "}\n"
                                                             "")
        self.inventory_search_invoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_invoice_checkBox, 5, 2, 1, 1)

        self.inventory_groups_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_groups_label.setObjectName(u"inventory_groups_label")
        sizePolicy.setHeightForWidth(
            self.inventory_groups_label.sizePolicy().hasHeightForWidth())
        self.inventory_groups_label.setSizePolicy(sizePolicy)
        self.inventory_groups_label.setFont(font1)
        self.inventory_groups_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_groups_label, 3, 6, 1, 1)

        self.inventory_invoice_lineedit = QLineEdit(
            self.widget_nhap_tabinventory)
        self.inventory_invoice_lineedit.setObjectName(
            u"inventory_invoice_lineedit")
        self.inventory_invoice_lineedit.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.inventory_invoice_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_invoice_lineedit.setSizePolicy(sizePolicy2)
        self.inventory_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                      "    background-color: #f0f0f0;\n"
                                                      "    border: 1px solid #ccc;\n"
                                                      "    border-radius: 4px;\n"
                                                      "    padding: 4px;\n"
                                                      "    font-size: 14px;\n"
                                                      "    color: #3333FF;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:focus {\n"
                                                      "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                      "}")
        self.inventory_invoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_invoice_lineedit, 5, 3, 1, 1)

        self.inventory_search_model_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_model_checkBox.setObjectName(
            u"inventory_search_model_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_model_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_model_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_model_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                           "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                           "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                           "}\n"
                                                           "\n"
                                                           "QCheckBox::indicator:unchecked {\n"
                                                           "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                           "}\n"
                                                           "\n"
                                                           "QCheckBox::indicator:checked {\n"
                                                           "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                           "}\n"
                                                           "")
        self.inventory_search_model_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_model_checkBox, 4, 7, 1, 1)

        self.inventory_model_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_model_label.setObjectName(u"inventory_model_label")
        sizePolicy.setHeightForWidth(
            self.inventory_model_label.sizePolicy().hasHeightForWidth())
        self.inventory_model_label.setSizePolicy(sizePolicy)
        self.inventory_model_label.setFont(font1)
        self.inventory_model_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_model_label, 4, 6, 1, 1)

        self.inventory_component_name_label = QLabel(
            self.widget_nhap_tabinventory)
        self.inventory_component_name_label.setObjectName(
            u"inventory_component_name_label")
        sizePolicy.setHeightForWidth(
            self.inventory_component_name_label.sizePolicy().hasHeightForWidth())
        self.inventory_component_name_label.setSizePolicy(sizePolicy)
        self.inventory_component_name_label.setFont(font1)
        self.inventory_component_name_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_component_name_label, 1, 6, 1, 1)

        self.inventory_search_component_name_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_component_name_checkBox.setObjectName(
            u"inventory_search_component_name_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_component_name_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_component_name_checkBox.setSizePolicy(
            sizePolicy1)
        self.inventory_search_component_name_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                    "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                    "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QCheckBox::indicator:unchecked {\n"
                                                                    "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QCheckBox::indicator:checked {\n"
                                                                    "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                    "}\n"
                                                                    "")
        self.inventory_search_component_name_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_component_name_checkBox, 1, 7, 1, 1)

        self.inventory_process_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_process_label.setObjectName(u"inventory_process_label")
        sizePolicy.setHeightForWidth(
            self.inventory_process_label.sizePolicy().hasHeightForWidth())
        self.inventory_process_label.setSizePolicy(sizePolicy)
        self.inventory_process_label.setFont(font1)
        self.inventory_process_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_process_label, 2, 6, 1, 1)

        self.inventory_component_name_lineedit = QLineEdit(
            self.widget_nhap_tabinventory)
        self.inventory_component_name_lineedit.setObjectName(
            u"inventory_component_name_lineedit")
        self.inventory_component_name_lineedit.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.inventory_component_name_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_component_name_lineedit.setSizePolicy(sizePolicy2)
        self.inventory_component_name_lineedit.setMaximumSize(
            QSize(16777215, 16777215))
        self.inventory_component_name_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                             "    background-color: #f0f0f0;\n"
                                                             "    border: 1px solid #ccc;\n"
                                                             "    border-radius: 4px;\n"
                                                             "    padding: 4px;\n"
                                                             "    font-size: 14px;\n"
                                                             "    color: #3333FF;\n"
                                                             "}\n"
                                                             "\n"
                                                             "QLineEdit:focus {\n"
                                                             "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                             "}")
        self.inventory_component_name_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_component_name_lineedit, 1, 8, 1, 1)

        self.inventory_search_process_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_process_checkBox.setObjectName(
            u"inventory_search_process_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_process_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_process_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_process_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                             "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                             "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                             "}\n"
                                                             "\n"
                                                             "QCheckBox::indicator:unchecked {\n"
                                                             "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                             "}\n"
                                                             "\n"
                                                             "QCheckBox::indicator:checked {\n"
                                                             "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                             "}\n"
                                                             "")
        self.inventory_search_process_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_process_checkBox, 2, 7, 1, 1)

        self.inventory_material_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_material_widget.setObjectName(
            u"inventory_material_widget")
        self.horizontalLayout_30 = QHBoxLayout(self.inventory_material_widget)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_material_widget, 3, 3, 1, 1)

        self.inventory_process_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_process_widget.setObjectName(
            u"inventory_process_widget")
        self.horizontalLayout_36 = QHBoxLayout(self.inventory_process_widget)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_process_widget, 2, 8, 1, 1)

        self.inventory_groups_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_groups_widget.setObjectName(u"inventory_groups_widget")
        self.horizontalLayout_37 = QHBoxLayout(self.inventory_groups_widget)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_groups_widget, 3, 8, 1, 1)

        self.inventory_model_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_model_widget.setObjectName(u"inventory_model_widget")
        self.horizontalLayout_38 = QHBoxLayout(self.inventory_model_widget)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_model_widget, 4, 8, 1, 1)

        self.inventory_search_status_checkBox = QCheckBox(
            self.widget_nhap_tabinventory)
        self.inventory_search_status_checkBox.setObjectName(
            u"inventory_search_status_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_search_status_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_status_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_search_status_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                            "    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                            "    height: 24px; /* Chi\u1ec1u cao icon */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:unchecked {\n"
                                                            "    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QCheckBox::indicator:checked {\n"
                                                            "    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                            "}\n"
                                                            "")
        self.inventory_search_status_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(
            self.inventory_search_status_checkBox, 2, 2, 1, 1)

        self.inventory_images_label.raise_()
        self.inventory_note_label.raise_()
        self.inventory_search_storage_location_checkBox.raise_()
        self.inventory_note_textedit.raise_()
        self.inventory_storage_location_label.raise_()
        self.inventory_search_note_checkBox.raise_()
        self.inventory_desinvoice_label.raise_()
        self.inventory_search_desinvoice_checkBox.raise_()
        self.inventory_desinvoice_lineedit.raise_()
        self.inventory_status_label.raise_()
        self.inventory_material_label.raise_()
        self.inventory_search_material_checkBox.raise_()
        self.inventory_size_label.raise_()
        self.inventory_search_size_checkBox.raise_()
        self.inventory_invoice_lineedit.raise_()
        self.inventory_search_model_checkBox.raise_()
        self.inventory_model_label.raise_()
        self.inventory_invoice_label.raise_()
        self.inventory_search_invoice_checkBox.raise_()
        self.inventory_component_name_label.raise_()
        self.inventory_search_component_name_checkBox.raise_()
        self.inventory_component_name_lineedit.raise_()
        self.inventory_process_label.raise_()
        self.inventory_search_process_checkBox.raise_()
        self.inventory_groups_label.raise_()
        self.inventory_search_groups_checkBox.raise_()
        self.inventory_material_widget.raise_()
        self.inventory_process_widget.raise_()
        self.inventory_groups_widget.raise_()
        self.inventory_model_widget.raise_()
        self.inventory_search_status_checkBox.raise_()

        self.verticalLayout_10.addWidget(self.widget_nhap_tabinventory)

        self.widget_button_tabinventory = QWidget(self.tabInventory)
        self.widget_button_tabinventory.setObjectName(
            u"widget_button_tabinventory")
        self.inputButtonLayout_2 = QHBoxLayout(self.widget_button_tabinventory)
        self.inputButtonLayout_2.setSpacing(5)
        self.inputButtonLayout_2.setObjectName(u"inputButtonLayout_2")
        self.inputButtonLayout_2.setContentsMargins(5, 5, 5, 5)
        self.inventory_filter_component_id_checkBox = QCheckBox(
            self.widget_button_tabinventory)
        self.inventory_filter_component_id_checkBox.setObjectName(
            u"inventory_filter_component_id_checkBox")
        sizePolicy1.setHeightForWidth(
            self.inventory_filter_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_filter_component_id_checkBox.setSizePolicy(sizePolicy1)
        self.inventory_filter_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
                                                                  "    width: 32px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
                                                                  "    height: 32px; /* Chi\u1ec1u cao icon */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:unchecked {\n"
                                                                  "    image: url(:/icon/images/icon/filter_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
                                                                  "}\n"
                                                                  "\n"
                                                                  "QCheckBox::indicator:checked {\n"
                                                                  "    image: url(:/icon/images/icon/filter_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
                                                                  "}\n"
                                                                  "")
        self.inventory_filter_component_id_checkBox.setChecked(False)

        self.inputButtonLayout_2.addWidget(
            self.inventory_filter_component_id_checkBox)

        self.inventory_search_button = QPushButton(
            self.widget_button_tabinventory)
        self.inventory_search_button.setObjectName(u"inventory_search_button")
        sizePolicy4.setHeightForWidth(
            self.inventory_search_button.sizePolicy().hasHeightForWidth())
        self.inventory_search_button.setSizePolicy(sizePolicy4)
        self.inventory_search_button.setMinimumSize(QSize(0, 40))
        self.inventory_search_button.setMaximumSize(QSize(16777215, 40))
        self.inventory_search_button.setSizeIncrement(QSize(0, 40))
        self.inventory_search_button.setFont(font1)
        self.inventory_search_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
                                                   "QPushButton {\n"
                                                   "    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
                                                   "    border: none;\n"
                                                   "    border-radius: 8px;\n"
                                                   "    color: white;\n"
                                                   "    font-size: 12px;\n"
                                                   "    font-weight: bold;\n"
                                                   "    padding: 8px 16px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
                                                   "    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed {\n"
                                                   "    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:disabled {\n"
                                                   "    background-color: #d3d3d3;\n"
                                                   "    color: #888;\n"
                                                   "}\n"
                                                   "")
        self.inventory_search_button.setIcon(icon6)
        self.inventory_search_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout_2.addWidget(self.inventory_search_button)

        self.inventory_export_button = QPushButton(
            self.widget_button_tabinventory)
        self.inventory_export_button.setObjectName(u"inventory_export_button")
        sizePolicy4.setHeightForWidth(
            self.inventory_export_button.sizePolicy().hasHeightForWidth())
        self.inventory_export_button.setSizePolicy(sizePolicy4)
        self.inventory_export_button.setMinimumSize(QSize(0, 40))
        self.inventory_export_button.setMaximumSize(QSize(16777215, 40))
        self.inventory_export_button.setSizeIncrement(QSize(0, 40))
        self.inventory_export_button.setFont(font2)
        self.inventory_export_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_export_button.setStyleSheet(u"/* QPushButton styling */\n"
                                                   "QPushButton {\n"
                                                   "    background-color: #4a90e2;\n"
                                                   "    border: none;\n"
                                                   "    border-radius: 10px;\n"
                                                   "    color: #fff;\n"
                                                   "    font-size: 12px;\n"
                                                   "    padding: 6px 12px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: #357ab7;\n"
                                                   "	font: 75 14pt;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed {\n"
                                                   "    background-color: #2a6cae;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:disabled {\n"
                                                   "    background-color: #ccc;\n"
                                                   "    color: #666;\n"
                                                   "}")
        self.inventory_export_button.setIcon(icon4)
        self.inventory_export_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout_2.addWidget(self.inventory_export_button)

        self.verticalLayout_10.addWidget(self.widget_button_tabinventory)

        self.inventory_data_tablewidget = QTableWidget(self.tabInventory)
        if (self.inventory_data_tablewidget.columnCount() < 3):
            self.inventory_data_tablewidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(
            0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(
            1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(
            2, __qtablewidgetitem5)
        self.inventory_data_tablewidget.setObjectName(
            u"inventory_data_tablewidget")
        self.inventory_data_tablewidget.setStyleSheet(u"/* QTableWidget styling */\n"
                                                      "QTableWidget {\n"
                                                      "    background-color: #f9fbfd; /* N\u1ec1n b\u1ea3ng xanh nh\u1ea1t */\n"
                                                      "    border: 1px solid #d3d9e3; /* \u0110\u01b0\u1eddng vi\u1ec1n nh\u1eb9 */\n"
                                                      "    font-size: 12px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
                                                      "    color: #333333; /* M\u00e0u ch\u1eef ch\u00ednh */\n"
                                                      "    gridline-color: #e7edf3; /* M\u00e0u \u0111\u01b0\u1eddng l\u01b0\u1edbi nh\u1ea1t */\n"
                                                      "    selection-background-color: #3b82cc; /* M\u00e0u n\u1ec1n khi ch\u1ecdn */\n"
                                                      "    selection-color: #ffffff; /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
                                                      "    outline: none; /* Lo\u1ea1i b\u1ecf vi\u1ec1n s\u00e1ng khi focus */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Ti\u00eau \u0111\u1ec1 c\u1ed9t */\n"
                                                      "QHeaderView::section {\n"
                                                      "    background-color: #e5effb; /* N\u1ec1n ti\u00eau \u0111\u1ec1 xanh nh\u1ea1t */\n"
                                                      "    color: #4a4a4a; /* M\u00e0u ch\u1eef ti\u00eau \u0111\u1ec1 */\n"
                                                      "    padding: 10px;\n"
                                                      "    border: 1px solid #d3d9e3; /* Vi\u1ec1n gi\u1eefa c\u00e1c ti\u00eau \u0111\u1ec1 */\n"
                                                      "    font-size"
                                                      ": 12px;\n"
                                                      "    font-weight: bold;\n"
                                                      "    text-align: center;\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* C\u00e1c \u00f4 */\n"
                                                      "QTableWidget::item {\n"
                                                      "    background-color: #ffffff; /* N\u1ec1n \u00f4 m\u1eb7c \u0111\u1ecbnh */\n"
                                                      "    border: none;\n"
                                                      "    padding: 8px;\n"
                                                      "    font-size: 13px;\n"
                                                      "    color: #333333; /* M\u00e0u ch\u1eef */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* \u00d4 xen k\u1ebd */\n"
                                                      "QTableWidget::item:alternate {\n"
                                                      "    background-color: #f4f8fc; /* N\u1ec1n xen k\u1ebd xanh nh\u1eb9 */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Hi\u1ec7u \u1ee9ng hover */\n"
                                                      "QTableWidget::item:hover {\n"
                                                      "    background-color: #dceaf7; /* M\u00e0u hover xanh nh\u1ea1t */\n"
                                                      "    color: #333333; /* Ch\u1eef v\u1eabn d\u1ec5 \u0111\u1ecdc */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Hi\u1ec7u \u1ee9ng hover n\u1ed5i b\u1eadt to\u00e0n d\u00f2ng */\n"
                                                      "QTableWidget::row:hover {\n"
                                                      "    background-color: #cce1f4; /* N\u1ec1n hover n\u1ed5i b\u1eadt c\u1ea3 d\u00f2ng */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Hi\u1ec7u \u1ee9ng khi ch\u1ecdn */\n"
                                                      "QTableWidget::item:selected {\n"
                                                      "    background-color: #3b82cc; /* M"
                                                      "\u00e0u n\u1ec1n xanh \u0111\u1eadm khi ch\u1ecdn */\n"
                                                      "    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng khi ch\u1ecdn */\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Scrollbar */\n"
                                                      "QScrollBar:vertical {\n"
                                                      "    border: none;\n"
                                                      "    background: #f4f8fc; /* N\u1ec1n thanh cu\u1ed9n xanh nh\u1ea1t */\n"
                                                      "    width: 12px;\n"
                                                      "    margin: 2px 0;\n"
                                                      "    border-radius: 6px;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QScrollBar::handle:vertical {\n"
                                                      "    background: #3b82cc; /* Thanh tr\u01b0\u1ee3t xanh \u0111\u1eadm */\n"
                                                      "    min-height: 20px;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QScrollBar::handle:vertical:hover {\n"
                                                      "    background: #2f6fa5; /* Thanh tr\u01b0\u1ee3t khi hover */\n"
                                                      "}\n"
                                                      "\n"
                                                      "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
                                                      "    background: none;\n"
                                                      "    border: none;\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* G\u00f3c cu\u1ed9n */\n"
                                                      "QScrollBar::corner {\n"
                                                      "    background: #ffffff;\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* Hi\u1ec7u \u1ee9ng khi focus */\n"
                                                      "QTableWidget:focus {\n"
                                                      "    border: 1px solid #3b82cc; /* Vi\u1ec1n xanh \u0111\u1eadm khi focus */\n"
                                                      "}\n"
                                                      "")
        self.inventory_data_tablewidget.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.inventory_data_tablewidget.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.inventory_data_tablewidget.setSortingEnabled(False)

        self.verticalLayout_10.addWidget(self.inventory_data_tablewidget)

        icon10 = QIcon()
        icon10.addFile(u":/icon/images/icon/Inventory Management.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabInventory, icon10, "")
        self.tabChangepassword = QWidget()
        self.tabChangepassword.setObjectName(u"tabChangepassword")
        self.verticalLayout_11 = QVBoxLayout(self.tabChangepassword)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget_Change = QWidget(self.tabChangepassword)
        self.horizontalWidget_Change.setObjectName(u"horizontalWidget_Change")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_Change)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.widgetk = QWidget(self.horizontalWidget_Change)
        self.widgetk.setObjectName(u"widgetk")
        self.verticalLayout_14 = QVBoxLayout(self.widgetk)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_changepassword = QWidget(self.widgetk)
        self.widget_changepassword.setObjectName(u"widget_changepassword")
        sizePolicy.setHeightForWidth(
            self.widget_changepassword.sizePolicy().hasHeightForWidth())
        self.widget_changepassword.setSizePolicy(sizePolicy)
        self.widget_changepassword.setMinimumSize(QSize(400, 0))
        self.widget_changepassword.setMaximumSize(QSize(600, 500))
        self.widget_changepassword.setStyleSheet(u"QWidget {\n"
                                                 "    background-color: rgba(0, 0, 0, 0.6); /* M\u00e0u n\u1ec1n \u0111en m\u1edd */\n"
                                                 "    border-radius: 15px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
                                                 "}\n"
                                                 "")
        self.verticalLayout_15 = QVBoxLayout(self.widget_changepassword)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_12 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.change_logo_label = QLabel(self.widget_changepassword)
        self.change_logo_label.setObjectName(u"change_logo_label")
        sizePolicy.setHeightForWidth(
            self.change_logo_label.sizePolicy().hasHeightForWidth())
        self.change_logo_label.setSizePolicy(sizePolicy)
        self.change_logo_label.setMaximumSize(QSize(100, 70))
        self.change_logo_label.setFont(font1)
        self.change_logo_label.setStyleSheet(u"QLabel {\n"
                                             "    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
                                             "}\n"
                                             "")
        self.change_logo_label.setPixmap(
            QPixmap(u":/icon/images/icon/logo.png"))
        self.change_logo_label.setScaledContents(True)
        self.change_logo_label.setAlignment(Qt.AlignCenter)
        self.change_logo_label.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.change_logo_label)

        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_14 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.change_msnv_label = QLabel(self.widget_changepassword)
        self.change_msnv_label.setObjectName(u"change_msnv_label")
        sizePolicy1.setHeightForWidth(
            self.change_msnv_label.sizePolicy().hasHeightForWidth())
        self.change_msnv_label.setSizePolicy(sizePolicy1)
        self.change_msnv_label.setMinimumSize(QSize(300, 40))
        self.change_msnv_label.setStyleSheet(u"QLabel {\n"
                                             "    background-color: #f0f0f0;\n"
                                             "    border: 1px solid #ccc;\n"
                                             "    border-radius: 4px;\n"
                                             "    padding: 4px;\n"
                                             "    color: #333;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel:focus {\n"
                                             "    border: 1px solid #4a90e2;\n"
                                             "}")
        self.change_msnv_label.setAlignment(Qt.AlignCenter)
        self.change_msnv_label.setMargin(7)

        self.horizontalLayout_12.addWidget(self.change_msnv_label)

        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_15 = QSpacerItem(
            20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.change_password_old_lineedit = QLineEdit(
            self.widget_changepassword)
        self.change_password_old_lineedit.setObjectName(
            u"change_password_old_lineedit")
        sizePolicy1.setHeightForWidth(
            self.change_password_old_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_old_lineedit.setSizePolicy(sizePolicy1)
        self.change_password_old_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_old_lineedit.setFont(font2)
        self.change_password_old_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                        "    background-color: #f0f0f0;\n"
                                                        "    border: 1px solid #ccc;\n"
                                                        "    border-radius: 4px;\n"
                                                        "    padding: 4px;\n"
                                                        "    font-size: 14px;\n"
                                                        "    color: #333;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:focus {\n"
                                                        "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                        "}")
        self.change_password_old_lineedit.setMaxLength(16)
        self.change_password_old_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_old_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_old_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.change_password_old_lineedit)

        self.verticalLayout_15.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_16 = QSpacerItem(
            20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.change_password_new_lineedit = QLineEdit(
            self.widget_changepassword)
        self.change_password_new_lineedit.setObjectName(
            u"change_password_new_lineedit")
        sizePolicy1.setHeightForWidth(
            self.change_password_new_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_new_lineedit.setSizePolicy(sizePolicy1)
        self.change_password_new_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_new_lineedit.setFont(font2)
        self.change_password_new_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                        "    background-color: #f0f0f0;\n"
                                                        "    border: 1px solid #ccc;\n"
                                                        "    border-radius: 4px;\n"
                                                        "    padding: 4px;\n"
                                                        "    font-size: 14px;\n"
                                                        "    color: #333;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:focus {\n"
                                                        "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                        "}")
        self.change_password_new_lineedit.setMaxLength(16)
        self.change_password_new_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_new_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_new_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_15.addWidget(self.change_password_new_lineedit)

        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.change_password_new2_lineedit = QLineEdit(
            self.widget_changepassword)
        self.change_password_new2_lineedit.setObjectName(
            u"change_password_new2_lineedit")
        sizePolicy1.setHeightForWidth(
            self.change_password_new2_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_new2_lineedit.setSizePolicy(sizePolicy1)
        self.change_password_new2_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_new2_lineedit.setFont(font2)
        self.change_password_new2_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                         "    background-color: #f0f0f0;\n"
                                                         "    border: 1px solid #ccc;\n"
                                                         "    border-radius: 4px;\n"
                                                         "    padding: 4px;\n"
                                                         "    font-size: 14px;\n"
                                                         "    color: #333;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:focus {\n"
                                                         "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                         "}")
        self.change_password_new2_lineedit.setMaxLength(16)
        self.change_password_new2_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_new2_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_new2_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_16.addWidget(self.change_password_new2_lineedit)

        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_19 = QSpacerItem(
            20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_19)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.change_changing_button = QPushButton(self.widget_changepassword)
        self.change_changing_button.setObjectName(u"change_changing_button")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.change_changing_button.sizePolicy().hasHeightForWidth())
        self.change_changing_button.setSizePolicy(sizePolicy6)
        self.change_changing_button.setMinimumSize(QSize(300, 50))
        self.change_changing_button.setMaximumSize(QSize(16777215, 50))
        self.change_changing_button.setSizeIncrement(QSize(0, 40))
        self.change_changing_button.setFont(font2)
        self.change_changing_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_changing_button.setStyleSheet(u"/* QPushButton styling */\n"
                                                  "QPushButton {\n"
                                                  "    background-color: #4a90e2;\n"
                                                  "    border: none;\n"
                                                  "    border-radius: 25px;\n"
                                                  "    color: #fff;\n"
                                                  "    font-size: 14px;\n"
                                                  "    padding: 6px 12px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: #357ab7;\n"
                                                  "	font: 75 16pt;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed {\n"
                                                  "    background-color: #2a6cae;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:disabled {\n"
                                                  "    background-color: #ccc;\n"
                                                  "    color: #666;\n"
                                                  "}")
        self.change_changing_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.change_changing_button)

        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_17 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_17)

        self.verticalLayout_14.addWidget(self.widget_changepassword)

        self.horizontalLayout_6.addWidget(self.widgetk)

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)

        self.verticalLayout_11.addWidget(self.horizontalWidget_Change)

        icon11 = QIcon()
        icon11.addFile(u":/icon/images/icon/changepassword_logo.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabChangepassword, icon11, "")
        self.tabadduser = QWidget()
        self.tabadduser.setObjectName(u"tabadduser")
        self.verticalLayout_18 = QVBoxLayout(self.tabadduser)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget_Login_2 = QWidget(self.tabadduser)
        self.horizontalWidget_Login_2.setObjectName(
            u"horizontalWidget_Login_2")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget_Login_2)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)

        self.widget_themUser = QWidget(self.horizontalWidget_Login_2)
        self.widget_themUser.setObjectName(u"widget_themUser")
        self.verticalLayout_16 = QVBoxLayout(self.widget_themUser)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_adduser = QWidget(self.widget_themUser)
        self.widget_adduser.setObjectName(u"widget_adduser")
        sizePolicy.setHeightForWidth(
            self.widget_adduser.sizePolicy().hasHeightForWidth())
        self.widget_adduser.setSizePolicy(sizePolicy)
        self.widget_adduser.setMinimumSize(QSize(400, 0))
        self.widget_adduser.setMaximumSize(QSize(600, 500))
        self.widget_adduser.setStyleSheet(u"QWidget {\n"
                                          "    background-color: rgba(0, 0, 0, 0.6); /* M\u00e0u n\u1ec1n \u0111en m\u1edd */\n"
                                          "    border-radius: 15px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
                                          "}\n"
                                          "")
        self.verticalLayout_17 = QVBoxLayout(self.widget_adduser)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_23 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_23)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.adduser_msnv_lineedit = QLineEdit(self.widget_adduser)
        self.adduser_msnv_lineedit.setObjectName(u"adduser_msnv_lineedit")
        sizePolicy1.setHeightForWidth(
            self.adduser_msnv_lineedit.sizePolicy().hasHeightForWidth())
        self.adduser_msnv_lineedit.setSizePolicy(sizePolicy1)
        self.adduser_msnv_lineedit.setMinimumSize(QSize(300, 40))
        self.adduser_msnv_lineedit.setFont(font2)
        self.adduser_msnv_lineedit.setAutoFillBackground(False)
        self.adduser_msnv_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                 "    background-color: #f0f0f0;\n"
                                                 "    border: 1px solid #ccc;\n"
                                                 "    border-radius: 4px;\n"
                                                 "    padding: 4px;\n"
                                                 "    color: #333;\n"
                                                 "	font-size: 14px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus {\n"
                                                 "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                 "}")
        self.adduser_msnv_lineedit.setMaxLength(30)
        self.adduser_msnv_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.adduser_msnv_lineedit)

        self.verticalLayout_17.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.adduser_password_lineedit = QLineEdit(self.widget_adduser)
        self.adduser_password_lineedit.setObjectName(
            u"adduser_password_lineedit")
        sizePolicy1.setHeightForWidth(
            self.adduser_password_lineedit.sizePolicy().hasHeightForWidth())
        self.adduser_password_lineedit.setSizePolicy(sizePolicy1)
        self.adduser_password_lineedit.setMinimumSize(QSize(300, 40))
        self.adduser_password_lineedit.setFont(font2)
        self.adduser_password_lineedit.setStyleSheet(u"QLineEdit {\n"
                                                     "    background-color: #f0f0f0;\n"
                                                     "    border: 1px solid #ccc;\n"
                                                     "    border-radius: 4px;\n"
                                                     "    padding: 4px;\n"
                                                     "    font-size: 14px;\n"
                                                     "    color: #333;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                     "}")
        self.adduser_password_lineedit.setMaxLength(16)
        self.adduser_password_lineedit.setEchoMode(QLineEdit.Password)
        self.adduser_password_lineedit.setAlignment(Qt.AlignCenter)
        self.adduser_password_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.adduser_password_lineedit)

        self.verticalLayout_17.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tabadduser_level_combobox = QComboBox(self.widget_adduser)
        self.tabadduser_level_combobox.setObjectName(
            u"tabadduser_level_combobox")
        sizePolicy1.setHeightForWidth(
            self.tabadduser_level_combobox.sizePolicy().hasHeightForWidth())
        self.tabadduser_level_combobox.setSizePolicy(sizePolicy1)
        self.tabadduser_level_combobox.setMinimumSize(QSize(300, 40))
        self.tabadduser_level_combobox.setFont(font2)
        self.tabadduser_level_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabadduser_level_combobox.setLayoutDirection(Qt.LeftToRight)
        self.tabadduser_level_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                     "QComboBox {\n"
                                                     "    background-color: #f0f0f0;\n"
                                                     "    border: 1px solid #ccc;\n"
                                                     "    border-radius: 4px;\n"
                                                     "    padding: 4px;\n"
                                                     "    font-size: 14px;\n"
                                                     "    color: #333;\n"
                                                     "}\n"
                                                     "\n"
                                                     "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                     "QComboBox:focus {\n"
                                                     "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::drop-down {\n"
                                                     "    border-left: 1px solid #ccc;\n"
                                                     "    width: 20px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::down-arrow {\n"
                                                     "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                     "}")
        self.tabadduser_level_combobox.setEditable(False)

        self.horizontalLayout_27.addWidget(self.tabadduser_level_combobox)

        self.verticalLayout_17.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.tabadduser_team_combobox = QComboBox(self.widget_adduser)
        self.tabadduser_team_combobox.setObjectName(
            u"tabadduser_team_combobox")
        sizePolicy1.setHeightForWidth(
            self.tabadduser_team_combobox.sizePolicy().hasHeightForWidth())
        self.tabadduser_team_combobox.setSizePolicy(sizePolicy1)
        self.tabadduser_team_combobox.setMinimumSize(QSize(300, 40))
        self.tabadduser_team_combobox.setFont(font2)
        self.tabadduser_team_combobox.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabadduser_team_combobox.setLayoutDirection(Qt.LeftToRight)
        self.tabadduser_team_combobox.setStyleSheet(u"/* QComboBox styling */\n"
                                                    "QComboBox {\n"
                                                    "    background-color: #f0f0f0;\n"
                                                    "    border: 1px solid #ccc;\n"
                                                    "    border-radius: 4px;\n"
                                                    "    padding: 4px;\n"
                                                    "    font-size: 14px;\n"
                                                    "    color: #333;\n"
                                                    "}\n"
                                                    "\n"
                                                    "/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
                                                    "QComboBox:focus {\n"
                                                    "    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::drop-down {\n"
                                                    "    border-left: 1px solid #ccc;\n"
                                                    "    width: 20px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::down-arrow {\n"
                                                    "    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
                                                    "}")
        self.tabadduser_team_combobox.setEditable(False)

        self.horizontalLayout_28.addWidget(self.tabadduser_team_combobox)

        self.verticalLayout_17.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.adduser_them_button = QPushButton(self.widget_adduser)
        self.adduser_them_button.setObjectName(u"adduser_them_button")
        sizePolicy6.setHeightForWidth(
            self.adduser_them_button.sizePolicy().hasHeightForWidth())
        self.adduser_them_button.setSizePolicy(sizePolicy6)
        self.adduser_them_button.setMinimumSize(QSize(300, 50))
        self.adduser_them_button.setMaximumSize(QSize(16777215, 50))
        self.adduser_them_button.setSizeIncrement(QSize(0, 40))
        self.adduser_them_button.setFont(font2)
        self.adduser_them_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.adduser_them_button.setStyleSheet(u"/* QPushButton styling */\n"
                                               "QPushButton {\n"
                                               "    background-color: #4a90e2;\n"
                                               "    border: none;\n"
                                               "    border-radius: 25px;\n"
                                               "    color: #fff;\n"
                                               "    font-size: 14px;\n"
                                               "    padding: 6px 12px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: #357ab7;\n"
                                               "	font: 16pt;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: #2a6cae;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:disabled {\n"
                                               "    background-color: #ccc;\n"
                                               "    color: #666;\n"
                                               "}")
        self.adduser_them_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.adduser_them_button)

        self.verticalLayout_17.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_26 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_26)

        self.verticalLayout_16.addWidget(self.widget_adduser)

        self.horizontalLayout_17.addWidget(self.widget_themUser)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_23)

        self.verticalLayout_18.addWidget(self.horizontalWidget_Login_2)

        icon12 = QIcon()
        icon12.addFile(u":/icon/images/icon/add_user.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabadduser, icon12, "")
        self.tabChat = QWidget()
        self.tabChat.setObjectName(u"tabChat")
        self.horizontalLayout_9 = QHBoxLayout(self.tabChat)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        icon13 = QIcon()
        icon13.addFile(u":/icon/images/icon/chat.png", QSize(),
                       QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabChat, icon13, "")

        self.verticalLayout_3.addWidget(self.tabWidget_main)

        self.widget_foot = QWidget(self.MyWidget)
        self.widget_foot.setObjectName(u"widget_foot")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_foot)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.title_foot_label = QLabel(self.widget_foot)
        self.title_foot_label.setObjectName(u"title_foot_label")
        sizePolicy5.setHeightForWidth(
            self.title_foot_label.sizePolicy().hasHeightForWidth())
        self.title_foot_label.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.title_foot_label.setFont(font6)
        self.title_foot_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.title_foot_label)

        self.verticalLayout_3.addWidget(self.widget_foot)

        self.verticalLayout_8.addWidget(self.MyWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabLogin), QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.input_status_labels.setText(
            QCoreApplication.translate("MainWindow", u"Status:", None))
        self.input_groups_labels.setText(
            QCoreApplication.translate("MainWindow", u"Groups:", None))
# if QT_CONFIG(tooltip)
        self.input_search_process_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_process_checkBox.setText("")
        self.input_model_labels.setText(
            QCoreApplication.translate("MainWindow", u"Model:", None))
# if QT_CONFIG(tooltip)
        self.input_search_model_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_model_checkBox.setText("")
        self.input_material_labels.setText(
            QCoreApplication.translate("MainWindow", u"Mat.:", None))
# if QT_CONFIG(tooltip)
        self.input_search_groups_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_groups_checkBox.setText("")
        self.input_desinvoice_labels.setText(
            QCoreApplication.translate("MainWindow", u"Des. Inv.:", None))
# if QT_CONFIG(tooltip)
        self.input_search_material_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_material_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_desinvoice_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp t\u00ean mod linh ki\u1ec7n nh\u1eadp v\u1ec1", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.input_search_desinvoice_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_desinvoice_checkBox.setText("")
        self.input_invoice_labels.setText(
            QCoreApplication.translate("MainWindow", u"Invoice:", None))
# if QT_CONFIG(tooltip)
        self.input_search_invoice_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_invoice_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_invoice_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp m\u00e3 s\u1ed1 invoice nh\u1eadp v\u1ec1", None))
# endif // QT_CONFIG(tooltip)
        self.input_component_name_labels.setText(
            QCoreApplication.translate("MainWindow", u"CName:", None))
# if QT_CONFIG(tooltip)
        self.input_size_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp k\u00edch th\u01b0\u1edbc chi\u1ec1u d\u00e0i linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.input_size_lineedit.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp chi\u1ec1u d\u00e0i", None))
# endif // QT_CONFIG(statustip)
        self.input_size_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"... x ... x ...", None))
        self.input_size_label_2.setText(
            QCoreApplication.translate("MainWindow", u"mm", None))
        self.input_storage_location_labels.setText(
            QCoreApplication.translate("MainWindow", u"SLoc.:", None))
# if QT_CONFIG(tooltip)
        self.input_search_storage_location_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_storage_location_checkBox.setText("")
        self.input_images_label.setText("")
        self.input_note_labels.setText(
            QCoreApplication.translate("MainWindow", u"Note:", None))
# if QT_CONFIG(tooltip)
        self.input_search_note_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_note_checkBox.setText("")
        self.input_note_fillter_combobox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Contains", None))
        self.input_note_fillter_combobox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Does not contains", None))
        self.input_note_fillter_combobox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Is empty", None))
        self.input_note_fillter_combobox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"Is not empty", None))

# if QT_CONFIG(tooltip)
        self.input_note_fillter_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Ch\u1ecdn t\u00ean c\u00f4ng \u0111o\u1ea1n \u0111\u1ec3 g\u1eafn linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.input_note_fillter_combobox.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Ch\u1ecdn \u0111i\u1ec1u ki\u1ec7n l\u1ecdc d\u1eef li\u1ec7u", None))
# endif // QT_CONFIG(statustip)
# if QT_CONFIG(tooltip)
        self.input_paste_button.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Ch\u1ee9c n\u0103ng :</p><p>Paste d\u1eef li\u1ec7u chuy\u1ec3n \u0111\u1ed5i copy trong invoice excel</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.input_paste_button.setText(
            QCoreApplication.translate("MainWindow", u"Paste", None))
# if QT_CONFIG(tooltip)
        self.input_storage_location_combobox.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.input_search_component_id_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_component_id_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_component_id_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.input_component_id_lineedit.setInputMask("")
# if QT_CONFIG(tooltip)
        self.input_check_id_auto_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"T\u1ea1o m\u1edbi m\u00e3 CID t\u1ef1 \u0111\u1ed9ng theo m\u00e3 s\u1ed1 th\u00f9ng hi\u1ec7n t\u1ea1i", None))
# endif // QT_CONFIG(tooltip)
        self.input_check_id_auto_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_status_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"\u0110\u01a1n v\u1ecb", None))
# endif // QT_CONFIG(tooltip)
        self.input_quantity_labels.setText(
            QCoreApplication.translate("MainWindow", u"  Qty.:", None))
# if QT_CONFIG(tooltip)
        self.input_quantity_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng", None))
# endif // QT_CONFIG(tooltip)
        self.input_quantity_lineedit.setInputMask(
            QCoreApplication.translate("MainWindow", u"0000;_", None))
# if QT_CONFIG(tooltip)
        self.input_unit_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"\u0110\u01a1n v\u1ecb", None))
# endif // QT_CONFIG(tooltip)
        self.input_process_labels.setText(
            QCoreApplication.translate("MainWindow", u"Process:", None))
# if QT_CONFIG(tooltip)
        self.input_search_component_name_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_component_name_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_component_name_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp t\u00ean g\u1ecdi linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.input_search_status_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_status_checkBox.setText("")
        self.input_size_labels.setText(
            QCoreApplication.translate("MainWindow", u"Size:", None))
# if QT_CONFIG(tooltip)
        self.input_search_size_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.input_search_size_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.input_filter_component_id_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"S\u1eafp x\u1ebfp d\u1eef li\u1ec7u c\u1ed9t ID", None))
# endif // QT_CONFIG(tooltip)
        self.input_filter_component_id_checkBox.setText("")
        self.input_new_button.setText(
            QCoreApplication.translate("MainWindow", u"New", None))
        self.input_edit_button.setText(
            QCoreApplication.translate("MainWindow", u"Edit", None))
        self.input_delete_button.setText(
            QCoreApplication.translate("MainWindow", u"Delete", None))
        self.input_export_button.setText(QCoreApplication.translate(
            "MainWindow", u"Export to Excel", None))
        self.input_down_button.setText(QCoreApplication.translate(
            "MainWindow", u"Download Image", None))
        self.input_search_button.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabInput), QCoreApplication.translate("MainWindow", u"STOCK IN", None))
        self.output_quantity_label.setText(
            QCoreApplication.translate("MainWindow", u"Qty.:", None))
        self.output_images_label.setText("")
        self.output_storage_location_label_2.setText(
            QCoreApplication.translate("MainWindow", u"SLoc.:", None))
# if QT_CONFIG(tooltip)
        self.output_storage_location_label.setToolTip(QCoreApplication.translate(
            "MainWindow", u"V\u1ecb tr\u00ed b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.output_storage_location_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
# if QT_CONFIG(tooltip)
        self.output_search_component_id_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.output_search_component_id_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.output_component_id_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.output_check_id_auto_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Ki\u1ec3m tra t\u1ed3n kho v\u00e0 th\u00f4ng tin", None))
# endif // QT_CONFIG(tooltip)
        self.output_check_id_auto_checkBox.setText("")
        self.output_desinvoice_labels_2.setText(
            QCoreApplication.translate("MainWindow", u"Des. Inv.:", None))
# if QT_CONFIG(tooltip)
        self.output_desinvoice_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
# endif // QT_CONFIG(tooltip)
        self.output_desinvoice_lineedit.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.output_note_label.setText(
            QCoreApplication.translate("MainWindow", u"Note:", None))
# if QT_CONFIG(tooltip)
        self.output_search_note_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.output_search_note_checkBox.setText("")
        self.output_component_name_label_2.setText(
            QCoreApplication.translate("MainWindow", u"CName.:", None))
        self.output_process_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Process:", None))
        self.output_groups_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Groups:", None))
# if QT_CONFIG(tooltip)
        self.output_quantity_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng c\u1ea7n xu\u1ea5t", None))
# endif // QT_CONFIG(tooltip)
        self.output_quantity_lineedit.setInputMask(
            QCoreApplication.translate("MainWindow", u"0000;_", None))
# if QT_CONFIG(tooltip)
        self.output_inventory_label.setToolTip(QCoreApplication.translate(
            "MainWindow", u"\u0110\u00e2y l\u00e0 s\u1ed1 l\u01b0\u1ee3ng t\u1ed3n kho hi\u1ec7n t\u1ea1i", None))
# endif // QT_CONFIG(tooltip)
        self.output_inventory_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.output_unit_label.setText(
            QCoreApplication.translate("MainWindow", u"pcs", None))
        self.output_invoice_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Invoice:", None))
# if QT_CONFIG(tooltip)
        self.output_invoice_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
# endif // QT_CONFIG(tooltip)
        self.output_invoice_lineedit.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.output_model_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Model:", None))
# if QT_CONFIG(tooltip)
        self.output_status_label.setToolTip(QCoreApplication.translate(
            "MainWindow", u"V\u1ecb tr\u00ed b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.output_status_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.output_size_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Size:", None))
# if QT_CONFIG(tooltip)
        self.output_size_label.setToolTip(QCoreApplication.translate(
            "MainWindow", u"K\u00edch th\u01b0\u1edbc linh ki\u1ec7n D\u00e0i x R\u1ed9ng x Cao", None))
# endif // QT_CONFIG(tooltip)
        self.output_size_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
# if QT_CONFIG(tooltip)
        self.output_component_name_label.setToolTip(QCoreApplication.translate(
            "MainWindow", u"T\u00ean g\u1ecdi linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.output_component_name_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.output_status_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Status:", None))
        self.output_material_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Mat.:", None))
        self.output_new_button.setText(
            QCoreApplication.translate("MainWindow", u"New", None))
        self.output_delete_button.setText(
            QCoreApplication.translate("MainWindow", u"Delete", None))
        self.output_export_button.setText(
            QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.output_search_button.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.output_data_tablewidget.horizontalHeaderItem(
            0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.output_data_tablewidget.horizontalHeaderItem(
            1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate(
            "MainWindow", u"Component ID", None))
        ___qtablewidgetitem2 = self.output_data_tablewidget.horizontalHeaderItem(
            2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabOutput), QCoreApplication.translate("MainWindow", u"STOCK OUT", None))
        self.layout_process_label.setText(
            QCoreApplication.translate("MainWindow", u"Process:", None))
        self.layout_search_process_radio.setText("")
# if QT_CONFIG(tooltip)
        self.layout_process_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.layout_storage_location_label.setText(
            QCoreApplication.translate("MainWindow", u"Storage Location:", None))
        self.layout_search_storage_location_radio.setText("")
# if QT_CONFIG(tooltip)
        self.layout_storage_location_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.layout_search_button.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        self.layout_label.setText(
            QCoreApplication.translate("MainWindow", u"Box", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabLayout), QCoreApplication.translate("MainWindow", u"LAYOUT", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabOther), QCoreApplication.translate("MainWindow", u"OTHER", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_material_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_material_checkBox.setText("")
        self.inventory_status_label.setText(
            QCoreApplication.translate("MainWindow", u"Status:", None))
# if QT_CONFIG(tooltip)
        self.inventory_status_combobox.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_quantity_label.setText(
            QCoreApplication.translate("MainWindow", u"Qty.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_quantity_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng nh\u1eadp", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_quantity_lineedit.setInputMask(
            QCoreApplication.translate("MainWindow", u"0000;_", None))
# if QT_CONFIG(tooltip)
        self.inventory_unit_combobox.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.inventory_search_size_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_size_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_search_storage_location_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_storage_location_checkBox.setText("")
        self.inventory_note_label.setText(
            QCoreApplication.translate("MainWindow", u"Note:", None))
        self.inventory_images_label.setText("")
        self.inventory_storage_location_label.setText(
            QCoreApplication.translate("MainWindow", u"SLoc.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_note_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_note_checkBox.setText("")
        self.inventory_desinvoice_label.setText(
            QCoreApplication.translate("MainWindow", u"Des. Inv.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_desinvoice_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_desinvoice_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_desinvoice_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"T\u00ean mod linh ki\u1ec7n c\u1ee7a invoice", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_size_label.setText(
            QCoreApplication.translate("MainWindow", u"Size:", None))
        self.inventory_material_label.setText(
            QCoreApplication.translate("MainWindow", u"Mat.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_size_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.inventory_size_lineedit.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Nh\u1eadp chi\u1ec1u d\u00e0i", None))
# endif // QT_CONFIG(statustip)
        self.inventory_size_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"... x ... x ...", None))
        self.input_size_label_7.setText(
            QCoreApplication.translate("MainWindow", u"mm", None))
# if QT_CONFIG(tooltip)
        self.inventory_storage_location_combobox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_component_id_label.setText(
            QCoreApplication.translate("MainWindow", u"CID.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_component_id_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_component_id_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_component_id_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"M\u00e3 s\u1ed1 linh ki\u1ec7n nh\u1eadp", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_component_id_lineedit.setInputMask("")
        self.inventory_invoice_label.setText(
            QCoreApplication.translate("MainWindow", u"Invoice:", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_groups_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_groups_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_search_invoice_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_invoice_checkBox.setText("")
        self.inventory_groups_label.setText(
            QCoreApplication.translate("MainWindow", u"Groups:", None))
# if QT_CONFIG(tooltip)
        self.inventory_invoice_lineedit.setToolTip(
            QCoreApplication.translate("MainWindow", u"M\u00e3 s\u1ed1 invoice", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.inventory_search_model_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_model_checkBox.setText("")
        self.inventory_model_label.setText(
            QCoreApplication.translate("MainWindow", u"Model:", None))
        self.inventory_component_name_label.setText(
            QCoreApplication.translate("MainWindow", u"CName.:", None))
# if QT_CONFIG(tooltip)
        self.inventory_search_component_name_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_component_name_checkBox.setText("")
        self.inventory_process_label.setText(
            QCoreApplication.translate("MainWindow", u"Process:", None))
# if QT_CONFIG(tooltip)
        self.inventory_component_name_lineedit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.inventory_search_process_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_process_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_search_status_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_search_status_checkBox.setText("")
# if QT_CONFIG(tooltip)
        self.inventory_filter_component_id_checkBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"S\u1eafp x\u1ebfp d\u1eef li\u1ec7u c\u1ed9t Component ID", None))
# endif // QT_CONFIG(tooltip)
        self.inventory_filter_component_id_checkBox.setText("")
        self.inventory_search_button.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        self.inventory_export_button.setText(
            QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        ___qtablewidgetitem3 = self.inventory_data_tablewidget.horizontalHeaderItem(
            0)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem4 = self.inventory_data_tablewidget.horizontalHeaderItem(
            1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate(
            "MainWindow", u"Component ID", None))
        ___qtablewidgetitem5 = self.inventory_data_tablewidget.horizontalHeaderItem(
            2)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabInventory), QCoreApplication.translate("MainWindow", u"STOCK SUMMARY", None))
        self.change_logo_label.setText("")
        self.change_msnv_label.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.change_password_old_lineedit.setInputMask("")
        self.change_password_old_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.change_password_new_lineedit.setInputMask("")
        self.change_password_new_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"New Password", None))
        self.change_password_new2_lineedit.setInputMask("")
        self.change_password_new2_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"New Password again", None))
        self.change_changing_button.setText(
            QCoreApplication.translate("MainWindow", u"Change password", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabChangepassword), QCoreApplication.translate("MainWindow", u"CHANGE PASSWORD", None))
        self.adduser_msnv_lineedit.setInputMask("")
        self.adduser_msnv_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Nh\u1eadp MSNV", None))
        self.adduser_password_lineedit.setInputMask("")
        self.adduser_password_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Nh\u1eadp Password", None))
# if QT_CONFIG(tooltip)
        self.tabadduser_level_combobox.setToolTip(
            QCoreApplication.translate("MainWindow", u"Level", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.tabadduser_team_combobox.setToolTip(
            QCoreApplication.translate("MainWindow", u"Level", None))
# endif // QT_CONFIG(tooltip)
        self.adduser_them_button.setText(
            QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabadduser), QCoreApplication.translate("MainWindow", u"ADD USER", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(
            self.tabChat), QCoreApplication.translate("MainWindow", u"CHAT", None))
        self.title_foot_label.setText(QCoreApplication.translate(
            "MainWindow", u"\u00a9 2024 WSE Company - Developed by Khoa 14-1733. For internal use only. (verson 7.0_update 2025.11.15)", None))
    # retranslateUi
