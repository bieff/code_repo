# 数据可视化分析界面，调用生成的analysis_ui.py文件
from PyQt5.Qt import *
from resource.analysis_ui import Ui_Form
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import networkx as nx
import pymysql

class AnalysisPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.user_account = "201601033017" # 当前账号
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.show_herb_comboBox()
        self.herb = ""
        self.compound = ""
        self.layout_type = "spring_layout"
        self.figure_alive = 0

    def show_herb_comboBox(self):
        # print("初始化中药下拉框")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.herb_comboBox.clear()
        self.herb_comboBox.addItem("请选择中药名称")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            sql = "select distinct herb_name from herb_table"
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','是','"+sql.replace("'","\\'")+"')")
            conn.commit()
            rowCount = len(data)
            for i in range(rowCount):
                self.herb_comboBox.addItem(data[i][0])
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()

    def show_compound_comboBox(self):
        # print("初始化成分下拉框")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.compound_comboBox.clear()
        self.compound_comboBox.addItem("请选择成分名称")
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            if self.herb == "":
                return
            else:
                sql = "select distinct compound_chinese_name from compound_table where herb_name='%s'"%self.herb
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','是','"+sql.replace("'","\\'")+"')")
            conn.commit()
            rowCount = len(data)
            for i in range(rowCount):
                if data[i][0] != "":
                    self.compound_comboBox.addItem(data[i][0])
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()

    def herb_selected(self,herb_name):
        # print("选中药物:", herb_name)
        if herb_name == "请选择中药名称":
            self.herb = ""
        else:
            self.herb = herb_name
        self.compound = ""
        self.show_compound_comboBox()

    def compound_selected(self, compound_name):
        # print("选中成分:", compound_name)
        if compound_name == "请选择成分名称":
            self.compound = ""
        else:
            self.compound = compound_name

    def change_layout(self, layout_name):
        # print("改变网络图的布局")
        if layout_name == "Circular Layout":
            self.layout_type = "circular_layout"
        elif layout_name == "Random Layout":
            self.layout_type = "random_layout"
        elif layout_name == "Shell Layout":
            self.layout_type = "shell_layout"
        elif layout_name == "Spring Layout":
            self.layout_type = "spring_layout"

    def submit_clicked(self):
        # print("点击提交")
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.node_list = []
        self.edge_list = []
        self.node_color = []
        if self.figure_alive == 1:
            self.plotCanvas.close()
            self.mpl_ntb.close()
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset = 'utf8')
            cur = conn.cursor()
            if self.herb == "":
                return
            else:
                sql = "select distinct compound_chinese_name from compound_table where herb_name='%s'"%self.herb
            cur.execute(sql)
            data = cur.fetchall()
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','是','"+sql.replace("'","\\'")+"')")
            conn.commit()
            rowCount = len(data)
            self.node_list.append(self.herb)
            self.node_color.append("#ff0000") # 红#ff0000、黄#ffff00、绿#00aa00、蓝#0055ff
            for i in range(rowCount):
                if data[i][0] != "":
                    self.node_list.append(data[i][0])
                    self.edge_list.append((self.herb, data[i][0]))
                    self.node_color.append("#ffff00")  # 红#ff0000、黄#ffff00、绿#00aa00、蓝#0055ff
            if self.compound != "":
                sql2 = "select distinct target_common_name from target_table where compound_chinese_name='"+self.compound+"'"
                cur.execute(sql2)
                data = cur.fetchall()
                cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','是','"+sql2.replace("'","\\'")+"')")
                conn.commit()
                rowCount = len(data)
                if rowCount >= 20:
                    # 由于数据太多，限制个数
                    rowCount = 20
                for i in range(rowCount):
                    if data[i][0] != "":
                        self.node_list.append(data[i][0])
                        self.edge_list.append((self.compound, data[i][0]))
                        self.node_color.append("#00aa00")  # 红#ff0000、黄#ffff00、绿#00aa00、蓝#0055ff
        except Exception as e:
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql.replace("'","\\'")+"')")
            cur.execute("insert into work_log values('"+current_account+"','"+current_time+"','否','"+sql2.replace("'","\\'")+"')")
            conn.commit()
        finally:
            conn.close()
        self.plotCanvas = PlotCanvas()
        self.plotCanvas.plot(self.node_list, self.edge_list, self.node_color, self.layout_type)
        self.verticalLayout_3.addWidget(self.plotCanvas)
        self.mpl_ntb = NavigationToolbar(self.plotCanvas, self)  # 添加完整的 toolbar,增加图片放大、移动的按钮
        self.verticalLayout_3.addWidget(self.mpl_ntb)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False
        self.figure_alive = 1


class PlotCanvas(FigureCanvas):  # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas
    def __init__(self, parent=None, width=500, height=500, dpi=100):
        self.fig = Figure(figsize=(width, height),dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        self.fig.suptitle("Network node diagram")  # 不要设置中文，否则会乱码错误
        self.axes = self.fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        # self.plot()
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, node_list, edge_list, color_list, layout_name):
        G = nx.Graph()
        G.add_nodes_from(node_list)
        G.add_edges_from(edge_list)
        if layout_name == "circular_layout":
            nx.draw(G, pos=nx.circular_layout(G), node_color=color_list, node_shape='o', ax=self.axes,
                    edge_color='#00ffff', with_labels=True, alpha=1,
                    font_size=12, node_size=200, arrows=True)
        elif layout_name == "random_layout":
            nx.draw(G, pos=nx.random_layout(G), node_color=color_list, node_shape='o', ax=self.axes,
                    edge_color='#00ffff', with_labels=True, alpha=1,
                    font_size=12, node_size=200, arrows=True)
        elif layout_name == "shell_layout":
            nx.draw(G, pos=nx.shell_layout(G), node_color=color_list, node_shape='o', ax=self.axes,
                    edge_color='#00ffff', with_labels=True, alpha=1,
                    font_size=12, node_size=200, arrows=True)
        elif layout_name == "spring_layout":
            nx.draw(G, pos=nx.spring_layout(G), node_color=color_list, node_shape='o', ax=self.axes,
                    edge_color='#00ffff', with_labels=True, alpha=1,
                    font_size=12, node_size=200, arrows=True)


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = AnalysisPane()
    window.show()
    sys.exit(app.exec_())
