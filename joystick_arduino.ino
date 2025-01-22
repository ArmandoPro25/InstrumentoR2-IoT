
const int xPin = 34;
const int yPin = 35;


const int redPin = 15;
const int greenPin = 2;  
const int bluePin = 4;   

void setup() {

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);


  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
}

void loop() {
  int xValue = analogRead(xPin); 
  int yValue = analogRead(yPin);


  if (yValue > 3000) { 
    setColor(255, 0, 0); 
  } else if (yValue < 1000) { 
    setColor(0, 0, 255); 
  } else if (xValue > 3000) { 
    setColor(0, 255, 0); 
  } else if (xValue < 1000) { 
    setColor(255, 255, 0); 
  } else { 
    setColor(0, 0, 0); 
  }

  delay(100);
}


void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
