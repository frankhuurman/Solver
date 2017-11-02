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

//Define movelist array
String moveList[] = {};
int moveListBuffer = 0; // buffer for the moveList array used when receiving raw bytes through PySerial
int p = 0; // used for iterating through the posMoves array
int n = 0; // used for iterating through the negMoves array
String nextMove; // contains the next move
int moveMin = 0; // for iterating through arrays
int moveMax = 5; // for iterating through arrays
String posMoves[] = {"f", "d", "r", "b", "l", "u"}; //array containing all the positive moves
String negMoves[] = {"F", "D", "R", "B", "L", "U"}; // array containing all the negative moves

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
			Serial.print("next");
		}
	}
}
