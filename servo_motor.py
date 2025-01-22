from machine import Pin, PWM
from time import sleep
from dht import DHT22

# Configuración del sensor DHT22 y servos
sensor = DHT22(Pin(15))
servo1 = PWM(Pin(2), freq=50)
servo2 = PWM(Pin(4), freq=50)

def set_servo_angle(servo, angle):
    duty = int((angle / 180) * 1024 + 1024 / 18)
    servo.duty_u16(duty)

while True:
    try:
        sensor.measure()
        humidity = sensor.humidity()

        # Controlar servo1 según la humedad
        if humidity < 30:
            set_servo_angle(servo1, 90)
        else:
            set_servo_angle(servo1, 0)

        # Controlar servo2 según la humedad
        if humidity < 50:
            set_servo_angle(servo2, 90)
        else:
            set_servo_angle(servo2, 0)

        sleep(2) 

    except Exception as e:
        print("Error al leer el sensor:", e)
        sleep(2)
