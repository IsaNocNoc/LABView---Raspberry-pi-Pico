from machine import UART, Pin
from time import sleep_ms

# Configura los pines de los LEDs
pinled1 = Pin(18,Pin.OUT)
pinled2 = Pin(19,Pin.OUT)
pinled3 = Pin(20,Pin.OUT)
pinled4 = Pin(21,Pin.OUT)

# Configura la comunicación UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))

# Asigna cada pin a un bit en el orden correcto
bit_to_pin = {3: pinled4, 2: pinled3, 1: pinled2, 0: pinled1}

while True:
    if uart.any():
        data = uart.read().decode()  # Leer todos los bytes disponibles
        print("Mensaje UART recibido:", data)
        
         # Apaga todos los LEDs
        for pin in bit_to_pin.values():
            pin.off()
        
        # Enciende el LED correspondiente al bit de entrada
        for i, bit in enumerate(data.split(',')[:4]):
            if bit == '1':
                bit_to_pin[i].on()
                
        sleep_ms(100)