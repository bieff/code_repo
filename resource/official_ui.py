# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'official.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(766, 458)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.school_label = QtWidgets.QLabel(Form)
        self.school_label.setMinimumSize(QtCore.QSize(0, 120))
        self.school_label.setStyleSheet("QLabel{\n"
"    border-image: url(:/official/images/school.png);\n"
"}")
        self.school_label.setText("")
        self.school_label.setObjectName("school_label")
        self.verticalLayout.addWidget(self.school_label)
        self.beijing_label = QtWidgets.QLabel(Form)
        self.beijing_label.setMinimumSize(QtCore.QSize(730, 50))
        self.beijing_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.beijing_label.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"微软雅黑\";\n"
"    background-color: rgb(170, 170, 255);\n"
"}")
        self.beijing_label.setObjectName("beijing_label")
        self.verticalLayout.addWidget(self.beijing_label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(730, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:red;\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/official/images/qqqun_code.jpg);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-image: url(:/official/images/weixin_code.jpg);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-image: url(:/official/images/wechat_code.jpg);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border-image: url(:/official/images/weibo_code.png);\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:blue;\n"
"    border:none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/official/images/qq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:blue;\n"
"    border:none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/official/images/WeChat_public.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:blue;\n"
"    border:none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/official/images/wechat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:blue;\n"
"    border:none;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/official/images/weibo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.beijing_label.setText(_translate("Form", "项目开发背景：江西中医药大学计算机学院本科毕业设计作品"))
        self.label_5.setText(_translate("Form", "扫一扫，了解更多信息"))
        self.pushButton_5.setText(_translate("Form", "QQ交流群"))
        self.pushButton_6.setText(_translate("Form", "微信公众号"))
        self.pushButton_7.setText(_translate("Form", "微信"))
        self.pushButton_8.setText(_translate("Form", "微博"))
import my_images_rc
