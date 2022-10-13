# 官方社交账号界面，调用生成的official_ui.py文件
from PyQt5.Qt import *
from resource.official_ui import Ui_Form
class OfficialPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = OfficialPane()
    window.show()
    sys.exit(app.exec_())
