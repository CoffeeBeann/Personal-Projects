// Ian Coffey
// Ball_Switch.INO
// To Play A Buzzer And Light An LED When A Tilt Is Detected

// Variable Declarations
const int tilt = 8;
const int buzzer = 11;
const int photoResistor = 0;
const int redPin = 5;
const int greenPin = 6;
int tiltState;
int lightValue = 0;

// Setup
void setup()
{ 
  // Set Serial Communications To 9600 Bytes
  Serial.begin(9600);
  
  // Set PinModes To Respective Functions
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(photoResistor, INPUT);

  // Provide Power TO Tilt Switch
  digitalWrite(tilt, HIGH);
} 

void loop() 
{  
  // Read In Tilt State
  tiltState = digitalRead(tilt);
  lightValue = analogRead(photoResistor);

  // Output Analog Value To Console
  Serial.println(lightValue);
  
  if(tiltState == HIGH)
  {
    // Turn On LED To Red And PLay Buzzer
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    tone(buzzer, 2500, 1);
  }
  else
  {
    // Turn LED To Green And Buzzer Off
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(buzzer, LOW);
  }

  // Add A 10 Millisecond Delay
  delay(10);
}


