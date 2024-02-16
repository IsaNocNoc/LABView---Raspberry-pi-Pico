from machine import ADC, UART, Pin
from time import sleep_ms
import utime

# Crear una instancia ADC en el pin GP26
adc = ADC(Pin(26))

# Configurar UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))

# Variables
varA0 = 0
msegi = utime.ticks_ms()

# Bucle principal
while True:
    varA0 = adc.read_u16()  # Leer el valor del ADC
    msegf = utime.ticks_ms()  # Obtener el tiempo actual en milisegundos
    if utime.ticks_diff(msegf, msegi) >= 100:  # Si han pasado 100 ms
        msegi = msegf  # Actualizar el tiempo inicial
        uart.write(str(varA0) + '\n')  # Enviar el valor del ADC a través de UART
        
#uart.write('Voltaje: {} V\n'.format(voltaje))  # Enviar el valor del voltaje a través de UART

