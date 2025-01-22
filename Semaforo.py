from machine import Pin 
from dht import DHT22
from time import sleep
ledVerde = Pin(32, Pin.OUT)  
ledAmarillo = Pin(25, Pin.OUT) 
ledRojo = Pin(14, Pin.OUT)

sensor = DHT22(Pin(15))

while True:
    sensor.measure()
    temperatura = sensor.temperature()
    humedad = sensor.humidity()

    print("Temperatura: %3.1f °C" % temperatura)
    print("Humedad: %3.0f %%" % humedad)
    
    if temperatura < 30:
        ledVerde.on()
        ledAmarillo.off()
        ledRojo.off()
    elif 30 <= temperatura < 50:
        ledVerde.off()
        ledAmarillo.on()
        ledRojo.off()
    else: 
        ledVerde.off()
        ledAmarillo.off()
        ledRojo.on()
    sleep(1)