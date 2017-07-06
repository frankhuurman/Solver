byte myByte;

void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once

/*
char test = ' ';
test = Serial.read();
//Serial.println(test);
if(test == "hello"){
  Serial.println("nope");
}
else{
  Serial.println("jo");
}
*/
}
void loop() {
//char incomingByte = ' ';

if (Serial.available()>0) { // there are bytes in the serial buffer to read
      while(Serial.available()>0) { // every time a byte is read it is expunged 
      // from the serial buffer so keep reading the buffer until all the bytes 
      // have been read.
         myByte = Serial.read(); // read in the next byte
         Serial.write(myByte); // ASCII character
      }
      //Serial.println(myByte, DEC); // base 10, this is the default
      //Serial.println(myByte, HEX); // base 16
      //Serial.println(myByte, OCT); // base 8
      //Serial.println(myByte, BIN); // base 2
      Serial.println(); // carriage return
      delay(100); // a short delay
   }
/*
if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                //String thisString = String(incomingByte);
                Serial.print("I received: ");
                Serial.println(incomingByte);
}
*/
/*
char test = ' ';
String totalstring = " ";
if(Serial.available()){
test = Serial.read();
Serial.println(test);

if(test == "hello"){
Serial.println("hello");
}
else{
  Serial.println("martin");
}
}
*/


/*
char inByte = ' ';
if(Serial.available()){ // only send data back if data has been sent
char inByte = Serial.read(); // read the incoming data
//Serial.println(inByte); // send the data back in a new line so that it is not all one long line
}
*/
delay(100); // delay for 1/10 of a second
}
