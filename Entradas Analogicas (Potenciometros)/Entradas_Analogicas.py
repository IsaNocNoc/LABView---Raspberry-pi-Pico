from machine import ADC, UART, Pin
import utime

# Crear una instancia ADC en los pines GP26 y GP27
adc1 = ADC(Pin(26))
adc2 = ADC(Pin(27))

# Configurar UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))
# Variables
varA0 = 0
varA1 = 0
msegi = utime.ticks_ms()

# Bucle principal
while True:
    varA0 = adc1.read_u16()  # Leer el valor del ADC1
    varA1 = adc2.read_u16()  # Leer el valor del ADC2
    msegf = utime.ticks_ms()  # Obtener el tiempo actual en milisegundos
    if utime.ticks_diff(msegf, msegi) >= 100:  # Si han pasado 100 ms
        msegi = msegf  # Actualizar el tiempo inicial
        uart.write('{},{}\n'.format(varA0, varA1))  # Línea corregida
