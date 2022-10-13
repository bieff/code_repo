# 生成图片验证码
import random
import string
from PIL import Image,ImageDraw,ImageFont,ImageFilter
class CodeImage():
    def __init__(self):
        self.font_path = 'Arial.ttf'
        self.number = 4
        self.size = (100, 30)
        self.bgcolor = (255, 255, 255)
        self.fontcolor = (0, 0, 255)
        self.linecolor = (255, 0, 0)
        self.draw_line = True
        self.line_number = (1, 5)
        self.code_text = None # 验证码文本

    def gene_text(self):
        source = list(string.ascii_letters)
        for index in range(0, 10):
            source.append(str(index))
        return ''.join(random.sample(source, self.number))

    def gene_line(self, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill = self.linecolor)

    def gene_code(self):
        width,height = self.size
        image = Image.new('RGBA', (width, height), self.bgcolor)
        font = ImageFont.truetype(self.font_path, 25)
        draw = ImageDraw.Draw(image)
        self.code_text = self.gene_text()
        font_width, font_height = font.getsize(self.code_text)
        draw.text(((width - font_width) / self.number, (height - font_height) / self.number), self.code_text, font= font, fill = self.fontcolor)
        if self.draw_line:
            self.gene_line(draw, width, height)
        image = image.transform((width+20, height+10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
        self.code_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # self.code_image.save('idencode.png')
if __name__ == "__main__":
    codeimage = CodeImage()
    image = codeimage.gene_code()
    code_text = codeimage.code_text
    codeimage.code_image.save('idencode.png')
    print(code_text)
