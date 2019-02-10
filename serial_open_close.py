import serial

serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)

serial.close()
