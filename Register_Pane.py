# 注册界面，调用生成的register_ui.py文件
from PyQt5.Qt import *
from resource.register_ui import Ui_Form
class RegisterPane(QWidget, Ui_Form):
    exit_signal = pyqtSignal() # 向外界发射退出信号
    register_account_pwd_signal = pyqtSignal(str, str) # 向外界发送账号和密码数据

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle("注册")

        self.animation_targets = [self.btn_policy, self.btn_reset, self.btn_exit]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        self.btn_policy.move(self.btn_menu.pos())
        self.btn_reset.move(self.btn_menu.pos())
        self.btn_exit.move(self.btn_menu.pos())

    def show_hide_menu(self, checked):
        animation_group = QSequentialAnimationGroup(self)
        for index, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if checked:
                animation.setStartValue(self.btn_menu.pos())
                animation.setEndValue(self.animation_targets_pos[index])
            else:
                animation.setStartValue(self.animation_targets_pos[index])
                animation.setEndValue(self.btn_menu.pos())
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation_group.addAnimation(animation)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def policy(self):
        pass

    def exit_register(self):
        self.exit_signal.emit()

    def reset(self):
        self.lineEdit_account.clear()
        self.lineEdit_password.clear()
        self.lineEdit_confirm.clear()

    def check_register(self):
        account_txt = self.lineEdit_account.text()
        password_txt = self.lineEdit_password.text()
        self.register_account_pwd_signal.emit(account_txt, password_txt)

    def enable_register(self):
        account_txt = self.lineEdit_account.text()
        password_txt = self.lineEdit_password.text()
        confirm_txt = self.lineEdit_confirm.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(confirm_txt)>0 and password_txt == confirm_txt:
            self.btn_register.setEnabled(True)
        else:
            self.btn_register.setEnabled(False)

    def show_register_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.register_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.register_bottom.pos())
        animation.setKeyValueAt(0.25, self.register_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.register_bottom.pos())
        animation.setKeyValueAt(0.75, self.register_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.register_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = RegisterPane()
    # window.exit_signal.connect(lambda:print("退出"))
    # window.register_account_pwd_signal.connect(lambda account, password: print(account, password))
    window.show()
    sys.exit(app.exec_())
