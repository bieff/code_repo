# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 276)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane#tabWidget{\n"
"    border-top:2px solid #00C2C7CB;\n"
"    background:#002d2f33;\n"
"}\n"
"QTabWidget#tabWidget::tab-bar{\n"
"    alginment:center;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #00000000;\n"
"    border: none;\n"
"    border-bottom-color: #dcdde4;\n"
"    min-width: 10px;\n"
"    margin-right: 20px;\n"
"    padding-left:20px;\n"
"    padding-right:20px;\n"
"    padding-top:5px;\n"
"    padding-bottom:5px;\n"
"    color:#686a6e;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background: #BEDAFA;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-color: #F8F7F2;\n"
"    color:black;\n"
"    border-bottom: 2px solid #3c3e42;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.black_btn = QtWidgets.QPushButton(self.widget)
        self.black_btn.setGeometry(QtCore.QRect(19, 14, 90, 90))
        self.black_btn.setMinimumSize(QtCore.QSize(90, 90))
        self.black_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.black_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.black_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/black.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.black_btn.setText("")
        self.black_btn.setProperty("id", "")
        self.black_btn.setObjectName("black_btn")
        self.red_btn = QtWidgets.QPushButton(self.widget)
        self.red_btn.setGeometry(QtCore.QRect(125, 14, 90, 90))
        self.red_btn.setMinimumSize(QtCore.QSize(90, 90))
        self.red_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.red_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.red_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/red.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.red_btn.setText("")
        self.red_btn.setProperty("id", "")
        self.red_btn.setObjectName("red_btn")
        self.pink_btn = QtWidgets.QPushButton(self.widget)
        self.pink_btn.setGeometry(QtCore.QRect(231, 14, 90, 90))
        self.pink_btn.setMinimumSize(QtCore.QSize(90, 90))
        self.pink_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.pink_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pink_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/pink.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.pink_btn.setText("")
        self.pink_btn.setProperty("id", "")
        self.pink_btn.setObjectName("pink_btn")
        self.black_label = QtWidgets.QLabel(self.widget)
        self.black_label.setGeometry(QtCore.QRect(21, 81, 90, 20))
        self.black_label.setMinimumSize(QtCore.QSize(90, 20))
        self.black_label.setMaximumSize(QtCore.QSize(90, 20))
        self.black_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.black_label.setObjectName("black_label")
        self.red_label = QtWidgets.QLabel(self.widget)
        self.red_label.setGeometry(QtCore.QRect(126, 81, 90, 20))
        self.red_label.setMinimumSize(QtCore.QSize(90, 20))
        self.red_label.setMaximumSize(QtCore.QSize(90, 20))
        self.red_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.red_label.setObjectName("red_label")
        self.pinl_label = QtWidgets.QLabel(self.widget)
        self.pinl_label.setGeometry(QtCore.QRect(231, 81, 90, 20))
        self.pinl_label.setMinimumSize(QtCore.QSize(90, 20))
        self.pinl_label.setMaximumSize(QtCore.QSize(90, 20))
        self.pinl_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pinl_label.setObjectName("pinl_label")
        self.black_icon = QtWidgets.QPushButton(self.widget)
        self.black_icon.setGeometry(QtCore.QRect(86, 81, 30, 30))
        self.black_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.black_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.black_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.black_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.black_icon.setText("")
        self.black_icon.setIconSize(QtCore.QSize(16, 16))
        self.black_icon.setCheckable(True)
        self.black_icon.setAutoExclusive(False)
        self.black_icon.setObjectName("black_icon")
        self.red_icon = QtWidgets.QPushButton(self.widget)
        self.red_icon.setGeometry(QtCore.QRect(191, 81, 30, 30))
        self.red_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.red_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.red_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.red_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.red_icon.setText("")
        self.red_icon.setCheckable(True)
        self.red_icon.setAutoExclusive(False)
        self.red_icon.setObjectName("red_icon")
        self.pink_icon = QtWidgets.QPushButton(self.widget)
        self.pink_icon.setGeometry(QtCore.QRect(296, 81, 30, 30))
        self.pink_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.pink_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.pink_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pink_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.pink_icon.setText("")
        self.pink_icon.setCheckable(True)
        self.pink_icon.setAutoExclusive(False)
        self.pink_icon.setObjectName("pink_icon")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.blue_btn = QtWidgets.QPushButton(self.widget_2)
        self.blue_btn.setGeometry(QtCore.QRect(19, 8, 90, 95))
        self.blue_btn.setMinimumSize(QtCore.QSize(90, 95))
        self.blue_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.blue_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.blue_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/blue.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.blue_btn.setText("")
        self.blue_btn.setProperty("id", "")
        self.blue_btn.setObjectName("blue_btn")
        self.green_btn = QtWidgets.QPushButton(self.widget_2)
        self.green_btn.setGeometry(QtCore.QRect(125, 8, 90, 95))
        self.green_btn.setMinimumSize(QtCore.QSize(90, 95))
        self.green_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.green_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.green_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/green.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.green_btn.setText("")
        self.green_btn.setProperty("id", "")
        self.green_btn.setObjectName("green_btn")
        self.gold_btn = QtWidgets.QPushButton(self.widget_2)
        self.gold_btn.setGeometry(QtCore.QRect(231, 8, 90, 95))
        self.gold_btn.setMinimumSize(QtCore.QSize(90, 95))
        self.gold_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.gold_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gold_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/skin/images/gold.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px double rgb(41,44,50);\n"
"}")
        self.gold_btn.setText("")
        self.gold_btn.setProperty("id", "")
        self.gold_btn.setObjectName("gold_btn")
        self.blue_label = QtWidgets.QLabel(self.widget_2)
        self.blue_label.setGeometry(QtCore.QRect(21, 81, 90, 20))
        self.blue_label.setMinimumSize(QtCore.QSize(90, 20))
        self.blue_label.setMaximumSize(QtCore.QSize(90, 20))
        self.blue_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.blue_label.setObjectName("blue_label")
        self.green_label = QtWidgets.QLabel(self.widget_2)
        self.green_label.setGeometry(QtCore.QRect(126, 81, 90, 20))
        self.green_label.setMinimumSize(QtCore.QSize(90, 20))
        self.green_label.setMaximumSize(QtCore.QSize(90, 20))
        self.green_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.green_label.setObjectName("green_label")
        self.gold_label = QtWidgets.QLabel(self.widget_2)
        self.gold_label.setGeometry(QtCore.QRect(231, 81, 90, 20))
        self.gold_label.setMinimumSize(QtCore.QSize(90, 20))
        self.gold_label.setMaximumSize(QtCore.QSize(90, 20))
        self.gold_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    font: 12pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.gold_label.setObjectName("gold_label")
        self.green_icon = QtWidgets.QPushButton(self.widget_2)
        self.green_icon.setGeometry(QtCore.QRect(190, 81, 30, 30))
        self.green_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.green_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.green_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.green_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.green_icon.setText("")
        self.green_icon.setCheckable(True)
        self.green_icon.setAutoExclusive(False)
        self.green_icon.setObjectName("green_icon")
        self.gold_icon = QtWidgets.QPushButton(self.widget_2)
        self.gold_icon.setGeometry(QtCore.QRect(295, 81, 30, 30))
        self.gold_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.gold_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.gold_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gold_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.gold_icon.setText("")
        self.gold_icon.setCheckable(True)
        self.gold_icon.setAutoExclusive(False)
        self.gold_icon.setObjectName("gold_icon")
        self.blue_icon = QtWidgets.QPushButton(self.widget_2)
        self.blue_icon.setGeometry(QtCore.QRect(85, 81, 30, 30))
        self.blue_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.blue_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.blue_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.blue_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}\n"
"\n"
"")
        self.blue_icon.setText("")
        self.blue_icon.setCheckable(True)
        self.blue_icon.setAutoExclusive(False)
        self.blue_icon.setObjectName("blue_icon")
        self.verticalLayout.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(9, 9, 324, 104))
        self.widget_4.setObjectName("widget_4")
        self.color1_btn = QtWidgets.QPushButton(self.widget_4)
        self.color1_btn.setGeometry(QtCore.QRect(7, 6, 40, 40))
        self.color1_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color1_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color1_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(255, 92, 138);\n"
"}")
        self.color1_btn.setText("")
        self.color1_btn.setObjectName("color1_btn")
        self.color2_btn = QtWidgets.QPushButton(self.widget_4)
        self.color2_btn.setGeometry(QtCore.QRect(60, 6, 40, 40))
        self.color2_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color2_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color2_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color2_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(239, 122, 158);\n"
"}")
        self.color2_btn.setText("")
        self.color2_btn.setObjectName("color2_btn")
        self.color3_btn = QtWidgets.QPushButton(self.widget_4)
        self.color3_btn.setGeometry(QtCore.QRect(113, 6, 40, 40))
        self.color3_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color3_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color3_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color3_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(254, 118, 200);\n"
"}")
        self.color3_btn.setText("")
        self.color3_btn.setObjectName("color3_btn")
        self.color4_btn = QtWidgets.QPushButton(self.widget_4)
        self.color4_btn.setGeometry(QtCore.QRect(166, 6, 40, 40))
        self.color4_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color4_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color4_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color4_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(113, 127, 249);\n"
"}")
        self.color4_btn.setText("")
        self.color4_btn.setObjectName("color4_btn")
        self.color5_btn = QtWidgets.QPushButton(self.widget_4)
        self.color5_btn.setGeometry(QtCore.QRect(219, 6, 40, 40))
        self.color5_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color5_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color5_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color5_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(71, 145, 235);\n"
"}")
        self.color5_btn.setText("")
        self.color5_btn.setObjectName("color5_btn")
        self.color6_btn = QtWidgets.QPushButton(self.widget_4)
        self.color6_btn.setGeometry(QtCore.QRect(272, 6, 40, 40))
        self.color6_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color6_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color6_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color6_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(57, 175, 234);\n"
"}")
        self.color6_btn.setText("")
        self.color6_btn.setObjectName("color6_btn")
        self.color7_btn = QtWidgets.QPushButton(self.widget_4)
        self.color7_btn.setGeometry(QtCore.QRect(7, 58, 40, 40))
        self.color7_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color7_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color7_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color7_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(43, 182, 105);\n"
"}")
        self.color7_btn.setText("")
        self.color7_btn.setObjectName("color7_btn")
        self.color8_btn = QtWidgets.QPushButton(self.widget_4)
        self.color8_btn.setGeometry(QtCore.QRect(60, 58, 40, 40))
        self.color8_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color8_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color8_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color8_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(106, 204, 25);\n"
"}")
        self.color8_btn.setText("")
        self.color8_btn.setObjectName("color8_btn")
        self.color9_btn = QtWidgets.QPushButton(self.widget_4)
        self.color9_btn.setGeometry(QtCore.QRect(113, 58, 40, 40))
        self.color9_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color9_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color9_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color9_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(226, 171, 18);\n"
"}")
        self.color9_btn.setText("")
        self.color9_btn.setObjectName("color9_btn")
        self.color10_btn = QtWidgets.QPushButton(self.widget_4)
        self.color10_btn.setGeometry(QtCore.QRect(166, 58, 40, 40))
        self.color10_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color10_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color10_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color10_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(255, 143, 87);\n"
"}")
        self.color10_btn.setText("")
        self.color10_btn.setObjectName("color10_btn")
        self.color11_btn = QtWidgets.QPushButton(self.widget_4)
        self.color11_btn.setGeometry(QtCore.QRect(219, 58, 40, 40))
        self.color11_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color11_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color11_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color11_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(253, 114, 109);\n"
"}")
        self.color11_btn.setText("")
        self.color11_btn.setObjectName("color11_btn")
        self.color12_btn = QtWidgets.QPushButton(self.widget_4)
        self.color12_btn.setGeometry(QtCore.QRect(272, 58, 40, 40))
        self.color12_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.color12_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.color12_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color12_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(253, 84, 78);\n"
"}")
        self.color12_btn.setText("")
        self.color12_btn.setObjectName("color12_btn")
        self.color1_icon = QtWidgets.QPushButton(self.widget_4)
        self.color1_icon.setGeometry(QtCore.QRect(34, 31, 20, 20))
        self.color1_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color1_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color1_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color1_icon.setText("")
        self.color1_icon.setCheckable(True)
        self.color1_icon.setAutoExclusive(False)
        self.color1_icon.setObjectName("color1_icon")
        self.color2_icon = QtWidgets.QPushButton(self.widget_4)
        self.color2_icon.setGeometry(QtCore.QRect(87, 31, 20, 20))
        self.color2_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color2_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color2_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color2_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color2_icon.setText("")
        self.color2_icon.setCheckable(True)
        self.color2_icon.setAutoExclusive(False)
        self.color2_icon.setObjectName("color2_icon")
        self.color3_icon = QtWidgets.QPushButton(self.widget_4)
        self.color3_icon.setGeometry(QtCore.QRect(140, 31, 20, 20))
        self.color3_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color3_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color3_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color3_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color3_icon.setText("")
        self.color3_icon.setCheckable(True)
        self.color3_icon.setAutoExclusive(False)
        self.color3_icon.setObjectName("color3_icon")
        self.color4_icon = QtWidgets.QPushButton(self.widget_4)
        self.color4_icon.setGeometry(QtCore.QRect(193, 31, 20, 20))
        self.color4_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color4_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color4_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color4_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color4_icon.setText("")
        self.color4_icon.setCheckable(True)
        self.color4_icon.setAutoExclusive(False)
        self.color4_icon.setObjectName("color4_icon")
        self.color5_icon = QtWidgets.QPushButton(self.widget_4)
        self.color5_icon.setGeometry(QtCore.QRect(246, 31, 20, 20))
        self.color5_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color5_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color5_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color5_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color5_icon.setText("")
        self.color5_icon.setCheckable(True)
        self.color5_icon.setAutoExclusive(False)
        self.color5_icon.setObjectName("color5_icon")
        self.color6_icon = QtWidgets.QPushButton(self.widget_4)
        self.color6_icon.setGeometry(QtCore.QRect(299, 31, 20, 20))
        self.color6_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color6_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color6_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color6_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color6_icon.setText("")
        self.color6_icon.setCheckable(True)
        self.color6_icon.setAutoExclusive(False)
        self.color6_icon.setObjectName("color6_icon")
        self.color7_icon = QtWidgets.QPushButton(self.widget_4)
        self.color7_icon.setGeometry(QtCore.QRect(34, 83, 20, 20))
        self.color7_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color7_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color7_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color7_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color7_icon.setText("")
        self.color7_icon.setCheckable(True)
        self.color7_icon.setAutoExclusive(False)
        self.color7_icon.setObjectName("color7_icon")
        self.color8_icon = QtWidgets.QPushButton(self.widget_4)
        self.color8_icon.setGeometry(QtCore.QRect(87, 83, 20, 20))
        self.color8_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color8_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color8_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color8_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color8_icon.setText("")
        self.color8_icon.setCheckable(True)
        self.color8_icon.setAutoExclusive(False)
        self.color8_icon.setObjectName("color8_icon")
        self.color9_icon = QtWidgets.QPushButton(self.widget_4)
        self.color9_icon.setGeometry(QtCore.QRect(140, 83, 20, 20))
        self.color9_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color9_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color9_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color9_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color9_icon.setText("")
        self.color9_icon.setCheckable(True)
        self.color9_icon.setAutoExclusive(False)
        self.color9_icon.setObjectName("color9_icon")
        self.color10_icon = QtWidgets.QPushButton(self.widget_4)
        self.color10_icon.setGeometry(QtCore.QRect(193, 83, 20, 20))
        self.color10_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color10_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color10_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color10_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color10_icon.setText("")
        self.color10_icon.setCheckable(True)
        self.color10_icon.setAutoExclusive(False)
        self.color10_icon.setObjectName("color10_icon")
        self.color11_icon = QtWidgets.QPushButton(self.widget_4)
        self.color11_icon.setGeometry(QtCore.QRect(246, 83, 20, 20))
        self.color11_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color11_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color11_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color11_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color11_icon.setText("")
        self.color11_icon.setCheckable(True)
        self.color11_icon.setAutoExclusive(False)
        self.color11_icon.setObjectName("color11_icon")
        self.color12_icon = QtWidgets.QPushButton(self.widget_4)
        self.color12_icon.setGeometry(QtCore.QRect(299, 83, 20, 20))
        self.color12_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.color12_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.color12_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color12_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.color12_icon.setText("")
        self.color12_icon.setCheckable(True)
        self.color12_icon.setAutoExclusive(False)
        self.color12_icon.setObjectName("color12_icon")
        self.widget_5 = QtWidgets.QWidget(self.tab_2)
        self.widget_5.setGeometry(QtCore.QRect(9, 119, 324, 104))
        self.widget_5.setObjectName("widget_5")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.r_slider = QtWidgets.QSlider(self.widget_5)
        self.r_slider.setGeometry(QtCore.QRect(80, 40, 240, 20))
        self.r_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.r_slider.setStyleSheet("QSlider::add-page:Horizontal{\n"
"    background-color: rgb(69, 69, 70);\n"
"    height:5px;\n"
"}\n"
"QSlider::sub-page:Horizontal{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\n"
"    height:5px;\n"
"}\n"
"QSlider::handle:Horizontal{\n"
"    width:10px;\n"
"    margin:-1px -1px;\n"
"}\n"
"QSlider::groove:Horizontal{\n"
"    background:rgb(0, 255, 0);\n"
"    height:5px;\n"
"    padding-left:-3px;\n"
"    padding-right:-3px;\n"
"}")
        self.r_slider.setMaximum(255)
        self.r_slider.setOrientation(QtCore.Qt.Horizontal)
        self.r_slider.setObjectName("r_slider")
        self.b_slider = QtWidgets.QSlider(self.widget_5)
        self.b_slider.setGeometry(QtCore.QRect(80, 80, 240, 20))
        self.b_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_slider.setStyleSheet("QSlider::add-page:Horizontal{\n"
"    background-color: rgb(69, 69, 70);\n"
"    height:5px;\n"
"}\n"
"QSlider::sub-page:Horizontal{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\n"
"    height:5px;\n"
"}\n"
"QSlider::handle:Horizontal{\n"
"    width:10px;\n"
"    margin:-1px -1px;\n"
"}\n"
"QSlider::groove:Horizontal{\n"
"    background:rgb(0, 255, 0);\n"
"    height:5px;\n"
"    padding-left:-3px;\n"
"    padding-right:-3px;\n"
"}")
        self.b_slider.setMaximum(255)
        self.b_slider.setOrientation(QtCore.Qt.Horizontal)
        self.b_slider.setObjectName("b_slider")
        self.g_slider = QtWidgets.QSlider(self.widget_5)
        self.g_slider.setGeometry(QtCore.QRect(80, 60, 240, 20))
        self.g_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.g_slider.setStyleSheet("QSlider::add-page:Horizontal{\n"
"    background-color: rgb(69, 69, 70);\n"
"    height:5px;\n"
"}\n"
"QSlider::sub-page:Horizontal{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\n"
"    height:5px;\n"
"}\n"
"QSlider::handle:Horizontal{\n"
"    width:10px;\n"
"    margin:-1px -1px;\n"
"}\n"
"QSlider::groove:Horizontal{\n"
"    background:rgb(0, 255, 0);\n"
"    height:5px;\n"
"    padding-left:-3px;\n"
"    padding-right:-3px;\n"
"}")
        self.g_slider.setMaximum(255)
        self.g_slider.setOrientation(QtCore.Qt.Horizontal)
        self.g_slider.setObjectName("g_slider")
        self.pane_btn = QtWidgets.QPushButton(self.widget_5)
        self.pane_btn.setGeometry(QtCore.QRect(10, 40, 60, 60))
        self.pane_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.pane_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.pane_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pane_btn.setStyleSheet("QPushButton{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\n"
"    border:none;\n"
"}")
        self.pane_btn.setText("")
        self.pane_btn.setObjectName("pane_btn")
        self.pane_icon = QtWidgets.QPushButton(self.widget_5)
        self.pane_icon.setGeometry(QtCore.QRect(50, 80, 20, 20))
        self.pane_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.pane_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.pane_icon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pane_icon.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton::checked{\n"
"    background-color:white;\n"
"    border-image: url(:/skin/images/colorselect.png);\n"
"}")
        self.pane_icon.setText("")
        self.pane_icon.setCheckable(True)
        self.pane_icon.setAutoExclusive(False)
        self.pane_icon.setObjectName("pane_icon")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.color1_btn.clicked.connect(Form.change_color)
        self.color2_btn.clicked.connect(Form.change_color)
        self.color3_btn.clicked.connect(Form.change_color)
        self.color4_btn.clicked.connect(Form.change_color)
        self.color5_btn.clicked.connect(Form.change_color)
        self.color6_btn.clicked.connect(Form.change_color)
        self.color7_btn.clicked.connect(Form.change_color)
        self.color8_btn.clicked.connect(Form.change_color)
        self.color9_btn.clicked.connect(Form.change_color)
        self.color10_btn.clicked.connect(Form.change_color)
        self.color11_btn.clicked.connect(Form.change_color)
        self.color12_btn.clicked.connect(Form.change_color)
        self.r_slider.valueChanged['int'].connect(Form.change_color)
        self.g_slider.valueChanged['int'].connect(Form.change_color)
        self.b_slider.valueChanged['int'].connect(Form.change_color)
        self.black_btn.clicked.connect(Form.change_style)
        self.red_btn.clicked.connect(Form.change_style)
        self.pink_btn.clicked.connect(Form.change_style)
        self.blue_btn.clicked.connect(Form.change_style)
        self.green_btn.clicked.connect(Form.change_style)
        self.gold_btn.clicked.connect(Form.change_style)
        self.pane_btn.clicked.connect(Form.change_color)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.black_label.setText(_translate("Form", " 酷炫黑"))
        self.red_label.setText(_translate("Form", " 官方红"))
        self.pinl_label.setText(_translate("Form", " 可爱粉"))
        self.blue_label.setText(_translate("Form", " 天际蓝"))
        self.green_label.setText(_translate("Form", " 清新绿"))
        self.gold_label.setText(_translate("Form", " 土豪金"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "主题"))
        self.label.setText(_translate("Form", "自定义颜色"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "纯色"))
import my_images_rc
