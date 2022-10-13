# 使用向导界面，调用生成的guide_ui.py文件
from PyQt5.Qt import *
from resource.guide_ui import Ui_Form
class GuidePane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.guide_stackedWidget.setCurrentIndex(0)  # 设置当前页面
        self.guide_label.setText("一、登录界面\n1.输入账号和密码点击登录\n2.若没有账号可以点击左下角的注册按钮前往注册\n3点击右下角二维码，即可加入技术交流QQ群")

    def page_change(self, index):
        # print("切换页面")
        if index == 0:
            self.guide_label.setText("一、登录界面\n1.输入账号和密码点击登录\n2.若没有账号可以点击左下角的注册按钮前往注册\n3点击右下角二维码，即可加入技术交流QQ群")
        elif index == 1:
            self.guide_label.setText("二、注册界面\n1.点击左侧菜单按钮即可展开子按钮\n2.输入账号密码进行注册")
        elif index == 2:
            self.guide_label.setText("三、主界面\n1.主界面主要分为三大板块，上部是工具栏，左侧是功能列表，右侧是功能实现")
        elif index == 3:
            self.guide_label.setText("四、脚本执行\n1.这是一个SQL脚本编辑器，新建、打开、保存、另存为SQL文件\n2.点击左侧转换按钮，切换编辑器模式\n3.选中相应SQL语句，点击执行按钮，执行SQL语句，若执行查询操作，查询结果以表格形式弹出")
        elif index == 4:
            self.guide_label.setText("五、表格视图\n1.分为两大板块，上部按钮、下部表格\n2.右侧下拉框可选择数据表，新建、编辑、删除功能")
        elif index == 5:
            self.guide_label.setText("六、账号管理\n1.用户信息页面，可修改个人信息；密码页面，可修改密码\n2.登录日志页面，查看登录信息；工作日志页面，查看工作日志信息")
        elif index == 6:
            self.guide_label.setText("七、文章推送\n1.精选有关中药精油的文章，由管理员手动更新")
        elif index == 7:
            self.guide_label.setText("八、软件信息\n1.可查看软件是否最新版本，并提供更新选项；用户意见反馈\n2.查看软件有关隐私政策和使用说明\n3.软件有关版权信息")
        elif index == 8:
            self.guide_label.setText("九、联系我们\n本项目为江西中医药大学计算机学院本科毕业设计项目，扫码联系作者一起探讨及时问题")
        elif index == 9:
            self.guide_label.setText("十、迷你中心\n1.用户签到等级\n2.切换界面语言\n3.切换账号/退出登录")
        elif index == 10:
            self.guide_label.setText("十一、界面换肤\n1.主题换肤\n2.纯色换肤，并提供颜色滑块自定义界面颜色")

    def pre_btn_clicked(self):
        # print("上一张")
        pageCount = self.guide_stackedWidget.count()
        pageIndex = self.guide_stackedWidget.currentIndex()
        if pageIndex == 0:
            self.guide_stackedWidget.setCurrentIndex(pageCount - 1)
        else:
            self.guide_stackedWidget.setCurrentIndex(pageIndex - 1)

    def next_btn_clicked(self):
        # print("下一张")
        pageCount = self.guide_stackedWidget.count()
        pageIndex = self.guide_stackedWidget.currentIndex()
        if pageIndex == pageCount - 1:
            self.guide_stackedWidget.setCurrentIndex(0)
        else:
            self.guide_stackedWidget.setCurrentIndex(pageIndex + 1)


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = GuidePane()
    window.show()
    sys.exit(app.exec_())
