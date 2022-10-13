# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editCompoundData.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
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
        self.herb_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.herb_name_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.herb_name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.herb_name_lineEdit.setObjectName("herb_name_lineEdit")
        self.horizontalLayout.addWidget(self.herb_name_lineEdit)
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
        self.compound_id_lineEdit = QtWidgets.QLineEdit(Form)
        self.compound_id_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.compound_id_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.compound_id_lineEdit.setObjectName("compound_id_lineEdit")
        self.horizontalLayout_2.addWidget(self.compound_id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(65, 0))
        self.label_3.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.chinese_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.chinese_name_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.chinese_name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.chinese_name_lineEdit.setObjectName("chinese_name_lineEdit")
        self.horizontalLayout_3.addWidget(self.chinese_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(65, 0))
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.english_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.english_name_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.english_name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.english_name_lineEdit.setObjectName("english_name_lineEdit")
        self.horizontalLayout_4.addWidget(self.english_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(65, 0))
        self.label_5.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.smiles_lineEdit = QtWidgets.QLineEdit(Form)
        self.smiles_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.smiles_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.smiles_lineEdit.setObjectName("smiles_lineEdit")
        self.horizontalLayout_5.addWidget(self.smiles_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(65, 0))
        self.label_7.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.sources_lineEdit = QtWidgets.QLineEdit(Form)
        self.sources_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.sources_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.sources_lineEdit.setReadOnly(False)
        self.sources_lineEdit.setObjectName("sources_lineEdit")
        self.horizontalLayout_7.addWidget(self.sources_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(65, 0))
        self.label_8.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.oil_lineEdit = QtWidgets.QLineEdit(Form)
        self.oil_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.oil_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.oil_lineEdit.setReadOnly(False)
        self.oil_lineEdit.setObjectName("oil_lineEdit")
        self.horizontalLayout_8.addWidget(self.oil_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.ok_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_10.addWidget(self.ok_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_10.addWidget(self.cancel_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.retranslateUi(Form)
        self.ok_btn.clicked.connect(Form.edit_compound_table)
        self.cancel_btn.clicked.connect(Form.cancel_edit_compound_table)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "成分表"))
        self.label.setText(_translate("Form", "药物名称："))
        self.label_2.setText(_translate("Form", "成分ID："))
        self.label_3.setText(_translate("Form", "中文名称："))
        self.label_4.setText(_translate("Form", "英文名称："))
        self.label_5.setText(_translate("Form", "化学式："))
        self.label_7.setText(_translate("Form", "成分来源："))
        self.label_8.setText(_translate("Form", "所属精油："))
        self.ok_btn.setText(_translate("Form", "确定"))
        self.cancel_btn.setText(_translate("Form", "取消"))
