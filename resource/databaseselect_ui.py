# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databaseselect.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 240)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(168, 168, 252);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(722, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.close_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border-image: url(:/editor/images/select_close.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addWidget(self.widget)
        self.data_tableWidget = QtWidgets.QTableWidget(Form)
        self.data_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.data_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.data_tableWidget.setObjectName("data_tableWidget")
        self.data_tableWidget.setColumnCount(0)
        self.data_tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.data_tableWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        self.close_btn.clicked.connect(Form.close_btn_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import my_images_rc
