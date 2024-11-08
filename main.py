import time
import micropython
import pyb

# Setup
led = pyb.LED(1)
button = pyb.Switch()
rtc = pyb.RTC()
adc = pyb.ADC(pyb.Pin.board.PA0)
uart = pyb.UART(2, 9600)

micropython.alloc_emergency_exception_buf(100)

def read_temperature():
    raw = adc.read()
    voltage = (raw * 3.3) / 4095
    return ((voltage - 0.76) / 0.0025) + 25

def log_data():
    datetime = rtc.datetime()
    temperature = read_temperature()
    with open('log.txt', 'a') as f:
        f.write(f"{datetime[0]}-{datetime[1]}-{datetime[2]} {datetime[4]}:{datetime[5]}:{datetime[6]}, Temp: {temperature:.2f}°C\n")

def button_callback(line):
    print("Button pressed!")
    led.toggle()

button_pin = pyb.Pin('PC13', pyb.Pin.IN, pyb.Pin.PULL_UP)
button_pin.irq(trigger=pyb.Pin.IRQ_FALLING, handler=button_callback)

print("NUCLEO-L476RG MicroPython Demo")
print("Press the user button to light up the LED")

while True:
    if button.value():  # Check if the button is pressed
        led.on()  # Turn on the LED
        print("Button pressed - LED ON")
    else:
        led.off()  # Turn off the LED when the button is not pressed
    
    time.sleep(0.1)  # Small delay to prevent excessive CPU usage
