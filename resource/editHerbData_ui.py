# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editHerbData.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 160)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(65, 0))
        self.label.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.herb_id_lineEdit = QtWidgets.QLineEdit(Form)
        self.herb_id_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.herb_id_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.herb_id_lineEdit.setReadOnly(True)
        self.herb_id_lineEdit.setObjectName("herb_id_lineEdit")
        self.horizontalLayout.addWidget(self.herb_id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(65, 0))
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.herb_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.herb_name_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.herb_name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.herb_name_lineEdit.setObjectName("herb_name_lineEdit")
        self.horizontalLayout_2.addWidget(self.herb_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.edit_herb_table)
        self.pushButton_2.clicked.connect(Form.cancel_edit_herb_table)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "通路表"))
        self.label.setText(_translate("Form", "中药ID："))
        self.label_2.setText(_translate("Form", "中药名称："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
