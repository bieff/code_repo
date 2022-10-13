# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(999, 600)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainwindow_widget = QtWidgets.QWidget(Form)
        self.mainwindow_widget.setStyleSheet("QWidget{\n"
"    border-bottom:1px solid gray;\n"
"}")
        self.mainwindow_widget.setObjectName("mainwindow_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainwindow_widget)
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mainicon_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.mainicon_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.mainicon_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.mainicon_btn.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    border:none;\n"
"    border-image: url(:/mainwindow/images/syc.ico);\n"
"}")
        self.mainicon_btn.setText("")
        self.mainicon_btn.setObjectName("mainicon_btn")
        self.horizontalLayout_3.addWidget(self.mainicon_btn)
        self.mainname_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.mainname_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.mainname_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    font: 75 14pt \"微软雅黑\";\n"
"    color:white;\n"
"}")
        self.mainname_btn.setObjectName("mainname_btn")
        self.horizontalLayout_3.addWidget(self.mainname_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.time_label = QtWidgets.QLabel(self.mainwindow_widget)
        self.time_label.setMinimumSize(QtCore.QSize(150, 30))
        self.time_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.time_label.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}")
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_4.addWidget(self.time_label)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.userIcon_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.userIcon_btn.setMinimumSize(QtCore.QSize(36, 36))
        self.userIcon_btn.setMaximumSize(QtCore.QSize(36, 36))
        self.userIcon_btn.setStyleSheet("")
        self.userIcon_btn.setText("")
        self.userIcon_btn.setObjectName("userIcon_btn")
        self.horizontalLayout_2.addWidget(self.userIcon_btn)
        self.userName_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.userName_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.userName_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.userName_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.userName_btn.setText("")
        self.userName_btn.setObjectName("userName_btn")
        self.horizontalLayout_2.addWidget(self.userName_btn)
        self.arrow_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.arrow_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.arrow_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.arrow_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-image: url(:/mainwindow/images/arrow-down.png);\n"
"}")
        self.arrow_btn.setText("")
        self.arrow_btn.setObjectName("arrow_btn")
        self.horizontalLayout_2.addWidget(self.arrow_btn)
        self.skin_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.skin_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.skin_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.skin_btn.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    border:none;\n"
"    border-image: url(:/mainwindow/images/skin.png);\n"
"}")
        self.skin_btn.setText("")
        self.skin_btn.setObjectName("skin_btn")
        self.horizontalLayout_2.addWidget(self.skin_btn)
        self.setting_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.setting_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.setting_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.setting_btn.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    border:none;\n"
"    border-image: url(:/mainwindow/images/setting.png);\n"
"}")
        self.setting_btn.setText("")
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout_2.addWidget(self.setting_btn)
        self.label = QtWidgets.QLabel(self.mainwindow_widget)
        self.label.setMinimumSize(QtCore.QSize(10, 30))
        self.label.setMaximumSize(QtCore.QSize(10, 30))
        self.label.setStyleSheet("QLabel{\n"
"    font-size:22px;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.min_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.min_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.min_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.min_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/mainwindow/images/minus.png);\n"
"}")
        self.min_btn.setText("")
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_2.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.max_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.max_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.max_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/mainwindow/images/max.png);\n"
"}")
        self.max_btn.setText("")
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_2.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.mainwindow_widget)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.close_btn.setStatusTip("")
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    border:none;\n"
"    border-image: url(:/mainwindow/images/exit.png);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.mainwindow_widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_2)
        self.listWidget.setMinimumSize(QtCore.QSize(170, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(170, 16777215))
        self.listWidget.setStyleSheet("")
        self.listWidget.setIconSize(QtCore.QSize(40, 40))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainwindow/images/sqlscript.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainwindow/images/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mainwindow/images/data_analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon2)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mainwindow/images/account_management.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon3)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mainwindow/images/today_article.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon4)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/mainwindow/images/user_guide.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon5)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/mainwindow/images/soft_information.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon6)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/mainwindow/images/our_code.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon7)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"    border-radius:10px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(-1)
        self.listWidget.currentItemChanged['QListWidgetItem*','QListWidgetItem*'].connect(Form.change_frame)
        self.userIcon_btn.clicked.connect(Form.open_usermanagement_pane)
        self.userName_btn.clicked.connect(Form.open_personcard)
        self.arrow_btn.clicked.connect(Form.open_personcard)
        self.skin_btn.clicked.connect(Form.open_skin)
        self.setting_btn.clicked.connect(Form.open_information_pane)
        self.min_btn.clicked.connect(Form.showMin)
        self.max_btn.clicked.connect(Form.showMax)
        self.close_btn.clicked.connect(Form.close_mysystem)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mainname_btn.setText(_translate("Form", "中药精油靶点数据库"))
        self.skin_btn.setToolTip(_translate("Form", "换肤"))
        self.setting_btn.setToolTip(_translate("Form", "设置"))
        self.label.setText(_translate("Form", "|"))
        self.min_btn.setToolTip(_translate("Form", "最小化"))
        self.max_btn.setToolTip(_translate("Form", "最大化"))
        self.close_btn.setToolTip(_translate("Form", "关闭"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "脚本操作"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "表格操作"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "数据分析"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "账号管理"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "今日文章"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "使用向导"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "软件信息"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "联系我们"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
import my_images_rc
