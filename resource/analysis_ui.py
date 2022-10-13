# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.herb_comboBox = QtWidgets.QComboBox(self.widget_3)
        self.herb_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.herb_comboBox.setFont(font)
        self.herb_comboBox.setStyleSheet("QComboBox QAbstractItemView{\n"
"    min-height:30px;\n"
"}")
        self.herb_comboBox.setIconSize(QtCore.QSize(30, 30))
        self.herb_comboBox.setObjectName("herb_comboBox")
        self.herb_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.herb_comboBox)
        self.compound_comboBox = QtWidgets.QComboBox(self.widget_3)
        self.compound_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.compound_comboBox.setFont(font)
        self.compound_comboBox.setIconSize(QtCore.QSize(30, 30))
        self.compound_comboBox.setObjectName("compound_comboBox")
        self.compound_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.compound_comboBox)
        self.submit_btn = QtWidgets.QPushButton(self.widget_3)
        self.submit_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.submit_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.submit_btn.setIconSize(QtCore.QSize(35, 35))
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout_2.addWidget(self.submit_btn)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_comboBox = QtWidgets.QComboBox(self.widget_4)
        self.layout_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.layout_comboBox.setFont(font)
        self.layout_comboBox.setObjectName("layout_comboBox")
        self.layout_comboBox.addItem("")
        self.layout_comboBox.addItem("")
        self.layout_comboBox.addItem("")
        self.layout_comboBox.addItem("")
        self.gridLayout.addWidget(self.layout_comboBox, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.herb_label = QtWidgets.QLabel(self.widget_4)
        self.herb_label.setStyleSheet("QLabel#herb_label{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.herb_label.setObjectName("herb_label")
        self.gridLayout.addWidget(self.herb_label, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton_2.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.compound_label = QtWidgets.QLabel(self.widget_4)
        self.compound_label.setStyleSheet("QLabel#compound_label{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.compound_label.setObjectName("compound_label")
        self.gridLayout.addWidget(self.compound_label, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton_3.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.target_label = QtWidgets.QLabel(self.widget_4)
        self.target_label.setStyleSheet("QLabel#target_label{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.target_label.setObjectName("target_label")
        self.gridLayout.addWidget(self.target_label, 3, 1, 1, 1)
        self.line_label = QtWidgets.QLabel(self.widget_4)
        self.line_label.setMinimumSize(QtCore.QSize(24, 3))
        self.line_label.setMaximumSize(QtCore.QSize(24, 3))
        self.line_label.setStyleSheet("QLabel#line_label{\n"
"    background-color: rgb(0, 255, 255);\n"
"}")
        self.line_label.setText("")
        self.line_label.setObjectName("line_label")
        self.gridLayout.addWidget(self.line_label, 4, 0, 1, 1)
        self.correlation_label = QtWidgets.QLabel(self.widget_4)
        self.correlation_label.setStyleSheet("QLabel#correlation_label{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.correlation_label.setObjectName("correlation_label")
        self.gridLayout.addWidget(self.correlation_label, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)

        self.retranslateUi(Form)
        self.herb_comboBox.currentTextChanged['QString'].connect(Form.herb_selected)
        self.compound_comboBox.currentTextChanged['QString'].connect(Form.compound_selected)
        self.submit_btn.clicked.connect(Form.submit_clicked)
        self.layout_comboBox.currentTextChanged['QString'].connect(Form.change_layout)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.herb_comboBox.setItemText(0, _translate("Form", "请选择中药名称"))
        self.compound_comboBox.setItemText(0, _translate("Form", "请选择成分名称"))
        self.submit_btn.setText(_translate("Form", "提交"))
        self.layout_comboBox.setItemText(0, _translate("Form", "Circular Layout"))
        self.layout_comboBox.setItemText(1, _translate("Form", "Random Layout"))
        self.layout_comboBox.setItemText(2, _translate("Form", "Shell Layout"))
        self.layout_comboBox.setItemText(3, _translate("Form", "Spring Layout"))
        self.herb_label.setText(_translate("Form", "中药名称"))
        self.compound_label.setText(_translate("Form", "成分名称"))
        self.target_label.setText(_translate("Form", "靶点名称"))
        self.correlation_label.setText(_translate("Form", "属性关联"))
