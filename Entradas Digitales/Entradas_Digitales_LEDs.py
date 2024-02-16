from machine import Pin, UART
import utime
from time import sleep_ms

# Configura los pines como entrada con un pull-down interno
pinbutton1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
pinbutton2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
pinbutton3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
pinbutton4 = Pin(21, Pin.IN, Pin.PULL_DOWN)

#conexion UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0))
#el comando ticks hace el calculo de diferencia de tiempos
msegi = utime.ticks_ms()

while True:
    try:
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