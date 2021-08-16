#include <Servo.h>

Servo myservo;
int buttonInput = 2;
int output = 12;

int isSend = 0;
int buttonState = 0;
int incomingByte = 0;

void setup() {
  Serial.begin(9600);   
  Serial.setTimeout(1000);
  
  // put your setup code here, to run once:
  pinMode(buttonInput, INPUT_PULLUP); 
  pinMode(output, OUTPUT); 

  myservo.attach(9);  
  myservo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  incomingByte = Serial.read();
  if (incomingByte != -1) {
    delay(1000);
    myservo.write(85);
    delay(300);
    myservo.write(90);
  }
  buttonState = digitalRead(buttonInput); 
  if (buttonState == HIGH) { 
    digitalWrite(output, LOW);
    if (isSend == 0) { 
      isSend = 1; 
      tone(output, 1000, 1000);
      Serial.print("here");
    } 
  } else { 
    digitalWrite(output, HIGH);
    isSend = 0;
  }
}
