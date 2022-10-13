# 文本编辑器
from PyQt5.Qt import *
class QCodeEditor(QPlainTextEdit, QTextEdit):
    class NumberBar(QWidget):
        def __init__(self, editor):
            # 因为NumberBar是类中类，故我们在初始化的时候也要把外部类的对象带进来
            QWidget.__init__(self, editor)
            self.editor = editor
            # 每当块数（段落）发生变化时都会发出该信号并调用updateWidth()函数。
            self.editor.blockCountChanged.connect(self.updateWidth)
            # 当文本文档需要更新指定的矩形时，会发出此信号。
            # 如果文字滚动，矩形将覆盖整个视区。如果文本垂直滚动，dy将携带视口滚动的像素数量（dy是信号给槽函数的参数）。
            self.editor.updateRequest.connect(self.updateContents)
            self.font = QFont()# 获取字体和设置颜色
            self.numberBarColor = QColor("#e8e8e8")

        # 重写小部件的绘图事件
        def paintEvent(self, event):
            # 构建绘画设备，并用指定的颜色填充给定的矩形。
            # 这里的矩形是QPaintEvent中返回需要更新的矩形，颜色就是QColor(“#e8e8e8”)。
            painter = QPainter(self)
            painter.fillRect(event.rect(), self.numberBarColor)
            block = self.editor.firstVisibleBlock()

            while block.isValid():
                # 在文本块有效的情况下进入循环，返回此文本块的编号（行号），如果块无效，则返回-1
                # 同时我们使用blockBoundingGeometry()函数以内容坐标返回文本块的边界矩形，
                # 并使用contentOffset()转义得到矩形以获得视口上的视觉坐标。这里得到top。
                blockNumber = block.blockNumber() # 返回第一个可见块，也就是文本块
                block_top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
                # 当鼠标移动到某一行的时候，其对应的行号会相应的变黑加粗，否则就是另外一种表现
                if blockNumber == self.editor.textCursor().blockNumber():
                    self.font.setBold(True)
                    painter.setPen(QColor("#000000"))
                else:
                    self.font.setBold(False)
                    painter.setPen(QColor("#717171"))
                # 行号绘画区域是paint_rect，居中对齐，具体的内容是str(blockNumber+1)
                paint_rect = QRect(0, block_top, self.width(), self.editor.fontMetrics().height())
                painter.drawText(paint_rect, Qt.AlignCenter, str(blockNumber + 1))
                block = block.next() # 返回此块后面的文档中的文本块，如果这是最后一个，则返回空文本块

        def getWidth(self):
            count = self.editor.blockCount() # 该属性保存文档中文本块的数量
            # 若行数小于99999行，返回小部件当前字体的宽度，这个宽度是内容’99999’的字体宽度。否则就返回实际宽度
            if 0 <= count < 99999:
                width = self.fontMetrics().width('99999')
            else:
                width = self.fontMetrics().width(str(count))
            return width

        def updateWidth(self):
            width = self.getWidth()
            self.editor.setViewportMargins(width, 0, 0, 0) # 通过setViewportMargins设置编辑器显示行号位置的实际宽度

        # updateRequest()信号产生时调用。这个信号的产生，它会将两个参数传给槽函数：QRect对象和dy像素
        def updateContents(self, rect, dy):
            if dy:
                self.scroll(0, dy)
            else:
                self.update(0, rect.y(), self.width(), rect.height())
            # 如果存在垂直滚动，且像素dy > 0，那么将小部件向下滚动。滚动后，小部件将接收需要重新绘制区域的绘画事件
            # 否则更新小部件内的矩形（x，y，w，h）
            if rect.contains(self.editor.viewport().rect()): # 如果给定的矩形位于此矩形内，则返回True。 否则返回False
                fontSize = self.editor.currentCharFormat().font().pointSize()
                self.font.setPointSize(fontSize)
                self.font.setStyle(QFont.StyleNormal)
                self.updateWidth()

    def __init__(self):
        super(QCodeEditor, self).__init__()
        # self.setFont(QFont("Arial", 12))
        # self.highligter = SqlHighlighter(self.document()) # 设置语法高亮
        self.pattern = 0 # 模式0，默认为普通文本编辑
        self.setTabChangesFocus(True)
        self.setTabStopDistance(20)
        self.setStyleSheet("QPlainTextEdit{background-color:white; font: 12pt Arial; border-radius:5px; border:2px solid lightblue;}")
        self.setLineWrapMode(QPlainTextEdit.WidgetWidth)  # 默认自动换行
        # self.setLineWrapMode(QPlainTextEdit.NoWrap) # 不自动换行
        self.number_bar = self.NumberBar(self)
        self.currentLineNumber = None # 当前行号初始值为None
        self.cursorPositionChanged.connect(self.highligtCurrentLine) # 光标位置发生改变
        self.setViewportMargins(30, 0, 0, 0) # 将滚动区域周围边距设置为左侧，顶部，右侧和底部。行号部件放在未使用的区域
        self.highligtCurrentLine()
        self.setCenterOnScroll(True)

    # 接收在事件参数中传递的小部件大小调整事件。当调用resizeEvent()时，窗口小部件已经有了新的几何图形
    # 旧尺寸可通过QResizeEvent.oldSize()访问
    def resizeEvent(self, *e):
        cr = self.contentsRect() # 返回小部件边界内的区域
        # 创建QRect对象，在平面中定义一个矩形（左，顶，宽和高）
        rec = QRect(cr.left(), cr.top(), self.number_bar.getWidth(), cr.height())
        self.number_bar.setGeometry(rec) # 重新设置尺寸，将这个矩形应用到number_bar上

    # 突出显示包含光标的行
    def highligtCurrentLine(self):
        newCurrentLineNumber = self.textCursor().blockNumber() # 返回光标所在块的编号，如果光标无效，则返回0
        # 光标换行判断
        if newCurrentLineNumber != self.currentLineNumber:
            lineColor = QColor(Qt.yellow).lighter(160) # 设置颜色
            self.currentLineNumber = newCurrentLineNumber
            hi_selection = QTextEdit.ExtraSelection()
            hi_selection.format.setBackground(lineColor)
            hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True) # 设定文本的整个宽度显示为选中状态
            hi_selection.cursor = self.textCursor()
            hi_selection.cursor.clearSelection() # 通过将锚点设置为光标位置来清除当前选择。不会删除选择的文本
            self.setExtraSelections([hi_selection]) # 用指定的颜色临时标记文档中的某些区域，并将其指定为选项

# 高亮显示语法
class SqlHighlighter(QSyntaxHighlighter):
    Rules = []
    Formats = {}
    def __init__(self, parent=None):
        super(SqlHighlighter, self).__init__(parent)
        self.initializeFormats()
        KEYWORDS = ["var", "sql_variant", "datetime", "smalldatetime", "float", "real", "decimal",
                "money", "smallmoney", "bigint", "int", "smallint", "tinyint", "bit", "ntext", "text",
                "image", "integer", "timestamp", "uniqueidentifier", "nvarchar", "nchar", "varchar",
                "char", "character", "varbinary", "binary",
                    "VAR", "SQL_VARIANT", "DATETIME", "SMALLDATETIME", "FLOAT", "REAL", "DECIMAL",
                "MONEY", "SMALLMONEY", "BIGINT", "INT", "SMALLINT", "TINYINT", "BIT", "NTEXT", "TEXT",
                "IMAGE", "INTEGER", "TIMESTAMP", "UINQUEIDENTIFIER", "NVARCHAR", "NCHAR", "VARCHAR",
                "CHAR", "CHARACTER", "VARBINARY", "BINARY"]
        BUILTINS = ["add", "all", "alter", "and", "any", "as", "asc",
        "authorization", "avg", "backup", "begin", "between", "break", "browse", "bulk", "by", "cascade", "case",
        "check", "checkpoint", "close", "clustered", "coalesce", "column", "commit", "comment", "committed",
        "compute", "confirm", "connect", "constraint", "contains", "containstable", "continue", "controlrow",
        "convert", "count", "create", "cross", "current", "current_date", "current_time", "current_timestamp",
        "current_user", "cursor", "database", "dbcc", "deallocate", "declare", "default", "delete", "deny",
        "desc", "disk", "distinct", "distributed", "double", "drop", "dummy", "dump", "else", "end", "errlvl",
        "errorexit", "escape", "except", "exec", "execute", "exists", "exit", "fetch", "file", "fillfactor",
        "floppy", "for", "foreing", "freetext", "freetexttable", "from", "full", "goto", "grant", "group",
        "having", "holdlock", "identity", "identity_insert", "identitycol", "IF", "in", "index", "inner", "insert",
        "intersect", "into", "is", "isolation", "join","key", "kill", "left", "level", "like", "lineno", "load",
        "max", "min", "mirrorexit", "national", "nocheck","nonclustered", "not", "null", "nullif", "of", "off",
        "offsets", "on", "once", "only", "open", "opendatasource", "openquery", "openrowset", "option", "or",
        "order", "outer", "over", "percent", "perm", "permanent", "pipe", "plan", "precision", "prepare", "primary",
        "print", "privileges", "proc", "procedure", "processexit", "public", "raiserror", "read", "readtext",
        "reconfigure", "references", "repeatable", "replication", "restore", "restrict", "return", "revoke", "right",
        "rollback", "rowcount", "rowguidcol", "rule", "save", "schema", "select", "serializable", "session_user",
        "set", "setuser", "shutdown", "some", "statistics", "substr", "sum",  "table", "tape",
        "temp", "temporary", "textsize", "then", "timestamp", "to", "top", "tran", "transaction", "trigger",
        "truncate", "tesqual", "uncommitted", "union", "unique", "update", "updatetext", "use", "user", "using",
        "values", "varying", "view", "waitfor", "when", "where", "while", "with", "work", "writetext",
            "ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC",
        "AUTHORIZATION", "AVG", "BACKUP", "BEGIN", "BETWEEN", "BREAK", "BROWSE", "BULK", "BY", "CASCADE", "CASE",
        "CHECK", "CHECKPOINT", "CLOSE", "CLUSTERED", "COALESCE", "COLUMN", "COMMIT", "COMMENT", "COMMITTED",
        "COMPUTE", "CONFIRM", "CONNECT", "CONSTRAINT", "CONTAINS", "CONTAINSTABLE", "CONTINUE", "CONTROLROW",
        "CONVERT", "COUNT", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP",
        "CURRENT_USER", "CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE", "DEFAULT", "DELETE", "DENY",
        "DESC", "DISK", "DISTINCT", "DISTRIBUTED", "DOUBLE", "DROP", "DUMMY", "DUMP", "ELSE", "END", "ERRLVL",
        "ERROREXIT", "ESCAPE", "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", "FETCH", "FILE", "FILLFACTOR",
        "FLOPPY", "FOR", "FOREIGN", "FREETEXT", "FREETEXTTABLE", "FROM", "FULL", "GOTO", "GRANT", "GROUP",
        "HAVING", "HOLDLOCK", "IDENTITY", "IDENTITY_INSERT", "IDENTITYCOL", "IF", "IN", "INDEX", "INNER", "INSERT",
        "INTERSECT", "INTO", "IS", "ISOLATION", "JOIN","KEY", "KILL", "LEFT", "LEVEL", "LIKE", "LINENO", "LOAD",
        "MAX", "MIN", "MIRROREXIT", "NATIONAL", "NOCHECK","NONCLUSTERED", "NOT", "NULL", "NULLIF", "OF", "OFF",
        "OFFSETS", "ON", "ONCE", "ONLY", "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", "OPTION", "OR",
        "ORDER", "OUTER", "OVER", "PERCENT", "PERM", "PERMANENT", "PIPE", "PLAN", "PRECISION", "PREPARE", "PRIMARY",
        "PRINT", "PRIVILEGES", "PROC", "PROCEDURE", "PROCESSEXIT", "PUBLIC", "RAISERROR", "READ", "READTEXT",
        "RECONFIGURE", "REFERENCES", "REPEATABLE", "REPLICATION", "RESTORE", "RESTRICT", "RETURN", "REVOKE", "RIGHT",
        "ROLLBACK", "ROWCOUNT", "ROWGUIDCOL", "RULE", "SAVE", "SCHEMA", "SELECT", "SERIALIZABLE", "SESSION_USER",
        "SET", "SETUSER", "SHUTDOWN", "SOME", "STATISTICS", "SUBSTR", "SUM", "SYSTEM_USER", "TABLE", "TAPE",
        "TEMP", "TEMPORARY", "TEXTSIZE", "THEN", "TIMESTAMP", "TO", "TOP", "TRAN", "TRANSACTION", "TRIGGER",
        "TRUNCATE", "TSEQUAL", "UNCOMMITTED", "UNION", "UNIQUE", "UPDATE", "UPDATETEXT", "USE", "USER", "USING",
        "VALUES", "VARYING", "VIEW", "WAITFOR", "WHEN", "WHERE", "WHILE", "WITH", "WORK", "WRITETEXT"]

        CONSTANTS = ["False", "True", "None"]
        SqlHighlighter.Rules.append((QRegExp("|".join([r"\b%s\b" % keyword for keyword in KEYWORDS])), "keyword"))
        SqlHighlighter.Rules.append((QRegExp("|".join([r"\b%s\b" % builtin for builtin in BUILTINS])), "builtin"))
        SqlHighlighter.Rules.append((QRegExp("|".join([r"\b%s\b" % constant for constant in CONSTANTS])), "constant"))
        SqlHighlighter.Rules.append((QRegExp(
                r"\b[+-]?[0-9]+[lL]?\b"
                r"|\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b"
                r"|\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b"),
                "number"))
        SqlHighlighter.Rules.append((QRegExp(r"\bPyQt4\b|\bQt?[A-Z][a-z]\w+\b"), "pyqt"))
        SqlHighlighter.Rules.append((QRegExp(r"\b@\w+\b"),"decorator"))
        stringRe = QRegExp(r"""(?:'[^']*'|"[^"]*")""")
        stringRe.setMinimal(True)
        SqlHighlighter.Rules.append((stringRe, "string"))
        self.stringRe = QRegExp(r"""(:?"["]".*"["]"|'''.*''')""")
        self.stringRe.setMinimal(True)
        SqlHighlighter.Rules.append((self.stringRe, "string"))
        self.tripleSingleRe = QRegExp(r"""'''(?!")""")
        self.tripleDoubleRe = QRegExp(r'''"""(?!')''')

    def initializeFormats(self):
        baseFormat = QTextCharFormat()
        baseFormat.setFontFamily("courier")
        baseFormat.setFontPointSize(12)
        for name, color in (("normal", Qt.green),
                ("keyword", Qt.cyan), ("builtin", Qt.magenta),
                ("constant", Qt.darkGreen),
                ("decorator", Qt.darkBlue), ("comment", Qt.darkCyan),
                ("string", Qt.red), ("number", Qt.black),
                ("error", Qt.darkRed), ("pyqt", Qt.darkCyan)):
            format = QTextCharFormat(baseFormat)
            format.setForeground(QColor(color))
            if name in ("keyword", "decorator"):
                format.setFontWeight(QFont.Bold)
            if name == "comment":
                format.setFontItalic(True)
            SqlHighlighter.Formats[name] = format

    def highlightBlock(self, text):
        NORMAL, TRIPLESINGLE, TRIPLEDOUBLE, ERROR = range(4)
        textLength = len(text)
        prevState = self.previousBlockState()
        self.setFormat(0, textLength, SqlHighlighter.Formats["normal"])
        if text.startswith("Traceback") or text.startswith("Error: "):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength, SqlHighlighter.Formats["error"])
            return
        if (prevState == ERROR and
            not (text.startswith(sys.ps1) or text.startswith("#"))):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength, SqlHighlighter.Formats["error"])
            return
        for regex, format in SqlHighlighter.Rules:
            i = regex.indexIn(text)
            while i >= 0:
                length = regex.matchedLength()
                self.setFormat(i, length, SqlHighlighter.Formats[format])
                i = regex.indexIn(text, i + length)
        if not text:
            pass
        elif text[0] == "#":
            self.setFormat(0, len(text), SqlHighlighter.Formats["comment"])
        else:
            stack = []
            for i, c in enumerate(text):
                if c in ('"', "'"):
                    if stack and stack[-1] == c:
                        stack.pop()
                    else:
                        stack.append(c)
                elif c == "#" and len(stack) == 0:
                    self.setFormat(i, len(text),
                    SqlHighlighter.Formats["comment"])
                    break
        self.setCurrentBlockState(NORMAL)
        if self.stringRe.indexIn(text) != -1:
            return
        for i, state in ((self.tripleSingleRe.indexIn(text),TRIPLESINGLE),(self.tripleDoubleRe.indexIn(text),TRIPLEDOUBLE)):
            if self.previousBlockState() == state:
                if i == -1:
                    i = text.length()
                    self.setCurrentBlockState(state)
                self.setFormat(0, i + 3, SqlHighlighter.Formats["string"])
            elif i > -1:
                self.setCurrentBlockState(state)
                self.setFormat(i, text.length(), SqlHighlighter.Formats["string"])

    def rehighlight(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QSyntaxHighlighter.rehighlight(self)
        QApplication.restoreOverrideCursor()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = QCodeEditor()
    window.show()
    sys.exit(app.exec_())