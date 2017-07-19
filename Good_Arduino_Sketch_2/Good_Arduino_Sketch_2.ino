/* Full Arduino Code for powering Rubik's Cube Solver Stepper Motors
 * Start Solverfinal2.py in command line to send data to Arduino
 *  
 *  By T.K. Strijker & F.L. 'Loli licker' Huurman
 *  
 *  Version 1.0.2 : Meowing Masterfully Mellow Melon
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

int readline(int readch, char *buffer, int len){
  static int pos = 0;
  int rpos;

  if (readch > 0) {
    switch(readch){
    case '\n': // ignore new-line characters
      break;
    case '\r':
      rpos = pos;
      pos = 0; // reset position index for next time
      return rpos;
    default:
      if (pos < len-1) {
        buffer[pos++] = readch;
        buffer[pos] = 0;
      }
    }
  }
  // no end of line found, so return -1
  return -1;
}

// Initialize incoming bytes, byte array, ascii char array and stepper constants
byte incomingByte;
byte moveListBytes[100];
char moveListAscii[100];
byte i = 0;
const byte rDir = 2; // (Rechts Boven)
const byte rStep = 3; 
const byte dDir = 4; // (Rechts Onder)
const byte dStep = 5;
const byte bDir = 6; // (Achterkant)
const byte bStep = 7;
const byte uDir = 8; // (Links Boven)
const byte uStep = 9;
const byte lDir = 10;  // (Links Onder)
const byte lStep = 11;
const byte fDir = 12;  // (Voorkant)
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

  static char buffer[180];
  if (readline(Serial.read(), buffer, 180) > 0) {
    Serial.print("You entered: >");
    Serial.print(buffer);
    Serial.println("<");
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
