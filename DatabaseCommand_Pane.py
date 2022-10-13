# 数据库命令行操作界面，调用生成的databasecommand_ui.py文件
import re
import pymysql
from PyQt5.Qt import *
from PyQt5 import QtGui, QtWidgets
from resource.databasecommand_ui import Ui_MainWindow
from DatabaseSelect_Pane import DatabaseSelectPane
from Editor import QCodeEditor, SqlHighlighter
class DatabaseCommandPane(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DatabaseCommandPane, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.user_account = "201601033017"  # 当前账号
        # 显示查询结果的表格
        self.databaseSelectPane = DatabaseSelectPane(self)
        self.databaseSelectPane.setVisible(False)

        self.editor_splitter = QSplitter(self.centralwidget)
        self.verticalLayout.addWidget(self.editor_splitter)
        self.verticalLayout.setStretch(0, 10)
        self.editor_splitter.addWidget(self.widget_4)
        self.editor_splitter.addWidget(self.widget_5)
        self.editor_splitter.setOrientation(Qt.Vertical)
        self.editor_splitter.setSizes([self.editor_splitter.height()/4*3, self.editor_splitter.height()/4])
        self.editor_splitter.setOpaqueResize(False)
        self.editor_splitter.setCollapsible(0, False)
        self.editor_splitter.setCollapsible(1, False)

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionSaveAs.triggered.connect(self.fileSaveAs)
        self.actionPrint.triggered.connect(self.filePrint)
        self.actionUndo.triggered.connect(self.fileUndo)
        self.actionRedo.triggered.connect(self.fileRedo)
        self.actionShear.triggered.connect(self.fileShear)
        self.actionCopy.triggered.connect(self.fileCopy)
        self.actionPaste.triggered.connect(self.filePaste)
        self.actionDelete.triggered.connect(self.fileDelete)
        self.actionFind.triggered.connect(self.fileFind)
        self.actionChange.triggered.connect(self.fileChange)
        self.actionSelectAll.triggered.connect(self.fileSelectAll)
        self.actionHelp.triggered.connect(self.fileHelp)
        self.actionAbout.triggered.connect(self.fileAbout)
        self.actionT_New.triggered.connect(self.fileNew)
        self.actionT_Open.triggered.connect(self.fileOpen)
        self.actionT_Save.triggered.connect(self.fileSave)
        self.actionT_Copy.triggered.connect(self.fileCopy)
        self.actionT_Paste.triggered.connect(self.filePaste)
        self.actionT_Shear.triggered.connect(self.fileShear)
        self.actionT_Undo.triggered.connect(self.fileUndo)
        self.actionT_Redo.triggered.connect(self.fileRedo)
        self.actionT_Bold.triggered.connect(self.fileBold)
        self.actionT_Incline.triggered.connect(self.fileIncline)
        self.actionT_Underline.triggered.connect(self.fileUnderline)
        self.actionT_Lower2upper.triggered.connect(self.fileLower2upper)
        self.actionT_Upper2lower.triggered.connect(self.fileUpper2lower)
        self.actionaT_Alignleft.triggered.connect(self.fileAlignleft)
        self.actionaT_Aligncenter.triggered.connect(self.fileAligncenter)
        self.actionaT_Alignright.triggered.connect(self.fileAlignright)
        self.actionT_Font.triggered.connect(self.fileFont)
        self.actionT_Color.triggered.connect(self.fileColor)
        self.actionT_Pattern.triggered.connect(self.patternSwitch)
        self.actionT_Execution.triggered.connect(self.sqlExecution)

        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        self.tabWidget.setStyleSheet("QTabWidget::pane{ border: none;}\n"
                                     "QTabWidget::tab-bar{background:transparent;}\n"
                                     "QTabBar::tab{background:transparent;}\n"
                                     "QTabBar::tab:selected{background-color:white;color: blue;}\n"
                                     "QTabBar::tab:!selected{ background-color: lightgray;}\n"
                                     "QTabBar::tab:hover{color: rgb(36,197,219);background:transparent;}")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.tabCloseRequested['int'].connect(self.tab_close)
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/editor/images/sqlscript.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.console_textEdit = QtWidgets.QTextEdit(self.widget_5)
        self.console_textEdit.setStyleSheet(
            "QTextEdit{background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
        self.console_textEdit.setReadOnly(True)
        self.console_textEdit.setObjectName("console_textEdit")
        self.verticalLayout_3.addWidget(self.console_textEdit)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.sql_textEdit_qss = "QTextEdit{background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightblue;}"
        self.create_tab_1()
        self.create_tab_2()
        self.create_tab_3()
        self.create_tab_4()
        self.create_tab_5()
        self.currentFilename = None # 当前文件名
        self.tabList = [self.tab_1, self.tab_2, self.tab_3, self.tab_4, self.tab_5]  # 可创建选项卡列表，暂时限制最多创建5个
        self.sql_textEditList = [self.sql_textEdit_tab_1, self.sql_textEdit_tab_2, self.sql_textEdit_tab_3, self.sql_textEdit_tab_4, self.sql_textEdit_tab_5]  # 可创建文本编辑区列表，暂时限制最多创建5个
        self.filenameDict = dict()  # 已打开文件字典，暂时限制最多创建5个
        self.newFile_num = 0 # 当前已经打开的新建文件个数

    def create_tab_1(self):
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1.setStyleSheet("QWidget{background-color: white;}")
        self.verticalLayout_tab_1 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_tab_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_1.setSpacing(0)
        self.verticalLayout_tab_1.setObjectName("verticalLayout_tab_1")
        self.sql_textEdit_tab_1 = QCodeEditor()
        self.sql_textEdit_tab_1.setStyleSheet(self.sql_textEdit_qss)
        self.sql_textEdit_tab_1.setObjectName("sql_textEdit_tab_1")
        self.verticalLayout_tab_1.addWidget(self.sql_textEdit_tab_1)

    def create_tab_2(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("QWidget{background-color: white;}")
        self.verticalLayout_tab_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_tab_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_2.setSpacing(0)
        self.verticalLayout_tab_2.setObjectName("verticalLayout_tab_2")
        self.sql_textEdit_tab_2 = QCodeEditor()
        self.sql_textEdit_tab_2.setStyleSheet(self.sql_textEdit_qss)
        self.sql_textEdit_tab_2.setObjectName("sql_textEdit_tab_2")
        self.verticalLayout_tab_2.addWidget(self.sql_textEdit_tab_2)

    def create_tab_3(self):
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setStyleSheet("QWidget{background-color: white;}")
        self.verticalLayout_tab_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_tab_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_3.setSpacing(0)
        self.verticalLayout_tab_3.setObjectName("verticalLayout_tab_3")
        self.sql_textEdit_tab_3 = QCodeEditor()
        self.sql_textEdit_tab_3.setStyleSheet(self.sql_textEdit_qss)
        self.sql_textEdit_tab_3.setObjectName("sql_textEdit_tab_3")
        self.verticalLayout_tab_3.addWidget(self.sql_textEdit_tab_3)

    def create_tab_4(self):
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tab_4.setStyleSheet("QWidget{background-color: white;}")
        self.verticalLayout_tab_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_tab_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_4.setSpacing(0)
        self.verticalLayout_tab_4.setObjectName("verticalLayout_tab_4")
        self.sql_textEdit_tab_4 = QCodeEditor()
        self.sql_textEdit_tab_4.setStyleSheet(self.sql_textEdit_qss)
        self.sql_textEdit_tab_4.setObjectName("sql_textEdit_tab_4")
        self.verticalLayout_tab_4.addWidget(self.sql_textEdit_tab_4)

    def create_tab_5(self):
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab_5.setStyleSheet("QWidget{background-color: white;}")
        self.verticalLayout_tab_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_tab_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_5.setSpacing(0)
        self.verticalLayout_tab_5.setObjectName("verticalLayout_tab_5")
        self.sql_textEdit_tab_5 = QCodeEditor()
        self.sql_textEdit_tab_5.setStyleSheet(self.sql_textEdit_qss)
        self.sql_textEdit_tab_5.setObjectName("sql_textEdit_tab_5")
        self.verticalLayout_tab_5.addWidget(self.sql_textEdit_tab_5)

    # 判定此时哪个选项卡被选中
    def choose_judge(self):
        if self.tabWidget.currentWidget().objectName() == "tab_1":
            return 1
        elif self.tabWidget.currentWidget().objectName() == "tab_2":
            return 2
        elif self.tabWidget.currentWidget().objectName() == "tab_3":
            return 3
        elif self.tabWidget.currentWidget().objectName() == "tab_4":
            return 4
        elif self.tabWidget.currentWidget().objectName() == "tab_5":
            return 5

    def get_currentFileName(self, str):
        self.currentFilename = list(self.filenameDict.keys())[list(self.filenameDict.values()).index(str)]

    def tab_close(self, int):
        if self.tabWidget.count() == 1:
            # 此时只剩一个选项卡，执行关闭操作后就没有选项卡了，因此把self.newFile_num初始化
            self.newFile_num = 0
        self.tabWidget.setCurrentIndex(int)
        current_tab = self.choose_judge()
        if current_tab == 1:
            current_tab_index = self.tabList.index(self.tab_1)
            current_sql_textEdit_index = self.sql_textEditList.index(self.sql_textEdit_tab_1)
            del self.tab_1
            self.create_tab_1()
            self.tabList.pop(current_tab_index)
            self.tabList.insert(current_tab_index, self.tab_1)
            self.sql_textEditList.pop(current_sql_textEdit_index)
            self.sql_textEditList.insert(current_sql_textEdit_index, self.sql_textEdit_tab_1)
            self.tabList.insert(0, self.tabList.pop(current_tab_index))
            self.sql_textEditList.insert(0, self.sql_textEditList.pop(current_sql_textEdit_index))
            self.get_currentFileName("self.tab_1")
            del self.filenameDict[self.currentFilename]
        elif current_tab == 2:
            current_tab_index = self.tabList.index(self.tab_2)
            current_sql_textEdit_index = self.sql_textEditList.index(self.sql_textEdit_tab_2)
            del self.tab_2
            self.create_tab_2()
            self.tabList.pop(current_tab_index)
            self.tabList.insert(current_tab_index, self.tab_2)
            self.sql_textEditList.pop(current_sql_textEdit_index)
            self.sql_textEditList.insert(current_sql_textEdit_index, self.sql_textEdit_tab_2)
            self.tabList.insert(0, self.tabList.pop(current_tab_index))
            self.sql_textEditList.insert(0, self.sql_textEditList.pop(current_sql_textEdit_index))
            self.get_currentFileName("self.tab_2")
            del self.filenameDict[self.currentFilename]
        elif current_tab == 3:
            current_tab_index = self.tabList.index(self.tab_3)
            current_sql_textEdit_index = self.sql_textEditList.index(self.sql_textEdit_tab_3)
            del self.tab_3
            self.create_tab_3()
            self.tabList.pop(current_tab_index)
            self.tabList.insert(current_tab_index, self.tab_3)
            self.sql_textEditList.pop(current_sql_textEdit_index)
            self.sql_textEditList.insert(current_sql_textEdit_index, self.sql_textEdit_tab_3)
            self.tabList.insert(0, self.tabList.pop(current_tab_index))
            self.sql_textEditList.insert(0, self.sql_textEditList.pop(current_sql_textEdit_index))
            self.get_currentFileName("self.tab_3")
            del self.filenameDict[self.currentFilename]
        elif current_tab == 4:
            current_tab_index = self.tabList.index(self.tab_4)
            current_sql_textEdit_index = self.sql_textEditList.index(self.sql_textEdit_tab_4)
            del self.tab_4
            self.create_tab_4()
            self.tabList.pop(current_tab_index)
            self.tabList.insert(current_tab_index, self.tab_4)
            self.sql_textEditList.pop(current_sql_textEdit_index)
            self.sql_textEditList.insert(current_sql_textEdit_index, self.sql_textEdit_tab_4)
            self.tabList.insert(0, self.tabList.pop(current_tab_index))
            self.sql_textEditList.insert(0, self.sql_textEditList.pop(current_sql_textEdit_index))
            self.get_currentFileName("self.tab_4")
            del self.filenameDict[self.currentFilename]
        elif current_tab == 5:
            current_tab_index = self.tabList.index(self.tab_5)
            current_sql_textEdit_index = self.sql_textEditList.index(self.sql_textEdit_tab_5)
            del self.tab_5
            self.create_tab_5()
            self.tabList.pop(current_tab_index)
            self.tabList.insert(current_tab_index, self.tab_5)
            self.sql_textEditList.pop(current_sql_textEdit_index)
            self.sql_textEditList.insert(current_sql_textEdit_index, self.sql_textEdit_tab_5)
            self.tabList.insert(0, self.tabList.pop(current_tab_index))
            self.sql_textEditList.insert(0, self.sql_textEditList.pop(current_sql_textEdit_index))
            self.get_currentFileName("self.tab_5")
            del self.filenameDict[self.currentFilename]
        self.tabWidget.removeTab(int)

    def fileNew(self):
        # print("新建文件")
        if self.tabWidget.count() == 5:
            QMessageBox.information(self, "提示", "最多允许打开5个页面", QMessageBox.Yes)
            return
        chongfu_count = 0
        # 先做一个判断，当前是否已经有一个新建文件
        for name_ in self.filenameDict:
            if re.search(r'新建*', name_) != None:
                chongfu_count = chongfu_count + 1
        if chongfu_count > self.newFile_num :
            self.newFile_num = chongfu_count
        else:
            self.newFile_num = self.newFile_num + 1
        if self.newFile_num != 0:
            new_filename = "新建" + str(self.newFile_num) + ".sql"
        else:
            new_filename = "新建.sql"
        self.tabWidget.addTab(self.tabList[0], self.icon, new_filename)
        if self.tabList[0] == self.tab_1:
            self.filenameDict[new_filename] = "self.tab_1"  # 文件名和相应的tab关联起来
        if self.tabList[0] == self.tab_2:
            self.filenameDict[new_filename] = "self.tab_2"  # 文件名和相应的tab关联起来
        if self.tabList[0] == self.tab_3:
            self.filenameDict[new_filename] = "self.tab_3"  # 文件名和相应的tab关联起来
        if self.tabList[0] == self.tab_4:
            self.filenameDict[new_filename] = "self.tab_4"  # 文件名和相应的tab关联起来
        if self.tabList[0] == self.tab_5:
            self.filenameDict[new_filename] = "self.tab_5"  # 文件名和相应的tab关联起来
        self.tabList.append(self.tabList.pop(0))
        self.sql_textEditList.append(self.sql_textEditList.pop(0))
        self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

    def fileOpen(self):
        # print("打开文件")
        if self.tabWidget.count() == 5:
            QMessageBox.information(self, "提示", "最多允许打开5个页面", QMessageBox.Yes)
            return
        # filename, ok = QFileDialog.getOpenFileName(self, "打开文件", "C:/", "All Files(*);;TXT Files(*.txt)")
        filename, ok = QFileDialog.getOpenFileName(self, "打开文件", "./resource/scripts/", "*.sql;;All Files(*)")
        if filename:
            # 先做一个判断，当前是否已经打开了文件，或者说是否想要打开的文件已经打开了
            if not filename in self.filenameDict:
                f = open(filename, "r", encoding='utf8')
                with f :
                    data = f.read()
                    self.tabWidget.addTab(self.tabList[0], self.icon, filename.split("/")[-1])
                    if self.tabList[0] == self.tab_1:
                        self.filenameDict[filename] = "self.tab_1"  # 文件名和相应的tab关联起来
                    if self.tabList[0] == self.tab_2:
                        self.filenameDict[filename] = "self.tab_2"  # 文件名和相应的tab关联起来
                    if self.tabList[0] == self.tab_3:
                        self.filenameDict[filename] = "self.tab_3"  # 文件名和相应的tab关联起来
                    if self.tabList[0] == self.tab_4:
                        self.filenameDict[filename] = "self.tab_4"  # 文件名和相应的tab关联起来
                    if self.tabList[0] == self.tab_5:
                        self.filenameDict[filename] = "self.tab_5"  # 文件名和相应的tab关联起来
                    self.tabList.append(self.tabList.pop(0))
                    self.sql_textEditList[0].setPlainText(data)
                    self.sql_textEditList.append(self.sql_textEditList.pop(0))
                    self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
                f.close()
            else:
                self.tabWidget.setCurrentWidget(self.filenameDict[filename]) # 打开了相同的文件

    def fileSave(self):
        # print("保存文件")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        textString = None
        if current_tab == 1:
            textString = self.sql_textEdit_tab_1.toPlainText()
            self.get_currentFileName("self.tab_1")
        elif current_tab == 2:
            textString = self.sql_textEdit_tab_2.toPlainText()
            self.get_currentFileName("self.tab_2")
        elif current_tab == 3:
            textString = self.sql_textEdit_tab_3.toPlainText()
            self.get_currentFileName("self.tab_3")
        elif current_tab == 4:
            textString = self.sql_textEdit_tab_4.toPlainText()
            self.get_currentFileName("self.tab_4")
        elif current_tab == 5:
            textString = self.sql_textEdit_tab_5.toPlainText()
            self.get_currentFileName("self.tab_5")
        if re.search(r'新建*', self.currentFilename) != None:
            # filename, ok = QFileDialog.getSaveFileName(self, "文件保存为", "C:/", "All Files(*);;TXT Files(*.txt)")
            filename, ok = QFileDialog.getSaveFileName(self, "文件保存为", "./resource/scripts/", "*.sql;;All Files(*)")
            if filename:
                f = open(filename, "w", encoding='utf8')
                with f:
                    f.write(textString)
                f.close()
        else:
            f = open(self.currentFilename, "w")
            with f :
                f.write(textString)
            f.close()

    def fileSaveAs(self):
        # print("文件另存为")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        filename, ok = QFileDialog.getSaveFileName(self, "文件另存为", "./resource/scripts/", "*.sql;;All Files(*)")
        if filename:
            f = open(filename, "w", encoding='utf8')
            with f :
                if current_tab == 1:
                    f.write(self.sql_textEdit_tab_1.toPlainText())
                elif current_tab == 2:
                    f.write(self.sql_textEdit_tab_2.toPlainText())
                elif current_tab == 3:
                    f.write(self.sql_textEdit_tab_3.toPlainText())
                elif current_tab == 4:
                    f.write(self.sql_textEdit_tab_4.toPlainText())
                elif current_tab == 5:
                    f.write(self.sql_textEdit_tab_5.toPlainText())
            f.close()

    def filePrint(self):
        # print("打印文件")
        printer = QPrinter()
        printdialog = QPrintDialog(printer, self)
        if printdialog.exec_():
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.img.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.img.rect)
            painter.drawImage(0, 0, self.img)

    def fileUndo(self):
        # print("撤销")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.undo()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.undo()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.undo()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.undo()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.undo()

    def fileRedo(self):
        # print("重做")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.redo()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.redo()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.redo()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.redo()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.redo()

    def fileShear(self):
        # print("剪切")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.cut()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.cut()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.cut()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.cut()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.cut()

    def fileCopy(self):
        # print("复制")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.copy()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.copy()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.copy()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.copy()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.copy()

    def filePaste(self):
        # print("粘贴")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.paste()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.paste()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.paste()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.paste()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.paste()

    def fileDelete(self):
        # print("删除")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            if self.sql_textEdit_tab_1.textCursor().hasSelection():
                self.sql_textEdit_tab_1.textCursor().removeSelectedText()
            else:
                self.sql_textEdit_tab_1.textCursor().deletePreviousChar()  # 删除光标前内容
        elif current_tab == 2:
            if self.sql_textEdit_tab_2.textCursor().hasSelection():
                self.sql_textEdit_tab_2.textCursor().removeSelectedText()
            else:
                self.sql_textEdit_tab_2.textCursor().deletePreviousChar()  # 删除光标前内容
        elif current_tab == 3:
            if self.sql_textEdit_tab_3.textCursor().hasSelection():
                self.sql_textEdit_tab_3.textCursor().removeSelectedText()
            else:
                self.sql_textEdit_tab_3.textCursor().deletePreviousChar()  # 删除光标前内容
        elif current_tab == 4:
            if self.sql_textEdit_tab_4.textCursor().hasSelection():
                self.sql_textEdit_tab_4.textCursor().removeSelectedText()
            else:
                self.sql_textEdit_tab_4.textCursor().deletePreviousChar()  # 删除光标前内容
        elif current_tab == 5:
            if self.sql_textEdit_tab_5.textCursor().hasSelection():
                self.sql_textEdit_tab_5.textCursor().removeSelectedText()
            else:
                self.sql_textEdit_tab_5.textCursor().deletePreviousChar()  # 删除光标前内容

    def fileFind(self):
        # print("查找")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        pattern, okPressed = QInputDialog.getText(self, "查找", "查找字符串:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and pattern != '':
            sub = None
            if current_tab == 1:
                sub = self.sql_textEdit_tab_1
            elif current_tab == 2:
                sub = self.sql_textEdit_tab_2
            elif current_tab == 3:
                sub = self.sql_textEdit_tab_3
            elif current_tab == 4:
                sub = self.sql_textEdit_tab_4
            elif current_tab == 5:
                sub = self.sql_textEdit_tab_5
            sub.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
            if sub.find(pattern):
                palette = sub.palette()
                palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
                sub.setPalette(palette)

    def fileChange(self):
        # print("替换")
        if self.tabWidget.count() == 0:
            return

    def fileSelectAll(self):
        # print("全选")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            self.sql_textEdit_tab_1.selectAll()
        elif current_tab == 2:
            self.sql_textEdit_tab_2.selectAll()
        elif current_tab == 3:
            self.sql_textEdit_tab_3.selectAll()
        elif current_tab == 4:
            self.sql_textEdit_tab_4.selectAll()
        elif current_tab == 5:
            self.sql_textEdit_tab_5.selectAll()

    def fileHelp(self):
        # print("帮助")
        QMessageBox.about(self, "需要帮助", "您可以前往使用帮助查询相关用法")

    def fileAbout(self):
        # print("关于")
        QMessageBox.about(self, "功能说明", "这是一个文本编辑器，可自由切换普通文本和SQL脚本两种模式")

    def fileBold(self):
        # print("粗体")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        sub = None
        if current_tab == 1:
            sub = self.sql_textEdit_tab_1
        elif current_tab == 2:
            sub = self.sql_textEdit_tab_2
        elif current_tab == 3:
            sub = self.sql_textEdit_tab_3
        elif current_tab == 4:
            sub = self.sql_textEdit_tab_4
        elif current_tab == 5:
            sub = self.sql_textEdit_tab_5
        tmpFormat = sub.currentCharFormat()
        if tmpFormat.fontWeight() == QtGui.QFont.Bold:
            tmpFormat.setFontWeight(QtGui.QFont.Normal)
        else:
            tmpFormat.setFontWeight(QtGui.QFont.Bold)
        sub.mergeCurrentCharFormat(tmpFormat)

    def fileIncline(self):
        # print("倾斜")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        tmpTextBox = None
        if current_tab == 1:
            tmpTextBox = self.sql_textEdit_tab_1
        elif current_tab == 2:
            tmpTextBox = self.sql_textEdit_tab_2
        elif current_tab == 3:
            tmpTextBox = self.sql_textEdit_tab_3
        elif current_tab == 4:
            tmpTextBox = self.sql_textEdit_tab_4
        elif current_tab == 5:
            tmpTextBox = self.sql_textEdit_tab_5
        tmpTextBox.setFontItalic(not tmpTextBox.fontItalic())

    def fileUnderline(self):
        # print("下划线")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        tmpTextBox = None
        if current_tab == 1:
            tmpTextBox = self.sql_textEdit_tab_1
        elif current_tab == 2:
            tmpTextBox = self.sql_textEdit_tab_2
        elif current_tab == 3:
            tmpTextBox = self.sql_textEdit_tab_3
        elif current_tab == 4:
            tmpTextBox = self.sql_textEdit_tab_4
        elif current_tab == 5:
            tmpTextBox = self.sql_textEdit_tab_5
        print(tmpTextBox.fontUnderline())
        tmpTextBox.setFontUnderline(not tmpTextBox.fontUnderline())

    def fileLower2upper(self):
        # print("转大写")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        new_c = []
        if current_tab == 1:
            if self.sql_textEdit_tab_1.textCursor().hasSelection():
                str = self.sql_textEdit_tab_1.textCursor().selectedText()
                for c in str:
                    if 97<= ord(c) <= 122:
                        new_c.append(chr(ord(c) - 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                # str_change = "".join(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in str)
                self.sql_textEdit_tab_1.textCursor().removeSelectedText()
                self.sql_textEdit_tab_1.textCursor().insertText(str_change)
        elif current_tab == 2:
            if self.sql_textEdit_tab_2.textCursor().hasSelection():
                str = self.sql_textEdit_tab_2.textCursor().selectedText()
                for c in str:
                    if 97 <= ord(c) <= 122:
                        new_c.append(chr(ord(c) - 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_2.textCursor().removeSelectedText()
                self.sql_textEdit_tab_2.textCursor().insertText(str_change)
        elif current_tab == 3:
            if self.sql_textEdit_tab_3.textCursor().hasSelection():
                str = self.sql_textEdit_tab_3.textCursor().selectedText()
                for c in str:
                    if 97 <= ord(c) <= 122:
                        new_c.append(chr(ord(c) - 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_3.textCursor().removeSelectedText()
                self.sql_textEdit_tab_3.textCursor().insertText(str_change)
        elif current_tab == 4:
            if self.sql_textEdit_tab_4.textCursor().hasSelection():
                str = self.sql_textEdit_tab_4.textCursor().selectedText()
                for c in str:
                    if 97 <= ord(c) <= 122:
                        new_c.append(chr(ord(c) - 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_4.textCursor().removeSelectedText()
                self.sql_textEdit_tab_4.textCursor().insertText(str_change)
        elif current_tab == 5:
            if self.sql_textEdit_tab_5.textCursor().hasSelection():
                str = self.sql_textEdit_tab_5.textCursor().selectedText()
                for c in str:
                    if 97 <= ord(c) <= 122:
                        new_c.append(chr(ord(c) - 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_5.textCursor().removeSelectedText()
                self.sql_textEdit_tab_5.textCursor().insertText(str_change)

    def fileUpper2lower(self):
        # print("转小写")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        new_c = []
        if current_tab == 1:
            if self.sql_textEdit_tab_1.textCursor().hasSelection():
                str = self.sql_textEdit_tab_1.textCursor().selectedText()
                for c in str:
                    if 65 <= ord(c) <= 90:
                        new_c.append(chr(ord(c) + 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                # str_change = "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
                self.sql_textEdit_tab_1.textCursor().removeSelectedText()
                self.sql_textEdit_tab_1.textCursor().insertText(str_change)
        elif current_tab == 2:
            if self.sql_textEdit_tab_2.textCursor().hasSelection():
                str = self.sql_textEdit_tab_2.textCursor().selectedText()
                for c in str:
                    if 65 <= ord(c) <= 90:
                        new_c.append(chr(ord(c) + 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_2.textCursor().removeSelectedText()
                self.sql_textEdit_tab_2.textCursor().insertText(str_change)
        elif current_tab == 3:
            if self.sql_textEdit_tab_3.textCursor().hasSelection():
                str = self.sql_textEdit_tab_3.textCursor().selectedText()
                for c in str:
                    if 65 <= ord(c) <= 90:
                        new_c.append(chr(ord(c) + 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_3.textCursor().removeSelectedText()
                self.sql_textEdit_tab_3.textCursor().insertText(str_change)
        elif current_tab == 4:
            if self.sql_textEdit_tab_4.textCursor().hasSelection():
                str = self.sql_textEdit_tab_4.textCursor().selectedText()
                for c in str:
                    if 65 <= ord(c) <= 90:
                        new_c.append(chr(ord(c) + 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_4.textCursor().removeSelectedText()
                self.sql_textEdit_tab_4.textCursor().insertText(str_change)
        elif current_tab == 5:
            if self.sql_textEdit_tab_5.textCursor().hasSelection():
                str = self.sql_textEdit_tab_5.textCursor().selectedText()
                for c in str:
                    if 65 <= ord(c) <= 90:
                        new_c.append(chr(ord(c) + 32))
                    else:
                        new_c.append(c)
                str_change = "".join(new_c)
                self.sql_textEdit_tab_5.textCursor().removeSelectedText()
                self.sql_textEdit_tab_5.textCursor().insertText(str_change)

    def fileAlignleft(self):
        # print("居左")
        QMessageBox.about(self, "提示", "当前编辑模式不支持设置对齐方式")

    def fileAligncenter(self):
        # print("居中")
        QMessageBox.about(self, "提示", "当前编辑模式不支持设置对齐方式")

    def fileAlignright(self):
        # print("居右")
        QMessageBox.about(self, "提示", "当前编辑模式不支持设置对齐方式")

    def fileFont(self):
        # print("字体")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        font, okPressed = QFontDialog.getFont()
        fmt = QTextCharFormat()
        fmt.setFont(font)
        if okPressed:
            if current_tab == 1:
                if self.sql_textEdit_tab_1.textCursor().hasSelection():
                    self.sql_textEdit_tab_1.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_1.setCurrentCharFormat(fmt)
                    # self.sql_textEdit_tab_1.setFont(font) # 效果相同
            elif current_tab == 2:
                if self.sql_textEdit_tab_2.textCursor().hasSelection():
                    self.sql_textEdit_tab_2.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_2.setCurrentCharFormat(fmt)
            elif current_tab == 3:
                if self.sql_textEdit_tab_3.textCursor().hasSelection():
                    self.sql_textEdit_tab_3.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_3.setCurrentCharFormat(fmt)
            elif current_tab == 4:
                if self.sql_textEdit_tab_4.textCursor().hasSelection():
                    self.sql_textEdit_tab_4.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_4.setCurrentCharFormat(fmt)
            elif current_tab == 5:
                if self.sql_textEdit_tab_5.textCursor().hasSelection():
                    self.sql_textEdit_tab_5.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_5.setCurrentCharFormat(fmt)

    def fileColor(self):
        # print("颜色")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        col = QColorDialog.getColor()
        fmt = QTextCharFormat()
        fmt.setForeground(col)
        if col.isValid():
            if current_tab == 1:
                if self.sql_textEdit_tab_1.textCursor().hasSelection():
                    self.sql_textEdit_tab_1.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_1.setCurrentCharFormat(fmt)
            elif current_tab == 2:
                if self.sql_textEdit_tab_2.textCursor().hasSelection():
                    self.sql_textEdit_tab_2.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_2.setCurrentCharFormat(fmt)
            elif current_tab == 3:
                if self.sql_textEdit_tab_3.textCursor().hasSelection():
                    self.sql_textEdit_tab_3.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_3.setCurrentCharFormat(fmt)
            elif current_tab == 4:
                if self.sql_textEdit_tab_4.textCursor().hasSelection():
                    self.sql_textEdit_tab_4.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_4.setCurrentCharFormat(fmt)
            elif current_tab == 5:
                if self.sql_textEdit_tab_5.textCursor().hasSelection():
                    self.sql_textEdit_tab_5.textCursor().mergeCharFormat(fmt)
                else:
                    self.sql_textEdit_tab_5.setCurrentCharFormat(fmt)

    def patternSwitch(self):
        # print("模式切换")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        if current_tab == 1:
            if self.sql_textEdit_tab_1.pattern == 0:
                self.sql_textEdit_tab_1.highligter = SqlHighlighter(self.sql_textEdit_tab_1.document())  # 设置语法高亮
                self.sql_textEdit_tab_1.pattern = 1 # 设置模式为语法高亮模式
            else:
                del self.sql_textEdit_tab_1.highligter
                self.sql_textEdit_tab_1.pattern = 0
        elif current_tab == 2:
            if self.sql_textEdit_tab_2.pattern == 0:
                self.sql_textEdit_tab_2.highligter = SqlHighlighter(self.sql_textEdit_tab_2.document())
                self.sql_textEdit_tab_2.pattern = 1
            else:
                del self.sql_textEdit_tab_2.highligter
                self.sql_textEdit_tab_2.pattern = 0
        elif current_tab == 3:
            if self.sql_textEdit_tab_3.pattern == 0:
                self.sql_textEdit_tab_3.highligter = SqlHighlighter(self.sql_textEdit_tab_3.document())
                self.sql_textEdit_tab_3.pattern = 1
            else:
                del self.sql_textEdit_tab_3.highligter
                self.sql_textEdit_tab_3.pattern = 0
        elif current_tab == 4:
            if self.sql_textEdit_tab_4.pattern == 0:
                self.sql_textEdit_tab_4.highligter = SqlHighlighter(self.sql_textEdit_tab_4.document())
                self.sql_textEdit_tab_4.pattern = 1
            else:
                del self.sql_textEdit_tab_4.highligter
                self.sql_textEdit_tab_4.pattern = 0
        elif current_tab == 5:
            if self.sql_textEdit_tab_5.pattern == 0:
                self.sql_textEdit_tab_5.highligter = SqlHighlighter(self.sql_textEdit_tab_5.document())
                self.sql_textEdit_tab_5.pattern = 1
            else:
                del self.sql_textEdit_tab_5.highligter
                self.sql_textEdit_tab_5.pattern = 0

    def resizeEvent(self, event):
        # print("窗口大小改变")
        x = self.centralwidget.pos().x()
        y = self.centralwidget.pos().y() + self.centralwidget.height() - self.databaseSelectPane.height()
        self.databaseSelectPane.move(x, y)
        self.databaseSelectPane.resize(self.centralwidget.width(), self.databaseSelectPane.height())

    def show_select_pane(self, sqlstr, data):
        # print("执行select操作时显示结果界面")
        self.databaseSelectPane.show()
        self.databaseSelectPane.data_tableWidget.setRowCount(0)
        if sqlstr.find(" where ") == -1:
            if sqlstr.find(";") == -1:
                par = sqlstr.partition("from ")
                table_name = par[2].partition(" ")[0][:]
            else:
                par = sqlstr.partition("from ")
                table_name = par[2].partition(";")[0][:]
        else:
            par = sqlstr.partition("from ")
            table_name = par[2].partition(" where")[0][:]
        sql = "select COLUMN_NAME from INFORMATION_SCHEMA.Columns where table_name='" + table_name + "'"
        try:
            conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
            cur = conn.cursor()
            cur.execute(sql)
            column_name = cur.fetchall()
            conn.commit()
            column_name_rowCount = len(column_name)
            column_name_columnCount = len(column_name[0])
            headTitle_list = [] # 存放表的字段名称
            for i in range(column_name_rowCount):
                for j in range(column_name_columnCount):
                    headTitle_list.append(column_name[i][j])
            rowCount = len(data)
            if rowCount == 0:
                self.databaseSelectPane.data_tableWidget.setRowCount(1)  # 设置行数
                self.databaseSelectPane.data_tableWidget.setColumnCount(column_name_rowCount)  # 设置列数
                for i in range(column_name_rowCount):
                    temp_data = "Null"  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.databaseSelectPane.data_tableWidget.setItem(0, i, data1)
            else:
                columnCount = len(data[0])
                self.databaseSelectPane.data_tableWidget.setRowCount(rowCount)  # 设置行数
                self.databaseSelectPane.data_tableWidget.setColumnCount(columnCount)  # 设置列数
                for i in range(rowCount):
                    for j in range(columnCount):
                        temp_data = data[i][j]  # 临时记录，不能直接插入表格
                        data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.databaseSelectPane.data_tableWidget.setItem(i, j, data1)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        self.databaseSelectPane.data_tableWidget.setHorizontalHeaderLabels(headTitle_list)  # 设置行表头
        self.databaseSelectPane.data_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.databaseSelectPane.data_tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.databaseSelectPane.data_tableWidget.horizontalHeader().setSectionsClickable(False)  # 可以禁止点击表头的列
        self.databaseSelectPane.data_tableWidget.sortItems(0, Qt.AscendingOrder)  # 设置按照第一列自动升序排序（DescendingOrder降序）
        self.databaseSelectPane.data_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:lightgray}')

    def sqlExecution(self):
        # print("执行sql语句，操作数据库")
        if self.tabWidget.count() == 0:
            return
        current_tab = self.choose_judge()
        current_account = self.user_account
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.databaseSelectPane.setVisible(False) # 隐藏查询结果界面
        if current_tab == 1:
            if self.sql_textEdit_tab_1.textCursor().hasSelection():
                sqlstr = self.sql_textEdit_tab_1.textCursor().selectedText()
                try:
                    conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                    cur = conn.cursor()
                    cur.execute(sqlstr)
                    data = cur.fetchall()
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    rowCount = len(data)
                    success_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nMessage：%d" %rowCount+"row(s) returned"
                    self.console_textEdit.setText(success_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:green;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                    if type(data) == tuple:
                        if sqlstr.find("select") == -1:
                            return
                        # print("这是查询操作")
                        self.show_select_pane(sqlstr, data)
                except Exception as e:
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','否','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    error_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nError Code：%d" % (e.args[0]) + "\nMessage：" + e.args[1]
                    self.console_textEdit.setText(error_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:red;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                finally:
                    conn.close()
            else:
                QMessageBox.about(self, "提示", "请选中要执行的SQL语句")
        elif current_tab == 2:
            if self.sql_textEdit_tab_2.textCursor().hasSelection():
                sqlstr = self.sql_textEdit_tab_2.textCursor().selectedText()
                try:
                    conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                    cur = conn.cursor()
                    cur.execute(sqlstr)
                    data = cur.fetchall()
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    rowCount = len(data)
                    success_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nMessage：%d" % rowCount + "row(s) returned"
                    self.console_textEdit.setText(success_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:green;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                    if type(data) == tuple:
                        if sqlstr.find("select") == -1:
                            return
                        # print("这是查询操作")
                        self.show_select_pane(sqlstr, data)
                except Exception as e:
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','否','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    error_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nError Code：%d" % (e.args[0]) + "\nMessage：" + e.args[1]
                    self.console_textEdit.setText(error_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:red;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                finally:
                    conn.close()
            else:
                QMessageBox.about(self, "提示", "请选中要执行的SQL语句")
        elif current_tab == 3:
            if self.sql_textEdit_tab_3.textCursor().hasSelection():
                sqlstr = self.sql_textEdit_tab_3.textCursor().selectedText()
                try:
                    conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                    cur = conn.cursor()
                    cur.execute(sqlstr)
                    data = cur.fetchall()
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    rowCount = len(data)
                    success_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nMessage：%d" % rowCount + "row(s) returned"
                    self.console_textEdit.setText(success_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:green;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                    if type(data) == tuple:
                        if sqlstr.find("select") == -1:
                            return
                        # print("这是查询操作")
                        self.show_select_pane(sqlstr, data)
                except Exception as e:
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','否','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    error_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nError Code：%d" % (e.args[0]) + "\nMessage：" + e.args[1]
                    self.console_textEdit.setText(error_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:red;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                finally:
                    conn.close()
            else:
                QMessageBox.about(self, "提示", "请选中要执行的SQL语句")
        elif current_tab == 4:
            if self.sql_textEdit_tab_4.textCursor().hasSelection():
                sqlstr = self.sql_textEdit_tab_4.textCursor().selectedText()
                try:
                    conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                    cur = conn.cursor()
                    cur.execute(sqlstr)
                    data = cur.fetchall()
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    rowCount = len(data)
                    success_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nMessage：%d" % rowCount + "row(s) returned"
                    self.console_textEdit.setText(success_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:green;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                    if type(data) == tuple:
                        if sqlstr.find("select") == -1:
                            return
                        # print("这是查询操作")
                        self.show_select_pane(sqlstr, data)
                except Exception as e:
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','否','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    error_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nError Code：%d" % (e.args[0]) + "\nMessage：" + e.args[1]
                    self.console_textEdit.setText(error_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:red;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                finally:
                    conn.close()
            else:
                QMessageBox.about(self, "提示", "请选中要执行的SQL语句")
        elif current_tab == 5:
            if self.sql_textEdit_tab_5.textCursor().hasSelection():
                sqlstr = self.sql_textEdit_tab_5.textCursor().selectedText()
                try:
                    conn = pymysql.connect("localhost", "root", "123456", "bsdb", charset='utf8')
                    cur = conn.cursor()
                    cur.execute(sqlstr)
                    data = cur.fetchall()
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','是','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    rowCount = len(data)
                    success_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nMessage：%d" % rowCount + "row(s) returned"
                    self.console_textEdit.setText(success_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:green;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                    if type(data) == tuple:
                        if sqlstr.find("select") == -1:
                            return
                        # print("这是查询操作")
                        self.show_select_pane(sqlstr, data)
                except Exception as e:
                    cur.execute("insert into work_log values('" + current_account + "','" + current_time + "','否','" + sqlstr.replace("'", "\\'") + "')")
                    conn.commit()
                    error_text = "Time：" + current_time + "\nAction：" + sqlstr + "\nError Code：%d" % (e.args[0]) + "\nMessage：" + e.args[1]
                    self.console_textEdit.setText(error_text)
                    self.console_textEdit.setStyleSheet(
                        "QTextEdit{color:red;background-color:white; font: 12pt \"Arial\"; border-radius:5px; border:2px solid lightgray;}")
                finally:
                    conn.close()
            else:
                QMessageBox.about(self, "提示", "请选中要执行的SQL语句")


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = DatabaseCommandPane()
    window.show()
    sys.exit(app.exec_())
