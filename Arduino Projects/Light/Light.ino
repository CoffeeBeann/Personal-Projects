// Ian Coffey
// Light.ino

// Variable Declaration
const int led1 = 11;
const int led2 = 10;
const int led3 = 9;
const int led4 = 6;
const int led5 = 5;
//const int led6 = 3;
int delay_time = 100;
int max_brightness = 75;
int brightness = 0;
int fade = 25;

void setup() {

    Serial.begin(9600);
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
    //pinMode(led6, OUTPUT);
      
}

void loop() {

  // LED 1
  analogWrite(led1, brightness);

  if (brightness <= 0 || brightness >= max_brightness) {
    
      fade = -fade;
      
  }

  delay(delay_time);

  // LED 2
  analogWrite(led2, brightness);

  if (brightness <= 0 || brightness >= max_brightness) {
    
      fade = -fade;
      
  }

  delay(delay_time);

  // LED 3
  analogWrite(led3, brightness);

  if (brightness <= 0 || brightness >= max_brightness) {
    
      fade = -fade;
      
  }

  delay(delay_time);

  // LED 4
  analogWrite(led4, brightness);

  if (brightness <= 0 || brightness >= max_brightness) {
    
      fade = -fade;
      
  }

  delay(delay_time);

  // LED 5
  analogWrite(led5, brightness);

  if (brightness <= 0 || brightness >= max_brightness) {
    
      fade = -fade;
      
  }

  delay(delay_time);

  // LED 6
  //analogWrite(led6, brightness);
  //brightness = brightness + fade;

  //if (brightness <= 0 || brightness >= max_brightness) {
    
      //fade = -fade;
      
 //}

  //delay(delay_time);

}






















