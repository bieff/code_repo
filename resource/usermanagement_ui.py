# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usermanagement.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.account_ad_btn = QtWidgets.QPushButton(self.widget)
        self.account_ad_btn.setEnabled(True)
        self.account_ad_btn.setGeometry(QtCore.QRect(10, 0, 120, 40))
        self.account_ad_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.account_ad_btn.setStyleSheet("QPushButton{\n"
"    font-size:16px;\n"
"    border:none;\n"
"    border-bottom:2px solid gray;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/usermanagement/images/accountmanage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_ad_btn.setIcon(icon)
        self.account_ad_btn.setIconSize(QtCore.QSize(75, 40))
        self.account_ad_btn.setObjectName("account_ad_btn")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(5, 9, 5, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet("QTabWidget::pane#tabWidget{\n"
"    border-top:2px solid #00C2C7CB;\n"
"    position:absolute;\n"
"    top:10px;\n"
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
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.userIfo = QtWidgets.QWidget()
        self.userIfo.setStyleSheet("QWidget#userIfo{\n"
"    border-image: url(:/usermanagement/images/cherry_tree_3.png);\n"
"}")
        self.userIfo.setObjectName("userIfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.userIfo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.userIfo)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.email_label = QtWidgets.QLabel(self.widget_3)
        self.email_label.setMinimumSize(QtCore.QSize(60, 30))
        self.email_label.setMaximumSize(QtCore.QSize(60, 30))
        self.email_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)
        self.introduce_textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.introduce_textEdit.setMinimumSize(QtCore.QSize(250, 60))
        self.introduce_textEdit.setMaximumSize(QtCore.QSize(500, 100))
        self.introduce_textEdit.setStyleSheet("QTextEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.introduce_textEdit.setObjectName("introduce_textEdit")
        self.gridLayout.addWidget(self.introduce_textEdit, 4, 1, 1, 3)
        self.name_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.name_lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        self.name_lineEdit.setMaximumSize(QtCore.QSize(500, 45))
        self.name_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.name_lineEdit.setReadOnly(True)
        self.name_lineEdit.setClearButtonEnabled(False)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 1, 1, 1, 3)
        self.email_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.email_lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        self.email_lineEdit.setMaximumSize(QtCore.QSize(500, 45))
        self.email_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.email_lineEdit.setReadOnly(True)
        self.email_lineEdit.setClearButtonEnabled(False)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.gridLayout.addWidget(self.email_lineEdit, 2, 1, 1, 3)
        self.sex_label = QtWidgets.QLabel(self.widget_3)
        self.sex_label.setMinimumSize(QtCore.QSize(60, 30))
        self.sex_label.setMaximumSize(QtCore.QSize(60, 30))
        self.sex_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.sex_label.setObjectName("sex_label")
        self.gridLayout.addWidget(self.sex_label, 3, 0, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.widget_3)
        self.save_btn.setEnabled(True)
        self.save_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.save_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.save_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 5, 1, 1, 2)
        self.introduce__label = QtWidgets.QLabel(self.widget_3)
        self.introduce__label.setMinimumSize(QtCore.QSize(60, 30))
        self.introduce__label.setMaximumSize(QtCore.QSize(60, 30))
        self.introduce__label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.introduce__label.setObjectName("introduce__label")
        self.gridLayout.addWidget(self.introduce__label, 4, 0, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(self.widget_3)
        self.cancel_btn.setEnabled(True)
        self.cancel_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.cancel_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.cancel_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 5, 3, 1, 1)
        self.account_label = QtWidgets.QLabel(self.widget_3)
        self.account_label.setMinimumSize(QtCore.QSize(60, 30))
        self.account_label.setMaximumSize(QtCore.QSize(60, 30))
        self.account_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.account_label.setObjectName("account_label")
        self.gridLayout.addWidget(self.account_label, 0, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.widget_3)
        self.name_label.setMinimumSize(QtCore.QSize(60, 30))
        self.name_label.setMaximumSize(QtCore.QSize(60, 30))
        self.name_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.woman_rbtn = QtWidgets.QRadioButton(self.widget_3)
        self.woman_rbtn.setMinimumSize(QtCore.QSize(60, 30))
        self.woman_rbtn.setMaximumSize(QtCore.QSize(60, 30))
        self.woman_rbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/usermanagement/images/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.woman_rbtn.setIcon(icon1)
        self.woman_rbtn.setIconSize(QtCore.QSize(30, 30))
        self.woman_rbtn.setCheckable(True)
        self.woman_rbtn.setObjectName("woman_rbtn")
        self.gridLayout.addWidget(self.woman_rbtn, 3, 2, 1, 1)
        self.edit_name_btn = QtWidgets.QPushButton(self.widget_3)
        self.edit_name_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.edit_name_btn.setMaximumSize(QtCore.QSize(90, 30))
        self.edit_name_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    border:none;\n"
"    border-bottom:1px solid lightblue;\n"
"}\n"
"QPushButton:hover{\n"
"    border-bottom:2px solid blue;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/usermanagement/images/editEnable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_name_btn.setIcon(icon2)
        self.edit_name_btn.setIconSize(QtCore.QSize(25, 25))
        self.edit_name_btn.setCheckable(False)
        self.edit_name_btn.setObjectName("edit_name_btn")
        self.gridLayout.addWidget(self.edit_name_btn, 1, 4, 1, 1)
        self.edit_email_btn = QtWidgets.QPushButton(self.widget_3)
        self.edit_email_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.edit_email_btn.setMaximumSize(QtCore.QSize(90, 30))
        self.edit_email_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    border:none;\n"
"    border-bottom:1px solid lightblue;\n"
"}\n"
"QPushButton:hover{\n"
"    border-bottom:2px solid blue;\n"
"}")
        self.edit_email_btn.setIcon(icon2)
        self.edit_email_btn.setIconSize(QtCore.QSize(25, 25))
        self.edit_email_btn.setCheckable(False)
        self.edit_email_btn.setObjectName("edit_email_btn")
        self.gridLayout.addWidget(self.edit_email_btn, 2, 4, 1, 1)
        self.man_rbtn = QtWidgets.QRadioButton(self.widget_3)
        self.man_rbtn.setMinimumSize(QtCore.QSize(60, 30))
        self.man_rbtn.setMaximumSize(QtCore.QSize(60, 30))
        self.man_rbtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/usermanagement/images/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.man_rbtn.setIcon(icon3)
        self.man_rbtn.setIconSize(QtCore.QSize(30, 30))
        self.man_rbtn.setCheckable(True)
        self.man_rbtn.setChecked(False)
        self.man_rbtn.setObjectName("man_rbtn")
        self.gridLayout.addWidget(self.man_rbtn, 3, 1, 1, 1)
        self.account_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.account_lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        self.account_lineEdit.setMaximumSize(QtCore.QSize(500, 45))
        self.account_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.account_lineEdit.setReadOnly(True)
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.gridLayout.addWidget(self.account_lineEdit, 0, 1, 1, 3)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.userIfo)
        self.widget_4.setObjectName("widget_4")
        self.headimage_label = QtWidgets.QLabel(self.widget_4)
        self.headimage_label.setGeometry(QtCore.QRect(70, 40, 150, 150))
        self.headimage_label.setStyleSheet("QLabel{\n"
"    border-image:url(:/usermanagement/images/man.png);\n"
"    background-color: rgb(186, 186, 186);\n"
"}\n"
"")
        self.headimage_label.setText("")
        self.headimage_label.setObjectName("headimage_label")
        self.edit_headimage_btn = QtWidgets.QPushButton(self.widget_4)
        self.edit_headimage_btn.setGeometry(QtCore.QRect(110, 200, 75, 30))
        self.edit_headimage_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_headimage_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_headimage_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.edit_headimage_btn.setObjectName("edit_headimage_btn")
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 4)
        self.tabWidget.addTab(self.userIfo, "")
        self.pwdAd = QtWidgets.QWidget()
        self.pwdAd.setStyleSheet("QWidget#pwdAd{\n"
"    border-image: url(:/usermanagement/images/cherry_tree.png);\n"
"}")
        self.pwdAd.setObjectName("pwdAd")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pwdAd)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.pwdAd)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pwd_labe = QtWidgets.QLabel(self.widget_5)
        self.pwd_labe.setMinimumSize(QtCore.QSize(80, 30))
        self.pwd_labe.setMaximumSize(QtCore.QSize(80, 30))
        self.pwd_labe.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pwd_labe.setObjectName("pwd_labe")
        self.gridLayout_2.addWidget(self.pwd_labe, 0, 0, 1, 1)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.pwd_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.pwd_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.pwd_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.pwd_lineEdit.setClearButtonEnabled(True)
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.gridLayout_2.addWidget(self.pwd_lineEdit, 0, 1, 1, 2)
        self.pwd_show_btn = QtWidgets.QPushButton(self.widget_5)
        self.pwd_show_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.pwd_show_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.pwd_show_btn.setStyleSheet("border:none;")
        self.pwd_show_btn.setText("")
        self.pwd_show_btn.setObjectName("pwd_show_btn")
        self.gridLayout_2.addWidget(self.pwd_show_btn, 0, 3, 1, 1)
        self.pwd_error_label = QtWidgets.QLabel(self.widget_5)
        self.pwd_error_label.setMinimumSize(QtCore.QSize(200, 20))
        self.pwd_error_label.setMaximumSize(QtCore.QSize(200, 20))
        self.pwd_error_label.setText("")
        self.pwd_error_label.setObjectName("pwd_error_label")
        self.gridLayout_2.addWidget(self.pwd_error_label, 0, 4, 1, 2)
        self.newpwd_label = QtWidgets.QLabel(self.widget_5)
        self.newpwd_label.setMinimumSize(QtCore.QSize(80, 30))
        self.newpwd_label.setMaximumSize(QtCore.QSize(80, 30))
        self.newpwd_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.newpwd_label.setObjectName("newpwd_label")
        self.gridLayout_2.addWidget(self.newpwd_label, 1, 0, 1, 1)
        self.newpwd_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.newpwd_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.newpwd_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.newpwd_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.newpwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpwd_lineEdit.setClearButtonEnabled(True)
        self.newpwd_lineEdit.setObjectName("newpwd_lineEdit")
        self.gridLayout_2.addWidget(self.newpwd_lineEdit, 1, 1, 1, 2)
        self.newpwd_show_btn = QtWidgets.QPushButton(self.widget_5)
        self.newpwd_show_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.newpwd_show_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.newpwd_show_btn.setStyleSheet("border:none;")
        self.newpwd_show_btn.setText("")
        self.newpwd_show_btn.setObjectName("newpwd_show_btn")
        self.gridLayout_2.addWidget(self.newpwd_show_btn, 1, 3, 1, 1)
        self.newpwd_error_label = QtWidgets.QLabel(self.widget_5)
        self.newpwd_error_label.setMinimumSize(QtCore.QSize(200, 20))
        self.newpwd_error_label.setMaximumSize(QtCore.QSize(200, 20))
        self.newpwd_error_label.setText("")
        self.newpwd_error_label.setObjectName("newpwd_error_label")
        self.gridLayout_2.addWidget(self.newpwd_error_label, 1, 4, 1, 2)
        self.confirm_label = QtWidgets.QLabel(self.widget_5)
        self.confirm_label.setMinimumSize(QtCore.QSize(80, 30))
        self.confirm_label.setMaximumSize(QtCore.QSize(80, 30))
        self.confirm_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.confirm_label.setObjectName("confirm_label")
        self.gridLayout_2.addWidget(self.confirm_label, 2, 0, 1, 1)
        self.confirm_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.confirm_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.confirm_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.confirm_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_lineEdit.setClearButtonEnabled(True)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")
        self.gridLayout_2.addWidget(self.confirm_lineEdit, 2, 1, 1, 2)
        self.confirm_show_btn = QtWidgets.QPushButton(self.widget_5)
        self.confirm_show_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.confirm_show_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.confirm_show_btn.setStyleSheet("border:none;")
        self.confirm_show_btn.setText("")
        self.confirm_show_btn.setObjectName("confirm_show_btn")
        self.gridLayout_2.addWidget(self.confirm_show_btn, 2, 3, 1, 1)
        self.confirm_error_label = QtWidgets.QLabel(self.widget_5)
        self.confirm_error_label.setMinimumSize(QtCore.QSize(200, 20))
        self.confirm_error_label.setMaximumSize(QtCore.QSize(200, 20))
        self.confirm_error_label.setText("")
        self.confirm_error_label.setObjectName("confirm_error_label")
        self.gridLayout_2.addWidget(self.confirm_error_label, 2, 4, 1, 2)
        self.code_label = QtWidgets.QLabel(self.widget_5)
        self.code_label.setMinimumSize(QtCore.QSize(80, 30))
        self.code_label.setMaximumSize(QtCore.QSize(80, 30))
        self.code_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.code_label.setObjectName("code_label")
        self.gridLayout_2.addWidget(self.code_label, 3, 0, 1, 1)
        self.code_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.code_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.code_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.code_lineEdit.setStyleSheet("QLineEdit{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.code_lineEdit.setClearButtonEnabled(True)
        self.code_lineEdit.setObjectName("code_lineEdit")
        self.gridLayout_2.addWidget(self.code_lineEdit, 3, 1, 1, 2)
        self.code_btn = QtWidgets.QPushButton(self.widget_5)
        self.code_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.code_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.code_btn.setStyleSheet("")
        self.code_btn.setText("")
        self.code_btn.setObjectName("code_btn")
        self.gridLayout_2.addWidget(self.code_btn, 3, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(191, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 5, 1, 1)
        self.changeIfo_btn = QtWidgets.QPushButton(self.widget_5)
        self.changeIfo_btn.setEnabled(False)
        self.changeIfo_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.changeIfo_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.changeIfo_btn.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.changeIfo_btn.setObjectName("changeIfo_btn")
        self.gridLayout_2.addWidget(self.changeIfo_btn, 4, 1, 1, 1)
        self.cancel_btn_2 = QtWidgets.QPushButton(self.widget_5)
        self.cancel_btn_2.setEnabled(False)
        self.cancel_btn_2.setMinimumSize(QtCore.QSize(100, 30))
        self.cancel_btn_2.setMaximumSize(QtCore.QSize(100, 30))
        self.cancel_btn_2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.cancel_btn_2.setObjectName("cancel_btn_2")
        self.gridLayout_2.addWidget(self.cancel_btn_2, 4, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.pwdAd)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)
        self.tabWidget.addTab(self.pwdAd, "")
        self.login_record = QtWidgets.QWidget()
        self.login_record.setObjectName("login_record")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.login_record)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_11 = QtWidgets.QWidget(self.login_record)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.login_record_tableWidget = QtWidgets.QTableWidget(self.widget_11)
        self.login_record_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_record_tableWidget.setAutoFillBackground(False)
        self.login_record_tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_record_tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.login_record_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.login_record_tableWidget.setObjectName("login_record_tableWidget")
        self.login_record_tableWidget.setColumnCount(5)
        self.login_record_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.login_record_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.login_record_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.login_record_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.login_record_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.login_record_tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.login_record_tableWidget)
        self.verticalLayout_4.addWidget(self.widget_11)
        self.verticalLayout_4.setStretch(0, 10)
        self.tabWidget.addTab(self.login_record, "")
        self.work_record = QtWidgets.QWidget()
        self.work_record.setStyleSheet("QWidget#work_record{\n"
"    border-image: url(:/usermanagement/images/cherry_tree_1.png);\n"
"}")
        self.work_record.setObjectName("work_record")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.work_record)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 120, -1, -1)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.close_query_btn_ = QtWidgets.QPushButton(self.work_record)
        self.close_query_btn_.setMinimumSize(QtCore.QSize(150, 30))
        self.close_query_btn_.setStyleSheet("QPushButton{\n"
"    font-size: 12pt;\n"
"    font-family: 微软雅黑,宋体;\n"
"}")
        self.close_query_btn_.setObjectName("close_query_btn_")
        self.gridLayout_3.addWidget(self.close_query_btn_, 1, 0, 1, 1)
        self.query_btn = QtWidgets.QPushButton(self.work_record)
        self.query_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.query_btn.setStyleSheet("QPushButton{\n"
"    font-size: 12pt;\n"
"    font-family: 微软雅黑,宋体;\n"
"}")
        self.query_btn.setObjectName("query_btn")
        self.gridLayout_3.addWidget(self.query_btn, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.sqllog_textEdit = QtWidgets.QTextEdit(self.work_record)
        self.sqllog_textEdit.setStyleSheet("QTextEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.sqllog_textEdit.setReadOnly(True)
        self.sqllog_textEdit.setObjectName("sqllog_textEdit")
        self.horizontalLayout_4.addWidget(self.sqllog_textEdit)
        self.tabWidget.addTab(self.work_record, "")
        self.next_work = QtWidgets.QWidget()
        self.next_work.setStyleSheet("QWidget#next_work{\n"
"    border-image: url(:/usermanagement/images/cherry_tree_2.png);\n"
"}")
        self.next_work.setObjectName("next_work")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.next_work)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_7 = QtWidgets.QWidget(self.next_work)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.next_work)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_8)
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.next_work)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3.addWidget(self.widget_9)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 1)
        self.tabWidget.addTab(self.next_work, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.save_btn.clicked.connect(Form.change_user_inf)
        self.edit_headimage_btn.clicked.connect(Form.change_user_headimage)
        self.edit_name_btn.clicked.connect(Form.username_editable)
        self.edit_email_btn.clicked.connect(Form.useremail_editable)
        self.code_btn.clicked.connect(Form.change_code)
        self.changeIfo_btn.clicked.connect(Form.change_pwd)
        self.cancel_btn_2.clicked.connect(Form.cancel_change_pwd)
        self.cancel_btn.clicked.connect(Form.cancel_change_ifo)
        self.name_lineEdit.textChanged['QString'].connect(Form.change_ifo_enable)
        self.email_lineEdit.textChanged['QString'].connect(Form.change_ifo_enable)
        self.man_rbtn.clicked.connect(Form.change_ifo_enable)
        self.woman_rbtn.clicked.connect(Form.change_ifo_enable)
        self.pwd_lineEdit.editingFinished.connect(Form.change_pwd_enable)
        self.newpwd_lineEdit.editingFinished.connect(Form.change_pwd_enable)
        self.confirm_lineEdit.editingFinished.connect(Form.change_pwd_enable)
        self.code_lineEdit.textChanged['QString'].connect(Form.change_pwd_enable)
        self.introduce_textEdit.textChanged.connect(Form.change_ifo_enable)
        self.query_btn.clicked.connect(Form.query_sqllog)
        self.close_query_btn_.clicked.connect(Form.close_sqllog)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.account_ad_btn.setText(_translate("Form", "账号管理"))
        self.email_label.setText(_translate("Form", "邮箱："))
        self.sex_label.setText(_translate("Form", "性别："))
        self.save_btn.setText(_translate("Form", "保存"))
        self.introduce__label.setText(_translate("Form", "简介："))
        self.cancel_btn.setText(_translate("Form", "取消"))
        self.account_label.setText(_translate("Form", "账号："))
        self.name_label.setText(_translate("Form", "昵称："))
        self.edit_name_btn.setText(_translate("Form", "修改"))
        self.edit_email_btn.setText(_translate("Form", "修改"))
        self.edit_headimage_btn.setText(_translate("Form", "修改头像"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userIfo), _translate("Form", "基本信息"))
        self.pwd_labe.setText(_translate("Form", "原密码："))
        self.newpwd_label.setText(_translate("Form", "新密码："))
        self.confirm_label.setText(_translate("Form", "确认新密码："))
        self.code_label.setText(_translate("Form", "验证码："))
        self.changeIfo_btn.setText(_translate("Form", "保存"))
        self.cancel_btn_2.setText(_translate("Form", "取消"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pwdAd), _translate("Form", "密码管理"))
        item = self.login_record_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "登录账号"))
        item = self.login_record_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "登陆时间"))
        item = self.login_record_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "IP地址"))
        item = self.login_record_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "操作系统"))
        item = self.login_record_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "计算机名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_record), _translate("Form", "登录日志"))
        self.close_query_btn_.setText(_translate("Form", "关闭"))
        self.query_btn.setText(_translate("Form", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_record), _translate("Form", "工作日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.next_work), _translate("Form", "我的日程"))
import my_images_rc
