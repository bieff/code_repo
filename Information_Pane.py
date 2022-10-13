# 软件信息界面，调用生成的information_ui.py文件
from PyQt5.Qt import *
from resource.information_ui import Ui_Form
from Feedback_Pane import FeedbackPane
class InformationPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.user_account = "201601033017" # 当前账号，默认是我本人的
        self.user_name = "夜晓希声"  # 当前用户名，默认是我本人的
        self.copyright_label.setText("版权公告：2020-2026 夜晓希声 版权所有"+"\n"+"Copyright© 2020Aixili,Inc.All right reserved.")
        self.copyright_label.setAlignment(Qt.AlignCenter)

    def showIfo(self):
        # print("初始化方法")
        account = self.user_account
        settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
        the_account = settings.value("%s/account" % account)
        if the_account == None:
            return
        the_autologin = settings.value("%s/autologin" % account)
        if the_autologin == "true" or the_autologin == True:
            self.autologin_checkBox.setChecked(True)

    def auto_login(self, checked):
        # print("自动登录")
        account = self.user_account
        if checked:
            settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
            settings.setValue("%s/autologin" % account, True)
            settings.setValue("%s/remeberpassword" % account, True)
        else:
            settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
            settings.setValue("%s/autologin" % account, False)
            settings.setValue("%s/remeberpassword" % account, True)

    def check_version(self):
        # print("检测更新")
        QMessageBox.information(self, "检测更新", "当前版本最新", QMessageBox.Yes)

    def show_feedback(self):
        # print("用户反馈")
        self.feedback = FeedbackPane()
        self.feedback.show()
        self.feedback.user_account = self.user_account
        self.feedback.user_name = self.user_name

    def official_web_link(self):
        # print("官网链接")
        QMessageBox.information(self, "温馨提示", "官网正在建设中，敬请期待", QMessageBox.Yes)

    def user_handbook_link(self):
        # print("用户管理手册")
        self.handbook = QWidget()
        self.handbook.resize(600, 400)
        self.horizontalLayout = QHBoxLayout(self.handbook)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit1 = QTextEdit(self.handbook)
        self.textEdit1.setReadOnly(True)
        self.textEdit1.setObjectName("textEdit1")
        self.horizontalLayout.addWidget(self.textEdit1)
        self.handbook.setWindowTitle("管理手册")
        self.textEdit1.setHtml(
             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
             "p, li { white-space: pre-wrap; }\n"
             "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">《管理细则》</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">我们提倡：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 本着原创、分享、互助、开放、自由的原则；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 理性、宽容的看待不同的看法、喜好、意见等；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 尊重他人著作权、隐私等。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">我们不欢迎：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 针对种族、国家、民族、宗教、性别、年龄、地缘、性取向、生理特征的歧视和仇恨言论；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 不雅词句、人身攻击、故意骚扰和恶意使用；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 色情、激进时政、意识形态方面的话题；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. 抄袭他人原创内容，或冒充他人；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. 发布广告信息、垃圾信息，或含有网络病毒网站链接，图片等内容。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">我们禁止：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 违反中国或所在地法律法规的行为和内容（相关政策法规）；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 威胁他人或用户自身的人身安全、法律安全的行为；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 对网站的运营安全有潜在威胁的内容。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">指导原则：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 所有用户均有责任和义务举报或反馈不欢迎、禁止的内容；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 用户之间的争执均由用户协商解决；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 如有不允许的内容，工作人员有责权介入。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">细则：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 用户违反行为规范时，可能受到内容处理或帐号处理；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 用户产生的数据属于不欢迎、禁止的范围内时，亦有可能受到内容处理或帐号处理；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 内容处理包括删除用户头像，个人资料，以及其他数据等；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. 工作人员对于用户之间违反社区精神的收费推广等行为有责权介入处理；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. 遇到特殊情况或政府相关机构要求时，网易云音乐保留处置或删除所有用户产生的内容；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6. 如果用户对处理有异议，可以通过页面中的「用户反馈」功能向我们进行反馈。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">图片政策：</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 请勿上传涉及他人隐私、淫秽色情、暴力、血腥、 违反国家法律法规及可能对我们带来潜在威胁的照片或图片；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 用户需要对所上传的照片或图片版权负责， 我们不承担因此带来的任何第三方责任及法律风险；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 违反使用规则的内容以及根据用户据实投诉、举报，我们有可能删除您所发布的内容，并保留对您的帐号的处理权利；</span></p>\n"
             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. 本规则适用系统中的所有图片，所有未涉及的情况参考行为规范和相关法律规定。</span></p>\n"
             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>")
        self.handbook.show()

    def server_link(self):
        # print("服务条款")
        self.service_terms = QWidget()
        self.service_terms.resize(600, 400)
        self.horizontalLayout = QHBoxLayout(self.service_terms)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit2 = QTextEdit(self.service_terms)
        self.textEdit2.setReadOnly(True)
        self.textEdit2.setObjectName("textEdit2")
        self.horizontalLayout.addWidget(self.textEdit2)
        self.service_terms.setWindowTitle("服务条款")
        self.textEdit2.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">《服务条款》</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-size:10pt;\">欢迎使用本公司提供的软件产品及服务。请您（下列简称为“用户”）仔细阅读以下全部内容（未成年人则应在监护人陪同下阅读）。如用户本软件或服务，即表示用户与网易公司已达成协议。<br />1、服务条款的确认和接纳<br />    本条款是用户与本公司之间关于用户使用软件或服务的条款，除另行明确声明外，用户使用软件或服务的行为将受本条款约束。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    本条款如由于软件发展需要进行修订的，我们将在官网平台公布。用户可前往查阅最新版协议，如果用户不接受修改后的条款，用户可以选择终止使用软件或服务。用户继续使用的，将被视为遵守协议。<br />2、网易云音乐账号规则<br />    用户通过使用软件或服务，可获取相关内容，并可在登录后享受更为完整的服务，帐号可以是用户本人的手机号、邮箱帐号或其他可登录帐号。"
            "用户应维持密码及帐号的机密，如果用户未保管好自己的帐号和密码而对用户、我们或第三方造成损害，用户将负全部责任。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    用户在使用网易云音乐服务时填写、登录、使用的帐号名称、头像、个人简介等帐号信息资料应遵守法律法规、公共秩序、社会道德风尚和信息真实性等底线，不得在帐号信息资料中出现违法和不良信息。<br />    若用户登录、使用帐号头像、个人简介等帐号信息资料存在违法和不良信息的，本公司有权采取通知限期改正，本公司有权取消该帐号的使用。<br />3、服务条款的修改<br /> "
            "   本公司有权在必要时通过在软件内或网页上发出公告等合理方式修改本条款。用户在使用时需自觉遵守本服务条款的相关内容。用户如继续使用软件或本服务条款涉及的服务，则视为遵守条款，以最新的服务条款为准；用户在不同意修改内容的情况下，有权停止使用本服务条款涉及的软件或服务。<br />4、用户管理<br />    用户独立承担其所发布内容的责任。用户对软件或服务的使用必须遵守所有适用于服<br />用户承诺：<br />（1）用户在网易云音乐上发布信息或者使用网易云音乐的软件或服务时必须符合中国有关法规，不得发布、传播法律、行政法规禁止的信息；"
            "<br />（2）用户发布信息或者利用软件或服务时还必须符合其他有关国家和地区的法律；<br />5、信息储存及相关知识产权<br />    本公司对软件上所有服务将尽力维护其安全性及方便性，但对服务中出现的信息删除或储存失败不承担任何责任。另外本公司有权判定用户的行为是否符合本服务条款的规定，本公司有权中止或者终止对其提供服务。<br />6、法律<br />    本条款适用中华人民共和国的法律，并且排除一切冲突法规定的适用。如您在使用本协议项下服务中出现纠纷的，您同意将纠纷交由中国国际经济贸易仲裁委员会仲裁解决，对双方都有约束力。仲裁费用"
            "由败诉一方承担。<br />7、其他<br />    用户可通过本服务条款文末列明的客服邮箱投诉、举报各类违法违规行为，我们将及时受理和处理。<br />    本条款自发布之日起实施，并构成用户和网易公司之间的共识。我们不行使、未能及时行使或者未充分行使权利，不应被视为放弃该权利，也不影响我们在将来行使该权利。如果用户对本条款内容有任何疑问，请发送邮件至我们的客服邮箱：2573100722@qq.com。<br /></span></p></body></html>")
        self.service_terms.show()

    def privacy_policy_link(self):
        # print("隐私政策")
        self.privacy_policy = QWidget()
        self.privacy_policy.resize(600, 400)
        self.horizontalLayout = QHBoxLayout(self.privacy_policy)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit3 = QTextEdit(self.privacy_policy)
        self.textEdit3.setReadOnly(True)
        self.textEdit3.setObjectName("textEdit3")
        self.horizontalLayout.addWidget(self.textEdit3)
        self.privacy_policy.setWindowTitle("隐私政策")
        self.textEdit3.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">《隐私政策》</span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    更新日期：2020年3月25日</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    生效日期：2019年3月25日</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    欢迎阅读隐私政策。感谢您花时间阅读本文件。我们感谢您相信我们，向我们提供您的信息。我们将努力始终维持您的这一信任。首先，我们将确保您了解我们收集的信息、我们为什么收集信息、如何使用信息以及您对于您的信息"
            "可以作何选择。本政策以通俗的语言描述了我们的隐私做法，并尽可能少地使用了法律和技术术语。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1、本隐私政策的适用范围</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    本隐私政策适用于由软件本身和提供的全部服务。为简单起见，我们在本隐私政策中将所有这些项目称为“服务”。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2、我们收集的信息</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    毫无疑问，如果没有关于您的某些信息，例如基本的详细个人资料以及您希望遇到的人的类型，我们无法帮助您建立有意义的联系。我们还会收集您在使用我们的服务时生成的信息（例如访问日志），并在您通过社交媒体帐户访问"
            "我们的服务等情况下收集来自第三方的信息。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3、您提供给我们的信息</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    您在使用我们的服务时，选择了向我们提供某些信息。这包括：</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（1）当您创建帐户时，您至少向我们提供您的登录凭据以及我们提供服务所必需的一些基本详细信息，例如您的性别和出生日期。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（2）当填写您的个人资料时，您可以与我们分享其他信息，例如关于您的个性、生活方式、兴趣和其他方面的详细信息以及照片和视频等内容。要添加某些内容，例如图片或视频，您可能需要允许我们访问您的相机或相册。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（3）当您通过我们的产品服务与用户进行互动时，您可能需要允许我们使用您的录音权限才能进行。例如在使用聊天功能中发送语音、进行语音通话等功能时。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（4）如果您联系我们的客户服务团队，我们会收集您在互动过程中提供给我们的信息。有时候，我们会监控或记录这些互动，以便进行培训和确保高质量的服务。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（5）社交媒体:您可能可以使用您的社交媒体创建并登录您的帐户。这样做可使您无需另记一个用户名和密码，并且与我们分享来自您社交媒体帐户中的一些信息。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（6）其他合作伙伴:我们可能会从我们的合作伙伴那里收到有关您的信息，例如，在合作伙伴的网站和平台上发布广告时（在这种情况下，他们可能会将活动成果的详细信息传给我们）。您使用我们的服务时收集的信息，"
            "我们会收集与您通过我们的服务进行的活动相关的信息。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（7）设备信息:我们会收集您访问我们的服务所使用的设备的信息，包括：硬件和软件信息，例如 IP 地址、设备 ID 和类型、特定设备和应用程序设置和特征、应用程序崩溃、广告 ID。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4、我们如何使用信息</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    我们使用您的信息的主要原因是提供和改进我们的服务。此外，我们会使用您的信息来帮助您保持安全，并为您提供您可能感兴趣的广告。管理您的帐户并向您提供我们的服务</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（1）创建和管理您的帐户；（2）为您提供客户支持并响应您的要求；（3）对用户行为进行研究和分析，以改善我们的服务和内容；（4）开发新的功能和服务。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5、我们如何保护您的信息</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    我们努力保护您的个人信息免遭未经授权的访问或更改、泄露或破坏。和所有技术公司一样，虽然我们采取措施保护您的信息，但我们不能保证、您也不能期望您的个人信息始终是安全的。"
            "我们会定期监控我们的系统以发现可能存在的漏洞和攻击，并定期审核我们的信息收集、存储和处理做法，以更新我们的物理、技术和组织安全措施。_如果我们怀疑或发现任何破坏安全的行为，我们可能会不经通知暂停您使用全部或部分服务的权利。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6、儿童隐私</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    我们的服务仅面向年满12岁的用户。我们不允许12岁以下的用户使用我们的平台，也不会故意收集12岁以下任何人的个人信息。如果您怀疑某用户未满 12岁，请使用服务中提供的报告机制报告。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">7、隐私政策变更</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    因为我们一直在寻求新的创新方式来帮助您建立有意义的联系，所以本政策可能会随着时间而变更。我们会在任何重大变更生效之前通知您，以便您有时间查看变更。</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">如果您对本隐私政策有疑问，请通过以下方式联系我们：Email：2573100722@qq.com</span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>")
        self.privacy_policy.show()


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = InformationPane()
    window.showIfo()
    window.show()
    sys.exit(app.exec_())
