// Ian Coffey
// Photoresistor.ino

// Variable Declaration
int pResistor = 0;
int pReading;
int LEDbrightness;
int ledPin = 11;

void setup() {

  Serial.begin(9600);

}

void loop() {

    pReading = analogRead(pResistor);

    pReading = 1023 - pReading;

    LEDbrightness = map(pReading, 0 , 1023, 0, 255);
    analogWrite(ledPin, LEDbrightness);

    delay(100);
  

}
