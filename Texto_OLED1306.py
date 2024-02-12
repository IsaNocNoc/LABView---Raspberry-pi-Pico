from easy_comms import Easy_comms
from time import sleep
from machine import I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
oled = SSD1306_I2C(128,64, i2c)
com1 = Easy_comms(uart_id=0, baud_rate=115200, tx=0, rx=1)
com1.start()

def display_oled(mensaje):
    oled.fill(0)
    oled.text(mensaje,0,0)
    oled.show()

while True:
    message = ""
    message = com1.read()
    
    if message is not None:
        print(f"message received: {message.strip('\n')}")
        display_oled(message)
    sleep(1)
