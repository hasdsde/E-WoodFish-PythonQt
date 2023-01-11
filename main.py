# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import json
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.score = 0
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - 电子木鱼"
        description = "电子木鱼"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU 侧栏是否可用
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # UI基础功能
        UIFunctions.uiDefinitions(self)

        # 表格参数
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 点击按钮
        # ///////////////////////////////////////////////////////////////

        #点击页面
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_tools.clicked.connect(self.buttonClick)
        widgets.btn_rank.clicked.connect(self.buttonClick)
        #功能按钮
        widgets.btn_click.clicked.connect(self.HomeBtnClick)

        # ///////////////////////////////////////////////////////////////
        #侧栏
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 关于
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        #自定义主题
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # 设置主页
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home_page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.ed_scoreplus.setText('')

        #初始化数据
        #本地模式
        if not os.path.exists('data.json'):
            localData = {'userName':'本地用户','score':0}
            with open('data.json', mode='w', encoding='utf-8') as f:
                json.dump(localData,f)
            print("文件已创建")
            f.close()
        with open('data.json','r+') as userDataFile:
            userData = json.load(fp=userDataFile)
            self.userName = userData['userName']
            self.score = userData['score']
            userDataFile.close()
        widgets.label_score.setText(f'你的功德值：{self.score}')

        widgets.ed_scoreplus.setText('')


    # 点击事件
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 首页
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        #物品页
        if btnName == "btn_tools":
            widgets.stackedWidget.setCurrentWidget(widgets.item_page)  
            UIFunctions.resetStyle(self, btnName)  
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))        
        #排行
        if btnName == "btn_rank":
            widgets.stackedWidget.setCurrentWidget(widgets.top_page)  
            UIFunctions.resetStyle(self, btnName)  
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # 组件页
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    # ///////////////////////////////////////////////////////////////

    #点击
    def HomeBtnClick(self):
        print("你敲了一下木鱼")
        self.score = self.score+1
        widgets.label_score.setText(f'你的功德值：{self.score}')
        # posAnime = QPropertyAnimation(widgets.ed_scoreplus,'pos')
        # posAnime.setDuration(1000)
        # posAnime.setStartValue(QPoint(360,160))
        # posAnime.setEndValue(QPoint(360,360))
        widgets.ed_scoreplus.setText('功德+1')
        self.ClickAnime = QPropertyAnimation(widgets.ed_scoreplus, b'geometry')
        self.ClickAnime.setDuration(300)
        self.ClickAnime.setStartValue(QRect(750,100,500,200))
        self.ClickAnime.setEndValue(QRect(750,100,500,0))
        self.ClickAnime.setLoopCount(1)
        self.ClickAnime.start()
        

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS 鼠标点击事件
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    #重写退出事件
    def closeEvent(self, event):
        dict = {'userName':self.userName,'score':self.score}
        with open('data.json', mode='w', encoding='utf-8') as dictF:
            json.dump(dict,dictF)
        print('退出软件，数据已保存')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
