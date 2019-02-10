import RPi.GPIO as GPIO
import serial
import time

quote_array = []

def wait_for_ready():
    while True:
        serial.write(str.encode("\n"))
        time.sleep(0.5)
        data = serial.read()
        if data.decode() == ':':
            break
        else:
            time.sleep(0.5)
            

def button_callback(indx):
    buffer = "S%s" % (quote_array[indx])
    #print("index = ", indx, "\n")
    #buffer = "Sdon't push me"
    serial.write(buffer.encode())
    wait_for_ready()


# Load the array of quotes from a text file
f = open("/home/pi/project/emic2/quotefile.txt", "r")
for x in f:
    quote_array.append(x)
#print("Array length = ",len(quote_array),"\n")

# Initialise the serial port UART
serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
serial.write(str.encode("\n"))
time.sleep(1)
serial.write(str.encode("V15\n")) # Adjust volume
wait_for_ready()
#print("Ready...\n")
serial.write(str.encode("Sready"))
wait_for_ready()

# Set up the GPIO for the button input
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Wait for buton press
indx = 0
while True:
    if GPIO.input(15) == GPIO.LOW:
        time.sleep(0.01)
    else:
        button_callback(indx)
        indx += 1
        time.sleep(1)
    if indx == len(quote_array):
        indx = 0 
        #break

serial.write(str.encode("Send of list"))
wait_for_ready()
GPIO.cleanup() # Clean up
