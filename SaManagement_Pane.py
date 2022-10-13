# 用户管理界面，调用生成的usermanagement_ui.py文件
from PyQt5.Qt import *
import pymysql
from PyQt5.QtCore import QTimer,QDateTime
from resource.samanagement_ui import Ui_Form
from EditUserIfo_Pane import EditUserIfoPane
class SaManagementPane(QWidget, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = False
    sa_exit_Signal = pyqtSignal() # 管理员退出
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏
        self.setupUi(self)

        self.Timer = QTimer()  # 自定义QTimer
        self.Timer.start(500)  # 每0.5秒运行一次
        self.Timer.timeout.connect(self.updateTime)  # 连接updateTime
        self.showIfo() # 调用初始化方法

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent): # 鼠标左键按下事件
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def updateTime(self):
        self.time_label.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd'))  # 显示时间的格式

    def showIfo(self):
        # 数据库查询，初始化用户信息
        self.userIfo_record() # 用户信息
        self.show_feeedback_record() # 用户反馈
        self.show_login_record() # 登录日志

    def userIfo_record(self):
        # print("用户信息")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute('select * from user_ifo')
            data = cur.fetchall()
            conn.commit()
            rowCount = len(data)
            if rowCount == 0:
                return
            columnCount = len(data[0])
            self.userIfo_tableWidget.setRowCount(rowCount)  # 设置行数
            self.userIfo_tableWidget.setColumnCount(columnCount)  # 设置列数
            for i in range(rowCount):
                for j in range(columnCount):
                    temp_data = data[i][j]  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.userIfo_tableWidget.setItem(i, j, data1)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.userIfo_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.userIfo_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.userIfo_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.userIfo_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.userIfo_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')

    def new_user(self):
        # print("新建用户")
        self.editUserIfoPane = EditUserIfoPane()
        self.editUserIfoPane.show()
        self.editUserIfoPane.headimageurl_lineEdit.setText('./resource/icos/default.ico')
        self.editUserIfoPane.experience_lineEdit.setText('0')
        self.editUserIfoPane.grade_lineEdit.setText('0')
        self.editUserIfoPane.edit_Signal.connect(self.new_userIfo_Signal)

    def new_userIfo_Signal(self, user_account, user_name, user_password, user_email, user_introduction, user_sex, user_headimageurl, user_experience, user_grade):
        # print("信号连接新建用户信息")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into user_ifo values('" + user_account + "','" + user_name + "','" + user_password + "','" + user_email + "','" + user_introduction + "','" + user_sex + "','" + user_headimageurl + "'," + user_experience + "," + user_grade + ")"
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.editUserIfoPane.close()
        self.refresh_record()

    def delete_user(self):
        # print("删除用户")
        row = self.userIfo_tableWidget.selectedItems()
        if row == []:
            QMessageBox.about(self, "提示", "您还未选中记录")
            return
        okpressed = QMessageBox.question(self, "删除选中用户", "您确定要删除此用户吗？", QMessageBox.Yes|QMessageBox.No)
        if okpressed == 16384: # No的值是65536，Yes的值是16384
            user_account = row[0].text()
            try:
                conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                cur = conn.cursor()
                cur.execute("delete from user_ifo where user_account='" + user_account + "'")
                conn.commit()
            except Exception as e:
                print(e)
            finally:
                conn.close()
            self.userIfo_tableWidget.setRowCount(0)
            self.userIfo_record()
        self.userIfo_tableWidget.setEditTriggers(QTableView.NoEditTriggers)

    def edit_user(self):
        # print("修改用户信息")
        row= self.userIfo_tableWidget.currentRow()
        if row == -1:
            QMessageBox.information(self, "提示", "您尚未选中用户")
            return
        user_account = self.userIfo_tableWidget.item(row, 0).text()
        user_name = self.userIfo_tableWidget.item(row, 1).text()
        user_password = self.userIfo_tableWidget.item(row, 2).text()
        user_email = self.userIfo_tableWidget.item(row, 3).text()
        user_introduction = self.userIfo_tableWidget.item(row, 4).text()
        user_sex = self.userIfo_tableWidget.item(row, 5).text()
        user_headimageurl = self.userIfo_tableWidget.item(row, 6).text()
        user_experience = self.userIfo_tableWidget.item(row, 7).text()
        user_grade = self.userIfo_tableWidget.item(row, 8).text()
        self.editUserIfoPane = EditUserIfoPane()
        self.editUserIfoPane.show()
        self.editUserIfoPane.account_lineEdit.setText(user_account)
        self.editUserIfoPane.name_lineEdit.setText(user_name)
        self.editUserIfoPane.password_lineEdit.setText(user_password)
        self.editUserIfoPane.email_lineEdit.setText(user_email)
        self.editUserIfoPane.introduction_lineEdit.setText(user_introduction)
        if user_sex == "男":
            self.editUserIfoPane.man_rbtn.setChecked(True)
        else:
            self.editUserIfoPane.woman_rbtn.setChecked(True)
        self.editUserIfoPane.headimageurl_lineEdit.setText(user_headimageurl)
        self.editUserIfoPane.experience_lineEdit.setText(user_experience)
        self.editUserIfoPane.grade_lineEdit.setText(user_grade)
        self.editUserIfoPane.edit_Signal.connect(self.edit_userIfo_Signal)

    def edit_userIfo_Signal(self, user_account, user_name, user_password, user_email, user_introduction, user_sex, user_headimageurl, user_experience, user_grade):
        # print("信号连接修改用户信息")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "update user_ifo set user_account='" + user_account + "',user_name='" + user_name + "',user_password='" + user_password + "',user_email='" + user_email + "',user_introduction='"+ user_introduction + "',user_sex='" + user_sex + "',user_headimageurl='" + user_headimageurl + "',user_experience=" + user_experience + ",user_grade=" + user_grade + " where user_account='" + user_account + "'"
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.editUserIfoPane.close()
        self.refresh_record()

    def refresh_record(self):
        # print("刷新用户信息")
        self.userIfo_tableWidget.setRowCount(0)
        self.userIfo_record()
        self.userIfo_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序
        self.userIfo_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑

    def show_feeedback_record(self):
        # print("用户反馈")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute('select * from feedback_log')
            data = cur.fetchall()
            conn.commit()
            rowCount = len(data)
            columnCount = len(data[0])
            self.feedback_tableWidget.setRowCount(rowCount)  # 设置行数
            self.feedback_tableWidget.setColumnCount(columnCount)  # 设置列数
            for i in range(rowCount):
                for j in range(columnCount):
                    temp_data = data[i][j]  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.feedback_tableWidget.setItem(i, j, data1)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.feedback_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.feedback_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.feedback_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.feedback_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.feedback_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')

    def show_login_record(self):
        # print("登录日志")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute('select * from login_log')
            data = cur.fetchall()
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
            print(e)
        finally:
            conn.close()
        self.login_record_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.login_record_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.login_record_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.login_record_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.login_record_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')

    def query_sqllog(self):
        # print("查询工作日志")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            cur.execute('select * from work_log')
            data = cur.fetchall()
            conn.commit()
            rowCount = len(data)
            log_str = ""
            for i in range(rowCount):
                work_account = data[i][0]
                work_time = data[i][1]
                work_success = data[i][2]
                work_text = data[i][3]
                log_str = log_str + "----------------------------\n"+ \
                          "账号："+work_account+"\n时间："+work_time+"\n是否成功："+work_success+"\n执行内容："+work_text+"\n"
            self.sqllog_textEdit.setText(log_str)
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def close_sqllog(self):
        # print("关闭工作日志")
        self.sqllog_textEdit.setText("")

    def sa_exit(self):
        okPressed = QMessageBox.question(self, "提示", "您确认退出系统吗？", QMessageBox.Yes | QMessageBox.No)
        if okPressed != 65536:
            self.sa_exit_Signal.emit()
            self.close()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = SaManagementPane()
    window.show()
    sys.exit(app.exec_())
