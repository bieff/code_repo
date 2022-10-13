# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editUserIfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(329, 455)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.account_lineEdit = QtWidgets.QLineEdit(Form)
        self.account_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.account_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.horizontalLayout.addWidget(self.account_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout_2.addWidget(self.name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.password_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_3.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.email_lineEdit = QtWidgets.QLineEdit(Form)
        self.email_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.email_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.horizontalLayout_4.addWidget(self.email_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.introduction_lineEdit = QtWidgets.QLineEdit(Form)
        self.introduction_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.introduction_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.introduction_lineEdit.setObjectName("introduction_lineEdit")
        self.horizontalLayout_5.addWidget(self.introduction_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.man_rbtn = QtWidgets.QRadioButton(Form)
        self.man_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.man_rbtn.setObjectName("man_rbtn")
        self.horizontalLayout_6.addWidget(self.man_rbtn)
        self.woman_rbtn = QtWidgets.QRadioButton(Form)
        self.woman_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.woman_rbtn.setObjectName("woman_rbtn")
        self.horizontalLayout_6.addWidget(self.woman_rbtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.headimageurl_lineEdit = QtWidgets.QLineEdit(Form)
        self.headimageurl_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.headimageurl_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.headimageurl_lineEdit.setReadOnly(True)
        self.headimageurl_lineEdit.setObjectName("headimageurl_lineEdit")
        self.horizontalLayout_7.addWidget(self.headimageurl_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.experience_lineEdit = QtWidgets.QLineEdit(Form)
        self.experience_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.experience_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.experience_lineEdit.setReadOnly(True)
        self.experience_lineEdit.setObjectName("experience_lineEdit")
        self.horizontalLayout_8.addWidget(self.experience_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setStyleSheet("QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.grade_lineEdit = QtWidgets.QLineEdit(Form)
        self.grade_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.grade_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.grade_lineEdit.setReadOnly(True)
        self.grade_lineEdit.setObjectName("grade_lineEdit")
        self.horizontalLayout_9.addWidget(self.grade_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.edit_userIfo)
        self.pushButton_2.clicked.connect(Form.cancel_edit_userIfo)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账号："))
        self.label_2.setText(_translate("Form", "昵称："))
        self.label_3.setText(_translate("Form", "密码："))
        self.label_4.setText(_translate("Form", "邮箱："))
        self.label_5.setText(_translate("Form", "简介："))
        self.label_6.setText(_translate("Form", "性别："))
        self.man_rbtn.setText(_translate("Form", "男"))
        self.woman_rbtn.setText(_translate("Form", "女"))
        self.label_7.setText(_translate("Form", "头像："))
        self.label_8.setText(_translate("Form", "经验："))
        self.label_9.setText(_translate("Form", "等级："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
