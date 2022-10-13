# 靶点表信息修改界面，调用生成的editTargetData_ui.py文件
from PyQt5.Qt import *
from resource.editTargetData_ui import Ui_Form
class EditTargetDataPane(QWidget, Ui_Form):
    edit_target_Signal = pyqtSignal(str, str, str, str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.table_name = "靶点表"
        self.herb_name =""
        self.english_name =""
        self.chinese_name =""
        self.target_name =""
        self.target_commonname =""
        self.showIfo()

    def showIfo(self):
        # print("初始化")
        self.herb_name_lineEdit.setText(self.herb_name)
        self.english_name_lineEdit.setText(self.english_name)
        self.chinese_name_lineEdit.setText(self.chinese_name)
        self.target_name_lineEdit.setText(self.target_name)
        self.target_commonname_lineEdit.setText(self.target_commonname)

    def edit_target_table(self):
        # print("修改靶点表信息")
        table_name = self.table_name
        herb_name = self.herb_name_lineEdit.text()
        english_name = self.english_name_lineEdit.text()
        chinese_name = self.chinese_name_lineEdit.text()
        target_name = self.target_name_lineEdit.text()
        target_commonname = self.target_commonname_lineEdit.text()
        self.edit_target_Signal.emit(table_name, herb_name, english_name, chinese_name, target_name, target_commonname)

    def cancel_edit_target_table(self):
        # print("取消")
        self.close()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = EditTargetDataPane()
    window.show()
    sys.exit(app.exec_())
