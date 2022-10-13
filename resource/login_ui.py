# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_top_label = QtWidgets.QLabel(self.widget)
        self.login_top_label.setText("")
        self.login_top_label.setObjectName("login_top_label")
        self.horizontalLayout_2.addWidget(self.login_top_label)
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom = QtWidgets.QWidget(Form)
        self.login_bottom.setStyleSheet("")
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 19)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.login_bottom)
        self.register_btn.setMinimumSize(QtCore.QSize(120, 0))
        self.register_btn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.register_btn.setStatusTip("")
        self.register_btn.setWhatsThis("")
        self.register_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/register_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_btn.setIcon(icon)
        self.register_btn.setIconSize(QtCore.QSize(30, 30))
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn, 0, QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(20, 20, 20, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.account_comboBox = QtWidgets.QComboBox(self.widget_3)
        self.account_comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.account_comboBox.setStyleSheet("QComboBox{\n"
"    font-size:20px;\n"
"    border:none;\n"
"    border-bottom:1px solid lightgray;\n"
"    background-color:transparent;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom:1px solid rgb(18,183,245);\n"
"}\n"
"QComboBox:drop-down{\n"
"    background-color:transparent;\n"
"    width:60px;\n"
"    height:30px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/login/images/arrow_down.png);\n"
"    width:60px;\n"
"    height:100px;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    min-height:60px;\n"
"}\n"
"QComboBox QAbstractItemView:item{\n"
"    color:lightblue;\n"
"}")
        self.account_comboBox.setEditable(True)
        self.account_comboBox.setObjectName("account_comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/images/201601033017.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/images/201601033034.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_comboBox.addItem(icon2, "")
        self.gridLayout.addWidget(self.account_comboBox, 0, 0, 1, 3)
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.password_lineEdit.setStyleSheet("QLineEdit {\n"
"    font-size:20px;\n"
"    border:none;\n"
"    border-bottom:1px solid lightgray;\n"
"    background-color:transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom:1px solid grb(18,183,245);\n"
"}")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setPlaceholderText("")
        self.password_lineEdit.setClearButtonEnabled(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 1, 0, 1, 3)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    font-size:20px;\n"
"    background-color:rgb(33,174,250);\n"
"    border-radius:8px;\n"
"    color:white;\n"
"    spacing:20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:rgb(189, 189, 189);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/login/images/safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon3)
        self.login_btn.setIconSize(QtCore.QSize(30, 30))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 4, 0, 1, 3)
        self.auto_login_checkbox = QtWidgets.QCheckBox(self.widget_3)
        self.auto_login_checkbox.setMinimumSize(QtCore.QSize(100, 30))
        self.auto_login_checkbox.setStyleSheet("QCheckBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.auto_login_checkbox.setObjectName("auto_login_checkbox")
        self.gridLayout.addWidget(self.auto_login_checkbox, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.remember_pwd_checkbox = QtWidgets.QCheckBox(self.widget_3)
        self.remember_pwd_checkbox.setMinimumSize(QtCore.QSize(100, 30))
        self.remember_pwd_checkbox.setStyleSheet("QCheckBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.remember_pwd_checkbox.setObjectName("remember_pwd_checkbox")
        self.gridLayout.addWidget(self.remember_pwd_checkbox, 3, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.binarycode_btn = QtWidgets.QPushButton(self.login_bottom)
        self.binarycode_btn.setMinimumSize(QtCore.QSize(120, 120))
        self.binarycode_btn.setMaximumSize(QtCore.QSize(120, 120))
        self.binarycode_btn.setStyleSheet("border-image:url(:/login/images/qq_binarycode.png);")
        self.binarycode_btn.setText("")
        self.binarycode_btn.setObjectName("binarycode_btn")
        self.horizontalLayout.addWidget(self.binarycode_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.login_bottom)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.show_register_pane)
        self.binarycode_btn.clicked.connect(Form.open_qq_link)
        self.account_comboBox.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.password_lineEdit.textChanged['QString'].connect(Form.enable_login_btn)
        self.login_btn.clicked.connect(Form.check_login)
        self.auto_login_checkbox.clicked['bool'].connect(Form.auto_login)
        self.remember_pwd_checkbox.clicked['bool'].connect(Form.remember_pwd)
        self.account_comboBox.currentTextChanged['QString'].connect(Form.change_user_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.account_comboBox.setItemText(0, _translate("Form", "201601033017"))
        self.account_comboBox.setItemText(1, _translate("Form", "201601033034"))
        self.login_btn.setText(_translate("Form", "安全登录"))
        self.auto_login_checkbox.setText(_translate("Form", "自动登录"))
        self.remember_pwd_checkbox.setText(_translate("Form", "记住密码"))
import my_images_rc
