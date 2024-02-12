from machine import UART, Pin
from time import sleep_ms

# Configura los pines de los LEDs
pinled1 = Pin(18,Pin.OUT)

# Configura la comunicación UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))


while True:
    if uart.any():
        data = uart.read(6)  # Leer 5 bytes
        print("Mensaje UART recibido:", data)
        sleep_ms(100)
        

