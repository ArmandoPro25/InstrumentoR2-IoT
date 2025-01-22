from machine import Pin, I2C
from time import sleep
from dht import DHT22
from ssd1306 import SSD1306_I2C

sensor_pin = Pin(15)
sensor = DHT22(sensor_pin)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        oled.fill(0)
        oled.text("Holaaa!!!!", 0, 0)
        oled.text("Temp: {:.1f}C".format(t), 0, 20)
        oled.text("Hum: {:.1f}%".format(h), 0, 40)
        oled.show()
    except Exception as e:
        oled.fill(0)
        oled.text("Error", 0, 0)
        oled.show()
    sleep(1)
