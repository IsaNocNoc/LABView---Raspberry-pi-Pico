from machine import Pin, PWM, UART
import time

# Configurar el pin del servo motor
servo_pin = 2
servo_pwm = PWM(Pin(servo_pin))

# Configurar la UART
uart = UART(0, baudrate=115200, rx=Pin(1), tx=Pin(0)) # Ajusta los pines tx y rx según la conexión física

def set_servo_angle(angle):
    min_pulse = 1311
    max_pulse = 7866
    pulse_width = int(((angle / 180) * (max_pulse - min_pulse)) + min_pulse)
    servo_pwm.duty_u16(pulse_width)  # Escala el valor del pulso para que esté en el rango correcto

while True:
    if uart.any():
        data = uart.readline().decode().strip()
        try:
            angle = int(data)
            set_servo_angle(angle)
            print(f'Servo motor configurado a {angle} grados')
        except ValueError:
            print('Entrada no válida. Introduce un valor numérico para el ángulo del servo.')

    time.sleep(0.1)