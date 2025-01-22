#import para acceso a red
import network
#Para usar protocolo MQTT
from umqtt.simple import MQTTClient
from machine import Pin, ADC
from time import sleep

#Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "gds0642/jarm"
MQTT_PORT = 1883
MQTT_TOPIC_PUBLISH = "gds0642/arm/potenciometro"

#Función para conectar a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
        print("WiFi Conectada!")

#Funcion encargada de encender un led cuando un mensaje se lo diga
def llegada_mensaje(topic, msg):
    print("Mensaje:", msg)
    if msg == b'1':
        ledRed.value(1)
    if msg == b'0':
        ledRed.value(0)
    if msg == b'3':
        ledGreen.value(1)
    if msg == b'2':
        ledGreen.value(0)
    if msg == b'5':
        ledBlue.value(1)
    if msg == b'4':
        ledBlue.value(0)
    if msg == b'7':
        ledYellow.value(1)
    if msg == b'6':
        ledYellow.value(0)
    if msg == b'9':
        ledWhite.value(1)
    if msg == b'8':
        ledWhite.value(0)
    


#Funcion para subscribir al broker, topic
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
    MQTT_BROKER, port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASSWORD,
    keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC_PUBLISH)
    print("Conectado a %s, en el topico %s"%(MQTT_BROKER, MQTT_TOPIC_PUBLISH))
    return client

#Declaro el pin led
ledRed = Pin(21, Pin.OUT)
ledRed.value(0)
ledGreen = Pin(19, Pin.OUT)
ledGreen.value(0)
ledBlue = Pin(18, Pin.OUT)
ledBlue.value(0)
ledYellow = Pin(5, Pin.OUT)
ledYellow.value(0)
ledWhite = Pin(17, Pin.OUT)
ledWhite.value(0)

#Configurar potenciometro
potenciometro = ADC(Pin(34))
potenciometro.atten(ADC.ATTN_11DB)
potenciometro.width(ADC.WIDTH_10BIT)

#Conectar a wifi
conectar_wifi()
#Subscripción a un broker mqtt
client = subscribir()

#Ciclo infinito
while True:
    client.wait_msg()
    #Leer valor de potenciometro
    valor = int(potenciometro.read() * 100 / 1023)
    client.publish(MQTT_TOPIC_PUBLISH, str(valor))
    sleep(1)