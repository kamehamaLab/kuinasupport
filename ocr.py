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

def clip_img(img):
    im_crop1 = img.crop(a, b, c, d)
    im_crop2 = img.crop(a, b, c, d)
    im_crop3 = img.crop(a, b, c, d)
    im_crop4 = img.crop(a, b, c, d)
    im_crop5 = img.crop(a, b, c, d)
    im_crop6 = img.crop(a, b, c, d)
    return (im_crop1, im_crop2, im_crop3, im_crop4, im_crop5, im_crop6)

#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C://Program Files//Tesseract-OCR//'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

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

def main():
    img = Image.open('images/dataset/0/0-2.jpg')
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    clim1, clim2, clim3, clim4, clim5, clim6 = clip_img(img)
    text1 = tool.image_to_string(clim1, lang="eng", builder=builder)
    text2 = tool.image_to_string(clim2, lang="eng", builder=builder)
    text3 = tool.image_to_string(clim3, lang="eng", builder=builder)
    text4 = tool.image_to_string(clim4, lang="eng", builder=builder)
    text5 = tool.image_to_string(clim5, lang="eng", builder=builder)
    text6 = tool.image_to_string(clim6, lang="eng", builder=builder)
    with open('Logs/deleteLog.csv', 'a') as f:
            dt_now = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
            writer = csv.writer(f)
            writer.writerow([dt_now, ])




if __name__ == "__main__":

    while True:
        try:
            main()

        except KeyboardInterrupt:
            print("Ctrl+C finished")
            break

        except BrokenPipeError:
            print("BrokenPipeError")
            print("reconnect")

        except ConnectionResetError:
            print("ConnectionResetError")
            print("reconnect")

        except Exception as e:
            print("unexpected error")
            print(e)