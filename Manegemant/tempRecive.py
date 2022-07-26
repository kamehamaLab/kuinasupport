import serial
import csv
import datetime

ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    String_data = ser.readline().strip()
    float_data = float(String_data)
    with open('Logs/temp.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str,str(float_data)])
ser.close()
