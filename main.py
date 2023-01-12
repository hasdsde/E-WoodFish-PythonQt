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
import requests
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
        self.username = '本地用户' #默认就是本地用户
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
        widgets.btn_login.clicked.connect(self.UserLogin)
        widgets.btn_register.clicked.connect(self.UserRegister)
        widgets.pushButton.clicked.connect(self.ReflashTop)


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

        
        #本地模式
        if not os.path.exists('data.json'):
            localData = {'userName':'本地用户','score':0}
            with open('data.json', mode='w', encoding='utf-8') as f:
                json.dump(localData,f)
            f.close()
        with open('data.json','r+') as userDataFile:
            userData = json.load(fp=userDataFile)
            self.userName = userData['userName']
            self.score = userData['score']
            userDataFile.close()
        widgets.label_score.setText(f'用户：{self.username}  功德值：{self.score}')
        #初始化数据
        widgets.ed_scoreplus.setText('')
        widgets.label_score_2.setText(f'用户：{self.username}  功德值：{self.score}')
        widgets.label_3.setText(f'用户：{self.username}  功德值：{self.score}')
        #初始化道具

        #初始化排行榜
        try:
            resp = requests.get('http://localhost:8000/user/top').json()
            for index,r in enumerate(resp['data']):
                item1 = QTableWidgetItem(resp['data'][index]['username'])
                item1.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,0,item1)
                item2 = QTableWidgetItem(str(resp['data'][index]['score']))
                item2.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,1,item2)   
                item3 = QTableWidgetItem(resp['data'][index]['createTime'][0:10])
                item3.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,2,item3)
        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self,'警告',f"网络连接失败，请检查网络设置",QMessageBox.Yes,QMessageBox.Yes)

    #左侧菜单栏
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

    #点击木鱼
    def HomeBtnClick(self):
        if self.username == '本地用户':
            print("你敲了一下本地木鱼")
            self.score = self.score+1
        else:
            sp = requests.get('http://localhost:8000/logs/swear',{'username':self.username,'score':1})
            resp = sp.json()
            self.score = resp['data']['score']
            self.username = resp['data']['username']
            print("你敲了一下赛博木鱼")
        widgets.label_score.setText(f'用户：{self.username}  功德值：{self.score}')
        widgets.label_score_2.setText(f'用户：{self.username}  功德值：{self.score}')
        widgets.label_3.setText(f'用户：{self.username}  功德值：{self.score}')
        #点击动画
        widgets.ed_scoreplus.setText('功德+1')
        self.ClickAnime = QPropertyAnimation(widgets.ed_scoreplus, b'geometry')
        self.ClickAnime.setDuration(300)
        self.ClickAnime.setStartValue(QRect(750,100,500,200))
        self.ClickAnime.setEndValue(QRect(750,100,500,0))
        self.ClickAnime.setLoopCount(1)
        self.ClickAnime.start()

    #用户登录
    def UserLogin(self):
        userName = widgets.et_username.text()
        password = widgets.et_password.text()
        params = {'username':userName,'password':password}
        try:
            sp =  requests.post("http://localhost:8000/user/log",json=params)
        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self,'警告',f"网络连接失败，请检查网络设置",QMessageBox.Yes,QMessageBox.Yes)
        resp = sp.json()
        if resp['code']==200:
            QMessageBox.information(self, '登录', '登录成功', QMessageBox.Yes, QMessageBox.Yes)
            self.username = resp['data']['username']
            self.score = resp['data']['score']
        else:
            QMessageBox.warning(self,'警告',f"信息：{resp['msg']}  错误代码:{resp['code']}",QMessageBox.Yes,QMessageBox.Yes)
        widgets.label_score.setText(f'用户：{self.username}  功德值：{self.score}')
        widgets.label_score_2.setText(f'用户：{self.username}  功德值：{self.score}')
        widgets.label_3.setText(f'用户：{self.username}  功德值：{self.score}')
    #用户注册
    def UserRegister(self):
        userName = widgets.et_username.text()
        password = widgets.et_password.text()
        params ={'username':userName,'password':password}
        try:
            sp =  requests.post("http://localhost:8000/user/reg",json=params)
        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self,'警告',f"网络连接失败，请检查网络设置",QMessageBox.Yes,QMessageBox.Yes)
        resp = sp.json()
        if resp['code']==200:
            QMessageBox.information(self, '注册', '注册成功', QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.warning(self,'警告',f"信息：{resp['msg']}  错误代码:{resp['code']}",QMessageBox.Yes,QMessageBox.Yes)
    #刷新排行榜
    def ReflashTop(self):
        try:
            resp = requests.get('http://localhost:8000/user/top').json()
            for index,r in enumerate(resp['data']):
                item1 = QTableWidgetItem(resp['data'][index]['username'])
                item1.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,0,item1)
                item2 = QTableWidgetItem(str(resp['data'][index]['score']))
                item2.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,1,item2)   
                item3 = QTableWidgetItem(resp['data'][index]['createTime'][0:10])
                item3.setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                widgets.top_table.setItem(index,2,item3)
        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self,'警告',f"网络连接失败，请检查网络设置",QMessageBox.Yes,QMessageBox.Yes)
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS 鼠标点击事件 下面的函数不能去掉
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    #     # PRINT MOUSE EVENTS
    #     if event.buttons() == Qt.LeftButton:
    #         print('Mouse click: LEFT CLICK')
    #     if event.buttons() == Qt.RightButton:
    #         print('Mouse click: RIGHT CLICK')
    #重写退出事件
    def closeEvent(self, event):
        if self.username == '本地用户':
            dict = {'userName':self.userName,'score':self.score}
            with open('data.json', mode='w', encoding='utf-8') as dictF:
                json.dump(dict,dictF)
            print('退出软件，数据已保存')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
