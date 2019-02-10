import serial
import time

def wait_for_ready():
    while True:
        serial.write("\n")
        time.sleep(0.75)
        data = serial.read()
        if data == ':':
            break
        else:
            time.sleep(0.1)


serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
#serial.open()
serial.write("\n")
time.sleep(1)
serial.write("V15\n") # Adjust volume

wait_for_ready()
input_text = input("Input text: ")
buffer = "S%s" % (input_text)
serial.write(buffer)
time.sleep(0.5)
serial.close()
