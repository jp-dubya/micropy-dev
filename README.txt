This is a MicroPython board

You can get started right away by writing your Python code in 'main.py'.

For a serial prompt:
 - Windows: you need to go to 'Device manager', right click on the unknown device,
   then update the driver software, using the 'pybcdc.inf' file found on this drive.
   Then use a terminal program like Hyperterminal or putty.
 - Mac OS X: use the command: screen /dev/tty.usbmodem*
 - Linux: use the command: screen /dev/ttyACM0

For online docs please visit http://docs.micropython.org/

IDEAS FOR HARDWARE TO CONTROL
1. LED
   a. Turn on/off
   b. PWM
2. Control LED based on motor speed or direction
3. 7-seg display
4. Temperature sensor
   a. I2C
   b. SPI

