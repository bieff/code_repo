# 文章推送界面，调用生成的article_ui.py文件
from PyQt5.Qt import *
from resource.article_ui import Ui_Form
class ArticlePane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = ArticlePane()
    window.show()
    sys.exit(app.exec_())
