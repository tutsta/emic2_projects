import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import serial
import time

quote_array = []
idx = 0

def wait_for_ready():
    while True:
        serial.write(str.encode("\n"))
        time.sleep(0.5)
        data = serial.read()
        if data.decode() == ':':
            break
        else:
            time.sleep(0.5)
            

def button_callback(channel):
    #buffer = "S%s" % (quote_array[idx])
    buffer = "Spush me"
    print(buffer + "\n")
    serial.write(buffer.encode())
    wait_for_ready()
    #idx += 1

    
serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
serial.write(str.encode("\n"))
time.sleep(1)
serial.write(str.encode("V15\n")) # Adjust volume
wait_for_ready()
print("Ready...\n")

f = open("quotefile.txt", "r")
for x in f:
  quote_array.append(x)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 15 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback, bouncetime = 2000) # Setup event on pin 15 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up