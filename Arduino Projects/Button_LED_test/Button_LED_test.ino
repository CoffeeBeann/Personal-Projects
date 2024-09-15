const int buzzer = 11;
const int increase = 9;
const int decrease = 6;
const int play = 10;
int frequency = 1000;
int increaseState;
int decreaseState;
int playState;

void setup() {

  pinMode(buzzer, OUTPUT);
  pinMode(increase, INPUT);
  pinMode(decrease, INPUT);
  pinMode(play, INPUT);

}

void loop() {

  increaseState = digitalRead(increase);
  decreaseState = digitalRead(decrease);
  playState = digitalRead(play);

  if (increaseState == HIGH) {
    
    frequency = frequency + 10;
    delay(100);
    
  } 
  if (decreaseState == HIGH) {
    
    frequency = frequency - 10;
    delay(100);
    
  } 
  if (playState == HIGH) {
    
    tone(buzzer, frequency, 1);
    
  } else {

    digitalWrite(buzzer, LOW);
    
  }

}
