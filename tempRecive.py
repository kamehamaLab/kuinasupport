import serial
import csv

ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    String_data = ser.readline().strip()
    float_data = float(String_data)
    print(float_data)
    with open('Logs/temp.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([str(float_data)])
ser.close()
