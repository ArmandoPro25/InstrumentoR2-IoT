from machine import Pin, ADC
import time


x_pin = ADC(Pin(34)) 
y_pin = ADC(Pin(35))  
x_pin.atten(ADC.ATTN_11DB)
y_pin.atten(ADC.ATTN_11DB)


red = Pin(15, Pin.OUT)   
green = Pin(2, Pin.OUT)  
blue = Pin(4, Pin.OUT)   


def set_color(r, g, b):
    red.value(r)
    green.value(g)
    blue.value(b)

while True:
    x_value = x_pin.read()
    y_value = y_pin.read()


    if y_value > 3000:
        set_color(1, 0, 0)
    elif y_value < 1000:
        set_color(0, 0, 1) 
    elif x_value > 3000:  
        set_color(0, 1, 0)  
    elif x_value < 1000:  
        set_color(1, 1, 0)  
    else:  
        set_color(0, 0, 0)  

    time.sleep(0.1)
