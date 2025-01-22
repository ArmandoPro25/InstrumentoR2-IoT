from machine import Pin, time_pulse_us
from time import sleep_us, sleep

PIN_TRIG = 15
PIN_ECHO = 4

trig = Pin(PIN_TRIG, Pin.OUT)
echo = Pin(PIN_ECHO, Pin.IN)

def measure_distance():
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, 30000)  # 3o ms
    if duration > 0:
        distance_cm = duration / 58.0
        return distance_cm
    else:
        return None, None

while True:
    distancia = measure_distance()
    if distancia is not None:
        print("Distancia: {:.2f}".format(distance_cm))
    else:
        print("No se puede sacar la distancia")
    sleep(1)
