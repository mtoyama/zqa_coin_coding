void setup(){
  
  // initialize the LED pins as an output:
  pinMode (2, OUTPUT);
  pinMode (3, OUTPUT);
  pinMode (4, OUTPUT);
  pinMode (5, OUTPUT);
  pinMode (6, OUTPUT);
  pinMode (7, OUTPUT);
  
  Serial.begin (9600); // initialize serial communications:
}

void loop (){
  
  // read the value of the dial:
  int analogValue = analogRead (A0); 
  
  // print the analog value:
  Serial.println (analogValue);
  
 // if the analog value is high enough, turn on the LED:
  if (analogValue > 170){ 
  digitalWrite(2, HIGH);
} else {
  digitalWrite(2, LOW);
}
 // if the analog value is high enough, turn on the LED:
if (analogValue > 340){ 
  digitalWrite(3, HIGH);
} else {
  digitalWrite(3, LOW);
}
// if the analog value is high enough, turn on the LED:
if (analogValue > 510){
  digitalWrite(4, HIGH);
} else {
  digitalWrite(4, LOW);
}
// if the analog value is high enough, turn on the LED:
if (analogValue > 680){ 
  digitalWrite(5, HIGH);
} else {
  digitalWrite(5, LOW);
}
// if the analog value is high enough, turn on the LED:
if (analogValue > 850){ 
  digitalWrite(6, HIGH);
} else {
  digitalWrite(6, LOW);
}
// if the analog value is high enough, turn on the LED:
if (analogValue > 1020){ 
  digitalWrite(7, HIGH);
} else {
  digitalWrite(7, LOW);
}

}