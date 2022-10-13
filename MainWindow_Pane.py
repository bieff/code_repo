# 主界面，调用生成的main_window_ui.py文件
from PyQt5.Qt import *
import pymysql
from resource.mainwindow_ui import Ui_Form
from DatabaseCommand_Pane import DatabaseCommandPane
from DatabaseVisual_Pane import DatabaseVisualPane
from Analysis_Pane import AnalysisPane
from Article_Pane import ArticlePane
from Guide_Pane import GuidePane
from Information_Pane import InformationPane
from Official_Pane import OfficialPane
from UserManagement_Pane import UserManagementPane
from Personcard_Pane import PersoncardPane
from Skin_Pane import SkinPane
from PyQt5.QtCore import QTimer,QDateTime

# 加载QSS表
class QSSLoad:
    def __init__(self):
        pass
    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r', encoding='UTF-8') as file:
            return file.read()

class MainWindowPane(QWidget, Ui_Form):
    switch_Signal = pyqtSignal()  # 切换账号信号
    exit_Signal = pyqtSignal() # 退出信号

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏
        self.setupUi(self)

        self.user_account = "201601033017" # 当前用户账号
        self.user_name = "夜晓希声"
        qssFileName = "./resource/qss/mainwindow_2.qss"
        qssFile = QSSLoad.readQssFile(qssFileName)
        self.setStyleSheet(qssFile)
        self.current_style_id = 2 # 当前样式id
        self.Timer = QTimer()  # 自定义QTimer
        self.Timer.start(500)  # 每0.5秒运行一次
        self.Timer.timeout.connect(self.updateTime)  # 连接updateTime
        # self.create_frame()
        self.trans = QTranslator() # 翻译家
        self.current_language = "zh_CN"
        self._padding = 5  # 设置边界宽度为5
        self.initDrag() # 设置鼠标跟踪判断默认值
        self.setMouseTracking(True)  # 设置widget鼠标跟踪

    def updateTime(self):
        self.time_label.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd'))  # 显示时间的格式

    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def resizeEvent(self, QResizeEvent):
        # 自定义窗口调整大小事件
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding)
                            for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.mainwindow_widget.geometry()):
            self._move_drag = True
            self._startPos = QPoint(event.x(), event.y())
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if Qt.LeftButton and self._right_drag:
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._move_drag:
            self._endPos = QMouseEvent.pos() - self._startPos
            self.move(self.pos() + self._endPos)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.setCursor(Qt.ArrowCursor)
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def sql_user_ifo(self):
        # print("初始化用户信息")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            cur.execute("select * from user_ifo where user_account='%s'"%self.user_account)
            row = cur.fetchone()
            self.user_account = row[0]
            self.user_name = row[1]
            self.user_password = row[2]
            self.user_email = row[3]
            self.user_introduction = row[4]
            self.user_sex = row[5]
            self.user_headimageurl = row[6]
            self.user_experience = row[7]
            self.user_grade = row[8]
            self.current_account = self.user_account  # 当前账号
            self.current_name = self.user_name  # 当前用户名
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def create_frame(self):
        # 初始化界面
        self.databaseCommandPane = DatabaseCommandPane() # 数据库命令行操作界面
        self.databaseCommandPane.setObjectName("databaseCommandPane")
        self.stackedWidget.addWidget(self.databaseCommandPane)
        self.databaseVisualPane = DatabaseVisualPane() # 数据库可视化操作界面
        self.databaseVisualPane.setObjectName("databaseVisualPane")
        self.stackedWidget.addWidget(self.databaseVisualPane)
        self.analysisPane = AnalysisPane() # 数据可视化分析界面
        self.analysisPane.setObjectName("analysisPane")
        self.stackedWidget.addWidget(self.analysisPane)
        self.userManagementPane = UserManagementPane() # 用户管理界面
        self.userManagementPane.setObjectName("userManagementPane")
        self.stackedWidget.addWidget(self.userManagementPane)
        self.articlePane = ArticlePane() # 文章推送界面
        self.articlePane.setObjectName("articlePane")
        self.stackedWidget.addWidget(self.articlePane)
        self.guidePane = GuidePane() # 使用向导界面
        self.guidePane.setObjectName("guidePane")
        self.stackedWidget.addWidget(self.guidePane)
        self.informationPane = InformationPane() # 软件信息界面
        self.informationPane.setObjectName("informationPane")
        self.stackedWidget.addWidget(self.informationPane)
        self.officialPane = OfficialPane() # 官方社交账号界面
        self.officialPane.setObjectName("officialPane")
        self.stackedWidget.addWidget(self.officialPane)
        self.userManagementPane.headimage_Signal.connect(self.change_userIfo)
        self.userManagementPane.username_Signal.connect(self.change_userIfo)
        self.stackedWidget.setCurrentIndex(0) # 设置当前页面
        self.listWidget.setCurrentRow(0) # 设置当前条目
        self.init_userIfo() # 调用用户信息初始化方法

    def init_userIfo(self):
        # print("初始化当前用户信息")
        self.sql_user_ifo()
        self.current_headimage_url = self.user_headimageurl
        self.current_username = self.user_name
        self.userIcon_btn.setStyleSheet("QPushButton{border-radius:18px;border:none;border-image: url(%s);}"%self.current_headimage_url)
        self.userName_btn.setText(self.current_username)
        self.databaseCommandPane.user_account = self.user_account
        self.databaseVisualPane.user_account = self.user_account
        self.analysisPane.user_account = self.user_account
        self.userManagementPane.user_account = self.user_account
        self.userManagementPane.user_name = self.user_name
        self.userManagementPane.showIfo()
        self.informationPane.user_account = self.user_account
        self.informationPane.user_name = self.user_name
        self.informationPane.showIfo()

    def change_frame(self, item):
        # print("切换页面")
        self.listWidget.row(item)
        if self.listWidget.row(item) == 0:
            self.stackedWidget.setCurrentIndex(0)
        elif self.listWidget.row(item) == 1:
            self.stackedWidget.setCurrentIndex(1)
        elif self.listWidget.row(item) == 2:
            self.stackedWidget.setCurrentIndex(2)
        elif self.listWidget.row(item) == 3:
            self.stackedWidget.setCurrentIndex(3)
        elif self.listWidget.row(item) == 4:
            self.stackedWidget.setCurrentIndex(4)
        elif self.listWidget.row(item) == 5:
            self.stackedWidget.setCurrentIndex(5)
        elif self.listWidget.row(item) == 6:
            self.stackedWidget.setCurrentIndex(6)
        elif self.listWidget.row(item) == 7:
            self.stackedWidget.setCurrentIndex(7)

    def open_usermanagement_pane(self):
        # print("打开用户管理界面")
        self.stackedWidget.setCurrentIndex(3)
        self.listWidget.setCurrentRow(3)  # 设置当前条目

    def open_guide_pane(self):
        # print("打开使用向导界面")
        self.stackedWidget.setCurrentIndex(5)
        self.listWidget.setCurrentRow(5)  # 设置当前条目

    def open_official_pane(self):
        # print("打开联系我们界面")
        self.stackedWidget.setCurrentIndex(7)
        self.listWidget.setCurrentRow(7)  # 设置当前条目

    def open_personcard(self):
        # print("打开个人资料卡")
        self.personcard_pane = PersoncardPane()
        self.personcard_pane.setFocusPolicy(Qt.ClickFocus)
        self.personcard_pane.user_account = self.user_account  # 当前账号
        self.personcard_pane.user_name = self.user_name
        self.personcard_pane.showIfo()
        self.personcard_pane.show()
        self.personcard_pane.touxiang_btn.setStyleSheet(
            "QPushButton{border-radius:25px;border-image: url(%s);}" % self.current_headimage_url)
        self.personcard_pane.username_label.setText(self.current_username)
        if self.current_language == "zh_CN":
            self.personcard_pane.actionSCn.setChecked(True)
            self.personcard_pane.actionTCn.setChecked(False)
            self.personcard_pane.actionEn.setChecked(False)
            self.personcard_pane.actionKo.setChecked(False)
            self.personcard_pane.actionJa.setChecked(False)
        elif self.current_language == "zh_TW":
            self.personcard_pane.actionSCn.setChecked(False)
            self.personcard_pane.actionTCn.setChecked(True)
            self.personcard_pane.actionEn.setChecked(False)
            self.personcard_pane.actionKo.setChecked(False)
            self.personcard_pane.actionJa.setChecked(False)
        elif self.current_language == "en":
            self.personcard_pane.actionSCn.setChecked(False)
            self.personcard_pane.actionTCn.setChecked(False)
            self.personcard_pane.actionEn.setChecked(True)
            self.personcard_pane.actionKo.setChecked(False)
            self.personcard_pane.actionJa.setChecked(False)
        elif self.current_language == "ko":
            self.personcard_pane.actionSCn.setChecked(False)
            self.personcard_pane.actionTCn.setChecked(False)
            self.personcard_pane.actionEn.setChecked(False)
            self.personcard_pane.actionKo.setChecked(True)
            self.personcard_pane.actionJa.setChecked(False)
        else:
            self.personcard_pane.actionSCn.setChecked(False)
            self.personcard_pane.actionTCn.setChecked(False)
            self.personcard_pane.actionEn.setChecked(False)
            self.personcard_pane.actionKo.setChecked(False)
            self.personcard_pane.actionJa.setChecked(True)
        self.personcard_pane.zh_CN_Signal.connect(self.change_language_zh_CN)
        self.personcard_pane.zh_TW_Signal.connect(self.change_language_zh_TW)
        self.personcard_pane.en_Signal.connect(self.change_language_en)
        self.personcard_pane.ko_Signal.connect(self.change_language_ko)
        self.personcard_pane.ja_Signal.connect(self.change_language_ja)
        self.personcard_pane.user_management_Signal.connect(self.open_usermanagement_pane)
        self.personcard_pane.guide_Signal.connect(self.open_guide_pane)
        self.personcard_pane.official_Signal.connect(self.open_official_pane)
        self.personcard_pane.switch_Signal.connect(self.switch_account)
        self.personcard_pane.exit_Signal.connect(self.exit_account)
        x = self.pos().x() + self.userName_btn.pos().x() + (self.userName_btn.width()/2) - (self.personcard_pane.width()/2)
        y = self.pos().y() + self.mainwindow_widget.pos().y() + self.mainwindow_widget.height()
        self.personcard_pane.move(x, y)

    def switch_account(self):
        # print("切换账号")
        self.switch_Signal.emit()
        self.personcard_pane.close()
        self.close()

    def exit_account(self):
        # print("main退出账号")
        self.exit_Signal.emit()
        self.personcard_pane.close()
        self.close()

    def open_skin(self):
        # print("打开换肤")
        self.skin_pane = SkinPane()
        self.skin_pane.setFocusPolicy(Qt.ClickFocus)
        self.skin_pane.show()
        if self.current_style_id == 1:
            self.skin_pane.r_slider.setValue(22)
            self.skin_pane.g_slider.setValue(24)
            self.skin_pane.b_slider.setValue(28)
            self.skin_pane.black_icon.setChecked(True)
        elif self.current_style_id == 2:
            self.skin_pane.r_slider.setValue(198)
            self.skin_pane.g_slider.setValue(47)
            self.skin_pane.b_slider.setValue(47)
            self.skin_pane.red_icon.setChecked(True)
        elif self.current_style_id == 3:
            self.skin_pane.r_slider.setValue(247)
            self.skin_pane.g_slider.setValue(153)
            self.skin_pane.b_slider.setValue(191)
            self.skin_pane.pink_icon.setChecked(True)
        elif self.current_style_id == 4:
            self.skin_pane.r_slider.setValue(85)
            self.skin_pane.g_slider.setValue(180)
            self.skin_pane.b_slider.setValue(251)
            self.skin_pane.blue_icon.setChecked(True)
        elif self.current_style_id == 5:
            self.skin_pane.r_slider.setValue(86)
            self.skin_pane.g_slider.setValue(198)
            self.skin_pane.b_slider.setValue(129)
            self.skin_pane.green_icon.setChecked(True)
        elif self.current_style_id == 6:
            self.skin_pane.r_slider.setValue(224)
            self.skin_pane.g_slider.setValue(165)
            self.skin_pane.b_slider.setValue(84)
            self.skin_pane.gold_icon.setChecked(True)
        elif self.current_style_id == 7:
            self.skin_pane.r_slider.setValue(255)
            self.skin_pane.g_slider.setValue(92)
            self.skin_pane.b_slider.setValue(138)
            self.skin_pane.color1_icon.setChecked(True)
        elif self.current_style_id == 8:
            self.skin_pane.r_slider.setValue(239)
            self.skin_pane.g_slider.setValue(122)
            self.skin_pane.b_slider.setValue(158)
            self.skin_pane.color2_icon.setChecked(True)
        elif self.current_style_id == 9:
            self.skin_pane.r_slider.setValue(254)
            self.skin_pane.g_slider.setValue(118)
            self.skin_pane.b_slider.setValue(200)
            self.skin_pane.color3_icon.setChecked(True)
        elif self.current_style_id == 10:
            self.skin_pane.r_slider.setValue(113)
            self.skin_pane.g_slider.setValue(127)
            self.skin_pane.b_slider.setValue(249)
            self.skin_pane.color4_icon.setChecked(True)
        elif self.current_style_id == 11:
            self.skin_pane.r_slider.setValue(71)
            self.skin_pane.g_slider.setValue(145)
            self.skin_pane.b_slider.setValue(235)
            self.skin_pane.color5_icon.setChecked(True)
        elif self.current_style_id == 12:
            self.skin_pane.r_slider.setValue(57)
            self.skin_pane.g_slider.setValue(175)
            self.skin_pane.b_slider.setValue(234)
            self.skin_pane.color6_icon.setChecked(True)
        elif self.current_style_id == 13:
            self.skin_pane.r_slider.setValue(43)
            self.skin_pane.g_slider.setValue(182)
            self.skin_pane.b_slider.setValue(105)
            self.skin_pane.color7_icon.setChecked(True)
        elif self.current_style_id == 14:
            self.skin_pane.r_slider.setValue(106)
            self.skin_pane.g_slider.setValue(204)
            self.skin_pane.b_slider.setValue(25)
            self.skin_pane.color8_icon.setChecked(True)
        elif self.current_style_id == 15:
            self.skin_pane.r_slider.setValue(226)
            self.skin_pane.g_slider.setValue(171)
            self.skin_pane.b_slider.setValue(18)
            self.skin_pane.color9_icon.setChecked(True)
        elif self.current_style_id == 16:
            self.skin_pane.r_slider.setValue(255)
            self.skin_pane.g_slider.setValue(143)
            self.skin_pane.b_slider.setValue(87)
            self.skin_pane.color10_icon.setChecked(True)
        elif self.current_style_id == 17:
            self.skin_pane.r_slider.setValue(253)
            self.skin_pane.g_slider.setValue(114)
            self.skin_pane.b_slider.setValue(109)
            self.skin_pane.color11_icon.setChecked(True)
        elif self.current_style_id == 18:
            self.skin_pane.r_slider.setValue(253)
            self.skin_pane.g_slider.setValue(84)
            self.skin_pane.b_slider.setValue(78)
            self.skin_pane.color12_icon.setChecked(True)
        elif self.current_style_id == 19:
            self.skin_pane.r_slider.setValue(self.color_r)
            self.skin_pane.g_slider.setValue(self.color_g)
            self.skin_pane.b_slider.setValue(self.color_b)
            self.skin_pane.pane_icon.setChecked(True)
        self.skin_pane.style_Signal.connect(self.change_style)
        self.skin_pane.color_Signal.connect(self.change_color)
        x = self.pos().x() + self.skin_btn.pos().x() + (self.skin_btn.width() / 2) - (self.skin_pane.width() / 2)
        y = self.pos().y() + self.mainwindow_widget.pos().y() + self.mainwindow_widget.height()
        self.skin_pane.move(x, y)

    def change_language_zh_CN(self):
        # print("设置简体中文")
        self.current_language = "zh_CN"
        self.trans.load("./resource/translation/mainwindow_zh_CN")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def change_language_zh_TW(self):
        # print("设置繁体中文")
        self.current_language = "zh_TW"
        self.trans.load("./resource/translation/mainwindow_zh_TW")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def change_language_en(self):
        # print("设置英语")
        self.current_language = "en"
        self.trans.load("./resource/translation/mainwindow_en")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def change_language_ko(self):
        # print("设置韩语")
        self.current_language = "ko"
        self.trans.load("./resource/translation/mainwindow_ko")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def change_language_ja(self):
        # print("设置日语")
        self.current_language = "ja"
        self.trans.load("./resource/translation/mainwindow_ja")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def change_style(self, style_id):
        # print("更换样式")
        if style_id == 1:
            qssFileName = "./resource/qss/mainwindow_1.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(22)
            self.skin_pane.g_slider.setValue(24)
            self.skin_pane.b_slider.setValue(28)
            self.current_style_id = 1
        elif style_id == 2:
            qssFileName = "./resource/qss/mainwindow_2.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(198)
            self.skin_pane.g_slider.setValue(47)
            self.skin_pane.b_slider.setValue(47)
            self.current_style_id = 2
        elif style_id == 3:
            qssFileName = "./resource/qss/mainwindow_3.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(247)
            self.skin_pane.g_slider.setValue(153)
            self.skin_pane.b_slider.setValue(191)
            self.current_style_id = 3
        elif style_id == 4:
            qssFileName = "./resource/qss/mainwindow_4.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(85)
            self.skin_pane.g_slider.setValue(180)
            self.skin_pane.b_slider.setValue(251)
            self.current_style_id = 4
        elif style_id == 5:
            qssFileName = "./resource/qss/mainwindow_5.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(86)
            self.skin_pane.g_slider.setValue(198)
            self.skin_pane.b_slider.setValue(129)
            self.current_style_id = 5
        elif style_id == 6:
            qssFileName = "./resource/qss/mainwindow_6.qss"
            qssFile = QSSLoad.readQssFile(qssFileName)
            self.setStyleSheet(qssFile)
            self.skin_pane.r_slider.setValue(224)
            self.skin_pane.g_slider.setValue(165)
            self.skin_pane.b_slider.setValue(84)
            self.current_style_id = 6

    def change_color(self, r, g, b):
        # print("换肤")
        if r == 255 and g == 92 and b == 138:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(255, 92, 138);}")
            self.skin_pane.r_slider.setValue(255)
            self.skin_pane.g_slider.setValue(92)
            self.skin_pane.b_slider.setValue(138)
            self.current_style_id = 7
        elif r == 239 and g == 122 and b == 158:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(239, 122, 158);}")
            self.skin_pane.r_slider.setValue(239)
            self.skin_pane.g_slider.setValue(122)
            self.skin_pane.b_slider.setValue(158)
            self.current_style_id = 8
        elif r == 254 and g == 118 and b == 200:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(254, 118, 200);}")
            self.skin_pane.r_slider.setValue(254)
            self.skin_pane.g_slider.setValue(118)
            self.skin_pane.b_slider.setValue(200)
            self.current_style_id = 9
        elif r == 113 and g == 127 and b == 249:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(113, 127, 249);}")
            self.skin_pane.r_slider.setValue(113)
            self.skin_pane.g_slider.setValue(127)
            self.skin_pane.b_slider.setValue(249)
            self.current_style_id = 10
        elif r == 71 and g == 145 and b == 235:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(71, 145, 235);}")
            self.skin_pane.r_slider.setValue(71)
            self.skin_pane.g_slider.setValue(145)
            self.skin_pane.b_slider.setValue(235)
            self.current_style_id = 11
        elif r == 57 and g == 175 and b == 234:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(57, 175, 234);}")
            self.skin_pane.r_slider.setValue(57)
            self.skin_pane.g_slider.setValue(175)
            self.skin_pane.b_slider.setValue(234)
            self.current_style_id = 12
        elif r == 43 and g == 182 and b == 105:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(43, 182, 105);}")
            self.skin_pane.r_slider.setValue(43)
            self.skin_pane.g_slider.setValue(182)
            self.skin_pane.b_slider.setValue(105)
            self.current_style_id = 13
        elif r == 106 and g == 204 and b == 25:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(106, 204, 25);}")
            self.skin_pane.r_slider.setValue(106)
            self.skin_pane.g_slider.setValue(204)
            self.skin_pane.b_slider.setValue(25)
            self.current_style_id = 14
        elif r == 226 and g == 171 and b == 18:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(226, 171, 18);}")
            self.skin_pane.r_slider.setValue(226)
            self.skin_pane.g_slider.setValue(171)
            self.skin_pane.b_slider.setValue(18)
            self.current_style_id = 15
        elif r == 255 and g == 143 and b == 87:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(255, 143, 87);}")
            self.skin_pane.r_slider.setValue(255)
            self.skin_pane.g_slider.setValue(143)
            self.skin_pane.b_slider.setValue(87)
            self.current_style_id = 16
        elif r == 253 and g == 114 and b == 109:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(253, 114, 109);}")
            self.skin_pane.r_slider.setValue(253)
            self.skin_pane.g_slider.setValue(114)
            self.skin_pane.b_slider.setValue(109)
            self.current_style_id = 17
        elif r == 253 and g == 84 and b == 78:
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(253, 84, 78);}")
            self.skin_pane.r_slider.setValue(253)
            self.skin_pane.g_slider.setValue(84)
            self.skin_pane.b_slider.setValue(78)
            self.current_style_id = 18
        else:
            self.color_r = self.skin_pane.r_slider.value()
            self.color_g = self.skin_pane.g_slider.value()
            self.color_b = self.skin_pane.b_slider.value()
            self.mainwindow_widget.setStyleSheet(
                "QWidget#mainwindow_widget{border-bottom:1px solid gray;background-color:rgb(%d, %d, %d);}"
                %(self.skin_pane.r_slider.value(), self.skin_pane.g_slider.value(), self.skin_pane.b_slider.value()))
            self.current_style_id = 19

    def change_userIfo(self):
        # print("用户信息改变")
        self.init_userIfo()
        self.current_username = self.user_name
        self.current_headimage_url = self.user_headimageurl
        self.userIcon_btn.setStyleSheet(
            "QPushButton{border-radius:18px;border:none;border-image: url(%s);}"%self.current_headimage_url)
        self.userName_btn.setText(self.current_username)

    def open_information_pane(self):
        # print("打开软件设置")
        self.stackedWidget.setCurrentIndex(6)
        self.listWidget.setCurrentRow(6)  # 设置当前条目

    def showMin(self):
        # print("最小化")
        self.showMinimized()

    def showMax(self):
        # print("最大化")
        if self.windowState() == Qt.WindowMaximized:
            self.showNormal()
            self.max_btn.setStyleSheet("QPushButton{border-image: url(:/mainwindow/images/max.png);}")
        elif self.windowState() == Qt.WindowNoState:
            self.showMaximized()
            self.max_btn.setStyleSheet("QPushButton{border-image: url(./resource/images/normal.png);}")

    def close_mysystem(self):
        # print("退出系统")
        okPressed = QMessageBox.question(self, "提示", "您确认退出系统吗？", QMessageBox.Yes | QMessageBox.No)
        if okPressed != 65536:
            self.close()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindowPane()
    window.create_frame()
    window.show()
    sys.exit(app.exec_())
