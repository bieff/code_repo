# 中药信息修改界面，调用生成的editHerbData_ui.py文件
from PyQt5.Qt import *
from resource.editHerbData_ui import Ui_Form
class EditHerbDataPane(QWidget, Ui_Form):
    edit_herb_Signal = pyqtSignal(str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.table_name = "中药表"
        self.herb_id = ""
        self.herb_name = ""
        self.showIfo()

    def showIfo(self):
        # print("初始化")
        self.herb_id_lineEdit.setText(self.herb_id)
        self.herb_name_lineEdit.setText(self.herb_name)

    def edit_herb_table(self):
        # print("修改中药表信息")
        table_name = self.table_name
        herb_id = self.herb_id_lineEdit.text()
        herb_name = self.herb_name_lineEdit.text()
        self.edit_herb_Signal.emit(table_name, herb_id, herb_name)

    def cancel_edit_herb_table(self):
        # print("取消")
        self.close()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = EditHerbDataPane()
    window.show()
    sys.exit(app.exec_())
