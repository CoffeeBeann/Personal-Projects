// Ian Coffey
// RGB.ino

// Variable Declaration
const int bluePin = 11;
const int greenPin = 10;
const int redPin = 9;
int delay_time = 500;

void setup() {

    Serial.begin(9600);
    pinMode(bluePin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(redPin, OUTPUT);
      
}

void loop() {

    // Purple
    digitalWrite(redPin, HIGH);
    digitalWrite(bluePin, HIGH);
    
}







