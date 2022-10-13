# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guide.ui'
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
        self.widget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.guide_label = QtWidgets.QLabel(self.widget)
        self.guide_label.setMinimumSize(QtCore.QSize(700, 0))
        self.guide_label.setStyleSheet("QLabel{\n"
"    font: 12pt \"微软雅黑\";\n"
"}")
        self.guide_label.setText("")
        self.guide_label.setWordWrap(True)
        self.guide_label.setObjectName("guide_label")
        self.horizontalLayout_2.addWidget(self.guide_label)
        spacerItem1 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pre_btn = QtWidgets.QPushButton(self.widget_2)
        self.pre_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.pre_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.pre_btn.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-image: url(:/guide/images/pre.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}")
        self.pre_btn.setText("")
        self.pre_btn.setObjectName("pre_btn")
        self.verticalLayout_2.addWidget(self.pre_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.guide_stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.guide_stackedWidget.setObjectName("guide_stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/login.png);\n"
"}")
        self.page1.setObjectName("page1")
        self.guide_stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/register.png);\n"
"}")
        self.page2.setObjectName("page2")
        self.guide_stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/mainwindow.png);\n"
"}")
        self.page3.setObjectName("page3")
        self.guide_stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/script.png);\n"
"}")
        self.page4.setObjectName("page4")
        self.guide_stackedWidget.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/tablepic.png);\n"
"}")
        self.page5.setObjectName("page5")
        self.guide_stackedWidget.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/management.png);\n"
"}")
        self.page6.setObjectName("page6")
        self.guide_stackedWidget.addWidget(self.page6)
        self.page7 = QtWidgets.QWidget()
        self.page7.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/article.png);\n"
"}")
        self.page7.setObjectName("page7")
        self.guide_stackedWidget.addWidget(self.page7)
        self.page8 = QtWidgets.QWidget()
        self.page8.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/information.png);\n"
"}")
        self.page8.setObjectName("page8")
        self.guide_stackedWidget.addWidget(self.page8)
        self.page9 = QtWidgets.QWidget()
        self.page9.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/official.png);\n"
"}")
        self.page9.setObjectName("page9")
        self.guide_stackedWidget.addWidget(self.page9)
        self.page10 = QtWidgets.QWidget()
        self.page10.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/personcard.png);\n"
"}")
        self.page10.setObjectName("page10")
        self.guide_stackedWidget.addWidget(self.page10)
        self.page11 = QtWidgets.QWidget()
        self.page11.setStyleSheet("QWidget{\n"
"    border-image: url(:/guide/images/skinpic.png);\n"
"}")
        self.page11.setObjectName("page11")
        self.guide_stackedWidget.addWidget(self.page11)
        self.horizontalLayout.addWidget(self.guide_stackedWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.next_btn = QtWidgets.QPushButton(self.widget_2)
        self.next_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.next_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.next_btn.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-image: url(:/guide/images/next.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}")
        self.next_btn.setText("")
        self.next_btn.setObjectName("next_btn")
        self.verticalLayout_3.addWidget(self.next_btn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(Form)
        self.guide_stackedWidget.setCurrentIndex(0)
        self.pre_btn.clicked.connect(Form.pre_btn_clicked)
        self.next_btn.clicked.connect(Form.next_btn_clicked)
        self.guide_stackedWidget.currentChanged['int'].connect(Form.page_change)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import my_images_rc
