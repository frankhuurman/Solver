//Define steppers
const byte rDir = 2; // (Rechts Boven) //rechts
const byte rStep = 3; 
const byte dDir = 4; // (Rechts Onder) //onder
const byte dStep = 5;
const byte bDir = 6; // (Achterkant) //achter
const byte bStep = 7;
const byte uDir = 8; // (Links Boven) //boven
const byte uStep = 9;
const byte lDir = 10;  // (Links Onder) //links
const byte lStep = 11;
const byte fDir = 12;  // (Voorkant) //voor
const byte fStep = 13;

//Define bytes that are received by Arduino
//small letters are for positive turns, capital for negative turns
byte r = 114;
byte R = 82;
byte d = 100;
byte D = 68;
byte b = 98;
byte B = 66;
byte u = 117;
byte U = 85;
byte l = 108;
byte L = 76;
byte f = 102;
byte F = 70;
byte carriage = 13;
byte ending = 63;

//Muziek
byte z = 122; //Mario tune

byte incomingByte; //Define byte to receive info from USB/Python script
int timerspeed = 50; //50 timerspeed is a quarter turn
int delayspeed = 800;
byte currentDir;
byte currentStep;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Ready"); // print "Ready" once to initiate connection to Python script
  pinMode(rDir, OUTPUT);
  pinMode(rStep, OUTPUT);
  pinMode(dDir, OUTPUT);
  pinMode(dStep, OUTPUT);
  pinMode(bDir, OUTPUT);
  pinMode(bStep, OUTPUT);
  pinMode(uDir, OUTPUT);
  pinMode(uStep, OUTPUT);
  pinMode(lDir, OUTPUT);
  pinMode(lStep, OUTPUT);
  pinMode(fDir, OUTPUT);
  pinMode(fStep, OUTPUT);
}

void posTurn(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(delayspeed);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(delayspeed);
  }
}

void negTurn(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, HIGH);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(delayspeed);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(delayspeed);
  }
}

void turn2(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1000);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1000);
  }
}
void turn3(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(665);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(665);
  }
}
void turn4(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1360);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1360);
  }
}
void turn5(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1600);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1600);
  }
}
void turn6(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1200);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1200);
  }
}
void turn7(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1070);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1070);
  }
}
void turn8(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(1130);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(1130);
  }
}
void turn9(){
  for(int timer = 0; timer < timerspeed; timer++){
    digitalWrite(currentDir, LOW);
    digitalWrite(currentStep, HIGH);
    delayMicroseconds(900);
    digitalWrite(currentStep, LOW);
    delayMicroseconds(900);
  }
}
void loop() {
  // put your main code here, to run repeatedly
  if (Serial.available()>0) { // there are bytes in the serial buffer to read
      while(Serial.available()>0) { // every time a byte is read it is destroyed
        incomingByte = Serial.read(); // read in the next byte
        Serial.print(incomingByte);
        
        if (incomingByte == r){
          currentDir = rDir;
          currentStep = rStep;
          posTurn();
        }
        else if (incomingByte == R){
          currentDir = rDir;
          currentStep = rStep;
          //posTurn();
          negTurn();
        }
        else if (incomingByte == d){
          currentDir = dDir;
          currentStep = dStep;
          posTurn();
        }
        else if (incomingByte == D){
          currentDir = dDir;
          currentStep = dStep;
          negTurn();
        }
        else if (incomingByte == b){
          currentDir = bDir;
          currentStep = bStep;
          //posTurn();
          posTurn();
        }
        else if (incomingByte == B){
          currentDir = bDir;
          currentStep = bStep;
          negTurn();
        }
        else if (incomingByte == u){
          currentDir = uDir;
          currentStep = uStep;
          posTurn();
        }
        else if (incomingByte == U){
          currentDir = uDir;
          currentStep = uStep;
          negTurn();
        }
        else if (incomingByte == l){
          currentDir = lDir;
          currentStep = lStep;
          posTurn();
        }
        else if (incomingByte == L){
          currentDir = lDir;
          currentStep = lStep;
          negTurn();
        }
        else if (incomingByte == f){
          currentDir = fDir;
          currentStep = fStep;
          posTurn();
        }
        else if (incomingByte == F){
          currentDir = fDir;
          currentStep = fStep;
          negTurn();
        }
        else if (incomingByte == z){
          currentDir = lDir;
          currentStep = lStep;
          negTurn(); //note 1
          delay(50);
          negTurn(); //note 1
          delay(200);
          negTurn(); //note 1
          delay(200);
          turn2(); //note 2
          delay(50);
          negTurn(); //note 1
          delay(200);
          turn3(); //note 3
          delay(500);
          turn4(); //note 4
          delay(500);
          turn2(); //note 2 //hier begint de lead
          delay(300);
          turn4(); //note 4
          delay(300);
          turn5(); //note 5
          delay(300);
          turn6(); //note 6
          delay(200);
          turn7(); //note 7
          delay(200);
          turn8(); //note 8
          delay(50);
          turn6(); //note 6
          delay(150);
          turn4(); //note 4
          delay(100);
          turn2(); //note 2
        }
        else if(incomingByte == ending){
          Serial.print(" Done ");
          delay(5000);
          Serial.print(" Countdown starting, please remove Cube ");
          delay(1000);
          Serial.print(" 3 ");
          delay(1000);
          Serial.print(" 2 ");
          delay(1000);
          Serial.print(" 1 ");
          delay(1000);
          Serial.print("Cube removed?");
        }
        
        else if (incomingByte == carriage){
          Serial.print(" EOL Reached ");  
        }
        else{
          Serial.print(" Error ");    
        }
        }
      }
}
