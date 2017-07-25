import pygame
import os
import calc_rest
import cube as kubus


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
	user_color = white_image #default picked color from start is white
	user_color_rect = pygame.Rect(150, 400, 40, 40)

	# Setup for positioning of rectangles.
	offsetx = [10, 300, 600]
	offsety = [40, 230]
	img_size = 40
	rects = []
	rects_col = []
	
	
	def __init__(self):
		# Initialize pygame
		pygame.init()
		
		# Set up the rectangles and their proper colors.
		for i , color in enumerate(self.imgs):
			if ((i - 3) >= 0):
				xoff = offsetx[i - 3]
			else:
				xoff = offsetx[i]
			if (i < 3):
				yoff = offsety[0]
			else:
				yoff = offsety[1]
			for y in range(3):
				for x in range(3):
					xpos = (xoff + (x * 50))
					ypos = (yoff + (y * 50))
					self.rects.append(pygame.Rect(xpos, ypos, img_size, img_size))
					if (color == "white" and x == 1 and y == 1):
						self.rects_col.append(rubiks_image)
					else:
						self.rects_col.append(color)

	
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
		self.solverDisplay.blit(white_image, white_pick)
		self.solverDisplay.blit(red_image, red_pick)
		self.solverDisplay.blit(green_image, green_pick)
		self.solverDisplay.blit(blue_image, blue_pick)
		self.solverDisplay.blit(orange_image, orange_pick)
		self.solverDisplay.blit(yellow_image, yellow_pick)
	
	def translateList(self, movelist):
		translated_list = []
		for item in movelist:
			sliced_list = list(item)

		count = 0

		try:
			for item in sliced_list[:-1]:
				if sliced_list[count + 1] == "'":
					translated_list.append(item.upper())
					count += 1
				elif item != "'":
					translated_list.append(item)
					count += 1
				elif item == "'":
					count += 1

			if sliced_list[-1] != "'":
				translated_list.append(sliced_list[-1])
		except IndexError:
			print ("end of list reached")
		print(translated_list)

	def resetFields(self):
		"""Sets all settable fields to white."""

		for i in range(len(self.rects_col)):
			if ((i + 5) % 9 == 0):
				continue
			self.rects_col[i] = self.imgs["white"]
			
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
					if confirmrect.collidepoint(event.pos):
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
					
						### START SOLVING ALGORITHM IN OTHER FILE ###
						###
						###
					
						# Create cube object
						cube = kubus.cube(calcu_list) # Values are returned on the line below this one
						calc_rest.vars.cube = cube
						ser = serial.Serial('/dev/tty.usbserial', 9600) #setup for pyserial
	
						moveList = calc_rest.algorithm() # Does algorithm magicy stuffs and returns the movelist.

						# Write movelist to arduino.
						transList = self.translateList(movelist)
						if ("list too long"):
							print(transList)
							partlist = []
							partsize = 50
							for i in range(int(len(transList) / partsize) - 1):
								partlist.append(transList[i : i * partsize])
							partlist.append(transList[int(len(transList) / partsize) : -1])
							for part in partlist:
								ser.write(bytes(part))
								# Wait for arduino to be done.
						else:
							ser.write(bytes(transList))
						# Reset rectangles to white and clear lists to solve another cube
						calcu_list.clear()
						self.showSavedText(saved, inforect)
						self.resetFields()

					#reset rects
					if resetrect.collidepoint(event.pos):
						resetFields()

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
							self.rects_col[i] = self.user_color
							break

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
			self.solverDisplay.blit(self.output_stringtext, (10, 550))
			# Blit front view rectangles with colors
			for color, rect in zip(self.rects_col, self.rects):
				self.solverDisplay.blit(color, rect)

			if confirmrect.collidepoint(mousepos):
				solverDisplay.blit(self.confirm2, self.confirmrect)
			else:
				solverDisplay.blit(self.confirm1, self.confirmrect)

			if resetrect.collidepoint(mousepos):
				solverDisplay.blit(self.reset2, self.resetrect)
			else:
				solverDisplay.blit(self.reset1, self.resetrect)

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
while game.active:
	game.showScreen()