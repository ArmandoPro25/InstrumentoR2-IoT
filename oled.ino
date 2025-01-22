#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHTesp.h>

int sensorPin = 15;
DHTesp sensor;

Adafruit_SSD1306 oled(128, 64, &Wire, -1);
  void setup(){
    oled.begin(SSD1306_SWITCHCAPVCC, 0X3C);
    oled.clearDisplay();
    oled.setTextSize(3);
    pinMode(sensorPin, INPUT);
    sensor.setup(sensorPin, DHTesp::DHT22);
  }
void loop(){
  TempAndHumidity values = sensor.getTempAndHumidity();
  float t = values.temperature;
  float h = values.humidity;
  oled.setCursor(1,1);
  oled.println("Holaaa!!!!");
  oled.display();
}

