import os
from PIL import Image, ImageFilter
import pyocr
import csv
import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5) # このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
dt_now_str = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
img_name = 'images/image' + dt_now_str + '.jpg'
camera.capture(img_name)