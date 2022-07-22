import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    String_data = ser.readline()
    print(String_data)
ser.close()
