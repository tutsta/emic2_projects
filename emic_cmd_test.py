import serial
import time


def wait_for_ready():
    while True:
        serial.write(str.encode("\n"))
        time.sleep(0.5)
        data = serial.read()
        if data.decode() == ':':
            break
        else:
            time.sleep(0.5)


serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
serial.write(str.encode("\n"))
time.sleep(1)
serial.write(str.encode("V15\n")) # Adjust volume

wait_for_ready()
while True:
    input_text = input("Input command (q to end): ")
    if input_text.lower() == 'q':
        break
    else:
        buffer = "%s" % (input_text)
        serial.write(buffer.encode())
        wait_for_ready()

time.sleep(0.5)
serial.close()
