import RPi.GPIO as GPIO
import threading
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

class ButtonHandler(threading.Thread):
    def __init__(self, pin, func, edge='both', bouncetime=200):
        super().__init__(daemon=True)

        self.edge = edge
        self.func = func
        self.pin = pin
        self.bouncetime = float(bouncetime)/1000
        self.indx = 0

        self.lastpinval = GPIO.input(self.pin)
        self.lock = threading.Lock()

    def __call__(self, *args):
        if not self.lock.acquire(blocking=False):
            return

        t = threading.Timer(self.bouncetime, self.read, args=args)
        t.start()

    def read(self, *args):
        self.func(self.indx)
        self.indx += 1
        self.lock.release()

        #pinval = GPIO.input(self.pin)

        #if (
        #        ((pinval == 0 and self.lastpinval == 1) and
        #         (self.edge in ['falling', 'both'])) or
        #        ((pinval == 1 and self.lastpinval == 0) and
        #         (self.edge in ['rising', 'both']))
        #):
        #    self.func(self.indx)
        #    self.indx += 1

        #self.lastpinval = pinval
        #self.lock.release()

serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
serial.write(str.encode("\n"))
time.sleep(1)
serial.write(str.encode("V15\n")) # Adjust volume
wait_for_ready()
#print("Ready...\n")
serial.write(str.encode("Sready"))
wait_for_ready()

f = open("quotefile.txt", "r")
for x in f:
    quote_array.append(x)

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
cb = ButtonHandler(15, button_callback, edge='rising', bouncetime=100)
cb.start()
GPIO.add_event_detect(15, GPIO.RISING, callback=cb)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
