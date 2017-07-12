import serial
from time import sleep
ser = serial.Serial("COM3", 9600, timeout=2)  # open serial port
print(ser.name)         # check which port was really used

while True:
	data = ser.readline() #the last bit gets rid of the new-line char
	if data:
		if data == b"Ready\r\n":
			print ("hi")
			arduino_string = input("Type string to send to arduino: ")
			arduino_send_bytes = str.encode(arduino_string)
			ser.write(arduino_send_bytes)
		elif data == b'hello':
			print ("it says hello!")
		else:
			# This actually prints the data received from Serial.print from Arduino
			# First it decodes the received raw byte data to a utf-8 string
			ascii_data = data.decode("utf-8")
			print (ascii_data)

	if not data:
		print("No data being received from Arduino anymore")
		break

test = input("Close?")
ser.close()             # close port
print ("Serial port closed")