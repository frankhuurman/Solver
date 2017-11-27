
import serial
import time


def sendToArduino(m, amount):
	
	for i in range(amount):
		data = ser.readline() # Read data from Arduino
		print("Sending move: " + m)
		ser.write(str.encode(m))

		if not data: # If there is no data coming back from Arduino
			print("No data being received from Arduino anymore")
			return


def getInput():
	allowed = ["f", "F", "l", "L", "r", "R",
					"b", "B", "d", "D", "u", "U", "q"]
	try:
		m, amount = input("Select move and rotation: ").split()
		m = int(amount)
		if (amount < 1):
			m = False
		if (not m in allowed):
			m = False
	except:
		print("wrong input!")
		m = False
	return(m, amount)

ser = serial.Serial("COM4", 38400, timeout=0.1)  # Open serial port (Met 0.1 timeout is python programma even snel klaar als moves van arduino)
print("Port used: " + ser.name)         # Check which port was really used
time.sleep(2)

while (m is not "q"):
	m, amount = getInput()
	if (m is not False):
		sendToArduino(m, amount)

		
test = input("Press enter to close serial connection")
ser.close()             # close port
print ("Serial port closed")