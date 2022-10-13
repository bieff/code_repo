# 成分表信息修改界面，调用生成的editCompoundData_ui.py文件
from PyQt5.Qt import *
from resource.editCompoundData_ui import Ui_Form
class EditCompoundDataPane(QWidget, Ui_Form):
    edit_compound_Signal = pyqtSignal(str, str, str, str, str, str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.table_name = "成分表"
        self.herb_name = ""
        self.compound_id = ""
        self.chinese_name = ""
        self.english_name = ""
        self.smiles = ""
        self.sources = ""
        self.oil = ""
        self.showIfo()

    def showIfo(self):
        # print("初始化")
        self.herb_name_lineEdit.setText(self.herb_name)
        self.compound_id_lineEdit.setText(self.compound_id)
        self.chinese_name_lineEdit.setText(self.chinese_name)
        self.english_name_lineEdit.setText(self.english_name)
        self.smiles_lineEdit.setText(self.smiles)
        self.sources_lineEdit.setText(self.sources)
        self.oil_lineEdit.setText(self.oil)

    def edit_compound_table(self):
        # print("修改成分表信息")
        table_name = self.table_name
        herb_name = self.herb_name_lineEdit.text()
        compound_id = self.compound_id_lineEdit.text()
        chinese_name = self.chinese_name_lineEdit.text()
        english_name = self.english_name_lineEdit.text()
        smiles = self.smiles_lineEdit.text()
        sources = self.sources_lineEdit.text()
        oil = self.oil_lineEdit.text()
        self.edit_compound_Signal.emit(table_name, herb_name, compound_id, chinese_name, english_name, smiles, sources, oil)

    def cancel_edit_compound_table(self):
        # print("取消")
        self.close()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = EditCompoundDataPane()
    window.show()
    sys.exit(app.exec_())
