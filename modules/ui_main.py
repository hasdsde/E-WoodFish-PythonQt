# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpQUtcg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1370, 781)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QWidget(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setLayoutDirection(Qt.LeftToRight)
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/woodfish_icon.png);")
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_tools = QPushButton(self.topMenu)
        self.btn_tools.setObjectName(u"btn_tools")
        sizePolicy.setHeightForWidth(self.btn_tools.sizePolicy().hasHeightForWidth())
        self.btn_tools.setSizePolicy(sizePolicy)
        self.btn_tools.setMinimumSize(QSize(0, 45))
        self.btn_tools.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tools.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.btn_tools)

        self.btn_rank = QPushButton(self.topMenu)
        self.btn_rank.setObjectName(u"btn_rank")
        sizePolicy.setHeightForWidth(self.btn_rank.sizePolicy().hasHeightForWidth())
        self.btn_rank.setSizePolicy(sizePolicy)
        self.btn_rank.setMinimumSize(QSize(0, 45))
        self.btn_rank.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rank.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.btn_rank)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);\n"
"font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extraLeftBox.sizePolicy().hasHeightForWidth())
        self.extraLeftBox.setSizePolicy(sizePolicy1)
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel_login = QLabel(self.extraTopBg)
        self.extraLabel_login.setObjectName(u"extraLabel_login")
        self.extraLabel_login.setMinimumSize(QSize(150, 0))
        self.extraLabel_login.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.extraTopLayout.addWidget(self.extraLabel_login, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        sizePolicy1.setHeightForWidth(self.extraContent.sizePolicy().hasHeightForWidth())
        self.extraContent.setSizePolicy(sizePolicy1)
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.extraTopMenu = QWidget(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.UserPwd = QWidget(self.extraTopMenu)
        self.UserPwd.setObjectName(u"UserPwd")
        self.UserPwdQW = QHBoxLayout(self.UserPwd)
        self.UserPwdQW.setObjectName(u"UserPwdQW")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.UserPwdQW.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(self.UserPwd)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.UserPwdQW.addWidget(self.label_2)

        self.et_username = QLineEdit(self.UserPwd)
        self.et_username.setObjectName(u"et_username")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.et_username.sizePolicy().hasHeightForWidth())
        self.et_username.setSizePolicy(sizePolicy3)
        self.et_username.setMinimumSize(QSize(180, 0))
        self.et_username.setMaximumSize(QSize(255, 16777215))
        self.et_username.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.et_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.UserPwdQW.addWidget(self.et_username, 0, Qt.AlignRight)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.UserPwdQW.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addWidget(self.UserPwd)

        self.verticalSpacer_2 = QSpacerItem(20, 11, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.UserNameQW = QWidget(self.extraTopMenu)
        self.UserNameQW.setObjectName(u"UserNameQW")
        self.horizontalLayout_14 = QHBoxLayout(self.UserNameQW)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.UserNameQW)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label)

        self.et_password = QLineEdit(self.UserNameQW)
        self.et_password.setObjectName(u"et_password")
        sizePolicy3.setHeightForWidth(self.et_password.sizePolicy().hasHeightForWidth())
        self.et_password.setSizePolicy(sizePolicy3)
        self.et_password.setMinimumSize(QSize(180, 0))
        self.et_password.setMaximumSize(QSize(220, 16777215))
        self.et_password.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.et_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.et_password, 0, Qt.AlignRight)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)


        self.verticalLayout_11.addWidget(self.UserNameQW)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalWidget = QWidget(self.extraTopMenu)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_login = QPushButton(self.horizontalWidget)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy3.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy3)
        self.btn_login.setMinimumSize(QSize(0, 0))
        self.btn_login.setMaximumSize(QSize(166, 16777215))
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_18.addWidget(self.btn_login)


        self.verticalLayout_11.addWidget(self.horizontalWidget)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.horizontalWidget1 = QWidget(self.extraTopMenu)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_register = QPushButton(self.horizontalWidget1)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy3.setHeightForWidth(self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy3)
        self.btn_register.setMinimumSize(QSize(99, 0))
        self.btn_register.setMaximumSize(QSize(166, 16777215))
        self.btn_register.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_19.addWidget(self.btn_register)


        self.verticalLayout_11.addWidget(self.horizontalWidget1)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy4)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy5)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font-family:'Microsoft YaHei UI'; font-size:10pt")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_22 = QVBoxLayout(self.home_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_score = QLabel(self.home_page)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")

        self.verticalLayout_22.addWidget(self.label_score)

        self.ed_scoreplus = QLabel(self.home_page)
        self.ed_scoreplus.setObjectName(u"ed_scoreplus")
        self.ed_scoreplus.setStyleSheet(u"font-family:'Microsoft YaHei UI'; font-size:15pt")

        self.verticalLayout_22.addWidget(self.ed_scoreplus, 0, Qt.AlignRight)

        self.widget = QWidget(self.home_page)
        self.widget.setObjectName(u"widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy6)
        self.widget.setStyleSheet(u"background-image: url(:/images/images/images/woodfish_purple.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.verticalLayout_22.addWidget(self.widget)

        self.horizontalWidget2 = QWidget(self.home_page)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.horizontalWidget2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget2.setSizePolicy(sizePolicy7)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btn_click = QPushButton(self.horizontalWidget2)
        self.btn_click.setObjectName(u"btn_click")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(29)
        sizePolicy8.setHeightForWidth(self.btn_click.sizePolicy().hasHeightForWidth())
        self.btn_click.setSizePolicy(sizePolicy8)
        self.btn_click.setMinimumSize(QSize(0, 32))
        self.btn_click.setMaximumSize(QSize(400, 16777215))
        self.btn_click.setStyleSheet(u"background-color: rgb(52, 59, 72);font-family:'Microsoft YaHei UI'; font-size:10pt")

        self.horizontalLayout_6.addWidget(self.btn_click)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_22.addWidget(self.horizontalWidget2)

        self.stackedWidget.addWidget(self.home_page)
        self.top_page = QWidget()
        self.top_page.setObjectName(u"top_page")
        self.verticalLayout_30 = QVBoxLayout(self.top_page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_3 = QLabel(self.top_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")

        self.verticalLayout_30.addWidget(self.label_3)

        self.horizontalFrame = QFrame(self.top_page)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalFrame.setMinimumSize(QSize(25, 25))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_9 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.pushButton = QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy9)
        self.pushButton.setMinimumSize(QSize(12, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777211))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);font-family:'Microsoft YaHei UI'; font-size:10pt")

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.horizontalSpacer_10 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)


        self.verticalLayout_30.addWidget(self.horizontalFrame)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.top_table = QTableWidget(self.top_page)
        if (self.top_table.columnCount() < 3):
            self.top_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.top_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.top_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.top_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.top_table.rowCount() < 17):
            self.top_table.setRowCount(17)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.top_table.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.top_table.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.top_table.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.top_table.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.top_table.setItem(1, 0, __qtablewidgetitem23)
        self.top_table.setObjectName(u"top_table")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.top_table.sizePolicy().hasHeightForWidth())
        self.top_table.setSizePolicy(sizePolicy10)
        self.top_table.setMinimumSize(QSize(0, 0))
        self.top_table.setFont(font1)
        self.top_table.setLayoutDirection(Qt.LeftToRight)
        self.top_table.setAutoFillBackground(True)
        self.top_table.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.top_table.setTabKeyNavigation(True)
        self.top_table.setShowGrid(True)
        self.top_table.setGridStyle(Qt.NoPen)
        self.top_table.horizontalHeader().setDefaultSectionSize(120)

        self.horizontalLayout_10.addWidget(self.top_table)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_30.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.top_page)
        self.item_page = QWidget()
        self.item_page.setObjectName(u"item_page")
        self.verticalLayout_23 = QVBoxLayout(self.item_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_score_2 = QLabel(self.item_page)
        self.label_score_2.setObjectName(u"label_score_2")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_score_2.sizePolicy().hasHeightForWidth())
        self.label_score_2.setSizePolicy(sizePolicy11)
        self.label_score_2.setMinimumSize(QSize(0, 0))
        self.label_score_2.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.label_score_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_23.addWidget(self.label_score_2)

        self.verticalFrame = QFrame(self.item_page)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_21 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.item_row_2 = QFrame(self.verticalFrame)
        self.item_row_2.setObjectName(u"item_row_2")
        self.horizontalLayout_8 = QHBoxLayout(self.item_row_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.item_row_1 = QFrame(self.item_row_2)
        self.item_row_1.setObjectName(u"item_row_1")
        self.horizontalLayout_7 = QHBoxLayout(self.item_row_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.item1_name = QLabel(self.item_row_1)
        self.item1_name.setObjectName(u"item1_name")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.item1_name.sizePolicy().hasHeightForWidth())
        self.item1_name.setSizePolicy(sizePolicy12)
        self.item1_name.setMinimumSize(QSize(0, 53))
        self.item1_name.setLayoutDirection(Qt.LeftToRight)
        self.item1_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item1_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_26.addWidget(self.item1_name)

        self.item1_desc = QLabel(self.item_row_1)
        self.item1_desc.setObjectName(u"item1_desc")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(5)
        sizePolicy13.setHeightForWidth(self.item1_desc.sizePolicy().hasHeightForWidth())
        self.item1_desc.setSizePolicy(sizePolicy13)
        self.item1_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item1_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.item1_desc)

        self.btn_item1 = QPushButton(self.item_row_1)
        self.btn_item1.setObjectName(u"btn_item1")
        sizePolicy12.setHeightForWidth(self.btn_item1.sizePolicy().hasHeightForWidth())
        self.btn_item1.setSizePolicy(sizePolicy12)
        self.btn_item1.setMinimumSize(QSize(133, 0))
        self.btn_item1.setMaximumSize(QSize(150, 16777215))
        self.btn_item1.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_26.addWidget(self.btn_item1)


        self.horizontalLayout_7.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.item2_name = QLabel(self.item_row_1)
        self.item2_name.setObjectName(u"item2_name")
        sizePolicy12.setHeightForWidth(self.item2_name.sizePolicy().hasHeightForWidth())
        self.item2_name.setSizePolicy(sizePolicy12)
        self.item2_name.setMinimumSize(QSize(0, 53))
        self.item2_name.setLayoutDirection(Qt.LeftToRight)
        self.item2_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item2_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_27.addWidget(self.item2_name)

        self.item2_desc = QLabel(self.item_row_1)
        self.item2_desc.setObjectName(u"item2_desc")
        sizePolicy13.setHeightForWidth(self.item2_desc.sizePolicy().hasHeightForWidth())
        self.item2_desc.setSizePolicy(sizePolicy13)
        self.item2_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item2_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.item2_desc)

        self.btn_item2 = QPushButton(self.item_row_1)
        self.btn_item2.setObjectName(u"btn_item2")
        sizePolicy12.setHeightForWidth(self.btn_item2.sizePolicy().hasHeightForWidth())
        self.btn_item2.setSizePolicy(sizePolicy12)
        self.btn_item2.setMinimumSize(QSize(133, 0))
        self.btn_item2.setMaximumSize(QSize(150, 16777215))
        self.btn_item2.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_27.addWidget(self.btn_item2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.item3_name = QLabel(self.item_row_1)
        self.item3_name.setObjectName(u"item3_name")
        sizePolicy12.setHeightForWidth(self.item3_name.sizePolicy().hasHeightForWidth())
        self.item3_name.setSizePolicy(sizePolicy12)
        self.item3_name.setMinimumSize(QSize(0, 53))
        self.item3_name.setLayoutDirection(Qt.LeftToRight)
        self.item3_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item3_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_28.addWidget(self.item3_name)

        self.item3_desc = QLabel(self.item_row_1)
        self.item3_desc.setObjectName(u"item3_desc")
        sizePolicy13.setHeightForWidth(self.item3_desc.sizePolicy().hasHeightForWidth())
        self.item3_desc.setSizePolicy(sizePolicy13)
        self.item3_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item3_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.item3_desc)

        self.btn_item3 = QPushButton(self.item_row_1)
        self.btn_item3.setObjectName(u"btn_item3")
        sizePolicy12.setHeightForWidth(self.btn_item3.sizePolicy().hasHeightForWidth())
        self.btn_item3.setSizePolicy(sizePolicy12)
        self.btn_item3.setMinimumSize(QSize(133, 0))
        self.btn_item3.setMaximumSize(QSize(150, 16777215))
        self.btn_item3.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_28.addWidget(self.btn_item3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.item4_name = QLabel(self.item_row_1)
        self.item4_name.setObjectName(u"item4_name")
        sizePolicy12.setHeightForWidth(self.item4_name.sizePolicy().hasHeightForWidth())
        self.item4_name.setSizePolicy(sizePolicy12)
        self.item4_name.setMinimumSize(QSize(0, 53))
        self.item4_name.setLayoutDirection(Qt.LeftToRight)
        self.item4_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item4_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_29.addWidget(self.item4_name)

        self.item4_desc = QLabel(self.item_row_1)
        self.item4_desc.setObjectName(u"item4_desc")
        sizePolicy13.setHeightForWidth(self.item4_desc.sizePolicy().hasHeightForWidth())
        self.item4_desc.setSizePolicy(sizePolicy13)
        self.item4_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item4_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.item4_desc)

        self.btn_item4 = QPushButton(self.item_row_1)
        self.btn_item4.setObjectName(u"btn_item4")
        sizePolicy12.setHeightForWidth(self.btn_item4.sizePolicy().hasHeightForWidth())
        self.btn_item4.setSizePolicy(sizePolicy12)
        self.btn_item4.setMinimumSize(QSize(133, 0))
        self.btn_item4.setMaximumSize(QSize(150, 16777215))
        self.btn_item4.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_29.addWidget(self.btn_item4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_29)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.item5_name = QLabel(self.item_row_1)
        self.item5_name.setObjectName(u"item5_name")
        sizePolicy12.setHeightForWidth(self.item5_name.sizePolicy().hasHeightForWidth())
        self.item5_name.setSizePolicy(sizePolicy12)
        self.item5_name.setMinimumSize(QSize(0, 53))
        self.item5_name.setLayoutDirection(Qt.LeftToRight)
        self.item5_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item5_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_20.addWidget(self.item5_name)

        self.item5_desc = QLabel(self.item_row_1)
        self.item5_desc.setObjectName(u"item5_desc")
        sizePolicy13.setHeightForWidth(self.item5_desc.sizePolicy().hasHeightForWidth())
        self.item5_desc.setSizePolicy(sizePolicy13)
        self.item5_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item5_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.item5_desc)

        self.btn_item5 = QPushButton(self.item_row_1)
        self.btn_item5.setObjectName(u"btn_item5")
        sizePolicy12.setHeightForWidth(self.btn_item5.sizePolicy().hasHeightForWidth())
        self.btn_item5.setSizePolicy(sizePolicy12)
        self.btn_item5.setMinimumSize(QSize(133, 0))
        self.btn_item5.setMaximumSize(QSize(150, 16777215))
        self.btn_item5.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_20.addWidget(self.btn_item5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_20)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.item6_name = QLabel(self.item_row_1)
        self.item6_name.setObjectName(u"item6_name")
        sizePolicy12.setHeightForWidth(self.item6_name.sizePolicy().hasHeightForWidth())
        self.item6_name.setSizePolicy(sizePolicy12)
        self.item6_name.setMinimumSize(QSize(0, 53))
        self.item6_name.setLayoutDirection(Qt.LeftToRight)
        self.item6_name.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"background-repeat: no-repeat;\n"
"color:rgb(223,121,198);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.item6_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_25.addWidget(self.item6_name)

        self.item6_desc = QLabel(self.item_row_1)
        self.item6_desc.setObjectName(u"item6_desc")
        sizePolicy13.setHeightForWidth(self.item6_desc.sizePolicy().hasHeightForWidth())
        self.item6_desc.setSizePolicy(sizePolicy13)
        self.item6_desc.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.item6_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.item6_desc)

        self.btn_item6 = QPushButton(self.item_row_1)
        self.btn_item6.setObjectName(u"btn_item6")
        sizePolicy12.setHeightForWidth(self.btn_item6.sizePolicy().hasHeightForWidth())
        self.btn_item6.setSizePolicy(sizePolicy12)
        self.btn_item6.setMinimumSize(QSize(133, 0))
        self.btn_item6.setMaximumSize(QSize(150, 16777215))
        self.btn_item6.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_25.addWidget(self.btn_item6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_25)


        self.horizontalLayout_8.addWidget(self.item_row_1)


        self.verticalLayout_24.addWidget(self.item_row_2)

        self.item_row_3 = QFrame(self.verticalFrame)
        self.item_row_3.setObjectName(u"item_row_3")
        self.item_row = QHBoxLayout(self.item_row_3)
        self.item_row.setObjectName(u"item_row")

        self.verticalLayout_24.addWidget(self.item_row_3)


        self.verticalLayout_21.addLayout(self.verticalLayout_24)


        self.verticalLayout_23.addWidget(self.verticalFrame)

        self.stackedWidget.addWidget(self.item_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_message = QPushButton(self.contentSettings)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-moon.png);font: 9pt \"Microsoft YaHei UI\";\n"
"")

        self.verticalLayout_10.addWidget(self.btn_message)

        self.btn_logout = QPushButton(self.contentSettings)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_10.addWidget(self.btn_logout)

        self.btn_message_3 = QPushButton(self.contentSettings)
        self.btn_message_3.setObjectName(u"btn_message_3")
        sizePolicy.setHeightForWidth(self.btn_message_3.sizePolicy().hasHeightForWidth())
        self.btn_message_3.setSizePolicy(sizePolicy)
        self.btn_message_3.setMinimumSize(QSize(0, 45))
        self.btn_message_3.setFont(font1)
        self.btn_message_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message_3.setLayoutDirection(Qt.LeftToRight)
        self.btn_message_3.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-star.png);font: 9pt \"Microsoft YaHei UI\";\n"
"")

        self.verticalLayout_10.addWidget(self.btn_message_3)

        self.btn_message_2 = QPushButton(self.contentSettings)
        self.btn_message_2.setObjectName(u"btn_message_2")
        sizePolicy.setHeightForWidth(self.btn_message_2.sizePolicy().hasHeightForWidth())
        self.btn_message_2.setSizePolicy(sizePolicy)
        self.btn_message_2.setMinimumSize(QSize(0, 45))
        self.btn_message_2.setFont(font1)
        self.btn_message_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_message_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-circle.png);font: 9pt \"Microsoft YaHei UI\";\n"
"")

        self.verticalLayout_10.addWidget(self.btn_message_2)

        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.topMenus)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u6728\u9c7c", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u5728\u505a\u4e86", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_tools.setText(QCoreApplication.translate("MainWindow", u"\u9053\u5177", None))
        self.btn_rank.setText(QCoreApplication.translate("MainWindow", u"\u6392\u884c\u699c", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.extraLabel_login.setText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u767b\u5f55/\u6ce8\u518c", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u6728\u9c7c", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"\u529f\u5fb7\u503c\uff1a999", None))
        self.ed_scoreplus.setText(QCoreApplication.translate("MainWindow", u"\u529f\u5fb7+1", None))
        self.btn_click.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4f60\u7684\u5206\u6570\uff1a\u4f60\u7684\u6392\u540d\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        ___qtablewidgetitem = self.top_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.top_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None));
        ___qtablewidgetitem2 = self.top_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
        ___qtablewidgetitem3 = self.top_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.top_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.top_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.top_table.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem7 = self.top_table.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem8 = self.top_table.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.top_table.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem10 = self.top_table.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.top_table.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem12 = self.top_table.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem13 = self.top_table.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem14 = self.top_table.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem15 = self.top_table.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem16 = self.top_table.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem17 = self.top_table.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem18 = self.top_table.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem19 = self.top_table.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"20", None));

        __sortingEnabled = self.top_table.isSortingEnabled()
        self.top_table.setSortingEnabled(False)
        self.top_table.setSortingEnabled(__sortingEnabled)

        self.label_score_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u5fb7\u503c\uff1a999", None))
        self.item1_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item1_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item1.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.item2_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item2_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item2.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.item3_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item3_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item3.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.item4_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item4_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item4.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.item5_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item5_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item5.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.item6_name.setText(QCoreApplication.translate("MainWindow", u"\u9053\u51771", None))
        self.item6_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u9053\u51771\u7684\u5177\u4f53\u89e3\u91ca", None))
        self.btn_item6.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u767b\u51fa\u767b\u5f55", None))
        self.btn_message_3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6e90\u5730\u5740", None))
        self.btn_message_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u72b6\u6001\u680f", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi



