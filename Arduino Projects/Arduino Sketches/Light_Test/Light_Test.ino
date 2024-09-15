// Ian Coffey
// Light_Test.INO
// To Turn On An LED

// Variable Declarations
const int redPin = 6;
const int greenPin = 5;

// Setup
void setup() 
{
  // Set PinModes To Respective Functions
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  
}

void loop() 
{
  digitalWrite(greenPin, HIGH);
  digitalWrite(greenPin, HIGH);
}
