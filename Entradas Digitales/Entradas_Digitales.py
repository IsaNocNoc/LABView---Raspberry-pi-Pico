from time import sleep_ms
from machine import Pin, UART

# Configura el pin 15 como entrada con un pull-down interno
boton = Pin(13, Pin.IN, Pin.PULL_DOWN)
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))

mensaje = '0'
uart.write(mensaje)
print(mensaje)

while True:
    # Si el botón está presionado (UP), enciende el LED
    if boton.value() == 1:
        mensaje = '1'
        uart.write(mensaje)
        print(mensaje)
    else:
        mensaje = '0'
        uart.write(mensaje)
        print(mensaje)
    sleep_ms(100)
