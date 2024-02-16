from machine import UART, Pin
from time import sleep_ms
import utime

# Configura los pines de los LEDs
pinled1 = Pin(17,Pin.OUT)
pinled2 = Pin(16,Pin.OUT)
pinled3 = Pin(13,Pin.OUT)
pinled4 = Pin(12,Pin.OUT)

pinbutton1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
pinbutton2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
pinbutton3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
pinbutton4 = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Configura la comunicación UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))

# Asigna cada pin a un bit en el orden correcto
bit_to_pin = {3: pinled4, 2: pinled3, 1: pinled2, 0: pinled1}

#el comando ticks hace el calculo de diferencia de tiempos
msegi = utime.ticks_ms()

while True:
    try:
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
                
        var1 = pinbutton1.value()
        var2 = pinbutton2.value()
        var3 = pinbutton3.value()
        var4 = pinbutton4.value()
        
        msegf = utime.ticks_ms()
        if utime.ticks_diff(msegf, msegi) >= 100:
            msegi = msegf
            uart.write('{},{},{},{}\n'.format(var1, var2, var3, var4))
                
        sleep_ms(100)
        
    except Exception as e:
        print("Ha ocurrido un error: ", e)