import serial
from time import sleep

ser = serial.Serial("COM4", 9600, timeout=2)  # Open serial port
print("Port used: " + ser.name)         # Check which port was really used

send_list = ["uUlLdDrRfFbB"]
send_list.append("\r")
while True:
	data = ser.readline() # Read data from Arduino
	if data: # If data comes in from Arduino
		if data == b"Ready\r\n": # Initialize handshake with Arduino
			print ("Handshake from Arduino received")
			#arduino_string = input("Type string to send to arduino: ")
			"""
			if len(send_list) > 6:
				for item in send_list:
					ser.write(str.encode(send_list.pop(0)))
			"""
			for item in send_list:
				ser.write(str.encode(item))
		elif data == b"somethingelse":
			arduino_string = input("Type another string to send to arduino: ")
			arduino_send_bytes = str.encode(arduino_string)
			ser.write(arduino_send_bytes)
		elif data == b'hello':
			print ("it says hello!")
		else:
			# This actually prints the data received from Serial.print from Arduino
			# First it decodes the received raw byte data to a utf-8 string
			ascii_data = data.decode()
			print (ascii_data)

	if not data: # If there is no data coming back from Arduino
		print("No data being received from Arduino anymore")
		break

test = input("Close?")
ser.close()             # close port
print ("Serial port closed")