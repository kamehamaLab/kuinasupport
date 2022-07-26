import serial
import csv
import datetime
from picamera import PiCamera
from time import sleep
from GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive
from InitialValue import KEYFILE, BATTERYIMAGESDIRID

camera = PiCamera()
ser = serial.Serial('/dev/ttyACM0', 115200)

keyFile = KEYFILE
dirname = "BatteryImages/"
updirID = BATTERYIMAGESDIRID

while True:
    String_data = ser.readline().strip()
    float_data = float(String_data)
    with open('Logs/TempLog.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str,str(float_data)])
        print("save temp")

    camera.start_preview()
    sleep(5)#このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
    dt_now_str = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    filename = dt_now_str + '.jpg'
    filepath = dirname + filename
    camera.capture(filepath)
    print("imageSaved")
    camera.stop_preview()

    fileID = uploadFileToGoogleDrive(filename, filepath, updirID, keyFile, "image/jpeg")
    os.remove(filepath)

    sleep(3600)

ser.close()
