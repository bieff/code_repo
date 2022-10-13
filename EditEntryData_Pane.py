# 通路表信息修改界面，调用生成的editEntryData_ui.py文件
from PyQt5.Qt import *
from resource.editEntryData_ui import Ui_Form
class EditEntryDataPane(QWidget, Ui_Form):
    edit_entry_Signal = pyqtSignal(str, str, str, str, str, str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.table_name = "通路表"
        self.herb_name = ""
        self.english_name = ""
        self.chinese_name = ""
        self.target_name = ""
        self.target_commonname = ""
        self.entry_commonname = ""
        self.entry_name = ""
        self.showIfo()

    def showIfo(self):
        # print("初始化")
        self.herb_name_lineEdit.setText(self.herb_name)
        self.english_name_lineEdit.setText(self.english_name)
        self.chinese_name_lineEdit.setText(self.chinese_name)
        self.target_name_lineEdit.setText(self.target_name)
        self.target_commonname_lineEdit.setText(self.target_commonname)
        self.entry_commonname_lineEdit.setText(self.entry_commonname)
        self.entry_name_lineEdit.setText(self.entry_name)

    def edit_signalentry_table(self):
        # print("修改通路表信息")
        table_name = self.table_name
        herb_name = self.herb_name_lineEdit.text()
        english_name = self.english_name_lineEdit.text()
        chinese_name = self.chinese_name_lineEdit.text()
        target_name = self.target_name_lineEdit.text()
        target_commonname = self.target_commonname_lineEdit.text()
        entry_commonname = self.entry_commonname_lineEdit.text()
        entry_name = self.entry_name_lineEdit.text()
        self.edit_entry_Signal.emit(table_name, herb_name, english_name, chinese_name, target_name, target_commonname, entry_commonname, entry_name)

    def cancel_edit_signalentry_table(self):
        # print("取消")
        self.close()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = EditEntryDataPane()
    window.show()
    sys.exit(app.exec_())
