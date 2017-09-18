# /----------------------------------------------\
# !                   Reminders                  !
# \----------------------------------------------/

#cube.faces[cube.facenames[0]].squares[0][0] left (red)
#cube.faces[cube.facenames[1]].squares[0][0] front (white)
#cube.faces[cube.facenames[2]].squares[0][0] right (orange)
#cube.faces[cube.facenames[3]].squares[0][0] back (yellow)
#cube.faces[cube.facenames[4]].squares[0][0] bottom (blue)
#cube.faces[cube.facenames[5]].squares[0][0] top (green)

# When holding the cube turning the cube 90 degrees left, right up or down to show another face the corner that is the in the top left is that face's [0][0], 
# this only applies to the back side if the rotation is done in a right or left motion but not for up / down tilting

import cube as kubus
import serial

class vars:
	moveListBuffer = ""
	solved = False
	algo1 = False
	algo2 = False
	algo3 = False
	algo4 = False
	algo5 = False
	algo6 = False
	aglo7 = False
	cube = None

def sendToArduino():
	"""This function sends the movelist to Arduino
	Arduino recognizes f as a positive/clockwise 90 degree turn for the front stepper motor
	and F as a negative/counter clockwise 90 degree turn for the front stepper motor.
	"""

	ser = serial.Serial("COM4", 9600, timeout=2)  # Open serial port
	print("Port used: " + ser.name)         # Check which port was really used

	# Init moveListBuffer
	moveListBuffer = ["uUlLdDrRfFbBuUlLdDrRfFbBuUlLdDrRfFbBuUlLdDrRfFbBuUlLdDrRfFbBuUlLdDrRfFbB"] # Temporary, can be removed altready I believe.
	"""
	if len(moveListBuffer) > 62:
		blah = []
		blah.append(moveListBuffer[i*64:(i+1)*64])
	"""
	moveListBuffer.append("\r")
	while True:
		data = ser.readline() # Read data from Arduino
		if data: # If data comes in from Arduino
			if data == b"Ready\r\n": # Initialize handshake with Arduino
				print ("Handshake from Arduino received")
				#The arduino_string part + while loop is for manual testing commands
				#Make this a comment and uncomment for item in moveListBuffer for regular use
				arduino_string = ""
				
				while arduino_string != "q":
					arduino_string = input("Type string to send to arduino: ")
					ser.write(str.encode(arduino_string))
				
				"""
				for item in moveListBuffer:
					if len(item) > 64:
						print ("item longer than 64")
				"""
				"""
				if len(moveListBuffer[0]) > 40:
					print("test")
					#for item in moveListBuffer:
					#	ser.write(str.encode(moveListBuffer.pop(0)))
				"""
				"""
				for item in moveListBuffer:
					ser.write(str.encode(item))
				"""
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

	test = input("Press enter to close serial connection")
	ser.close() # closes the serial port
	print ("Serial port closed")

def ifBulk(colorCombo, pos):
	#TODO: Reduce the amount of comments by being more descriptive. <IMPORTANT> 
	#TODO: Check if the same algorithm can be used for opposing faces <THINK>
	#TODO: Translate the RDrd sequence to work for all four sides using each side's respective stepper motors (RDrd refers to two specific stepper motors, which would mean one corner would constantly be moved when passing RDrd to the move list.) <-- PRIORITY
	#TODO: Write 'conversion' Code <Joost>
		#TODO: Check if universal code can be written using the face number itself to adjust what side does what <-- Genius
	#TODO: Look into making a function that adds 'RDrd' s depending on the position of the white surface relative to the white face when in the correct vertical row (Algo2) <-- important
	cube = vars.cube # Pulls the latest version of the cube object. 
	results = ""
	if not vars.algo1: #NOTE: White surface of the edge used for position.
		if colorCombo == whiteRed: # correct pos == cube.faces[cube.facenames[1]].squares[1][0] White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				results = "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				results = "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "bRurB"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "blU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "LBuubl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "rbuuBR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "UrbuuBRu"
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]:
				return # 7h15 w0rk5 :p
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V 
				results = "uubllBUU"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V 
				results = "RddLDDr"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V 
				results = "ddBllbDD"
			elif pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "ubllBu'"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "bdLDB"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "fulUF"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "LfulUFl"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "Ulu"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "l"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "uulUU"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "ulU"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V 
				results = "UbllBu"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V 
				results = "rUbllBuR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "bdLDB"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "RBdLDbr"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V 
				results = "DLd"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "L"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "ddLDD"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "DLd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "bllB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "bbllBB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "ll"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "Bllb"
		if colorCombo == whiteBlue: # correct pos == cube.faces[cube.facenames[1]].squares[2][1]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				results = "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				results = "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "bRurB"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "blU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "LBuubl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "rbuuBR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "UrbuuBRu"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				results = "uubbddBBUU"
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "llbddLLB"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				results = "rrBddbRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[0]].squares[0][1]: # V 
				results = "lldLL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "Ldl"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "ldL"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "d"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "bLdlb'"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "LbddBl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "rBddbR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "uLbddBlU"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "rrDRR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "RDr"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "rDr"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "D"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "dRBddbr"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "lbddDL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "RBddbr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "brD"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "rrDRR"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "RDr"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "rdR"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "D"
		if colorCombo == whiteOrange: # correct pos == cube.faces[cube.facenames[1]].squares[1][2]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				results = "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				results = "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "bRurB"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "blU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "LBuubl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "rbuuBR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "UrbuuBRu"
			elif pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "LbDrdBl"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "bDrrdb'"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "lDbrrBdL"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "DbrrBd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				results = "uuBrrbUU"
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "lddrDDL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				results = "ddbrrBDD"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "rBDrdb"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "RdbrrBD"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "BDrdb"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "RBDrdb"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "brrb'"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "rr"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "bbrrBB"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "Dr"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "drD"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "ddrDD"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "r"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "Drd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "brrB"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "ubrrBU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "R"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "URu"
		if colorCombo == whiteGreen: # correct pos == cube.faces[cube.facenames[1]].squares[0][1]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				results = "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				results = "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				results = "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				results = "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				results = "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				results = "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				results = "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				results = "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				results = "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				results = "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				results = "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				results = "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				results = "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				results = "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				results = "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				results = "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				results = "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				results = "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				results = "bRurB"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				results = "blU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				results = "LBuubl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				results = "rbuuBR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				results = "UrbuuBRu"
	if not vars.algo2: # List algo2 # The position is the position of the white surface of the corner. <-- IMPORTANT
		if colorCombo == whiteRedGreen: # Green considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][0]:
				results = "RDrd" 
			elif pos == cube.faces[cube.facenames[0]].squares[0][2]:
				results = "RDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][0]:
				results = "DRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][2]: 
				results = "rDDRdRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][0]:
				return # This is the correct position.
			elif pos == cube.faces[cube.facenames[1]].squares[0][2]:
				results = "ldLRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][0]:
				results = "rDDRdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][2]:
				results = "LDDlRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][0]:
				results = "ldLRDrdRDrdRDrdRDrdRDrd" 
			elif pos == cube.faces[cube.facenames[2]].squares[0][2]:
				results = "dRDrdRDrdRDrdRDrdRDrd" 
			elif pos == cube.faces[cube.facenames[2]].squares[2][0]:
				results = "lDDLRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][2]:
				results = "DDRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][0]:
				results = "dRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][2]:
				results = "RDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][0]:
				results = "DDRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][2]:
				results = "DRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][0]:
				results = "rDDRdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][2]:
				results = "LddlRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][0]:
				results = "DRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][2]:
				results = "DDRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][0]:
				results = "ldLRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][2]:
				results = "RDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][0]:
				results = "dRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][2]:
				results = "RDrdRDrdRDrdRDrdRDrd"
		if colorCombo == whiteRedBlue: # Red considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][0]:
				results = "dRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[0][2]:
				results = "ldLRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][0]:
				results = "RDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][2]:
				results = "RDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][0]:
				results = "ldLRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][2]:
				results = "LDDlRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][0]:
				return # This is the correct position.
			elif pos == cube.faces[cube.facenames[1]].squares[2][2]:
				results = "rDRDRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][0]:
				results = "LddlRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][2]:
				results = "ddRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][0]:
				results = "rDDRdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][2]:
				results = "DRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][0]:
				results = "DDRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][2]:
				results = "dRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][0]:
				results = "DRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][2]:
				results = "RDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][0]:
				results = "RDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][2]:
				results = "rDDRdRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][0]:
				results = "RDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][2]:
				results = "DRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][0]:
				results = "dRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][2]:
				results = "ddRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][0]:
				results = "ldLRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][2]:
				results = "LddLRDrd"
		if colorCombo == whiteOrangeBlue: # Blue considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][0]: # V
				results = "ddRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[0][2]:
				results = "LddlRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][0]:
				results = "dRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][2]:
				results = "ldLRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][0]:
				results = "LddlRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][2]:
				results = "rDDRdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][0]:
				results = "ldLRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][2]: # V
				return # This is the correct position.
			elif pos == cube.faces[cube.facenames[2]].squares[0][0]:
				results = "rDDRdRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][2]:
				results = "DRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][0]:
				results = "RDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][2]:
				results = "RDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][0]:
				results = "DRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][2]: # V
				results = "ddRDrdRDrdRDrd" 
			elif pos == cube.faces[cube.facenames[3]].squares[2][0]:
				results = "RDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][2]:
				results = "dRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][0]:
				results = "ldLRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][2]:
				results = "RDrdRDrdRDrdRDrd" 
			elif pos == cube.faces[cube.facenames[4]].squares[2][0]:
				results = "dRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][2]:
				results = "RDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][0]:
				results = "ddRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][2]:
				results = "DRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][0]:
				results = "LddlRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][2]:
				results = "rDDRdRDrdRDrdRDrd"
		if colorCombo == whiteOrangeGreen: # Orange considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][0]:
				results = "DRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[0][2]:
				results = "rDDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][0]:
				results = "ddRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[0]].squares[2][2]:
				results = "LDDlRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][0]:
				results = "rDDRdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[0][2]:
				return # This is the correct position.
			elif pos == cube.faces[cube.facenames[1]].squares[2][0]:
				results = "LddLRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[1]].squares[2][2]:
				results = "ldLRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][0]:
				results = "RDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[0][2]:
				results = "RDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][0]:
				results = "ldLRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[2]].squares[2][2]:
				results = "dRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][0]:
				results = "RDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][2]:
				results = "DRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][0]:
				results = "dRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[3]].squares[2][2]:
				results = "ddRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][0]:
				results = "LddlRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[0][2]:
				results = "ldLRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][0]:
				results = "ddRDrd"
			elif pos == cube.faces[cube.facenames[4]].squares[2][2]:
				results = "dRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][0]:
				results = "DRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[0][2]:
				results = "RDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][0]:
				results = "rDDRdRDrdRDrdRDrdRDrdRDrd"
			elif pos == cube.faces[cube.facenames[5]].squares[2][2]:
				results = "RDrdRDrd"
	if not vars.algo3: # List algo 3 # 
		if colorCombo == redBlue: # Red considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				results = "urURUFufuuULulufUFULulufUFuuULulufUF"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				results = "ULulufUF"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				results = "" #This is the correct position so just send back a empty string.
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				results = "ubUBURurUULulufUFULulufUFuuULulufUF" 
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				results = "uuULulufUF"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				results = "UBubulULuLulufUF"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				results = "ULulufUFULulufUFuu" 
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				results = "uuULulufUFULulufUFuuULulufUF" 
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				results = "ULulufUFULulufUFuuULulufUF"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				results = "UULulufUFULulufUFuuULulufUF"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				results = "ULulufUFuuULulufUF"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				results = "UBubuLULuULulufUFULulufUFuuULulufUF"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				results = "UULulufUF"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				results = "LulufUF"	
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # Red considered front
				results = "urURUFufuuULulufUF" 
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				results = "ubUBURurUULulufUFULulufUFuuULulufUF" 																	
			# Keep in mind that for all faces (except for yellow) there will always be one edge you don't need to check since this one is already in the correct position.
		if colorCombo == redGreen: # Red considered front
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				results = "" # this is the correct position so return a empty string.
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				results = "urURUFuf"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				results = "ULulufUFuuurURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				results = "URurubUBurURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				results = "uuurURUFuf"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				results = "ulULUBuburURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				results = "uurURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				results = "uuurURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				results = "urURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				results = "UurURUFufurURUFufuuurURUFuf"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				results = "ULulufUFuuurURUFuf"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				results = "ulULUBuburURUFuf"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				results = "UurURUFuf"			
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				results = "uurURUFuf"	
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				results = "urURUFuuurURUFuf"	
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				results = "URurubUBurURUFuf"								
		if colorCombo == orangeGreen: # O = 2 G = 5, orange goes first.
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				results = ""	
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				results = ""	
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				results = ""											
		if colorCombo == orangeBlue: # O = 2 B = 4, orange goes first.
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				results = ""
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				results = ""	
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				results = ""	
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				results = ""	
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				results = ""						
	if not vars.algo4: # List algo 4
		# Well then. Atleast this one's interesting.
	if not vars.algo5: # List algo 5 
		# Check the color combo.
			# Check if it's in the correct position.
				# return
			# else Check the colorCombos of the three other edges.
			# move accordingly.
			# repeat until done.
	if not vars.algo6: # List algo 6
		# Not even going to bother attempting to write pseudo code for this one at present.
	if not vars.algo7: # List algo 7
		if colorCombo == yellowOrangeBlue:
			# Code goes here.
		if colorCombo == yellowBlueRed:
			# Code goes here.
		if colorCombo == yellowRedGreen:
			# Code goes here.
		if colorCombo == yellowGreenOrange:
			# Code goes here.
	results = results 
	cube.sendmoves(results) # Sends results to the cube updating it.
	vars.moveListBuffer += results # Adds this cycle's moves into the buffer.

def algorithm():
	count = 0
	while not vars.solved: # Check if the cube is solved
		while not vars.algo1:# Check to see if the white edges are solved
			for name in vars.cube.facenames: # Check each face for edges # name comes from where?
				whiteEdges = vars.cube.faces[name].checkEdges("w") # Check each block asociated with an edge to see if it is white
				if (len(whiteEdges) > 0): # Don't need to go further if there are no white edges.
					for pos in whiteEdges:
						colorCombo = otherSide # Check the other side of the edge to see what color it is
						ifBulk(vars.cube, colorCombo, pos)
						count += 1 # Used to indicate a edge has been solved
						if count == 4: 
							count = 0 # reset count to 0
							algo1 = True
		while not vars.algo2:  # Check to see if the white face is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check each corner block for the color white
				count += 1
				if count == 4:# Increase a counter that keeps track of the amount of correct corners.
					count = 0 # If the counter indicates 3, meanig all four corners are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
					algo2 = True
				# Check the two other blocks of the corner for their color
					# Take the number asociated with the white block and run it through a list to see what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer.
		while not vars.algo3:  # Check to see if the middle layer is solved, simple Boolean TRUE / FALSE (LOOP)
			for name in vars.cube.facenames:
				for ro in ["r", "o"]:
					currentEdge = vars.cube.faces[name].checkEdges(ro) # Checks for both red AND orange edges.
					if (len(currentEdge) >0):
						for pos in currentEdge:
							colorCombo = otherSide
							ifBulk(vars.cube, colorCombo, pos)
							count += 1
							if count == 4:
								count = 0
								algo1 = True
		while not vars.algo4:  # Check to see if the yellow cross exists, simple Boolean TRUE / FALSE (LOOP)
			#Check each edge that is still not in the correct position (Back) for yellow
				# Check if the edge is in the correct position already
					# If the block is in the correct position then mark it as completed (Can be one of four spots. aslong as it is at a edge on the yellow face it counts as a correct position)
						count += 1 # Increase a counter that keeps track of the amount of correct edges
						if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
							count = 0
							algo4 = True
					# Else go through the list using the position of the yellow edge.
						# Store the corresponding moves required to put the edge in the correct position in moveListBuffer
		while not vars.algo5:  # Check to see if the yellow edges are solved, simple Boolean TRUE / FALSE (LOOP)
			# Check the color of the color on the non yellow sides of the edges.
				# If the color matches the color of the center of the face (5)
					count += 1# Increase a counter that keeps track of the amount of correct edges.
					if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
						count = 0
						algo5 = True
				# Else check the color of the adjacent edge, going clockwise (Start with face 0 then 4, 2 and finaly 5)
					# If the color of the adjacent edge matches the color of the center block of their respective face
						# Go back to looking for a unsolved block skipping this one for the next round
					# Else go through the list 
						# Store the moves in moveListBuffer
		while not vars.algo6: # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
		while not vars.solved: # Check to see if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check if all faces only contain one color 
				# Set the Boolean to TRUE and break out of this loop
			# Else check which yellow corners are placed incorrectly
				# If the yellow - orange - blue corner is correctly placed
					# Skip this block leaving it be as is.
				# Else go through the list
					# Store the 4 move block into the moveListBuffer as many time as is necesary (need to end with a turn of the yellow face)
				# Check if the next corner is correctly placed
					# Skip this block leaving it be as is.
				# Else go through the list
					# Store the 4 move block into the moveListBuffer as many time as is necesary (need to end with a turn of the yellow face)
				# Check if the next corner is correctly placed
					# Skip this block leaving it be as is.
				# Else go through the list
					# Store the 4 move block into the moveListBuffer as many time as is necesary (need to end with a turn of the yellow face)
				# Check if the next corner is correctly placed
					# Skip this block leaving it be as is.
				# Else go through the list
					# Store the 4 move block into the moveListBuffer as many time as is necesary (need to end with a turn of the yellow face) 
				# Break out of this loop (This is under the assumption everything up until now has worked)
	if vars.cube.solved() == True:
		return vars.moveListBuffer
# Send moveListBuffer to where exactly
# Send moveListBuffer to the arduino from here?ck into the moveListBuffer as many time as is necesary (need to end with a turn of the yellow face) 
				# Break out of this loop (This is under the assumption everything up until now has worked)
	if vars.cube.solved() == True:
		return vars.moveListBuffer
# Send moveListBuffer to where exactly
# Send moveListBuffer to the arduino from here?