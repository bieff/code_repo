# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samanagement.ui'
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.account_ad_btn = QtWidgets.QPushButton(self.widget)
        self.account_ad_btn.setEnabled(True)
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
        self.horizontalLayout_5.addWidget(self.account_ad_btn)
        spacerItem = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sa_icon_btn = QtWidgets.QPushButton(self.widget)
        self.sa_icon_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.sa_icon_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.sa_icon_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:15px;\n"
"}")
        self.sa_icon_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/samanagement/images/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sa_icon_btn.setIcon(icon1)
        self.sa_icon_btn.setIconSize(QtCore.QSize(30, 30))
        self.sa_icon_btn.setObjectName("sa_icon_btn")
        self.horizontalLayout_3.addWidget(self.sa_icon_btn)
        self.welcome_label = QtWidgets.QLabel(self.widget)
        self.welcome_label.setMinimumSize(QtCore.QSize(0, 30))
        self.welcome_label.setObjectName("welcome_label")
        self.horizontalLayout_3.addWidget(self.welcome_label)
        self.time_label = QtWidgets.QLabel(self.widget)
        self.time_label.setMinimumSize(QtCore.QSize(230, 30))
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_3.addWidget(self.time_label)
        self.exit_btn = QtWidgets.QPushButton(self.widget)
        self.exit_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:lightgray;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:gray;\n"
"}")
        self.exit_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/samanagement/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QtCore.QSize(30, 30))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_3.addWidget(self.exit_btn)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
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
        self.user_Ifo = QtWidgets.QWidget()
        self.user_Ifo.setStyleSheet("")
        self.user_Ifo.setObjectName("user_Ifo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.user_Ifo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.user_Ifo)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.new_btn = QtWidgets.QPushButton(self.widget_4)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/database/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_btn.setIcon(icon3)
        self.new_btn.setIconSize(QtCore.QSize(20, 20))
        self.new_btn.setCheckable(True)
        self.new_btn.setAutoExclusive(True)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout_4.addWidget(self.new_btn)
        self.delete_btn = QtWidgets.QPushButton(self.widget_4)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/database/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon4)
        self.delete_btn.setIconSize(QtCore.QSize(20, 20))
        self.delete_btn.setCheckable(True)
        self.delete_btn.setAutoExclusive(True)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_4.addWidget(self.delete_btn)
        self.edit_btn = QtWidgets.QPushButton(self.widget_4)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/database/images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon5)
        self.edit_btn.setIconSize(QtCore.QSize(20, 20))
        self.edit_btn.setCheckable(True)
        self.edit_btn.setAutoExclusive(True)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_4.addWidget(self.edit_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.widget_4)
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
"}\n"
"\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/database/images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon6)
        self.refresh_btn.setIconSize(QtCore.QSize(16, 16))
        self.refresh_btn.setCheckable(True)
        self.refresh_btn.setAutoExclusive(True)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_4.addWidget(self.refresh_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.userIfo_tableWidget = QtWidgets.QTableWidget(self.widget_3)
        self.userIfo_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.userIfo_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.userIfo_tableWidget.setObjectName("userIfo_tableWidget")
        self.userIfo_tableWidget.setColumnCount(9)
        self.userIfo_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.userIfo_tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_4.addWidget(self.userIfo_tableWidget)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout.addWidget(self.widget_3)
        self.tabWidget.addTab(self.user_Ifo, "")
        self.user_feedback = QtWidgets.QWidget()
        self.user_feedback.setObjectName("user_feedback")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.user_feedback)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.feedback_tableWidget = QtWidgets.QTableWidget(self.user_feedback)
        self.feedback_tableWidget.setObjectName("feedback_tableWidget")
        self.feedback_tableWidget.setColumnCount(6)
        self.feedback_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_tableWidget.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_2.addWidget(self.feedback_tableWidget)
        self.tabWidget.addTab(self.user_feedback, "")
        self.login_record = QtWidgets.QWidget()
        self.login_record.setObjectName("login_record")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_record)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.verticalLayout_3.addWidget(self.widget_11)
        self.tabWidget.addTab(self.login_record, "")
        self.work_record = QtWidgets.QWidget()
        self.work_record.setObjectName("work_record")
        self.gridLayout = QtWidgets.QGridLayout(self.work_record)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.sqllog_textEdit = QtWidgets.QTextEdit(self.work_record)
        self.sqllog_textEdit.setStyleSheet("QTextEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.sqllog_textEdit.setReadOnly(True)
        self.sqllog_textEdit.setObjectName("sqllog_textEdit")
        self.gridLayout.addWidget(self.sqllog_textEdit, 0, 1, 1, 1)
        self.tabWidget.addTab(self.work_record, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.exit_btn.clicked.connect(Form.sa_exit)
        self.new_btn.clicked.connect(Form.new_user)
        self.delete_btn.clicked.connect(Form.delete_user)
        self.edit_btn.clicked.connect(Form.edit_user)
        self.refresh_btn.clicked.connect(Form.refresh_record)
        self.query_btn.clicked.connect(Form.query_sqllog)
        self.close_query_btn_.clicked.connect(Form.close_sqllog)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.account_ad_btn.setText(_translate("Form", "后台管理"))
        self.welcome_label.setText(_translate("Form", "管理员，欢迎您！"))
        self.exit_btn.setToolTip(_translate("Form", "退出"))
        self.new_btn.setText(_translate("Form", "新建"))
        self.delete_btn.setText(_translate("Form", "删除"))
        self.edit_btn.setText(_translate("Form", "修改"))
        self.refresh_btn.setText(_translate("Form", "刷新"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "账号"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "昵称"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "密码"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "邮箱"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "简介"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "性别"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "头像"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "经验"))
        item = self.userIfo_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "等级"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_Ifo), _translate("Form", "用户信息"))
        item = self.feedback_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "账号"))
        item = self.feedback_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "昵称"))
        item = self.feedback_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "提交时间"))
        item = self.feedback_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "反馈类型"))
        item = self.feedback_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "反馈内容"))
        item = self.feedback_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "联系方式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_feedback), _translate("Form", "用户反馈"))
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
import my_images_rc
