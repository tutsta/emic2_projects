import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 15 to be an input pin and set initial value to be pulled low (off)

counter = 0

while True:
    if GPIO.input(15) == GPIO.LOW:
        time.sleep(0.01)
    else:
        print("Button pushed: ",counter,"\n")
        time.sleep(1)
        counter += 1
    if counter == 10:
        break

GPIO.cleanup() # Clean up


