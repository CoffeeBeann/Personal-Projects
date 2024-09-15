// Ian Coffey
// RGB.ino

// Variable Declaration
const int light1 = 13;
const int light2 = 12;
const int light3 = 11;
const int light4 = 10;
const int light5 = 9;
const int light6 = 8;
const int light7 = 7;
const int light8 = 6;
const int bluePin = 5;
const int greenPin = 4;
const int redPin = 3;
int delay_time = 750;
int delay_color = 500;

void setup() {

    Serial.begin(9600);
    pinMode(bluePin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(redPin, OUTPUT);
    pinMode(light1, OUTPUT);
    pinMode(light2, OUTPUT);
    pinMode(light3, OUTPUT);
    pinMode(light4, OUTPUT);
    pinMode(light5, OUTPUT);
    pinMode(light6, OUTPUT);
    pinMode(light7, OUTPUT);
    pinMode(light8, OUTPUT);
      
}

void loop() {

    // 9 digit
    digitalWrite(light1, HIGH);
    digitalWrite(light2, HIGH);
    digitalWrite(light3, HIGH);
    digitalWrite(light4, HIGH);
    digitalWrite(light5, LOW);
    digitalWrite(light6, LOW);
    digitalWrite(light7, HIGH);
    digitalWrite(light8, HIGH);
    delay(delay_time);
    
    // 8 digit
    digitalWrite(light5, HIGH);
    digitalWrite(light6, HIGH);
    delay(delay_time);
    
    // 7 digit
    digitalWrite(light1, LOW);
    digitalWrite(light2, LOW);
    digitalWrite(light5, LOW);
    digitalWrite(light6, LOW);
    delay(delay_time);
    
    // 6 digit
    digitalWrite(light1, HIGH);
    digitalWrite(light2, HIGH);
    digitalWrite(light4, LOW);
    digitalWrite(light5, HIGH);
    digitalWrite(light6, HIGH);
    delay(delay_time);
    
    // 5 digit
    digitalWrite(light5, LOW);
    delay(delay_time);
    
    // 4 digit
    digitalWrite(light3, LOW);
    digitalWrite(light4, HIGH);
    digitalWrite(light6, LOW);
    delay(delay_time);
    
    // 3 digit
    digitalWrite(light2, LOW);
    digitalWrite(light3, HIGH);
    digitalWrite(light6, HIGH);
    delay(delay_time); 
    
    // 2 digit
    digitalWrite(light5, HIGH);
    digitalWrite(light7, LOW);
    delay(delay_time); 
    
    // 1 digit
    digitalWrite(light1, LOW);
    digitalWrite(light3, LOW);
    digitalWrite(light5, LOW);
    digitalWrite(light6, LOW);
    digitalWrite(light7, HIGH);
    delay(delay_time); 
    
    // 0 digit
    digitalWrite(light2, HIGH);
    digitalWrite(light3, HIGH);
    digitalWrite(light4, HIGH);
    digitalWrite(light5, HIGH);
    digitalWrite(light6, HIGH);
    delay(delay_time); 

    // Turn Off 7 Segment Display
    digitalWrite(light2, LOW);
    digitalWrite(light3, LOW);
    digitalWrite(light4, LOW);
    digitalWrite(light5, LOW);
    digitalWrite(light6, LOW);
    digitalWrite(light7, LOW);
    digitalWrite(light8, LOW);

        // RGB Light Pattern   
    // Red
    digitalWrite(redPin, HIGH);
    delay(delay_color);

    // Yellow
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, HIGH);
    digitalWrite(greenPin, HIGH);
    delay(delay_color);

    // Green
    digitalWrite(bluePin, LOW);
    delay(delay_color);

    // Blue
    digitalWrite(bluePin, HIGH);
    digitalWrite(greenPin, LOW);
    delay(delay_color);

    // Violet
    digitalWrite(redPin, HIGH);
    delay(delay_color);

    // Turn Colors Off
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, LOW);
    digitalWrite(greenPin, LOW);
    
}







