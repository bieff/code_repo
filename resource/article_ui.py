# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'article.ui'
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.article_pic_label = QtWidgets.QLabel(Form)
        self.article_pic_label.setStyleSheet("QLabel{\n"
"    border-image: url(:/article/images/article_top.jpg);\n"
"}")
        self.article_pic_label.setText("")
        self.article_pic_label.setObjectName("article_pic_label")
        self.verticalLayout.addWidget(self.article_pic_label)
        self.article_textEdit = QtWidgets.QTextEdit(Form)
        self.article_textEdit.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.article_textEdit.setReadOnly(True)
        self.article_textEdit.setObjectName("article_textEdit")
        self.verticalLayout.addWidget(self.article_textEdit)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.article_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#0055ff;\">《我眼中的中药精油》</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#0055ff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_01.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaa00;\">前言</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffaa00;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:12pt;\">写这一篇文章，是因为小酸8年前第一次接触精油的时候，就知道了药油这个词，也看到很多中药精油的名称，可惜看到后来发现全是假的。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    然后逐渐从西方的芳疗体系里认识精油，再回过头来了解中药精油，我们当年还提出了中医芳疗的概念，相信是国内头一批人。只是资料太少，连最基本精油不是油，植物油跟食用油是两回事，都很难找到准确的描述。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    真精油很难找到，更不用说所谓中药精油了，中医芳疗这个事情就很难开展下去，非常苦。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    小酸的这些年的所思所想，整理一下，于是有了以下内容，仅供参考交流，有专业的人和机构从事相关工作，欢迎教我。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_02.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaa00;\">什么是中药精油？</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:12pt;\">能用来萃取精油的植物，到现在就几百种。在被传统认定为中药材的植物里，能提取芳香精油的植物，据说有198种。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    在西方的芳疗范畴，它们是植物精油，在我们这里，它们就是草药，就是中药材，在这个惯性下，我们叫它们中药精油，中药草精油，并且用中医的方法指导使用，是很自然的事情。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    如果我没记错，梁冬跟徐文兵先生做《中医太美》节目里，讲过西方利用植物，那叫植物药，不是中药。因为背后的指导思想不同。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_03.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:12pt;\">中药是在传统中医药理论指导下使用，而植物药是在现代医药理论指导下使用。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    欧盟对植物药的定义：“植物药是指用单一或多种植物配伍，含有专一活性成分或植物提取物，用于医疗目的的医疗产品。”</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    小酸这几年看了不同国家作者写的精油相关书籍，看了一些专业人士在做的推广内容，小酸发现，还是跟各自的文化背景有关：在不同文化背景下，形成各自的风格，最终以教学，应用，书籍等呈现在我们面前。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_04.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    比如，小酸个人观感里——法：偏医学研究与应用；德：偏医学与化学应用；英：偏经验与实际应用；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    东方系：中医哲学，按摩推拿，经络脏腑，五行学说，气血穴位，性味归经，从精油性质特点的解释，到调配，到使用，中医理论都有完整的方法论来指导。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    香港，台湾，日本，有一些这方面的书，国内的我还不知道有没有大师出中医芳疗相关的书。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_05.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:12pt;\"> 还有三脉七轮的脉轮能量理论、星座、音乐、性格等等理论下的使用指导（这些小酸不打算接触）。所以叫中药精油，重要的不是这个精油本身，是背后的指导理论。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    当然，我看了一本书上面写着：研究发现，中药精油，通常比常见的那些精油，用于皮肤上时，渗透力更强。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_06.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     <span style=\" font-size:12pt;\">中药精油，一是本来就是自古以来使用的中草药，本来就是芳香植物，可以萃取精油，然后在我们文化体系内这样称呼它；一是按照中医的方法，来指导精油的应用，可能不是传统的草药，而是某些不常见的植物，这是精油的中医化，用中医的观点来看待植物精油，指导配伍和应用。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    中医也不是没有对芳香油的使用，只是很懵懂而已。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    看过一个研究，说做艾灸好是为什么，除了燃烧的热力之外，燃烧时产生的挥发油，也可能是带来作用的原因。还有香囊，去邪醒神等，制作原料都是含有挥发油的植物。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_07.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <span style=\" font-size:10pt;\">   </span><span style=\" font-size:12pt;\">关于中药精油性味归经，我看了不同的书，大体上一致，局部混乱和互相矛盾。没有统一的标准和权威组织来做这个整理、规范的事情，可能随着发展未来会有高人来做。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    我也有一个疑问，草药煎熬以水溶性为主，精油以芳香物质为主，完全沿用以前的性味归经，是否可行？那些没做过性味归经的植物，植物精油，谁来做性味归经的确定？</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_08.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaa00;\">芳香疗法和中医中药太多相似之处</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     <span style=\" font-size:12pt;\">精油芳疗，和中医，都叫作实证疗法。中医和精油芳香疗法，有着天然的契合。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    精油芳疗，有时候也会面临中医一样功效验证上的窘迫。比如，寇特博士用了一段描述：“对于流感，高浓度的使用精油，没有科学验证，但是反正就是有用。”这个描述方式，跟很多中草药的使用上很相似。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    芳香疗法的整体观：“将人视为身心灵的整体组合，几乎每一种急性或者慢性疾病都伴随负面情绪或者心理状况，甚至主导特定器官的失调。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    要达到完全的治愈必须考虑身心灵三个面向，这与以病症外在表征为治疗切入点的正统医学，在本质上完全不同。”</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_09.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:12pt;\"> 这段话有没有很熟悉的感觉，中医讲，八纲辨证，四诊合参，辨证论治，其实早就提出了治疗的整体观，不但将情志情绪与脏腑与病症联系起来，甚至季节气候的变化，带来的身心影响，也有了恰当的解释。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    中医讲上医治未病，讲养生，讲因天之序，合道而行时，芳香疗法都还没诞生呢。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    精油化学，有很好的一面，可以知道，它对人体是否有益，如何起作用，哪些精油的哪些成分有害，进入人体时就有害还是在代谢的过程中发生转变，从而产生不利作用等。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_10.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:12pt;\">但容易进入正统医学的单一成分vs功效的思路，西药绝大部分都是单一成分的对吧。当然这没什么不好，好处是更容易把事物置于我们的掌控之下，避免中药注射液，马兜铃酸这样的尴尬问题，更有安全感，而可能的坏处，是容易失去对植物整体性，协同性与人体相互作用的认同。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    有趣的是，很多用来作为调料、调味品的植物，它们的精油，正好是对胃，肠道有帮助的精油。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    比如，姜，薄荷，神圣罗勒（金不换，炒田螺里面就经常用到），紫苏，甜茴香，豆蔻，而在中医上，归脾胃经。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_11.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:12pt;\">柑橘类，甜橙，橘，在精油的应用上，本来就有香薰或按摩，有助于开胃的作用，而甜橙，是我们的中药材陈皮，健胃消食促进消化的配伍里，都会有它的身影。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    很多临床上并不能证明的结果，在实际应用中，就是能解决问题，同时并没有什么副作用。精油的协同性，和杀菌能力，就是最好的证明。中医中药，不也常常这样嘛。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    在于明确知道，这是无害的。</span><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_12.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:12pt;\">精油的中医化，中医的精油化（种植，土壤，水，选材，萃取工艺，标准管理，成分分析上值得学习，药材的炮制工艺很多都在失传消失，精油却在不断发展），可以在互相的领域，汲取到不同的营养，丰富，壮大自身，小酸相信，在对植物的理解和应用上，对人体疗愈上的理论/方法论，即使有争议，也有鄙视链，中西也必将殊途同归，毕竟生死事大。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    自然疗法，实证疗法，容易被人感觉成玄学，幸好精油来自于化学家、医师的不断研究和发展，更容易给人以知其然也知其所以然之感，多少有一些与正统医学叫板的底气，中医总感觉缺少这方面的沉淀和发展推进。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    只是不断的解构老智慧，没有推陈出新，很牛逼的中医，只靠一小撮牛逼的人，撑不起来，华严宗为什么慢慢不如禅宗，那是因为更艰深晦涩啊，不好传播啊。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_13.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:12pt;\">中医的方法论，对指导精油的使用，是一种强强联合。利用中医的理论，加强对精油的研究和运用，可能是中医中药，对现代医学进行弯道超车的一个好尝试也未可知。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    中药精油，兴许某一天，就成了是中医的一个重要分支发展领域了。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaa00;\">对精油推广的看法</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:12pt;\"> 天主教如何在国内传播？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    “以马内利，哈利路亚”等，写成春联，故事，教义，编写成广场舞歌曲，以普罗大众能接受的通俗方式，进行传播，走的是底层群众路线。效果好。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_14.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    </span><span style=\" font-size:12pt;\">精油也应该如此。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    只有用都听得懂的话，才能提高传播的接受度。要更好的推广精油，精油的本土化，就是精油的中医化，这是必然。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    按摩，养生，经络穴位，最好接受了。也很容易出效果。没有生病但总是感觉不舒服的状态，心理，情志，精神上，关怀安慰激励，减少痛苦等的辅助，精油可以带来很多帮助，疗愈力十足。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/article/images/article_15.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    </span><span style=\" font-size:12pt;\">当然，假借精油之名行背锅之实的也很多，比如壮阳延时，隆鼻，开眼角，整脸，增高，丰唇等，打着精油的概念在某宝风行过一段时间，非常令人恶心，利用信息不对称，纯骗钱。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    不过在国内精油划归化妆品管理，所以宣传很难。只能看到护肤相关，其他都没法说。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    任何有医疗感的词都不能使用，比如消炎，抗菌这样的词。有这样描述的文章，也很难发出去。包括我现在这个。</span></p></body></html>"))
import my_images_rc
