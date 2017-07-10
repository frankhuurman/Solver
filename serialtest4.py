import serial
from time import sleep
ser = serial.Serial('COM3', 9600, timeout=2)  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string converted to bytes

while True:
	data = ser.readline() #the last bit gets rid of the new-line char
	#print (data)
	#print (data)
	if data:
		if data == b"Ready\r\n":
			print ("hi")
			arduino_string = input("send hello string now?")
			arduino_send_bytes = str.encode(arduino_string)
			ser.write(arduino_send_bytes)
		elif data == b'hello':
			print ("it says hello!")
		else:
			# deze print b'jo'
			print (data)
			#ser.write(b'hello')

	if not data:
		print("No data being received from Arduino anymore")
		break

test = input("Close?")
ser.close()             # close port
print ("Serial port closed")