# 迷你用户信息界面，调用生成的personcard_ui.py文件
from PyQt5.Qt import *
import  pymysql
from PyQt5.QtCore import QBasicTimer
from resource.personcard_ui import Ui_Form
class PersoncardPane(QWidget, Ui_Form):
    zh_CN_Signal = pyqtSignal() # 简体中文信号
    zh_TW_Signal = pyqtSignal() # 繁体中文信号
    en_Signal = pyqtSignal() # 英文信号
    ko_Signal = pyqtSignal()  # 韩语信号
    ja_Signal = pyqtSignal()  # 日语信号
    user_management_Signal = pyqtSignal() # 进入账号管理信号
    official_Signal = pyqtSignal() # 进入社交账号信号
    guide_Signal = pyqtSignal() # 进入使用指南信号

    switch_Signal = pyqtSignal() # 切换账号信号
    exit_Signal = pyqtSignal() # 退出信号

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏

        self.user_account = "201601033017"  # 当前账号
        self.user_name = "夜晓希声"

    def showIfo(self):
        # print("初始化方法")
        self.timer = QBasicTimer()  # 定时器
        self.trans = QTranslator()  # 翻译家
        self.step = 0
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute("select user_experience from user_ifo where user_account='%s'"%self.user_account)
            data = cur.fetchone()
            user_experience = data[0]
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        if user_experience>=0 and user_experience<1000:
            user_grade = 0
        elif user_experience>=1000 and user_experience<2000:
            user_grade = 1
        elif user_experience>=2000 and user_experience<3000:
            user_grade = 2
        elif user_experience>=3000 and user_experience<4000:
            user_grade = 3
        elif user_experience>=4000 and user_experience<5000:
            user_grade = 4
        elif user_experience>=5000 and user_experience<6000:
            user_grade = 5
        elif user_experience>=6000:
            user_grade = 6
        self.grade_btn.setStyleSheet("QPushButton#grade_btn{\n"
                                     "    border:none;border-image: url(:/personcard/images/user_level%d.png)}"%user_grade)
        self.user_experience = user_experience  # 从数据库读取数据，获取用户的经验值
        self.experience_progressBar.setValue(self.user_experience)
        self.timer.start(0.2, self)  # 控制速度，单位是毫秒级
        self.experience_label.setText("经验值：" + str(self.experience_progressBar.value()) + "/10000")
        # self.experience_label.setAlignment(Qt.AlignRight)
        self.setContextMenuPolicy(Qt.CustomContextMenu)  # 自定义菜单
        self.language_menu = QMenu(self)
        self.language_menu.setFocusPolicy(Qt.NoFocus)
        self.actionSCn = QAction("简体中文", self)
        self.actionSCn.setCheckable(True)
        self.actionSCn.setChecked(True)  # 默认选中简体中文模式
        self.actionTCn = QAction("繁体中文", self)
        self.actionTCn.setCheckable(True)
        self.actionTCn.setChecked(False)
        self.actionEn = QAction("English", self)
        self.actionEn.setCheckable(True)
        self.actionEn.setChecked(False)
        self.actionKo = QAction("韩语", self)
        self.actionKo.setCheckable(True)
        self.actionKo.setChecked(False)
        self.actionJa = QAction("日语", self)
        self.actionJa.setCheckable(True)
        self.actionJa.setChecked(False)
        self.actionSCn.triggered.connect(self.language_change)
        self.actionTCn.triggered.connect(self.language_change)
        self.actionEn.triggered.connect(self.language_change)
        self.actionKo.triggered.connect(self.language_change)
        self.actionJa.triggered.connect(self.language_change)
        self.language_menu.addAction(self.actionSCn)
        self.language_menu.addAction(self.actionTCn)
        self.language_menu.addAction(self.actionEn)
        self.language_menu.addAction(self.actionKo)
        self.language_menu.addAction(self.actionJa)
        self.setFocus()  # 设置控件获取焦点

    def focusInEvent(self, QFocusEvent):
        # print("获得焦点")
        pass

    def focusOutEvent(self, QFocusEvent):
        # print("失去焦点")
        if self.language_menu.isVisible() == False:
            self.close()
        else:
            self.setFocus()  # 设置控件获取焦点

    def timerEvent(self, e):
        if self.step >= self.user_experience:
            self.timer.stop()
            self.step = 0
            return
        self.step = self.step + 1
        self.experience_progressBar.setValue(self.step)
        self.experience_label.setText("经验值：" + str(self.experience_progressBar.value()) + "/10000")

    def sign_click(self):
        # print("签到成功")
        self.user_experience = self.user_experience + 10  # 增加经验值，然后写入数据库
        if self.user_experience>=0 and self.user_experience<1000:
            user_grade = 0
        elif self.user_experience>=1000 and self.user_experience<2000:
            user_grade = 1
        elif self.user_experience>=2000 and self.user_experience<3000:
            user_grade = 2
        elif self.user_experience>=3000 and self.user_experience<4000:
            user_grade = 3
        elif self.user_experience>=4000 and self.user_experience<5000:
            user_grade = 4
        elif self.user_experience>=5000 and self.user_experience<6000:
            user_grade = 5
        elif self.user_experience>=6000:
            user_grade = 6
        self.grade_btn.setStyleSheet("QPushButton#grade_btn{\n"
                                     "    border:none;border-image: url(:/personcard/images/user_level%d.png)}"%user_grade)
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute("update user_ifo set user_experience="+str(self.user_experience)+" where user_account='%s'"%self.user_account)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(0.2, self) # 控制速度，单位是毫秒级
        self.sign_btn.setText("已签到")
        self.sign_btn.setEnabled(False)

    def show_usermanagement_pane(self):
        # print("进入账号管理界面")
        self.user_management_Signal.emit()
        self.clearFocus()  # 设置控件失去焦点

    def bind_other(self):
        # print("社交账号")
        self.official_Signal.emit()
        self.clearFocus()  # 设置控件失去焦点

    def show_language_menu(self):
        x = self.frameGeometry().x() + self.language_btn.pos().x() + self.language_btn.width()
        y = self.frameGeometry().y() + self.language_btn.pos().y()
        self.language_menu.exec_(QPoint(x, y))

    def language_change(self):
        # print("切换语言")
        if self.sender() == self.actionSCn:
            # print("简体中文")
            self.actionSCn.setChecked(True)
            self.actionTCn.setChecked(False)
            self.actionEn.setChecked(False)
            self.actionKo.setChecked(False)
            self.actionJa.setChecked(False)
            self.zh_CN_Signal.emit()
        elif self.sender() == self.actionTCn:
            # print("繁体中文")
            self.actionSCn.setChecked(False)
            self.actionTCn.setChecked(True)
            self.actionEn.setChecked(False)
            self.actionKo.setChecked(False)
            self.actionJa.setChecked(False)
            self.zh_TW_Signal.emit()
        elif self.sender() == self.actionEn:
            # print("English")
            self.actionSCn.setChecked(False)
            self.actionTCn.setChecked(False)
            self.actionEn.setChecked(True)
            self.actionKo.setChecked(False)
            self.actionJa.setChecked(False)
            self.en_Signal.emit()
        elif self.sender() == self.actionKo:
            # print("韩语")
            self.actionSCn.setChecked(False)
            self.actionTCn.setChecked(False)
            self.actionEn.setChecked(False)
            self.actionKo.setChecked(True)
            self.actionJa.setChecked(False)
            self.ko_Signal.emit()
        else:
            # print("日语")
            self.actionSCn.setChecked(False)
            self.actionTCn.setChecked(False)
            self.actionEn.setChecked(False)
            self.actionKo.setChecked(False)
            self.actionJa.setChecked(True)
            self.ja_Signal.emit()
        self.close()

    def show_guide_pane(self):
        # print("使用指南")
        self.guide_Signal.emit()
        self.clearFocus()  # 设置控件失去焦点

    def switch_account(self):
        # print("切换账号")
        self.switch_Signal.emit()

    def logout(self):
        # print("card退出登录")
        self.exit_Signal.emit()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = PersoncardPane()
    window.showIfo()
    window.show()
    sys.exit(app.exec_())
