import serial
import time

serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
#serial.open()
serial.write(str.encode("\n"))
time.sleep(1)
serial.write("V15\n") # Adjust volume
c = 0
while True:
        serial.write(str.encode("\n"))
        time.sleep(0.75)
        data = serial.read()
        if data == ':':
                buffer = "S%d" % (c)
                c = c + 1
                serial.write(str.encode(buffer))
                time.sleep(0.5)
        else:
                time.sleep(0.5)

serial.close()