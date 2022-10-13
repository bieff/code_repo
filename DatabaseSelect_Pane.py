# 数据库可视化操作界面，调用生成的databaseselect_ui.py文件
from PyQt5.Qt import *
from resource.databaseselect_ui import Ui_Form
class DatabaseSelectPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏
        self.setupUi(self)

    def close_btn_clicked(self):
        # print("关闭")
        self.setVisible(False)

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = DatabaseSelectPane()
    window.show()
    sys.exit(app.exec_())
