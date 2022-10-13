# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 500)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setMaximumSize(QtCore.QSize(700, 500))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("\n"
"QWidget#widget{\n"
"border-image: url(:/register_background/images/register_background.jpg);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.register_bottom = QtWidgets.QWidget(Form)
        self.register_bottom.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_bottom.setStyleSheet("\n"
"QWidget#register_bottom {\n"
"border-image: url(:/register_background/images/register_background1.jpg);\n"
"}\n"
"")
        self.register_bottom.setObjectName("register_bottom")
        self.btn_menu = QtWidgets.QPushButton(self.register_bottom)
        self.btn_menu.setGeometry(QtCore.QRect(11, 157, 50, 50))
        self.btn_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_menu.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_menu.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: rgb(85, 255, 127);\n"
"    border:1px solid rgb(0, 255, 0)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 255, 0);\n"
"    border:4px double rgb(0, 255, 0)\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(85, 170, 0);\n"
"}")
        self.btn_menu.setCheckable(True)
        self.btn_menu.setObjectName("btn_menu")
        self.btn_policy = QtWidgets.QPushButton(self.register_bottom)
        self.btn_policy.setGeometry(QtCore.QRect(67, 101, 50, 50))
        self.btn_policy.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_policy.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_policy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_policy.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: rgb(85, 255, 127);\n"
"    border:1px solid rgb(0, 255, 0)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 255, 0);\n"
"    border:4px double rgb(0, 255, 0)\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(85, 170, 0);\n"
"}")
        self.btn_policy.setObjectName("btn_policy")
        self.btn_reset = QtWidgets.QPushButton(self.register_bottom)
        self.btn_reset.setGeometry(QtCore.QRect(67, 157, 50, 50))
        self.btn_reset.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_reset.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_reset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_reset.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: rgb(85, 255, 127);\n"
"    border:1px solid rgb(0, 255, 0)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 255, 0);\n"
"    border:4px double rgb(0, 255, 0)\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(85, 170, 0);\n"
"}")
        self.btn_reset.setObjectName("btn_reset")
        self.btn_exit = QtWidgets.QPushButton(self.register_bottom)
        self.btn_exit.setGeometry(QtCore.QRect(67, 213, 50, 50))
        self.btn_exit.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_exit.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_exit.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: rgb(85, 255, 127);\n"
"    border:1px solid rgb(0, 255, 0)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 255, 0);\n"
"    border:4px double rgb(0, 255, 0)\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(85, 170, 0);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_binarycode = QtWidgets.QPushButton(self.register_bottom)
        self.btn_binarycode.setGeometry(QtCore.QRect(540, 140, 150, 150))
        self.btn_binarycode.setMinimumSize(QtCore.QSize(150, 150))
        self.btn_binarycode.setMaximumSize(QtCore.QSize(150, 150))
        self.btn_binarycode.setStyleSheet("QPushButton{\n"
"    border-image: url(:/register_background/images/binarycode.jpg);\n"
"}")
        self.btn_binarycode.setText("")
        self.btn_binarycode.setObjectName("btn_binarycode")
        self.layoutWidget = QtWidgets.QWidget(self.register_bottom)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 70, 351, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_account = QtWidgets.QLabel(self.layoutWidget)
        self.label_account.setMinimumSize(QtCore.QSize(0, 40))
        self.label_account.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.label_account.setObjectName("label_account")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_account)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        self.label_password.setMinimumSize(QtCore.QSize(0, 40))
        self.label_password.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_password.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"font: 16pt \"黑体\";\n"
"border:none;\n"
"border-bottom:1px solid lightblue;")
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_confirm = QtWidgets.QLabel(self.layoutWidget)
        self.label_confirm.setMinimumSize(QtCore.QSize(0, 40))
        self.label_confirm.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";")
        self.label_confirm.setObjectName("label_confirm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_confirm)
        self.lineEdit_confirm = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_confirm.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_confirm.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"font: 16pt \"黑体\";\n"
"border:none;\n"
"border-bottom:1px solid lightblue;")
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm.setClearButtonEnabled(True)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_confirm)
        self.lineEdit_account = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_account.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_account.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"font: 16pt \"黑体\";\n"
"border:none;\n"
"border-bottom:1px solid lightblue;")
        self.lineEdit_account.setClearButtonEnabled(True)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_account)
        self.btn_register = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_register.setEnabled(False)
        self.btn_register.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_register.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 255, 255);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(175, 175, 175);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"")
        self.btn_register.setObjectName("btn_register")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btn_register)
        self.layoutWidget.raise_()
        self.btn_policy.raise_()
        self.btn_reset.raise_()
        self.btn_exit.raise_()
        self.btn_binarycode.raise_()
        self.btn_menu.raise_()
        self.verticalLayout.addWidget(self.register_bottom)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 7)

        self.retranslateUi(Form)
        self.btn_menu.clicked.connect(Form.show_hide_menu)
        self.btn_policy.clicked.connect(Form.policy)
        self.btn_exit.clicked.connect(Form.exit_register)
        self.btn_reset.clicked.connect(Form.reset)
        self.btn_register.clicked.connect(Form.check_register)
        self.btn_menu.clicked['bool'].connect(Form.show_hide_menu)
        self.lineEdit_account.textChanged['QString'].connect(Form.enable_register)
        self.lineEdit_password.textChanged['QString'].connect(Form.enable_register)
        self.lineEdit_confirm.textChanged['QString'].connect(Form.enable_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_menu.setText(_translate("Form", "菜单"))
        self.btn_policy.setText(_translate("Form", "声明"))
        self.btn_reset.setText(_translate("Form", "重置"))
        self.btn_exit.setText(_translate("Form", "退出"))
        self.layoutWidget.setStyleSheet(_translate("Form", "background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"font: 16pt \"黑体\";"))
        self.label_account.setText(_translate("Form", "账    号："))
        self.label_password.setText(_translate("Form", "密    码："))
        self.label_confirm.setText(_translate("Form", "确认密码："))
        self.btn_register.setText(_translate("Form", "注册"))
import my_images_rc
