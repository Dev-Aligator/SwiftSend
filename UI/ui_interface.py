# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacekUfhOG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from PySide2.QtWidgets import QWidget as QWidget
import UI.icon.resource_rc
from UI.widgets.scrollbar import MyScrollArea
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1579, 944)
        MainWindow.setMinimumSize(QSize(0, 75))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 100))
        self.header.setStyleSheet(u"*{\n"
"	background-color: #201C34;\n"
"}\n"
"\n"
"QFrame{\n"
"	border: none;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(221, 0))
        font = QFont()
        font.setPointSize(5)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.icon_button = QPushButton(self.frame)
        self.icon_button.setObjectName(u"icon_button")
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans Mono")
        font1.setPointSize(13)
        self.icon_button.setFont(font1)
        self.icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/swiftsend_nobg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_button.setIcon(icon)
        self.icon_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.icon_button)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"DejaVu Serif")
        font2.setPointSize(16)
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.account = QFrame(self.header)
        self.account.setObjectName(u"account")
        self.account.setMinimumSize(QSize(300, 0))
        self.account.setCursor(QCursor(Qt.ArrowCursor))
        self.account.setMouseTracking(False)
        self.account.setStyleSheet(u"QPushButton { \n"
"		border-radius: 36;\n"
"		background: white;\n"
"}\n"
"")
        self.account.setFrameShape(QFrame.StyledPanel)
        self.account.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.account)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(80, 0, 20, 0)
        self.pushButton = QPushButton(self.account)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(72, 72))
        self.pushButton.setMaximumSize(QSize(72, 72))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/default_face.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(56, 56))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.name_label = QLabel(self.account)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"QLabel {\n"
"	color: #4d88ff;\n"
"}")

        self.horizontalLayout_3.addWidget(self.name_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.account, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setStyleSheet(u"*{\n"
"\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.main_body)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_tab = QWidget(self.main_body)
        self.left_tab.setObjectName(u"left_tab")
        self.left_tab.setMinimumSize(QSize(221, 0))
        self.left_tab.setMaximumSize(QSize(221, 16777215))
        self.left_tab.setStyleSheet(u"* {\n"
"	background-color: #191F34; \n"
"}")
        self.left_button = QFrame(self.left_tab)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setGeometry(QRect(0, 0, 221, 331))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_button.sizePolicy().hasHeightForWidth())
        self.left_button.setSizePolicy(sizePolicy2)
        self.left_button.setMinimumSize(QSize(0, 0))
        self.left_button.setMaximumSize(QSize(221, 16777215))
        self.left_button.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.left_button)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 175, 0, -1)
        self.pushButton_2 = QPushButton(self.left_button)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"DejaVu Sans Mono")
        font3.setPointSize(12)
        self.pushButton_2.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/icon/telegram_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.left_button)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icon/loader_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_button)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/message_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout_4.addWidget(self.left_tab)

        self.transfer_page = QWidget(self.main_body)
        self.transfer_page.setObjectName(u"transfer_page")
        self.transfer_page.setStyleSheet(u"* {\n"
"	background-color: #1F243D;\n"
"}")

        self.horizontalLayout_4.addWidget(self.transfer_page)

        self.target_tab = QWidget(self.main_body)
        self.target_tab.setObjectName(u"target_tab")
        self.target_tab.setMinimumSize(QSize(300, 0))
        self.target_tab.setMaximumSize(QSize(300, 16777215))
        self.target_tab.setStyleSheet(u"* {\n"
"	background-color: #1F243D;\n"
"}\n"
"\n"
"\n"
"/* QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 4px;\n"
"	border-radius: 7px;\n"
" }\n"
"\n"
"QScrollBar::vertical:hover{\n"
"	width:14px;\n"
"}\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 20px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"*/\n"
"QScrollBar:vertical {\n"
"       width: 8px;\n"
"        background-color: transparent;\n"
"        margin: 0px 0px 0px 0px;\n"
"}\n"
"  QScrollBar::handle:vertical {\n"
"        background-color: rgb(80, 80, 122);\n"
"        min-height: 20px;\n"
"         border-radius: 10px;\n"
"         margin: 0px 2px 0px 2px;\n"
"  }\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.target_tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.scrollArea = MyScrollArea(self.target_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        ## self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -476, 285, 1318))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 1300))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout_4.addWidget(self.target_tab)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<span style='color: white;'>Swift</span><span style='color: #6699ff;'>Send</span>", None))
        self.pushButton.setText("")
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Henry S.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" FIle Transfer   ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Transfer Process", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" Message        ", None))
    # retranslateUi

