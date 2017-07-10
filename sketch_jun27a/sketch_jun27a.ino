byte myByte;

void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once

}
void loop() {

if (Serial.available()>0) { // there are bytes in the serial buffer to read
      while(Serial.available()>0) { // every time a byte is read it is expunged 
      // from the serial buffer so keep reading the buffer until all the bytes 
      // have been read.
         myByte = Serial.read(); // read in the next byte
         Serial.print(myByte);
         //Serial.write(myByte); // ASCII character
      }
      Serial.println(); // carriage return
      delay(100); // a short delay
   }
delay(100); // delay for 1/10 of a second
}
