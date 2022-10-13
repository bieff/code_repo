# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databasevisual.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_btn = QtWidgets.QPushButton(self.widget)
        self.new_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.new_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.new_btn.setStyleSheet("QPushButton {\n"
"    font-size:16px;\n"
"    border-radius:4px;\n"
"    border:1px solid lightgray;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked {\n"
"    border:1px solid green;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/database/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_btn.setIcon(icon)
        self.new_btn.setIconSize(QtCore.QSize(20, 20))
        self.new_btn.setCheckable(True)
        self.new_btn.setAutoExclusive(True)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout_2.addWidget(self.new_btn)
        self.delete_btn = QtWidgets.QPushButton(self.widget)
        self.delete_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.delete_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.delete_btn.setStyleSheet("QPushButton {\n"
"    font-size:16px;\n"
"    border-radius:4px;\n"
"    border:1px solid lightgray;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked {\n"
"    border:1px solid green;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/database/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setIconSize(QtCore.QSize(20, 20))
        self.delete_btn.setCheckable(True)
        self.delete_btn.setAutoExclusive(True)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        self.edit_btn = QtWidgets.QPushButton(self.widget)
        self.edit_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.edit_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.edit_btn.setStyleSheet("QPushButton {\n"
"    font-size:16px;\n"
"    border-radius:4px;\n"
"    border:1px solid lightgray;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked {\n"
"    border:1px solid green;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/database/images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon2)
        self.edit_btn.setIconSize(QtCore.QSize(20, 20))
        self.edit_btn.setCheckable(True)
        self.edit_btn.setAutoExclusive(True)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_2.addWidget(self.edit_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.widget)
        self.refresh_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.refresh_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.refresh_btn.setStyleSheet("QPushButton {\n"
"    font-size:16px;\n"
"    border-radius:4px;\n"
"    border:1px solid lightgray;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/database/images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon3)
        self.refresh_btn.setIconSize(QtCore.QSize(16, 16))
        self.refresh_btn.setCheckable(True)
        self.refresh_btn.setAutoExclusive(True)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_2.addWidget(self.refresh_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.table_comboBox = QtWidgets.QComboBox(self.widget)
        self.table_comboBox.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.table_comboBox.setFont(font)
        self.table_comboBox.setObjectName("table_comboBox")
        self.table_comboBox.addItem("")
        self.table_comboBox.addItem("")
        self.table_comboBox.addItem("")
        self.table_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.table_comboBox)
        self.keyword_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.keyword_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.keyword_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.keyword_lineEdit.setStyleSheet("QLineEdit{\n"
"    font-size:14px;\n"
"    border-radius:4px;\n"
"}")
        self.keyword_lineEdit.setObjectName("keyword_lineEdit")
        self.horizontalLayout_2.addWidget(self.keyword_lineEdit)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.search_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.search_btn.setStyleSheet("QPushButton {\n"
"    font-size:16px;\n"
"    border-radius:15px;\n"
"    border:1px solid gray;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}")
        self.search_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/database/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setCheckable(True)
        self.search_btn.setAutoExclusive(True)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_2.addWidget(self.search_btn)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.data_tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.data_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.data_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.data_tableWidget.setObjectName("data_tableWidget")
        self.data_tableWidget.setColumnCount(0)
        self.data_tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.data_tableWidget)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(Form)
        self.new_btn.clicked.connect(Form.new_data)
        self.delete_btn.clicked.connect(Form.delete_data)
        self.edit_btn.clicked.connect(Form.edit_data)
        self.refresh_btn.clicked.connect(Form.refresh_data)
        self.table_comboBox.currentTextChanged['QString'].connect(Form.change_table)
        self.search_btn.clicked.connect(Form.condition_search)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.new_btn.setText(_translate("Form", "新建"))
        self.delete_btn.setText(_translate("Form", "删除"))
        self.edit_btn.setText(_translate("Form", "修改"))
        self.refresh_btn.setText(_translate("Form", "刷新"))
        self.table_comboBox.setItemText(0, _translate("Form", "中药表"))
        self.table_comboBox.setItemText(1, _translate("Form", "成分表"))
        self.table_comboBox.setItemText(2, _translate("Form", "靶点表"))
        self.table_comboBox.setItemText(3, _translate("Form", "通路表"))
        self.keyword_lineEdit.setPlaceholderText(_translate("Form", "请输入关键字"))
import my_images_rc
