import csv
import datetime
from picamera import PiCamera
from time import sleep
import smbus
import os

camera = PiCamera()
bus = smbus.SMBus(1)
address_adt7410 = 0x48
register_adt7410 = 0x00
configration_adt7410 = 0x03

if not os.path.exists('Logs'):
    os.makedirs('Logs')

while True:
    bus.write_word_data(address_adt7410, configration_adt7410, 0x00)
    word_data = bus.read_word_data(address_adt7410, register_adt7410)
    data = (word_data & 0xff00) >> 8 | (word_data & 0xff) << 8
    data = data >> 3
    data = data/16.
    with open('Logs/TempLog.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str,str(data)])
        #print("save temp")

    camera.start_preview()
    sleep(5) # このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
    dt_now_str = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    camera.capture('images/image' + dt_now_str + '.jpg')
    #print("imageSaved")
    camera.stop_preview()

    sleep(10)

ser.close()
