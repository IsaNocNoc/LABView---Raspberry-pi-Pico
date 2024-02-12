import machine
import ssd1306
import time


# Set up the OLED display
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Set up the UART communication
uart= machine.UART(0, baudrate=115200, rx=machine.Pin(1), tx=machine.Pin(0))

# Set up the LED pin
led = machine.Pin(25, machine.Pin.OUT)

# Function to turn the LED on
def led_on():
    led.value(1)
    oled.fill(0)
    oled.text("LED ON", 0, 0)
    oled.show()

# Function to turn the LED off
def led_off():
    led.value(0)
    oled.fill(0)
    oled.text("LED OFF", 0, 0)
    oled.show()

# Main loop
while True:
    if uart.any():
        data = uart.read()
        if data == b'1':
            led_on()
        elif data == b'0':
            led_off()