To get the UART working on the IO header to communicate with the Emic2 board:

1. In the Raspberry Pi Configuration GUI enable "Serial Port" and disable "Serial Console"

2. Disable Bluetooth on the Raspberry Pi Zero
add the following line to /boot/config.txt

dtoverlay=pi3-disable-bt

To run the program on boot add the following line to /etc/rc.local

sudo python3 /home/pi/project/emic2_projects/push_for_affirmation_nt.py &
