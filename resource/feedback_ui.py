# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 420)
        Form.setMinimumSize(QtCore.QSize(320, 420))
        Form.setMaximumSize(QtCore.QSize(340, 420))
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(185, 185, 185);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 0, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_btn = QtWidgets.QPushButton(Form)
        self.icon_btn.setEnabled(True)
        self.icon_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.icon_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.icon_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feedback/images/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_btn.setIcon(icon)
        self.icon_btn.setIconSize(QtCore.QSize(60, 30))
        self.icon_btn.setObjectName("icon_btn")
        self.horizontalLayout_3.addWidget(self.icon_btn)
        spacerItem = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.close_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/feedback/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QtCore.QSize(30, 30))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line1_label = QtWidgets.QLabel(Form)
        self.line1_label.setMinimumSize(QtCore.QSize(320, 1))
        self.line1_label.setMaximumSize(QtCore.QSize(320, 1))
        self.line1_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line1_label.setText("")
        self.line1_label.setObjectName("line1_label")
        self.verticalLayout.addWidget(self.line1_label)
        self.chose_label = QtWidgets.QLabel(Form)
        self.chose_label.setMinimumSize(QtCore.QSize(0, 30))
        self.chose_label.setStyleSheet("QLabel{\n"
"    font: 11pt \"微软雅黑\";\n"
"}")
        self.chose_label.setObjectName("chose_label")
        self.verticalLayout.addWidget(self.chose_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.advice_rbtn = QtWidgets.QRadioButton(Form)
        self.advice_rbtn.setMinimumSize(QtCore.QSize(90, 20))
        self.advice_rbtn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.advice_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.advice_rbtn.setChecked(True)
        self.advice_rbtn.setObjectName("advice_rbtn")
        self.horizontalLayout_2.addWidget(self.advice_rbtn)
        self.program_rbtn = QtWidgets.QRadioButton(Form)
        self.program_rbtn.setMinimumSize(QtCore.QSize(90, 20))
        self.program_rbtn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.program_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.program_rbtn.setObjectName("program_rbtn")
        self.horizontalLayout_2.addWidget(self.program_rbtn)
        self.data_rbtn = QtWidgets.QRadioButton(Form)
        self.data_rbtn.setMinimumSize(QtCore.QSize(90, 20))
        self.data_rbtn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.data_rbtn.setStyleSheet("QRadioButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.data_rbtn.setObjectName("data_rbtn")
        self.horizontalLayout_2.addWidget(self.data_rbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 200))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    border-radius:5px;\n"
"    font: 12pt \"宋体\";\n"
"    font-size:16px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.phone_lineEdit = QtWidgets.QLineEdit(Form)
        self.phone_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.phone_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius:5px;\n"
"    font-size:16px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.verticalLayout.addWidget(self.phone_lineEdit)
        self.line2_label = QtWidgets.QLabel(Form)
        self.line2_label.setMinimumSize(QtCore.QSize(320, 1))
        self.line2_label.setMaximumSize(QtCore.QSize(320, 1))
        self.line2_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"}")
        self.line2_label.setText("")
        self.line2_label.setObjectName("line2_label")
        self.verticalLayout.addWidget(self.line2_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_btn = QtWidgets.QPushButton(Form)
        self.send_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.send_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.send_btn.setStyleSheet("QPushButton {\n"
"    font-size:14px;\n"
"    background-color:rgb(33,174,250);\n"
"    border-radius:5px;\n"
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
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout.addWidget(self.send_btn)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.cancel_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.cancel_btn.setStyleSheet("QPushButton {\n"
"    font-size:14px;\n"
"    border-radius:5px;\n"
"    border:2px solid gray;\n"
"    color:black;\n"
"    spacing:20px;\n"
"}\n"
"")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.close_btn.clicked.connect(Form.feedback_close)
        self.send_btn.clicked.connect(Form.feedback_send)
        self.cancel_btn.clicked.connect(Form.feedback_cancel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.icon_btn.setText(_translate("Form", "意见反馈"))
        self.close_btn.setToolTip(_translate("Form", "关闭"))
        self.chose_label.setText(_translate("Form", "选择反馈类型"))
        self.advice_rbtn.setText(_translate("Form", "产品建议"))
        self.program_rbtn.setText(_translate("Form", "程序报错"))
        self.data_rbtn.setText(_translate("Form", "数据错误"))
        self.phone_lineEdit.setPlaceholderText(_translate("Form", "你的联系方式(QQ/邮箱/手机)，可不填"))
        self.send_btn.setText(_translate("Form", "发送"))
        self.cancel_btn.setText(_translate("Form", "取消"))
import my_images_rc
