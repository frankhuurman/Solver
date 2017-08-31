/* Full Arduino Code for powering Rubik's Cube Solver Stepper Motors
 * Start Solverfinal2.py in command line to send data to Arduino
 *  
 *  By T.K. Strijker & F.L. Huurman
 *  
 *  Version 1.0.1 : Masterfully Mellow Melon
 *  
 *  New Functions : 
 *  -Changed and removed code to be compatible with the new design plan and quarter stepping.
 *  -Basic bug fixing.
 *  -Added Byte array as a movelist buffer
 *  -Serial writes Strings to Bytes now so convert those to ASCII for moves!
 *  
 *        Notes 
 * 
 * digitalWrite(directionValue,HIGH) causes a negative turn (also known as a ' turn (example : r' ))
 * digitalWrite(directionValue,LOW) causes a normal turn.
 * Code currently doesn't make the steppers move, this isn't something to do with the hardware but rather the variables being used to pick which stepper is to be activated being empty or 'null'
 * The steppers use quarter-stepping, meaning they only move 0,45 degrees with each step. This means each 90 degree turn takes 200 steps instead of 50
 * 
 *        To do
 *  Test if all the steppers skip a equal amounts of steps or even do this at all. // seems so
 */

// Initialize incoming bytes, byte array, ascii char array and stepper constants
byte incomingByte;
byte moveListBytes[100];
char moveListAscii[100];
byte i = 0;
const byte uDir = 2; // U face stepper (Top) (Rechts Boven)
const byte uStep = 3; 
const byte rDir = 4; // R face stepper (Right) (Rechts Onder)
const byte rStep = 5;
const byte bDir = 6; // B face stepper (Back) (Achterkant)
const byte bStep = 7;
const byte lDir = 8; // L face stepper (Left) (Links Boven)
const byte lStep = 9;
const byte dDir = 10;  // D face stepper (Down) (Links Onder)
const byte dStep = 11;
const byte fDir = 12;  // F face stepper (front) (Voorkant)
const byte fStep = 13;

int stepperArray[] = {fDir, fStep, dDir, dStep, rDir, rStep, bDir, bStep, lDir, lStep, uDir, uStep}; // Array containing all the stepper pins, 0 - 11 
String moveList[] = {}; // array storing the results of the algorithm
int moveListBuffer = 0; // buffer for the moveList array used when receiving raw bytes through PySerial
int p = 0; // used for itterating through the posMoves array
int n = 0; // used for itterating through the negMoves array
String nextMove; // contains the next move
int moveMin = 0; // for iterating through arrays
int moveMax = 5; // for iterating through arrays
String posMoves[] = {"f", "d", "r", "b", "l", "u"}; //array containing all the positive moves
String negMoves[] = {"f'", "d'", "r'", "b'", "l'", "u'"}; // array containing all the negative moves

int currentDir;
int currentStep;

void setup() {
  // does what it says on the can.
  Serial.begin(9600);
  Serial.println("Ready"); // print "Ready" once to initiate connection to Python script
  
  // Set all the (PWM) pins to output, why you can't set all pins to a particular state with one command is beyond me:
  int outMin = 2; // Lowest pin 
  int outMax = 13; // Highest pin
  for (int i=outMin; i<=outMax; i++) // Iterates over all the pins setting them to OUTPUT
  {
    pinMode(i,OUTPUT);
  }
}

// Does a positive turn.
void posTurn() {
  for(int timer = 0; timer < 200; timer++) {
    digitalWrite(currentDir,LOW);
    digitalWrite(currentStep,HIGH);
    delayMicroseconds(400);
    digitalWrite(currentStep,LOW);
    delayMicroseconds(400);
  }
}

// Does a negative turn.
void negTurn() { 
  for(int timer = 0; timer < 200; timer++) {
    digitalWrite(currentDir,HIGH);
    digitalWrite(currentStep,HIGH);
    delayMicroseconds(400);
    digitalWrite(currentStep,LOW);
    delayMicroseconds(400);
  }
}


void loop() {

// checks if serial data is coming in
if (Serial.available()>0) { // there are bytes in the serial buffer to read
      while(Serial.available()>0) { // every time a byte is read it is destroyed 
         // from the serial buffer so keep reading the buffer until all the bytes 
         // have been read. 
         //incomingByte = Serial.read(); // read in the next byte
         //moveListBytes[i] = incomingByte;
         //Serial.print(moveListBytes[0]);

         incomingByte = Serial.read(); // read in the next byte
         Serial.print(incomingByte);
          
         }
         for(int j = 0; j < 3; j++){
           //Serial.print(incomingByte);
           //Serial.print("test");
            //moveListBytes[j] = incomingByte; // add read byte to byte array
           moveListAscii[j] = incomingByte; // add read byte to char array(ASCII)
           //j++;
         //Serial.write(incomingByte); // ASCII character
         //i++;
      }
      //Serial.print(moveListBytes[0]);
      //Serial.print(moveListAscii[0]);
      //Serial.print(moveListAscii[0]);
      
      //Serial.println(); // carriage return
      //delay(100); // a short delay
   }


// Moves
if (nextMove != "") {
  for(int p=moveMin; p<moveMax; p++){ // iterating through the array
   if (nextMove == posMoves[p])
    {
      // set currentDir & currentStep to be the correct value 
      posTurn();
      moveList[i] = ""; // check if this works
      i += 1;
      nextMove = moveList[i];
    }
  }

  for(int n=moveMin; n<moveMax; n++){ // iterating through the array
   if (nextMove == negMoves[n])
    {
      negTurn();
      moveList[i] = ""; // check if this works
      i += 1;
      nextMove = moveList[i];
    }
  }
  
if (nextMove == "") { //Check if this works 
 while(true); {} // world's shittiest 'stop'
 Serial.print("Stop");
  }
 }
}
