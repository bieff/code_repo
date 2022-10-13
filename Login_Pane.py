# 登录界面，调用生成的login_ui.py文件
from PyQt5.Qt import *
import pymysql
from resource.login_ui import Ui_Form
class LoginPane(QWidget, Ui_Form):
    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setWindowFlags(Qt.FramelessWindowHint) # 去掉标题栏
        self.setupUi(self)
        self.setWindowTitle("登录")
        movie = QMovie(":/login/images/login_top_label.gif")
        movie.setScaledSize(QSize(700,200))
        self.login_top_label.setMovie(movie)
        movie.start()

        lock_label = QLabel(self.password_lineEdit)
        lock_label.setFixedSize(30, 50)
        lock_label.setStyleSheet("QLabel{image: url(:/login/images/lock.png);}")
        self.visible_btn = QPushButton()
        self.visible_btn.setFixedSize(30, 30)
        self.visible_btn.setCursor(QCursor(Qt.PointingHandCursor)) # 鼠标移到按钮上变为手形
        self.visible_btn.setStyleSheet("QPushButton{border:none;image: url(:/login/images/view_off.png);}")
        self.visible_btn_state = False # 初始化不可见密码
        self.visible_btn.clicked.connect(self.change_visible_btn)
        password_lineEdit_layout = QHBoxLayout()
        password_lineEdit_layout.addStretch()
        password_lineEdit_layout.addWidget(self.visible_btn)
        password_lineEdit_layout.setSpacing(0)
        password_lineEdit_layout.setContentsMargins(0, 0, 25, 0)
        self.password_lineEdit.setLayout(password_lineEdit_layout)
        self.password_lineEdit.setTextMargins(lock_label.width() + 10, 0, self.visible_btn.width(), 0)
        self.account_comboBox.setIconSize(QSize(35, 30))
        self.init_login_info() # 初始化登录信息
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.goto_autologin)
        self.timer.setSingleShot(True)
        self.timer.start(1000)

    def goto_autologin(self):
        if self.auto_login_checkbox.isChecked() == True:
            self.check_login()

    def change_visible_btn(self):
        if self.visible_btn_state == False:
            self.visible_btn.setStyleSheet("QPushButton{border:none;image: url(:/login/images/view_on.png);}")
            self.visible_btn_state = True
            self.password_lineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.visible_btn.setStyleSheet("QPushButton{border:none;image: url(:/login/images/view_off.png);}")
            self.visible_btn_state = False
            self.password_lineEdit.setEchoMode(QLineEdit.Password)

    def auto_login(self, checked):
        # print("自动登录", checked)
        if checked:
            self.remember_pwd_checkbox.setChecked(True)

    def remember_pwd(self, checked):
        # print("记住密码", checked)
        if  not checked:
            self.auto_login_checkbox.setChecked(False)

    # 保存登录信息
    def save_login_info(self):
        account = self.account_comboBox.currentText()
        password = self.password_lineEdit.text()
        # 从数据库查找账号是否存在
        if account == "sa" and password == "xzs":
            settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
            settings.setValue("%s/account" % account, self.account_comboBox.currentText())
            settings.setValue("%s/password" % account, self.password_lineEdit.text())
            settings.setValue("%s/autologin" % account, self.auto_login_checkbox.isChecked())
            settings.setValue("%s/remeberpassword" % account, self.remember_pwd_checkbox.isChecked())
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute("select user_password from user_ifo where user_account='%s'"%account)
            data = cur.fetchall()
            conn.commit()
            if len(data) == 1 and data[0][0] == password:
                settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
                settings.setValue("%s/account" % account, self.account_comboBox.currentText())
                settings.setValue("%s/password" % account, self.password_lineEdit.text())
                settings.setValue("%s/autologin" % account, self.auto_login_checkbox.isChecked())
                settings.setValue("%s/remeberpassword" % account, self.remember_pwd_checkbox.isChecked())
        except Exception as e:
            print(e)
        finally:
            conn.close()

    # 初始化登录信息
    def init_login_info(self):
        account = self.account_comboBox.currentText()
        settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
        the_account = settings.value("%s/account"%account)
        if the_account == None:
            return
        the_password = settings.value("%s/password"%account)
        the_remeberpassword = settings.value("%s/remeberpassword"%account)
        the_autologin = settings.value("%s/autologin"%account)
        self.account_comboBox.setCurrentText(the_account)
        if the_remeberpassword == "true" or the_remeberpassword == True:
            self.remember_pwd_checkbox.setChecked(True)
            self.password_lineEdit.setText(the_password)
        if the_autologin == "true" or the_autologin == True:
            self.auto_login_checkbox.setChecked(True)
            self.login_btn.click() # 自动登录

    def show_register_pane(self):
        self.show_register_pane_signal.emit()

    def open_qq_link(self):
        link = "http://shang.qq.com/wpa/qunwpa?idkey=" \
               "e3b016438c0afa7db3b0f68f3e211af1863192b343b656799cc93092ac69004b"
        QDesktopServices.openUrl(QUrl(link))

    def change_user_login(self):
        # print("更换账号登录")
        self.password_lineEdit.setText("")
        self.auto_login_checkbox.setChecked(False)
        self.remember_pwd_checkbox.setChecked(False)
        self.visible_btn.setStyleSheet("QPushButton{border:none;image: url(:/login/images/view_off.png);}")
        self.init_login_info()

    def enable_login_btn(self):
        # print("登录按钮是否有效")
        account = self.account_comboBox.currentText()
        password = self.password_lineEdit.text()
        if not (account == "201601033017" or account == "201601033034"):
            # 账号不存在，显示默认头像
            self.account_comboBox.setCurrentIndex(0)
            self.account_comboBox.setItemText(1, "201601033034")
            icon = QIcon()
            icon.addPixmap(QPixmap("./resource/icos/default.ico"), QIcon.Normal, QIcon.Off)
            self.account_comboBox.setItemIcon(self.account_comboBox.currentIndex(), icon)
            self.account_comboBox.setItemText(self.account_comboBox.currentIndex(), account)
        else:
            # 账号存在，检索数据库headimage_url
            headimage_url = ""
            if account == "201601033017":
                self.account_comboBox.setCurrentIndex(0)
                headimage_url = "./resource/icos/201601033017.ico"
            elif account == "201601033034":
                self.account_comboBox.setCurrentIndex(1)
                icon = QIcon()
                icon.addPixmap(QPixmap("./resource/icos/201601033017.ico"), QIcon.Normal, QIcon.Off)
                self.account_comboBox.setItemIcon(0, icon)
                self.account_comboBox.setItemText(0, "201601033017")
                headimage_url = "./resource/icos/201601033034.ico"
            icon = QIcon()
            icon.addPixmap(QPixmap("%s"%headimage_url), QIcon.Normal, QIcon.Off)
            self.account_comboBox.setItemIcon(self.account_comboBox.currentIndex(), icon)
            self.account_comboBox.setItemText(self.account_comboBox.currentIndex(), account)
        if len(account)>0 and len(password)>0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        # print("登录")
        account = self.account_comboBox.currentText()
        password = self.password_lineEdit.text()
        self.check_login_signal.emit(account, password)
        self.save_login_info() # 保存信息

    def show_login_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.25, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.75, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
