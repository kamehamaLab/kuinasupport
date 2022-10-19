import os
from PIL import Image, ImageFilter
import pyocr


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C://Program Files//Tesseract-OCR//'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#文字を抽出したい画像のパスを選ぶ
img = Image.open('images/dataset/0/0-2.jpg')
img = add_margin(img, 50, 50, 50, 50, (0, 0, 0))
img = img.filter(ImageFilter.GaussianBlur(radius=2))
img.save("test.jpg")

#画像の文字を抽出
builder = pyocr.builders.DigitBuilder(tesseract_layout=8)
# 0    Orientation and script detection (OSD) only.
#  1    Automatic page segmentation with OSD.
#  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#  3    Fully automatic page segmentation, but no OSD. (Default)
#  4    Assume a single column of text of variable sizes.
#  5    Assume a single uniform block of vertically aligned text.
#  6    Assume a single uniform block of text.
#  7    Treat the image as a single text line.
#  8    Treat the image as a single word.
#  9    Treat the image as a single word in a circle.
# 10    Treat the image as a single character.
# 11    Sparse text. Find as much text as possible in no particular order.
# 12    Sparse text with OSD.
# 13    Raw line. Treat the image as a single text line,
#       bypassing hacks that are Tesseract-specific.



text = tool.image_to_string(img, lang="eng", builder=builder)

print(text)
