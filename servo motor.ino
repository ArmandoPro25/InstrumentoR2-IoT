#include <Servo.h>

Servo servoMotor;

#define SERVO_PIN 18

void setup() {
  servoMotor.attach(SERVO_PIN);
  servoMotor.write(0);
  delay(1000);
}

void loop() {
  servoMotor.write(90);
  delay(1000);
}
