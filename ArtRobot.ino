#include <HCSR04.h>

#include <Servo.h>

byte triggerPin = 6;
byte echoCount = 1;
byte echoPin = 2;

int servoPin = 5;

Servo eyebrowServo;

int eyebrowRange = 20;

bool currently_looking = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  HCSR04.begin(triggerPin, echoPin);
   
  randomSeed(analogRead(0));
  
  eyebrowServo.attach(servoPin);
  eyebrowServo.write(90);

  Serial.println("start_sounds");

  delay(5000);
  
  
}

void loop() {
  while (!currently_looking){
    double* distances = HCSR04.measureDistanceCm();
    if (distances[0] <= 30 && distances[0] >= 5){
      currently_looking = false;
      looking(random(4, 7));
    }
  }

}

void looking(long cycles){

  for(int i = 0; i < cycles; i++){

    Serial.println("looking_sounds");

    eyebrowServo.write(90 + random(-eyebrowRange, eyebrowRange + 1));
    
    delay(random(4, 7) * 1000);
    
  }

  Serial.println("finished_sounds");
  eyebrowServo.write(90);

  delay(5000);

  currently_looking = false;
      
}
