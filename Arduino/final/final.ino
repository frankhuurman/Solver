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
const byte fStep = 13;  // Should't use pin 13 for this. It's used for the built-in LED which is used upon activation.

const int marioTune[][3] = {{800, 50, 1}, {800, 200, 1}, {800, 200, 1},
	{1000, 50, 0}, {800, 200, 1}, {665, 500, 0}, {1360, 500, 0},
	{1000, 300, 0}, {1360, 300, 0}, {1600, 300, 0}, {1200, 200, 0},
	{1070, 200, 0}, {1130, 50, 0}, {1200, 150, 0}, {1360, 100, 0}, {1000, 0, 0}};


char incomingByte; //Define byte to receive info from USB/Python script
const int timerspeed = 50; //50 timerspeed is a quarter turn
const int delayspeed = 800;
byte currentDir;
byte currentStep;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
  Serial.print("Ready"); // print "Ready" once to initiate connection to Python script
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

void turn(byte dirPin, byte stepPin, bool dir, int ds = delayspeed) {
	// dir: true is negturn, false is posturn.
	digitalWrite(dirPin, dir);
	for(int timer = 0; timer < timerspeed; timer++) {
		digitalWrite(stepPin, true);
		delayMicroseconds(ds);
		digitalWrite(stepPin, false);
		delayMicroseconds(ds);
	}
}

void loop() {
	// put your main code here, to run repeatedly
	if (Serial.available()>0) { // there are bytes in the serial buffer to read
		while(Serial.available()>0) { // every time a byte is read it is destroyed
			incomingByte = char(Serial.read()); // read in the next byte
			Serial.print(incomingByte);
        
			if (incomingByte == 'r'){
				turn(rDir, rStep, 0);
			}
			else if (incomingByte == 'R'){
				turn(rDir, rStep, 1);
			}
			else if (incomingByte == 'd'){
				turn(dDir, dStep, 0);
			}
			else if (incomingByte == 'D'){
				turn(dDir, dStep, 1);
			}
			else if (incomingByte == 'b'){
				turn(bDir, bStep, 0);
			}
			else if (incomingByte == 'B'){
				turn(bDir, bStep, 1);
			}
			else if (incomingByte == 'u'){
				turn(uDir, uStep, 0);
			}
			else if (incomingByte == 'U'){
				turn(uDir, uStep, 1);
			}
			else if (incomingByte == 'l'){
				turn(lDir, lStep, 0);
			}
			else if (incomingByte == 'L'){
				turn(lDir, lStep, 1);
			}
			else if (incomingByte == 'f'){
				turn(fDir, fStep, 0);
			}
			else if (incomingByte == 'F'){
				turn(fDir, fStep, 1);
			}
			else if (incomingByte == 'z'){
				for (int i = 0; i < sizeof(marioTune); i++) {
					turn(lDir, lStep, marioTune[i][2], marioTune[i][0]); //note 1
					delay(marioTune[i][1]);
				}
			}
			else if (incomingByte == '?'){
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
			else if (incomingByte == '\r'){
				Serial.print(" EOL Reached ");  
			}
			else{
				Serial.print(" Error ");    
			}
		}
	}
}
