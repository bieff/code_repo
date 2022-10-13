# 数据库可视化操作界面，调用生成的databasevisual_ui.py文件
from PyQt5.Qt import *
import pymysql
from resource.databasevisual_ui import Ui_Form
from EditHerbData_Pane import EditHerbDataPane
from EditCompoundData_Pane import EditCompoundDataPane
from EditEntryData_Pane import EditEntryDataPane
from EditTargetData_Pane import EditTargetDataPane
class DatabaseVisualPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.user_account = "201601033017"  # 当前账号
        self.showIfo()

    def showIfo(self):
        # 数据库查询，初始化用户信息
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            if self.table_comboBox.currentText() == "中药表":
                table_name = "herb_table"
            elif self.table_comboBox.currentText() == "成分表":
                table_name = "compound_table"
            elif self.table_comboBox.currentText() == "通路表":
                table_name = "signalentry_table"
            elif self.table_comboBox.currentText() == "靶点表":
                table_name = "target_table"
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "select * from " + table_name
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
            rowCount = len(data)
            columnCount = len(data[0])
            self.data_tableWidget.setRowCount(rowCount)  # 设置行数
            self.data_tableWidget.setColumnCount(columnCount)  # 设置列数
            for i in range(rowCount):
                for j in range(columnCount):
                    temp_data = data[i][j]  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.data_tableWidget.setItem(i, j, data1)
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        if self.table_comboBox.currentText() == "中药表":
            self.data_tableWidget.setHorizontalHeaderLabels(["中药ID", "中药名称"])
        elif self.table_comboBox.currentText() == "成分表":
            self.data_tableWidget.setHorizontalHeaderLabels(["药物名称", "成分ID", "中文名称", "英文名称", "化学式", "来源", "精油"])
        elif self.table_comboBox.currentText() == "通路表":
            self.data_tableWidget.setHorizontalHeaderLabels(["药物名称", "疾病英文", "疾病中文", "靶点名称", "靶点简称", "通路简称", "通路名称"])
        elif self.table_comboBox.currentText() == "靶点表":
            self.data_tableWidget.setHorizontalHeaderLabels(["药物名称", "成分英文", "成分中文", "靶点名称", "靶点简称"])
        self.data_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.data_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.data_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.data_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.data_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')

    def new_data(self):
        # print("新建数据")
        if self.table_comboBox.currentText() == "中药表":
            self.editHerbDataPane = EditHerbDataPane()
            self.editHerbDataPane.show()
            self.editHerbDataPane.herb_id_lineEdit.setReadOnly(False)
            self.editHerbDataPane.edit_herb_Signal.connect(self.new_herb_data_Signal)
        elif self.table_comboBox.currentText() == "成分表":
            self.editCompoundDataPane = EditCompoundDataPane()
            self.editCompoundDataPane.show()
            self.editCompoundDataPane.edit_compound_Signal.connect(self.new_compound_data_Signal)
        elif self.table_comboBox.currentText() == "通路表":
            self.editEntryDataPane = EditEntryDataPane()
            self.editEntryDataPane.show()
            self.editEntryDataPane.edit_entry_Signal.connect(self.new_entry_data_Signal)
        elif self.table_comboBox.currentText() == "靶点表":
            self.editTargetDataPane = EditTargetDataPane()
            self.editTargetDataPane.show()
            self.editTargetDataPane.edit_target_Signal.connect(self.new_target_data_Signal)

    def new_herb_data_Signal(self, table_name, herb_id, herb_name):
        # print("信号连接新建中药信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into herb_table values('"+herb_id+"','"+herb_name+"')"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def new_compound_data_Signal(self, table_name, herb_name, compound_id, chinese_name, english_name, smiles, sources, oil):
        # print("信号连接新建成分信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into compound_table values('"+herb_name+"','"+compound_id+"','"+chinese_name+"','"+english_name+"','"+smiles+"','"+sources+"','"+oil+"')"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def new_entry_data_Signal(self, table_name, herb_name, english_name, chinese_name, target_name, target_commonname, entry_commonname, entry_name):
        # print("信号连接新建通路信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into signalentry_table values('"+herb_name+"','"+english_name+"','"+chinese_name+"','"+target_name+"','"+target_commonname+"','"+entry_commonname+"','"+entry_name+"')"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def new_target_data_Signal(self, table_name, herb_name, english_name, chinese_name, target_name, target_commonname):
        # print("信号连接新建靶点信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "insert into target_table values('"+herb_name+"','"+english_name+"','"+chinese_name+"','"+target_name+"','"+target_commonname+"')"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def delete_data(self):
        # print("删除数据")
        row = self.data_tableWidget.selectedItems()
        if row == []:
            QMessageBox.about(self, "提示", "您还未选中记录")
            return
        if self.table_comboBox.currentText() == "中药表":
            herb_id = row[0].text()
            herb_name = row[1].text()
            sql = "delete from herb_table where herb_id='"+herb_id+"' and herb_name='"+herb_name+"'"
        elif self.table_comboBox.currentText() == "成分表":
            herb_name = row[0].text()
            compound_id = row[1].text()
            compound_chinese_name = row[2].text()
            compound_english_name = row[3].text()
            compound_smiles = row[4].text()
            compound_sources = row[5].text()
            compound_oil = row[6].text()
            sql = "delete from compound_table where herb_name='"+herb_name+"' and compound_id='"+compound_id+"' and compound_chinese_name='"+compound_chinese_name+"' and compound_english_name='"+compound_english_name+"' and compound_smiles='"+compound_smiles+"' and compound_sources='"+compound_sources+"' and compound_oil='"+compound_oil+"'"
        elif self.table_comboBox.currentText() == "靶点表":
            herb_name = row[0].text()
            compound_english_name = row[1].text()
            compound_chinese_name = row[2].text()
            target_name = row[3].text()
            target_common_name = row[4].text()
            sql = "delete from target_table where herb_name='"+herb_name+"' and compound_english_name='"+compound_english_name+"' and compound_chinese_name='"+compound_chinese_name+"' and target_name='"+target_name+"' and target_common_name='"+target_common_name+"'"
        elif self.table_comboBox.currentText() == "通路表":
            herb_name = row[0].text()
            disease_english_name = row[1].text()
            disease_chinese_name = row[2].text()
            intersection_target_name = row[3].text()
            intersection_target_common_name = row[4].text()
            entry_common_name = row[5].text()
            entry_name = row[6].text()
            sql = "delete from signalentry_table where herb_name='"+herb_name+"' and disease_english_name='"+disease_english_name+"' and disease_chinese_name='"+disease_chinese_name+"' and intersection_target_name='"+intersection_target_name+"' and intersection_target_common_name='"+intersection_target_common_name+"' and entry_common_name='"+entry_common_name+"' and entry_name='"+entry_name+"'"
        okpressed = QMessageBox.question(self, "删除选中记录", "您确定要删除此记录吗？", QMessageBox.Yes | QMessageBox.No)
        if okpressed == 16384:  # No的值是65536，Yes的值是16384
            current_account = self.user_account
            current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
            try:
                conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                cur = conn.cursor()
                cur.execute("SET SQL_SAFE_UPDATES = 0")
                cur.execute(sql)
                cur.execute("SET SQL_SAFE_UPDATES = 1")
                cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'", "\\'") + "')")
                conn.commit()
            except Exception as e:
                cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
                conn.commit()
            finally:
                conn.close()
        self.showIfo()

    def edit_data(self):
        # print("编辑数据")
        row = self.data_tableWidget.currentRow()
        if row == -1:
            QMessageBox.about(self, "提示", "您还未选中记录")
            return
        if self.table_comboBox.currentText() == "中药表":
            herb_id = self.data_tableWidget.item(row, 0).text()
            herb_name = self.data_tableWidget.item(row, 1).text()
            self.editHerbDataPane = EditHerbDataPane()
            self.editHerbDataPane.show()
            self.editHerbDataPane.herb_id_lineEdit.setText(herb_id)
            self.editHerbDataPane.herb_name_lineEdit.setText(herb_name)
            self.editHerbDataPane.edit_herb_Signal.connect(self.edit_herb_data_Signal)
        elif self.table_comboBox.currentText() == "成分表":
            herb_name = self.data_tableWidget.item(row, 0).text()
            compound_id = self.data_tableWidget.item(row, 1).text()
            chinese_name = self.data_tableWidget.item(row, 2).text()
            english_name = self.data_tableWidget.item(row, 3).text()
            smiles = self.data_tableWidget.item(row, 4).text()
            sources = self.data_tableWidget.item(row, 5).text()
            oil = self.data_tableWidget.item(row, 6).text()
            self.editCompoundDataPane = EditCompoundDataPane()
            self.editCompoundDataPane.show()
            self.editCompoundDataPane.herb_name_lineEdit.setText(herb_name)
            self.editCompoundDataPane.compound_id_lineEdit.setText(compound_id)
            self.editCompoundDataPane.chinese_name_lineEdit.setText(chinese_name)
            self.editCompoundDataPane.english_name_lineEdit.setText(english_name)
            self.editCompoundDataPane.smiles_lineEdit.setText(smiles)
            self.editCompoundDataPane.sources_lineEdit.setText(sources)
            self.editCompoundDataPane.oil_lineEdit.setText(oil)
            self.editCompoundDataPane.edit_compound_Signal.connect(self.edit_compound_data_Signal)
        elif self.table_comboBox.currentText() == "通路表":
            herb_name = self.data_tableWidget.item(row, 0).text()
            english_name = self.data_tableWidget.item(row, 1).text()
            chinese_name = self.data_tableWidget.item(row, 2).text()
            target_name = self.data_tableWidget.item(row, 3).text()
            target_commonname = self.data_tableWidget.item(row, 4).text()
            entry_commonname = self.data_tableWidget.item(row, 5).text()
            entry_name = self.data_tableWidget.item(row, 6).text()
            self.editEntryDataPane = EditEntryDataPane()
            self.editEntryDataPane.show()
            self.editEntryDataPane.herb_name_lineEdit.setText(herb_name)
            self.editEntryDataPane.english_name_lineEdit.setText(english_name)
            self.editEntryDataPane.chinese_name_lineEdit.setText(chinese_name)
            self.editEntryDataPane.target_name_lineEdit.setText(target_name)
            self.editEntryDataPane.target_commonname_lineEdit.setText(target_commonname)
            self.editEntryDataPane.entry_commonname_lineEdit.setText(entry_commonname)
            self.editEntryDataPane.entry_name_lineEdit.setText(entry_name)
            self.editEntryDataPane.edit_entry_Signal.connect(self.edit_entry_data_Signal)
        elif self.table_comboBox.currentText() == "靶点表":
            herb_name = self.data_tableWidget.item(row, 0).text()
            english_name = self.data_tableWidget.item(row, 1).text()
            chinese_name = self.data_tableWidget.item(row, 2).text()
            target_name = self.data_tableWidget.item(row, 3).text()
            target_commonname = self.data_tableWidget.item(row, 4).text()
            self.editTargetDataPane = EditTargetDataPane()
            self.editTargetDataPane.show()
            self.editTargetDataPane.herb_name_lineEdit.setText(herb_name)
            self.editTargetDataPane.english_name_lineEdit.setText(english_name)
            self.editTargetDataPane.chinese_name_lineEdit.setText(chinese_name)
            self.editTargetDataPane.target_name_lineEdit.setText(target_name)
            self.editTargetDataPane.target_commonname_lineEdit.setText(target_commonname)
            self.editTargetDataPane.edit_target_Signal.connect(self.edit_target_data_Signal)

    def edit_herb_data_Signal(self, table_name, herb_id, herb_name):
        # print("信号连接修改中药信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "update herb_table set herb_name='"+herb_name+"' where herb_id='"+ herb_id+"'"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def edit_compound_data_Signal(self, table_name, herb_name, compound_id, chinese_name, english_name, smiles, sources, oil):
        # print("信号连接修改成分信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        row = self.data_tableWidget.currentRow()
        pre_herb_name = self.data_tableWidget.item(row, 0).text()
        pre_compound_id = self.data_tableWidget.item(row, 1).text()
        pre_chinese_name = self.data_tableWidget.item(row, 2).text()
        pre_english_name = self.data_tableWidget.item(row, 3).text()
        pre_smiles = self.data_tableWidget.item(row, 4).text()
        pre_sources = self.data_tableWidget.item(row, 5).text()
        pre_oil = self.data_tableWidget.item(row, 6).text()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "update compound_table set herb_name='"+herb_name+"',compound_id='"+compound_id+"',compound_chinese_name='"+chinese_name+"',compound_english_name='"+english_name+"',compound_smiles='"+smiles+"',compound_sources='"+sources+"',compound_oil='"+oil+\
                  "' where herb_name='"+pre_herb_name+"' and compound_id='"+pre_compound_id+"' and compound_chinese_name='"+pre_chinese_name+"' and compound_english_name='"+pre_english_name+"' and compound_smiles='"+pre_smiles+"' and compound_sources='"+pre_sources+"' and compound_oil='"+pre_oil+"'"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def edit_entry_data_Signal(self, table_name, herb_name, english_name, chinese_name, target_name, target_commonname, entry_commonname, entry_name):
        # print("信号连接修改通路信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        row = self.data_tableWidget.currentRow()
        pre_herb_name = self.data_tableWidget.item(row, 0).text()
        pre_english_name = self.data_tableWidget.item(row, 1).text()
        pre_chinese_name = self.data_tableWidget.item(row, 2).text()
        pre_target_name = self.data_tableWidget.item(row, 3).text()
        pre_target_commonname = self.data_tableWidget.item(row, 4).text()
        pre_entry_commonname = self.data_tableWidget.item(row, 5).text()
        pre_entry_name = self.data_tableWidget.item(row, 6).text()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "update signalentry_table set herb_name='"+herb_name+"',disease_english_name='"+english_name+"',disease_chinese_name='"+chinese_name+"',intersection_target_name='"+target_name+"',intersection_target_common_name='"+target_commonname+"',entry_common_name='"+entry_commonname+"',entry_name='"+entry_name+\
                  "' where herb_name='"+pre_herb_name+"' and disease_english_name='"+pre_english_name+"' and disease_chinese_name='"+pre_chinese_name+"' and intersection_target_name='"+pre_target_name+"' and intersection_target_common_name='"+pre_target_commonname+"' and entry_common_name='"+pre_entry_commonname+"' and entry_name='"+pre_entry_name+"'"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def edit_target_data_Signal(self, table_name, herb_name, english_name, chinese_name, target_name, target_commonname):
        # print("信号连接修改靶点信息")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        row = self.data_tableWidget.currentRow()
        pre_herb_name = self.data_tableWidget.item(row, 0).text()
        pre_english_name = self.data_tableWidget.item(row, 1).text()
        pre_chinese_name = self.data_tableWidget.item(row, 2).text()
        pre_target_name = self.data_tableWidget.item(row, 3).text()
        pre_target_commonname = self.data_tableWidget.item(row, 4).text()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            sql = "update target_table set herb_name='"+herb_name+"',compound_english_name='"+english_name+"',compound_chinese_name='"+chinese_name + "',target_name='"+target_name+"',target_common_name='"+target_commonname+\
                  "' where herb_name='"+pre_herb_name+"' and compound_english_name='"+pre_english_name+"' and compound_chinese_name='"+pre_chinese_name+"' and target_name='"+pre_target_name+"' and target_common_name='"+pre_target_commonname+"'"
            cur.execute(sql)
            cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sql.replace("'","\\'") + "')")
            conn.commit()
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.showIfo()

    def refresh_data(self):
        # print("刷新")
        self.showIfo()

    def change_table(self):
        # print("改变下拉框更换表")
        self.showIfo()

    def condition_search(self):
        # print("条件查询")
        pass


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = DatabaseVisualPane()
    window.show()
    sys.exit(app.exec_())
