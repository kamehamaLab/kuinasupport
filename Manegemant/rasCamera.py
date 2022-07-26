from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)#このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
camera.capture('image.jpg')
camera.stop_preview()
