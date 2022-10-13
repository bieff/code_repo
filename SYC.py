# 主方法，作为入口文件
import PyQt5.sip
import sys
from PyQt5.Qt import *
from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from MainWindow_Pane import MainWindowPane
from SaManagement_Pane import SaManagementPane
import pymysql

class Xiao(object):
    def __init__(self):
        self.login_pane = LoginPane()
        self.login_pane.show()
        self.register_pane = RegisterPane(self.login_pane)
        self.register_pane.move(0, self.login_pane.height())
        self.register_pane.show()
        # self.mainwindow_pane = MainWindowPane()
        # self.mainwindow_pane.create_frame()
        # self.mainwindow_pane.switch_Signal.connect(self.main_switch_account)
        # self.mainwindow_pane.exit_Signal.connect(self.main_exit_account)
        self.login_pane.show_register_pane_signal.connect(self.show_register_pane)
        self.login_pane.check_login_signal.connect(self.login_check)
        self.register_pane.exit_signal.connect(self.exit_register_pane)
        self.register_pane.register_account_pwd_signal.connect(self.register_check)

    def main_switch_account(self):
        # print("切换账号")
        self.login_pane.show()

    def main_exit_account(self):
        # print("退出系统")
        sys.exit(0)

    def sa_exit(self):
        # print("管理员退出")
        self.login_pane.show()

    def show_register_pane(self):
        animation = QPropertyAnimation(self.register_pane)
        animation.setTargetObject(self.register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(self.register_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_register_pane(self):
        self.register_pane.show_hide_menu(False)
        self.register_pane.btn_menu.setChecked(False)
        self.register_pane.reset()
        animation = QPropertyAnimation(self.register_pane)
        animation.setTargetObject(self.register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(self.register_pane.pos())
        animation.setEndValue(QPoint(0, self.login_pane.height()))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def login_check(self, account, password):
        # 此处为数据库操作
        if account == "sa" and password == "xzs":
            # print("管理员登录")
            self.login_pane.hide()
            self.saManagementPane = SaManagementPane()
            self.saManagementPane.show()
            self.saManagementPane.sa_exit_Signal.connect(self.sa_exit)
        else:
            try:
                conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                cur = conn.cursor()
                cur.execute("select user_password from user_ifo where user_account='%s'"%account)
                data = cur.fetchall()
                conn.commit()
                if len(data) == 1:
                    if data[0][0] == password:
                        self.login_pane.hide()
                        self.mainwindow_pane = MainWindowPane()
                        self.mainwindow_pane.user_account = account
                        self.mainwindow_pane.create_frame()
                        self.mainwindow_pane.switch_Signal.connect(self.main_switch_account)
                        self.mainwindow_pane.exit_Signal.connect(self.main_exit_account)
                        self.mainwindow_pane.show()
                    else:
                        self.login_pane.show_login_error_animation()
                        QMessageBox.warning(self.register_pane, "登录失败", "密码输入错误", QMessageBox.Yes)
                else:
                    self.login_pane.show_login_error_animation()
                    QMessageBox.warning(self.register_pane, "登录失败", "用户不存在", QMessageBox.Yes)
            except Exception as e:
                print(e)
            finally:
                conn.close()

    def register_check(self, account, password):
        # 此处为数据库操作
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute("select * from user_ifo where user_account='%s'"%account)
            data = cur.fetchall()
            conn.commit()
            if len(data) == 1:
                self.register_pane.show_register_error_animation()
                QMessageBox.warning(self.register_pane, "注册失败", "账号信息已存在", QMessageBox.Yes)
            else:
                sql = "insert into user_ifo values('"+account+"','默认用户名','"+password+"','','','男','./resource/icos/default.ico',0,0)"
                cur.execute(sql)
                conn.commit()
                QMessageBox.information(self.register_pane, "注册成功", "即将跳往登录", QMessageBox.Yes)
                self.exit_register_pane()
        except Exception as e:
            print(e)
        finally:
            conn.close()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    xiao = Xiao()
    sys.exit(app.exec_())