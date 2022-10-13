# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personcard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(312, 400)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.help_btn = QtWidgets.QPushButton(self.widget)
        self.help_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.help_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        self.help_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.help_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/personcard/images/guide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_btn.setIcon(icon)
        self.help_btn.setIconSize(QtCore.QSize(30, 30))
        self.help_btn.setObjectName("help_btn")
        self.gridLayout_2.addWidget(self.help_btn, 8, 0, 1, 1)
        self.line2_label = QtWidgets.QLabel(self.widget)
        self.line2_label.setMinimumSize(QtCore.QSize(312, 1))
        self.line2_label.setMaximumSize(QtCore.QSize(312, 1))
        self.line2_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line2_label.setText("")
        self.line2_label.setObjectName("line2_label")
        self.gridLayout_2.addWidget(self.line2_label, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.grade_btn = QtWidgets.QPushButton(self.widget)
        self.grade_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.grade_btn.setMaximumSize(QtCore.QSize(40, 20))
        self.grade_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.grade_btn.setStyleSheet("QPushButton#grade_btn{\n"
"    border:none;\n"
"    border-image: url(:/personcard/images/user_level6.png);\n"
"}")
        self.grade_btn.setText("")
        self.grade_btn.setObjectName("grade_btn")
        self.horizontalLayout_5.addWidget(self.grade_btn)
        self.experience_label = QtWidgets.QLabel(self.widget)
        self.experience_label.setMinimumSize(QtCore.QSize(180, 30))
        self.experience_label.setMaximumSize(QtCore.QSize(180, 30))
        self.experience_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.experience_label.setObjectName("experience_label")
        self.horizontalLayout_5.addWidget(self.experience_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.experience_progressBar = QtWidgets.QProgressBar(self.widget)
        self.experience_progressBar.setMinimumSize(QtCore.QSize(0, 6))
        self.experience_progressBar.setMaximumSize(QtCore.QSize(16777215, 6))
        self.experience_progressBar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.experience_progressBar.setStyleSheet("QProgressBar{\n"
"    border: 1px solid lightgray;\n"
"    border-radius:5px;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\n"
"}\n"
"\n"
"")
        self.experience_progressBar.setMaximum(10000)
        self.experience_progressBar.setProperty("value", 666)
        self.experience_progressBar.setTextVisible(False)
        self.experience_progressBar.setFormat("")
        self.experience_progressBar.setObjectName("experience_progressBar")
        self.verticalLayout.addWidget(self.experience_progressBar)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.line1_label = QtWidgets.QLabel(self.widget)
        self.line1_label.setMinimumSize(QtCore.QSize(312, 1))
        self.line1_label.setMaximumSize(QtCore.QSize(312, 1))
        self.line1_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line1_label.setText("")
        self.line1_label.setObjectName("line1_label")
        self.gridLayout_2.addWidget(self.line1_label, 1, 0, 1, 1)
        self.switch_btn = QtWidgets.QPushButton(self.widget)
        self.switch_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.switch_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        self.switch_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.switch_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/personcard/images/switch .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.switch_btn.setIcon(icon1)
        self.switch_btn.setIconSize(QtCore.QSize(30, 30))
        self.switch_btn.setObjectName("switch_btn")
        self.gridLayout_2.addWidget(self.switch_btn, 10, 0, 1, 1)
        self.logout_btn = QtWidgets.QPushButton(self.widget)
        self.logout_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.logout_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        self.logout_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logout_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/personcard/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn.setIcon(icon2)
        self.logout_btn.setIconSize(QtCore.QSize(30, 30))
        self.logout_btn.setObjectName("logout_btn")
        self.gridLayout_2.addWidget(self.logout_btn, 11, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.touxiang_btn = QtWidgets.QPushButton(self.widget)
        self.touxiang_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.touxiang_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.touxiang_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.touxiang_btn.setStyleSheet("QPushButton#touxiang_btn{\n"
"    border-radius:25px;\n"
"    border-image: url(:/personcard/images/201601033017.ico);\n"
"}")
        self.touxiang_btn.setText("")
        self.touxiang_btn.setObjectName("touxiang_btn")
        self.horizontalLayout_4.addWidget(self.touxiang_btn)
        self.username_label = QtWidgets.QLabel(self.widget)
        self.username_label.setMinimumSize(QtCore.QSize(120, 30))
        self.username_label.setMaximumSize(QtCore.QSize(120, 30))
        self.username_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout_4.addWidget(self.username_label)
        self.sign_btn = QtWidgets.QPushButton(self.widget)
        self.sign_btn.setMinimumSize(QtCore.QSize(80, 25))
        self.sign_btn.setMaximumSize(QtCore.QSize(80, 25))
        self.sign_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/personcard/images/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sign_btn.setIcon(icon3)
        self.sign_btn.setObjectName("sign_btn")
        self.horizontalLayout_4.addWidget(self.sign_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.line3_label = QtWidgets.QLabel(self.widget)
        self.line3_label.setMinimumSize(QtCore.QSize(312, 1))
        self.line3_label.setMaximumSize(QtCore.QSize(312, 1))
        self.line3_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line3_label.setText("")
        self.line3_label.setObjectName("line3_label")
        self.gridLayout_2.addWidget(self.line3_label, 6, 0, 1, 1)
        self.line4_label = QtWidgets.QLabel(self.widget)
        self.line4_label.setMinimumSize(QtCore.QSize(312, 1))
        self.line4_label.setMaximumSize(QtCore.QSize(312, 1))
        self.line4_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line4_label.setText("")
        self.line4_label.setObjectName("line4_label")
        self.gridLayout_2.addWidget(self.line4_label, 9, 0, 1, 1)
        self.accountad_btn = QtWidgets.QPushButton(self.widget)
        self.accountad_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.accountad_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        self.accountad_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.accountad_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/personcard/images/account_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountad_btn.setIcon(icon4)
        self.accountad_btn.setIconSize(QtCore.QSize(30, 30))
        self.accountad_btn.setAutoRepeat(False)
        self.accountad_btn.setObjectName("accountad_btn")
        self.gridLayout_2.addWidget(self.accountad_btn, 4, 0, 1, 1)
        self.bind_btn = QtWidgets.QPushButton(self.widget)
        self.bind_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.bind_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        self.bind_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bind_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/personcard/images/bind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bind_btn.setIcon(icon5)
        self.bind_btn.setIconSize(QtCore.QSize(30, 30))
        self.bind_btn.setObjectName("bind_btn")
        self.gridLayout_2.addWidget(self.bind_btn, 5, 0, 1, 1)
        self.language_btn = QtWidgets.QPushButton(self.widget)
        self.language_btn.setMinimumSize(QtCore.QSize(312, 42))
        self.language_btn.setMaximumSize(QtCore.QSize(312, 42))
        self.language_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.language_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(159, 159, 159);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/personcard/images/language.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.language_btn.setIcon(icon6)
        self.language_btn.setIconSize(QtCore.QSize(30, 30))
        self.language_btn.setObjectName("language_btn")
        self.gridLayout_2.addWidget(self.language_btn, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.actionCN = QtWidgets.QAction(Form)
        self.actionCN.setObjectName("actionCN")
        self.actionEN = QtWidgets.QAction(Form)
        self.actionEN.setObjectName("actionEN")

        self.retranslateUi(Form)
        self.touxiang_btn.clicked.connect(Form.show_usermanagement_pane)
        self.sign_btn.clicked.connect(Form.sign_click)
        self.accountad_btn.clicked.connect(Form.show_usermanagement_pane)
        self.help_btn.clicked.connect(Form.show_guide_pane)
        self.switch_btn.clicked.connect(Form.switch_account)
        self.logout_btn.clicked.connect(Form.logout)
        self.bind_btn.clicked.connect(Form.bind_other)
        self.language_btn.clicked.connect(Form.show_language_menu)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.help_btn.setText(_translate("Form", "使用帮助"))
        self.experience_label.setText(_translate("Form", "经验值：999999/10000000"))
        self.switch_btn.setText(_translate("Form", "切换账号"))
        self.logout_btn.setText(_translate("Form", "退出登录"))
        self.username_label.setText(_translate("Form", "夜晓希声"))
        self.sign_btn.setText(_translate("Form", "签到"))
        self.accountad_btn.setText(_translate("Form", "账号中心"))
        self.bind_btn.setText(_translate("Form", "社交账号"))
        self.language_btn.setText(_translate("Form", "语言设置"))
        self.actionCN.setText(_translate("Form", "CN"))
        self.actionCN.setToolTip(_translate("Form", "中文"))
        self.actionEN.setText(_translate("Form", "EN"))
        self.actionEN.setToolTip(_translate("Form", "英文"))
import my_images_rc
