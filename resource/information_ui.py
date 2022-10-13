# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 450)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_btn = QtWidgets.QPushButton(Form)
        self.icon_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.icon_btn.setMaximumSize(QtCore.QSize(80, 80))
        self.icon_btn.setStyleSheet("QPushButton{\n"
"    border-radius:40px;\n"
"    border:none;\n"
"    border-image: url(:/information/images/syc.ico);\n"
"}")
        self.icon_btn.setText("")
        self.icon_btn.setObjectName("icon_btn")
        self.horizontalLayout_4.addWidget(self.icon_btn)
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setMinimumSize(QtCore.QSize(650, 0))
        self.name_label.setStyleSheet("QLabel{\n"
"    font: 28pt \"楷体\";\n"
"    color: rgb(0, 170, 255);\n"
"}")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_4.addWidget(self.name_label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setMinimumSize(QtCore.QSize(320, 50))
        self.version_label.setMaximumSize(QtCore.QSize(320, 50))
        self.version_label.setStyleSheet("QLabel{\n"
"    \n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.version_label.setObjectName("version_label")
        self.horizontalLayout_3.addWidget(self.version_label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.check_version_btn = QtWidgets.QPushButton(Form)
        self.check_version_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.check_version_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.check_version_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.check_version_btn.setObjectName("check_version_btn")
        self.horizontalLayout_3.addWidget(self.check_version_btn)
        self.feedback_btn = QtWidgets.QPushButton(Form)
        self.feedback_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.feedback_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.feedback_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.feedback_btn.setObjectName("feedback_btn")
        self.horizontalLayout_3.addWidget(self.feedback_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auto_rbtn = QtWidgets.QRadioButton(Form)
        self.auto_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.auto_rbtn.setChecked(True)
        self.auto_rbtn.setObjectName("auto_rbtn")
        self.verticalLayout.addWidget(self.auto_rbtn)
        self.remain_rbtn = QtWidgets.QRadioButton(Form)
        self.remain_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.remain_rbtn.setObjectName("remain_rbtn")
        self.verticalLayout.addWidget(self.remain_rbtn)
        self.autologin_checkBox = QtWidgets.QCheckBox(Form)
        self.autologin_checkBox.setStyleSheet("QCheckBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.autologin_checkBox.setObjectName("autologin_checkBox")
        self.verticalLayout.addWidget(self.autologin_checkBox)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("QLabel{\n"
"    \n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.windows_btn = QtWidgets.QPushButton(Form)
        self.windows_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.windows_btn.setMaximumSize(QtCore.QSize(120, 40))
        self.windows_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/information/images/Windows.jpg);\n"
"}")
        self.windows_btn.setText("")
        self.windows_btn.setObjectName("windows_btn")
        self.horizontalLayout.addWidget(self.windows_btn)
        self.linux_btn = QtWidgets.QPushButton(Form)
        self.linux_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.linux_btn.setMaximumSize(QtCore.QSize(120, 40))
        self.linux_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/information/images/Linux.jpg);\n"
"}")
        self.linux_btn.setText("")
        self.linux_btn.setObjectName("linux_btn")
        self.horizontalLayout.addWidget(self.linux_btn)
        self.mac_btn = QtWidgets.QPushButton(Form)
        self.mac_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.mac_btn.setMaximumSize(QtCore.QSize(120, 40))
        self.mac_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/information/images/Mac.jpg);\n"
"}")
        self.mac_btn.setText("")
        self.mac_btn.setObjectName("mac_btn")
        self.horizontalLayout.addWidget(self.mac_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.official_btn = QtWidgets.QPushButton(Form)
        self.official_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.official_btn.setMaximumSize(QtCore.QSize(120, 30))
        self.official_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-bottom:1px solid gray;\n"
"    font: 10pt \"微软雅黑\";\n"
"    color:blue;\n"
"}")
        self.official_btn.setObjectName("official_btn")
        self.horizontalLayout_2.addWidget(self.official_btn)
        self.handbook_btn = QtWidgets.QPushButton(Form)
        self.handbook_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.handbook_btn.setMaximumSize(QtCore.QSize(120, 30))
        self.handbook_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-bottom:1px solid gray;\n"
"    font: 10pt \"微软雅黑\";\n"
"    color:blue;\n"
"}")
        self.handbook_btn.setObjectName("handbook_btn")
        self.horizontalLayout_2.addWidget(self.handbook_btn)
        self.server_btn = QtWidgets.QPushButton(Form)
        self.server_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.server_btn.setMaximumSize(QtCore.QSize(120, 30))
        self.server_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-bottom:1px solid gray;\n"
"    font: 10pt \"微软雅黑\";\n"
"    color:blue;\n"
"}")
        self.server_btn.setObjectName("server_btn")
        self.horizontalLayout_2.addWidget(self.server_btn)
        self.policy_btn = QtWidgets.QPushButton(Form)
        self.policy_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.policy_btn.setMaximumSize(QtCore.QSize(120, 30))
        self.policy_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-bottom:1px solid gray;\n"
"    font: 10pt \"微软雅黑\";\n"
"    color:blue;\n"
"}")
        self.policy_btn.setObjectName("policy_btn")
        self.horizontalLayout_2.addWidget(self.policy_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.copyright_label = QtWidgets.QLabel(Form)
        self.copyright_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.copyright_label.setObjectName("copyright_label")
        self.verticalLayout_2.addWidget(self.copyright_label)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 1, 1)

        self.retranslateUi(Form)
        self.check_version_btn.clicked.connect(Form.check_version)
        self.feedback_btn.clicked.connect(Form.show_feedback)
        self.official_btn.clicked.connect(Form.official_web_link)
        self.handbook_btn.clicked.connect(Form.user_handbook_link)
        self.server_btn.clicked.connect(Form.server_link)
        self.policy_btn.clicked.connect(Form.privacy_policy_link)
        self.autologin_checkBox.clicked['bool'].connect(Form.auto_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_label.setText(_translate("Form", "中药精油靶点数据库"))
        self.version_label.setText(_translate("Form", "当前版本：1.1.0 (Build:20200510)"))
        self.check_version_btn.setText(_translate("Form", "检查更新"))
        self.feedback_btn.setText(_translate("Form", "意见反馈"))
        self.auto_rbtn.setText(_translate("Form", "自动更新"))
        self.remain_rbtn.setText(_translate("Form", "有新版本时提醒我"))
        self.autologin_checkBox.setText(_translate("Form", "自动登录"))
        self.label_5.setText(_translate("Form", "客户端下载："))
        self.official_btn.setText(_translate("Form", "《XXX官网》"))
        self.handbook_btn.setText(_translate("Form", "《用户管理手册》"))
        self.server_btn.setText(_translate("Form", "《服务条款》"))
        self.policy_btn.setText(_translate("Form", "《隐私政策》"))
        self.copyright_label.setText(_translate("Form", "版权公告：2020-2026 夜晓希声 版权所有  Copyright© 2020Aixili,Inc.All right reserved."))
import my_images_rc
