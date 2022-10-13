# 换肤界面，调用生成的skin_ui.py文件
from PyQt5.Qt import *
from resource.skin_ui import Ui_Form
class SkinPane(QWidget, Ui_Form):
    style_Signal = pyqtSignal(int) # 样式信号
    color_Signal = pyqtSignal(int, int, int) # 颜色信号
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint) # 去掉标题栏
        self.setupUi(self)

        btn_group = QButtonGroup(self)
        btn_group.setExclusive(True)
        btn_group.addButton(self.black_icon)
        btn_group.addButton(self.red_icon)
        btn_group.addButton(self.pink_icon)
        btn_group.addButton(self.blue_icon)
        btn_group.addButton(self.green_icon)
        btn_group.addButton(self.gold_icon)
        btn_group.addButton(self.color1_icon)
        btn_group.addButton(self.color2_icon)
        btn_group.addButton(self.color3_icon)
        btn_group.addButton(self.color4_icon)
        btn_group.addButton(self.color5_icon)
        btn_group.addButton(self.color6_icon)
        btn_group.addButton(self.color7_icon)
        btn_group.addButton(self.color8_icon)
        btn_group.addButton(self.color9_icon)
        btn_group.addButton(self.color10_icon)
        btn_group.addButton(self.color11_icon)
        btn_group.addButton(self.color12_icon)
        btn_group.addButton(self.pane_icon)
        self.setFocus()  # 设置控件获取焦点

    def change_style(self):
        # print("改变Style")
        if self.sender() == self.black_btn:
            self.style_Signal.emit(1)
            self.black_icon.setChecked(True)
        elif self.sender() == self.red_btn:
            self.style_Signal.emit(2)
            self.red_icon.setChecked(True)
        elif self.sender() == self.pink_btn:
            self.style_Signal.emit(3)
            self.pink_icon.setChecked(True)
        elif self.sender() == self.blue_btn:
            self.style_Signal.emit(4)
            self.blue_icon.setChecked(True)
        elif self.sender() == self.green_btn:
            self.style_Signal.emit(5)
            self.green_icon.setChecked(True)
        elif self.sender() == self.gold_btn:
            self.style_Signal.emit(6)
            self.gold_icon.setChecked(True)

    def change_color(self):
        # print("改变Color")
        if self.sender() == self.color1_btn:
            self.color_Signal.emit(255, 92, 138)
            self.color1_icon.setChecked(True)
        elif self.sender() == self.color2_btn:
            self.color_Signal.emit(239, 122, 158)
            self.color2_icon.setChecked(True)
        elif self.sender() == self.color3_btn:
            self.color_Signal.emit(254, 118, 200)
            self.color3_icon.setChecked(True)
        elif self.sender() == self.color4_btn:
            self.color_Signal.emit(113, 127, 249)
            self.color4_icon.setChecked(True)
        elif self.sender() == self.color5_btn:
            self.color_Signal.emit(71, 145, 235)
            self.color5_icon.setChecked(True)
        elif self.sender() == self.color6_btn:
            self.color_Signal.emit(57, 175, 234)
            self.color6_icon.setChecked(True)
        elif self.sender() == self.color7_btn:
            self.color_Signal.emit(43, 182, 105)
            self.color7_icon.setChecked(True)
        elif self.sender() == self.color8_btn:
            self.color_Signal.emit(106, 204, 25)
            self.color8_icon.setChecked(True)
        elif self.sender() == self.color9_btn:
            self.color_Signal.emit(226, 171, 18)
            self.color9_icon.setChecked(True)
        elif self.sender() == self.color10_btn:
            self.color_Signal.emit(255, 143, 87)
            self.color10_icon.setChecked(True)
        elif self.sender() == self.color11_btn:
            self.color_Signal.emit(253, 114, 109)
            self.color11_icon.setChecked(True)
        elif self.sender() == self.color12_btn:
            self.color_Signal.emit(253, 84, 78)
            self.color12_icon.setChecked(True)
        elif self.sender() == self.pane_btn:
            self.color_Signal.emit(self.r_slider.value(), self.g_slider.value(), self.b_slider.value())
            self.pane_icon.setChecked(True)
        elif self.sender() == self.r_slider:
            self.color_Signal.emit(self.r_slider.value(), self.g_slider.value(), self.b_slider.value())
            self.pane_icon.setChecked(True)
        elif self.sender() == self.g_slider:
            self.color_Signal.emit(self.r_slider.value(), self.g_slider.value(), self.b_slider.value())
            self.pane_icon.setChecked(True)
        elif self.sender() == self.b_slider:
            self.color_Signal.emit(self.r_slider.value(), self.g_slider.value(), self.b_slider.value())
            self.pane_icon.setChecked(True)

    def focusInEvent(self, QFocusEvent):
        # print("获得焦点")
        pass

    def focusOutEvent(self, QFocusEvent):
        # print("失去焦点")
        self.close()

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    window = SkinPane()
    window.show()
    sys.exit(app.exec_())
