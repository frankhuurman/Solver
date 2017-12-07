import pygame
pygame.init()
import os
import calc_rest
import cube as kubus
import serial
import threading
import time



class solverThread(threading.Thread):
	"""Use this to create new threads."""

	threadID = None
	name = None
	args = None

	def __init__(self, threadID, name, args = None):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.args = args

	def run(self):
		print("Starting thread{0}: {1}".format(self.threadID, self.name))
		self.args.solve()
		print("Exiting thread{0}: {1}".format(self.threadID, self.name))

class solver(object):
	
	# Set program window size and create program window
	display_width = 800
	display_height = 600
	solverDisplay = pygame.display.set_mode((display_width, display_height))
	# Outer loop variable
	active = True
	# Clock object to lock FPS(60)
	clock = pygame.time.Clock()

	# Init fonts and text variables for drawing on screen
	myfont = pygame.font.SysFont("monospace", 18, bold=True)
	myfontsmall = pygame.font.SysFont("monospace", 14, bold=True)
	front_text = myfont.render("Front", 1, (0,0,0))
	left_text = myfont.render("Left", 1, (0,0,0))
	right_text = myfont.render("Right", 1, (0,0,0))
	back_text = myfont.render("Back", 1, (0,0,0))
	bottom_text = myfont.render("Bottom", 1, (0,0,0))
	top_text = myfont.render("Top", 1, (0,0,0))
	usercolor_text = myfont.render("Your color:", 1, (0,0,0))
	output_stringtext = myfontsmall.render("Output string format: lllllllll, fffffffff, rrrrrrrrr, bababababababababa, bbbbbbbbb, ttttttttt", 1, (0,0,0))

	# Create confirm rectangle and load confirm images
	confirm1 = pygame.image.load("confirm1.png")
	confirm2 = pygame.image.load("confirm2.png")
	confirmrect = pygame.Rect(390, 470, 100, 50)
	# Create information rectangle and load information images
	inforect = pygame.Rect(500, 470, 100, 100)
	inforect2 = pygame.Rect(500, 470, 100, 100)
	saved = pygame.image.load("saved.png")
	filecreate = pygame.image.load("filecreate2.png")
	# # Create reset rectangle and load reset images
	reset1 = pygame.image.load("reset1.png")
	reset2 = pygame.image.load("reset2.png")
	resetrect = pygame.Rect(250, 470, 100, 50)

	# Color tuples
	black = (0, 0, 0)
	red = (255, 0 ,0)
	green = (0, 255, 0)
	blue = (0, 0, 255)

	# Color images for rectangles
	rubiks_image = pygame.image.load("rubiks.jpg")
	imgs = {"red" : pygame.image.load("red.png"),
			"white" : pygame.image.load("white.png"),
			"orange" : pygame.image.load("orange.png"),
			"yellow" : pygame.image.load("yellow.png"),
			"blue" : pygame.image.load("blue.png"),
			"green" : pygame.image.load("green.png")}

	# User color picker rectangles
	white_pick = pygame.Rect(230, 400, 40, 40)
	red_pick = pygame.Rect(280, 400, 40, 40)
	green_pick = pygame.Rect(330, 400, 40, 40)
	blue_pick = pygame.Rect(380, 400, 40, 40)
	orange_pick = pygame.Rect(430, 400, 40, 40)
	yellow_pick = pygame.Rect(480, 400, 40, 40)

	# User color variables
	user_color = imgs["white"] # Default picked color from start is white
	user_color_rect = pygame.Rect(150, 400, 40, 40)

	# Setup for positioning of rectangles.
	offsetx = [10, 300, 600]
	offsety = [40, 230]
	img_size = 40
	rects = []
	rects_col = []
	cube = None
	threadList = []
	ser = None # Serial connection
	
	def __init__(self):

		order = ["red", "white", "orange", "yellow", "blue", "green"]
		self.connectToSerial()

		# Set up the rectangles and their proper colors.
		for i , color in enumerate(order):
			if ((i - 3) >= 0):
				xoff = self.offsetx[i - 3]
			else:
				xoff = self.offsetx[i]
			if (i < 3):
				yoff = self.offsety[0]
			else:
				yoff = self.offsety[1]
			for y in range(3):
				for x in range(3):
					xpos = (xoff + (x * 50)) # Determine the x position of the rect.
					ypos = (yoff + (y * 50)) # Determine the y position of the rect.
					# Make a new rect and add it to rects list.
					self.rects.append(pygame.Rect((xpos, ypos), (self.img_size, self.img_size)))
					if (color == "white" and x == 1 and y == 1):
						# Exception for the rubiks image in the center of the white face.
						self.rects_col.append(self.rubiks_image)
					else:
						# Get the color for the rect. Colors are according to the color of the face.
						self.rects_col.append(self.imgs[color])


	def connectToSerial(self):
		"""Set up connection to arduino machine."""

		try:
			serial.Serial("COM4", 38400, timeout=0.1)		# Open serial port
			print("Port used: " + self.ser.name)			# Check which port was really usedused
			time.sleep(2)
			data = self.ser.readline()
			if data == b"Ready\r\n":							# Initialize handshake with Arduino
				print("Succesfully connected to Arduino...")
			else:
				print("Failed to connect to Arduino...")
				self.ser = None
		except:
			print("Failed to connect to Arduino...")
			self.ser = None
			
	def sendToArduino(self, send_list):
		"""This function sends the movelist to Arduino
		Arduino recognizes f as a positive/clockwise 90 degree turn for the front stepper motor
		and F as a negative/counter clockwise 90 degree turn for the front stepper motor.
		"""
		
		for m in send_list:
			data = ser.readline() # Read data from Arduino
			if m is not "q":
				print("Sending move: " + m)
				ser.write(str.encode(m))
				self.cube.sendMoves(m)

			if not data: # If there is no data coming back from Arduino
				print("No data being received from Arduino anymore")
				return
					
	def showSavedText(self, image, rect):
		image_time = 840
		while image_time > 0:
			self.solverDisplay.blit(image, rect)
			pygame.display.flip()
			image_time -= 1
		image_time = 840
	
	def userColor(self, color):
		"""Blits the picked color by user on the screen"""

		self.solverDisplay.blit(color, self.user_color_rect)
	
	def drawFields(self):
		"""Draws lines on the screen to section off the front/top-left/down-left views."""

		#left view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (5, 30), (155, 30), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (5, 190), (155, 190), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (5, 30), (5, 190), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (155, 30), (155, 190), 2)

		#front view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (295, 30), (445, 30), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (295, 190), (445, 190), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (295, 30), (295, 190), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (445, 30), (445, 190), 2)

		#right view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (595, 30), (745, 30), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (595, 190), (745, 190), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (595, 30), (595, 190), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (745, 30), (745, 190), 2)

		#back view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (5, 220), (155, 220), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (5, 380), (155, 380), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (5, 220), (5, 380), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (155, 220), (155, 380), 2)

		#bottom view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (295, 220), (445, 220), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (295, 380), (445, 380), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (295, 220), (295, 380), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (445, 220), (445, 380), 2)

		#top view
		#top-left to top-right
		pygame.draw.line(self.solverDisplay, self.black, (595, 220), (745, 220), 2)
		#down-left to down-right
		pygame.draw.line(self.solverDisplay, self.black, (595, 380), (745, 380), 2)
		#top-left to down-left
		pygame.draw.line(self.solverDisplay, self.black, (595, 220), (595, 380), 2)
		#top-right to down-right
		pygame.draw.line(self.solverDisplay, self.black, (745, 220), (745, 380), 2)

		# draw fields where user can pick colors
		self.solverDisplay.blit(self.imgs["white"], self.white_pick)
		self.solverDisplay.blit(self.imgs["red"], self.red_pick)
		self.solverDisplay.blit(self.imgs["green"], self.green_pick)
		self.solverDisplay.blit(self.imgs["blue"], self.blue_pick)
		self.solverDisplay.blit(self.imgs["orange"], self.orange_pick)
		self.solverDisplay.blit(self.imgs["yellow"], self.yellow_pick)
	
	def resetFields(self):
		"""Returns the virtual cube to the default state."""
		
		# Removing the virtual cube...
		if (self.cube is not None):
			self.cube.stopSolving = True
			self.cube = None
						
		# Waiting for the solver thread to terminate...
		for t in self.threadList:
			t.join()

		# Clearing out the move list buffer...
		calc_rest.vars.moveListBuffer = ""

		# Setting the algorithm bools to unsolved...
		for i in range(len(calc_rest.vars.algos)):
			calc_rest.vars.algos[i] = False

		# giving all squares the color of the solved state...
		order = ["red", "white", "orange", "yellow", "blue", "green"]
		for i in range(len(self.rects_col)):
			if ((i + 5) % 9 == 0):
				continue
			self.rects_col[i] = self.imgs[order[int(i/9)]]
	
	def getColorList(self):
		"""Returns an array with the first letter of the color of each of the 54 squares of the cube."""

		calcu_list = []

		for color in self.rects_col:
			if color == self.imgs["white"]:
				calcu_list.append("w")
			elif color == self.rubiks_image:
				calcu_list.append("w")
			elif color == self.imgs["red"]:
				calcu_list.append("r")
			elif color == self.imgs["green"]:
				calcu_list.append("g")
			elif color == self.imgs["blue"]:
				calcu_list.append("b")
			elif color == self.imgs["orange"]:
				calcu_list.append("o")
			elif color == self.imgs["yellow"]:
				calcu_list.append("y")
			else:
				calcu_list.append("<no color>")
		return(calcu_list)

	def confirmCheck(self):
		"""Run this check when starting to solve to ensure there are 9 squares of each color."""

		allColors = self.getColorList()
		colorSpread = {"r" : 0,
						"w" : 0,
						"o" : 0,
						"y" : 0,
						"b" : 0,
						"g" : 0,
						}
		offColors = {}
		for color in allColors:
			colorSpread[color] += 1
		for col, nr in colorSpread.items():
			print(nr)
			if (nr != 9):
				offColors[col] = nr
		print("offColors: ", offColors)
		if (len(offColors) > 0):
			return(False)
		return(True)

	def checkQuitandClicks(self):
		"""Check for exit and event handling."""

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.active = False
				pygame.quit()
				quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:  # left mouse button
					#check confirm
					if self.confirmrect.collidepoint(event.pos):
						# Start solving the cube using the algorithm in another thread.
						startThread = True
						for t in self.threadList:
							if (t.isAlive()):
								startThread = False
						if (not self.confirmCheck()):
							print("Colors be wrong!!!!!")
							return
						if (startThread):
							solverThr = solverThread(len(self.threadList), "Solver", self)
							solverThr.start()
							self.threadList.append(solverThr)
						else:
							print("Solver thread already going.")

					#reset rects
					if self.resetrect.collidepoint(event.pos):
						self.resetFields()

					# user color choice
					if self.white_pick.collidepoint(event.pos):
						self.user_color = self.imgs["white"]
					elif self.red_pick.collidepoint(event.pos):
						self.user_color = self.imgs["red"]
					elif self.green_pick.collidepoint(event.pos):
						self.user_color = self.imgs["green"]
					elif self.blue_pick.collidepoint(event.pos):
						self.user_color = self.imgs["blue"]
					elif self.orange_pick.collidepoint(event.pos):
						self.user_color = self.imgs["orange"]
					elif self.yellow_pick.collidepoint(event.pos):
						self.user_color = self.imgs["yellow"]

					# Changes rect color.
					for i in range(len(self.rects)):
						if (self.rects[i].collidepoint(event.pos)):
							if (not (i + 5) % 9 == 0):
								self.rects_col[i] = self.user_color
							break

	def updateColors(self):
		"""Sets the colors of the squares on the screen according to the current state of the Rubik's cube."""

		if (self.cube is not None):
			colorIndex = {"r": "red", "w": "white", "o": "orange", "y": "yellow", "b": "blue", "g": "green"}
			colors = ""
			for face in kubus.const.facenames:
				colors += self.cube.faces[face].getColors()
			for i in range(len(self.rects_col)):
				# Exception for the Rubik's cube logo.
				if (i == 13):
					continue
				self.rects_col[i] = self.imgs[colorIndex[colors[i]]]

	def solve(self):
		"""Run this in a seperate thread to start solving the cube."""
					
		# Create cube object
		self.cube = kubus.cube(self.getColorList())
		calc_rest.vars.cube = self.cube

		move_list = calc_rest.algorithm()
		print(len(move_list), move_list)
		if (self.ser != None):
			self.cube.setStart()
			self.sendToArduino(move_list + "q")
		self.cube = None

	def showScreen(self):

		while True:

			mousepos = pygame.mouse.get_pos()

			# Fill background
			self.solverDisplay.fill((255,255,255))
			# Blit text
			self.solverDisplay.blit(self.front_text, (300, 10))
			self.solverDisplay.blit(self.left_text, (10, 10))
			self.solverDisplay.blit(self.right_text, (600, 10))
			self.solverDisplay.blit(self.back_text, (10, 200))
			self.solverDisplay.blit(self.bottom_text, (300, 200))
			self.solverDisplay.blit(self.top_text, (600, 200))
			self.solverDisplay.blit(self.usercolor_text, (10, 410))
#			self.solverDisplay.blit(self.output_stringtext, (10, 550))
			# Blit front view rectangles with colors
			self.updateColors()

			for color, rect in zip(self.rects_col, self.rects):
				self.solverDisplay.blit(color, rect)

			if self.confirmrect.collidepoint(mousepos):
				self.solverDisplay.blit(self.confirm2, self.confirmrect)
			else:
				self.solverDisplay.blit(self.confirm1, self.confirmrect)

			if self.resetrect.collidepoint(mousepos):
				self.solverDisplay.blit(self.reset2, self.resetrect)
			else:
				self.solverDisplay.blit(self.reset1, self.resetrect)

			self.drawFields()
			# blit user color, must be before checkQuitandClicks!!
			self.userColor(self.user_color)
			# check for exit and clicks
			self.checkQuitandClicks()

			# update screen
			pygame.display.flip()

			# frames
			self.clock.tick(60)
			
game = solver()
try:
	while game.active:
		game.showScreen()
except KeyboardInterrupt:
	pass
finally:
	if (game.ser != None):
		game.ser.close()             # close port
		print ("Serial port closed")
	print("doei.")