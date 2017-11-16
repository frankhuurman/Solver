
import serial

	
def sendToArduino(self, send_list):
	"""This function sends the movelist to Arduino
	Arduino recognizes f as a positive/clockwise 90 degree turn for the front stepper motor
	and F as a negative/counter clockwise 90 degree turn for the front stepper motor.
	Maybe move this function to the algorithm or cube object python file?
	"""

	# Make sure the last character is 'q' so the communication will terminate correctly.
	if (not send_list[-1] == "q"):
		send_list += "q"

	ser = serial.Serial("COM4", 9600, timeout=2)  # Open serial port
	print("Port used: " + ser.name)         # Check which port was really used
	data = ser.readline()
	if data == b"Ready\r\n": # Initialize handshake with Arduino
		print("Succesfully connected to Arduino...")
	else:
		print("Failed to connect to Arduino. Exiting...")
		return
	for m in send_list:
		data = ser.readline() # Read data from Arduino
		if data: # If data comes in from Arduino
			if data == b"next\r\n": # Initialize handshake with Arduino
				print ("Handshake from Arduino received")
				#The arduino_string part + while loop is for manual testing commands
				#Make this a comment and uncomment for item in send_list for regular use
				arduino_string = ""
					
				if m is not "q":
					ser.write(str.encode(m))
					self.cube.sendMoves(m)
				
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

#		test = input("Press enter to close serial connection")
	ser.close()             # close port
	print ("Serial port closed")


sendToArduino("dDfFLl")