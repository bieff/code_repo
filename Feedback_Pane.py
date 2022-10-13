# 意见反馈界面，调用生成的feedback_ui.py文件
from PyQt5.Qt import *
import  pymysql
from resource.feedback_ui import Ui_Form
class FeedbackPane(QWidget, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = False
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint) # 去掉标题栏
        self.setupUi(self)
        self.user_account = "201601033017" # 当前账号
        self.user_name = "夜晓希声"  # 当前用户名

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent): # 鼠标左键按下事件
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent): # 鼠标左键松开事件
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def feedback_close(self):
        self.close()

    def feedback_send(self):
        # print("发送")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        feedback_account = self.user_account
        feedback_name = self.user_name
        feedback_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        if self.advice_rbtn.isChecked() == True:
            feedback_type = "产品建议"
        elif self.data_rbtn.isChecked() == True:
            feedback_type = "数据错误"
        elif self.program_rbtn.isChecked() == True:
            feedback_type = "程序报错"
        feedback_text = self.textEdit.toPlainText()
        user_phone = self.phone_lineEdit.text()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into feedback_log values('" + feedback_account + "','" + feedback_name + "','" + feedback_time + "','" + feedback_type + "','" + feedback_text + "','" + user_phone + "')"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.advice_rbtn.setChecked(True)
        self.textEdit.setText("")
        self.phone_lineEdit.setText("")
        QMessageBox.about(self, "提示", "发送成功！")

    def feedback_cancel(self):
        self.close()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = FeedbackPane()
    window.show()
    sys.exit(app.exec_())
