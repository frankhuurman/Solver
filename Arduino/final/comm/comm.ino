
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

	Serial.begin(38400);
	Serial.print("Ready");
}

void loop() {

//	Serial.print("Ready");
	if (Serial.available()>0) { // there are bytes in the serial buffer to read
		while(Serial.available()>0) { // every time a byte is read it is destroyed
			incomingByte = Serial.read(); // read in the next byte
			Serial.print(incomingByte);
        
			if(incomingByte == ending){
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
