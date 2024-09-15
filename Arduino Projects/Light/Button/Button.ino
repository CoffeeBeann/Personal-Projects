// Ian Coffey
// 7 Segment Display

// Variable Declaration
const int light1 = 13; 
const int light2 = 12;
const int light3 = 11;
const int light4 = 10;
const int light5 = 9;
const int light6 = 8;
const int light7 = 7;
const int light8 = 6;
const int test = 3;
int delay_time = 100;

void setup() {

  Serial.begin(9600);
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  pinMode(light3, OUTPUT);
  pinMode(light4, OUTPUT);
  pinMode(light5, OUTPUT);
  pinMode(light6, OUTPUT);
  pinMode(light7, OUTPUT);
  pinMode(light8, OUTPUT);
  pinMode(test, OUTPUT);
  
}

void loop() {

  // 9 digit
  digitalWrite(test, HIGH);
  digitalWrite(light1, LOW);
  digitalWrite(light2, LOW);
  digitalWrite(light3, HIGH);
  digitalWrite(light4, HIGH);
  digitalWrite(light5, HIGH);
  digitalWrite(light6, HIGH);
  digitalWrite(light7, HIGH);
  digitalWrite(light8, HIGH);
  delay(delay_time);

  // 8 digit
  digitalWrite(light1, HIGH);
  digitalWrite(light2, HIGH);
  delay(delay_time);

  // 7 digit
  digitalWrite(light1, LOW);
  digitalWrite(light2, LOW);
  digitalWrite(light7, LOW);
  digitalWrite(light8, LOW);
  delay(delay_time);

  // 6 digit
  digitalWrite(light5, LOW);
  digitalWrite(light1, HIGH);
  digitalWrite(light2, HIGH);
  digitalWrite(light7, HIGH);
  digitalWrite(light8, HIGH);
  delay(delay_time);

  // 5 digit
  digitalWrite(light1, LOW);
  delay(delay_time);

  // 4 digit
  digitalWrite(light6, LOW);
  digitalWrite(light5, HIGH);
  digitalWrite(light2, LOW);
  delay(delay_time);

  // 3 digit
  digitalWrite(light7, LOW);
  digitalWrite(light6, HIGH);
  digitalWrite(light2, HIGH);
  delay(delay_time);

  // 2 digit
  digitalWrite(light3, LOW);
  digitalWrite(light1, HIGH);
  delay(delay_time);

  // 1 digit
  digitalWrite(light8, LOW);
  digitalWrite(light6, LOW);
  digitalWrite(light3, HIGH);
  digitalWrite(light2, LOW);
  digitalWrite(light1, LOW);
  delay(delay_time);

  // 0 digit
  digitalWrite(light1, HIGH);
  digitalWrite(light2, HIGH);
  digitalWrite(light3, HIGH);
  digitalWrite(light5, HIGH);
  digitalWrite(light6, HIGH);
  digitalWrite(light7, HIGH);
  digitalWrite(light8, HIGH);
  delay(delay_time);

}









