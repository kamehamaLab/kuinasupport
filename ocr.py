import os
from PIL import Image, ImageFilter
import pyocr
import csv
import datetime
from picamera import PiCamera
from time import sleep


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def clip_img(img):
    im_crop1 = img.crop((132, 97, 167, 150))
    im_crop2 = img.crop((173, 95, 209, 152))
    im_crop3 = img.crop((209, 96, 245, 152))
    im_crop4 = img.crop((334, 110, 357, 165))
    im_crop5 = img.crop((359, 106, 398, 173))
    im_crop6 = img.crop((402, 107, 439, 174))
    im_crop7 = img.crop((549, 111, 580, 158))
    im_crop8 = img.crop((586, 114, 616, 158))
    im_crop9 = img.crop((614, 114, 643, 159))
    return (im_crop1, im_crop2, im_crop3, im_crop4, im_crop5, im_crop6, im_crop7, im_crop8, im_crop9)

#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C://Program Files//Tesseract-OCR//'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
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

camera = PiCamera()



def main():
    camera.start_preview()
    sleep(5) # このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
    dt_now_str = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    img_name = 'images/image' + dt_now_str + '.jpg'
    camera.capture(img_name)
    img = Image.open(img_name)
    img = img.rotate(180)
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    clim1, clim2, clim3, clim4, clim5, clim6, clim7, clim8, clim9 = clip_img(img)
    text1 = tool.image_to_string(clim1, lang="eng", builder=builder)
    text2 = tool.image_to_string(clim2, lang="eng", builder=builder)
    text3 = tool.image_to_string(clim3, lang="eng", builder=builder)
    text4 = tool.image_to_string(clim4, lang="eng", builder=builder)
    text5 = tool.image_to_string(clim5, lang="eng", builder=builder)
    text6 = tool.image_to_string(clim6, lang="eng", builder=builder)
    text7 = tool.image_to_string(clim7, lang="eng", builder=builder)
    text8 = tool.image_to_string(clim8, lang="eng", builder=builder)
    text9 = tool.image_to_string(clim9, lang="eng", builder=builder)
    with open('Logs/batteryLog.csv', 'a') as f:
            dt_now = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
            writer = csv.writer(f)
            writer.writerow([dt_now, (text1+text2+text3), (text4+text5+text6), (text7+text8+text9)])




if __name__ == "__main__":

    while True:
        try:
            main()
            sleep(3600)

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