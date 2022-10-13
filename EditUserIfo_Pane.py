# 用户信息修改界面，调用生成的editUserIfo_ui.py文件
from PyQt5.Qt import *
from resource.editUserIfo_ui import Ui_Form
class EditUserIfoPane(QWidget, Ui_Form):
    edit_Signal = pyqtSignal(str, str, str, str, str, str, str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle("修改用户信息")
        self.man_rbtn.setChecked(True)

    def edit_userIfo(self):
        # print("修改用户信息")
        user_account = self.account_lineEdit.text()
        user_name = self.name_lineEdit.text()
        user_password = self.password_lineEdit.text()
        user_email = self.email_lineEdit.text()
        user_introduction = self.introduction_lineEdit.text()
        if self.man_rbtn.isChecked() == True:
            user_sex = "男"
        else:
            user_sex = "女"
        user_headimageurl = self.headimageurl_lineEdit.text()
        user_experience = self.experience_lineEdit.text()
        user_grade = self.grade_lineEdit.text()
        self.edit_Signal.emit(user_account, user_name, user_password, user_email, user_introduction, user_sex, user_headimageurl, user_experience, user_grade)

    def cancel_edit_userIfo(self):
        # print("取消修改用户信息")
        self.close()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = EditUserIfoPane()
    window.show()
    sys.exit(app.exec_())
