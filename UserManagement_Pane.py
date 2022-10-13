# 用户管理界面，调用生成的usermanagement_ui.py文件
from PyQt5.Qt import *
import socket
import platform
import pymysql
from resource.code_images.Code_Image import CodeImage
from resource.usermanagement_ui import Ui_Form
class UserManagementPane(QWidget, Ui_Form):
    headimage_Signal = pyqtSignal() # 头像图片信号
    username_Signal = pyqtSignal() # 用户昵称信号
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.user_account = "201601033017"  # 当前账号
        self.user_name = "夜晓希声"
        # self.showIfo()

    def showIfo(self):
        # 数据库查询，初始化用户信息
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
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.headimage_url = self.user_headimageurl  # 当前头像图片路径
        self.account_lineEdit.setText(self.user_account)
        self.name_lineEdit.setText(self.user_name)
        self.email_lineEdit.setText(self.user_email)
        if self.user_sex == "男":
            self.man_rbtn.setChecked(True)
        elif self.user_sex == "女":
            self.woman_rbtn.setChecked(True)
        self.introduce_textEdit.setText(self.user_introduction)
        self.change_code() # 刷新验证码
        self.show_login_record() # 登录日志
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.headimage_label.setStyleSheet("QLabel{border-image:url(%s);}" % self.headimage_url)

    def show_login_record(self):
        # print("登录日志")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        login_account = self.user_account
        login_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        login_hostname = socket.gethostname()
        login_ip = socket.gethostbyname(login_hostname)
        os_name = platform.platform()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "insert into login_log values('"+login_account+"','"+login_time+"','"+login_ip+\
                  "','"+os_name+"','"+login_hostname+"')"
            cur.execute(sql)
            sql = "select * from login_log where login_account='%s'"%self.user_account
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
            rowCount = len(data)
            columnCount = len(data[0])
            self.login_record_tableWidget.setRowCount(rowCount)  # 设置行数
            self.login_record_tableWidget.setColumnCount(columnCount)  # 设置列数
            for i in range(rowCount):
                for j in range(columnCount):
                    temp_data = data[i][j]  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.login_record_tableWidget.setItem(i, j, data1)
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.login_record_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.login_record_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.login_record_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.login_record_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.login_record_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')  # 设置表头的背景色

    def query_sqllog(self):
        # print("查询工作日志")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "select * from work_log where work_account='%s'"%self.user_account
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
            rowCount = len(data)
            log_str = ""
            for i in range(rowCount):
                work_account = data[i][0]
                work_time = data[i][1]
                work_success = data[i][2]
                work_text = data[i][3]
                log_str = log_str + "--------------------------------------------------------\n"+ \
                          "账号："+work_account+"\n时间："+work_time+"\n是否成功："+work_success+"\n执行内容："+work_text+"\n"
            self.sqllog_textEdit.setText(log_str)
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()

    def close_sqllog(self):
        # print("关闭工作日志")
        self.sqllog_textEdit.setText("")

    def change_user_headimage(self):
        # print("改变用户头像")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "./resource/icos/", "*.ico;;*.jpg;;*.png;;All Files(*)")
        if not imgName:
            return
        self.headimage_url = "./resource/icos/" + imgName.split("/")[-1] # 新的文件名
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "update user_ifo set user_headimageurl='" + self.headimage_url + "' where user_account='%s'"%current_account
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.headimage_label.setStyleSheet("QLabel{border-image:url(%s);}"%self.headimage_url)
        self.headimage_Signal.emit()

    def username_editable(self):
        # print("改变用户昵称")
        self.name_lineEdit.setReadOnly(False)
        self.name_lineEdit.setClearButtonEnabled(True)

    def useremail_editable(self):
        # print("改变用户邮箱")
        self.email_lineEdit.setReadOnly(False)
        self.email_lineEdit.setClearButtonEnabled(True)

    def change_ifo_enable(self):
        # print("可以保存修改")
        self.save_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)

    def change_user_inf(self):
        # print("改变用户信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.username = self.name_lineEdit.text()
        self.email = self.email_lineEdit.text()
        if self.man_rbtn.isChecked():
            self.sex = '男'
        elif self.woman_rbtn.isChecked():
            self.sex = '女'
        self.introduce = self.introduce_textEdit.toPlainText()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "update user_ifo set user_name='" + self.username + "',user_email='" + self.email + \
                  "',user_sex='" + self.sex + "',user_introduction='" + self.introduce + "' where user_account='%s'"%current_account
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.username_Signal.emit()
        self.name_lineEdit.setReadOnly(True)
        self.name_lineEdit.setClearButtonEnabled(False)
        self.email_lineEdit.setReadOnly(True)
        self.email_lineEdit.setClearButtonEnabled(False)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.setFocus()

    def cancel_change_ifo(self):
        # print("取消修改用户信息")
        # 此处取消修改后，还原，即重新执行一次数据库操作，显示个人信息
        self.showIfo()
        self.name_lineEdit.setReadOnly(True)
        self.name_lineEdit.setClearButtonEnabled(False)
        self.email_lineEdit.setReadOnly(True)
        self.email_lineEdit.setClearButtonEnabled(False)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.setFocus()

    def change_code(self):
        # print("刷新验证码")
        codeimage = CodeImage()
        codeimage.font_path = 'resource/code_images/Arial.ttf'
        image = codeimage.gene_code()
        codeimage.code_image.save('resource/code_images/idencode.png')
        self.code_btn.setStyleSheet("QPushButton{border-image:url(./resource/code_images/idencode.png);}")
        self.code_text = codeimage.code_text

    def change_pwd_enable(self):
        pwd = self.pwd_lineEdit.text()
        newpwd = self.newpwd_lineEdit.text()
        confirmpwd = self.confirm_lineEdit.text()
        numcode = self.code_lineEdit.text()
        key = 0
        if pwd =="":
            return
        if pwd != self.user_password:
            self.pwd_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/no.png);")
            self.pwd_error_label.setText("输入原密码错误")
            self.pwd_error_label.setStyleSheet("font: 10pt \"宋体\"; color: rgb(255, 0, 0);")
        else:
            key = key +1
            self.pwd_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/yes.png);")
            self.pwd_error_label.setText("")
            self.pwd_error_label.setStyleSheet("border:none;")
            if newpwd == "":
                return
            if newpwd == pwd:
                self.newpwd_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/no.png);")
                self.newpwd_error_label.setText("输入新密码与原密码相同")
                self.newpwd_error_label.setStyleSheet("font: 10pt \"宋体\"; color: rgb(255, 0, 0);")
            else:
                key = key + 1
                self.newpwd_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/yes.png);")
                self.newpwd_error_label.setText("")
                self.newpwd_error_label.setStyleSheet("border:none;")
                if confirmpwd == "":
                    return
                if confirmpwd != newpwd:
                    self.confirm_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/no.png);")
                    self.confirm_error_label.setText("确认密码输入错误")
                    self.confirm_error_label.setStyleSheet("font: 10pt \"宋体\"; color: rgb(255, 0, 0);")
                else:
                    key = key + 1
                    self.confirm_show_btn.setStyleSheet("border:none;image: url(:/usermanagement/images/yes.png);")
                    self.confirm_error_label.setText("")
                    self.confirm_error_label.setStyleSheet("border:none;")
                    if numcode != self.code_text:
                        return
                    else :
                        key = key + 1
        if key == 4:
            self.changeIfo_btn.setEnabled(True)
            self.cancel_btn_2.setEnabled(True)

    def change_pwd(self):
        # print("修改用户密码")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        # 数据库操作
        self.user_password = self.newpwd_lineEdit.text()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "update user_ifo set user_password='" + self.user_password + "' where user_account='201601033017'"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.pwd_lineEdit.setText("")
        self.newpwd_lineEdit.setText("")
        self.confirm_lineEdit.setText("")
        self.code_lineEdit.setText("")
        self.pwd_show_btn.setStyleSheet("border:none;")
        self.newpwd_show_btn.setStyleSheet("border:none;")
        self.confirm_show_btn.setStyleSheet("border:none;")
        self.change_code()  # 刷新验证码
        self.changeIfo_btn.setEnabled(False)
        self.cancel_btn_2.setEnabled(False)
        self.setFocus()

    def cancel_change_pwd(self):
        # print("取消修改")
        self.pwd_lineEdit.setText("")
        self.newpwd_lineEdit.setText("")
        self.confirm_lineEdit.setText("")
        self.code_lineEdit.setText("")
        self.pwd_show_btn.setStyleSheet("border:none;")
        self.newpwd_show_btn.setStyleSheet("border:none;")
        self.confirm_show_btn.setStyleSheet("border:none;")
        self.change_code() # 刷新验证码
        self.changeIfo_btn.setEnabled(False)
        self.cancel_btn_2.setEnabled(False)
        self.setFocus()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = UserManagementPane()
    window.showIfo()
    window.show()
    sys.exit(app.exec_())
