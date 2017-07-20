import pygame
import os
import calc_rest
import cube as kubus
import serial

# Initialize pygame
pygame.init()
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
white_image = pygame.image.load("white.png")
red_image = pygame.image.load("red.png")
green_image = pygame.image.load("green.png")
blue_image = pygame.image.load("blue.png")
orange_image = pygame.image.load("orange.png")
yellow_image = pygame.image.load("yellow.png")
rubiks_image = pygame.image.load("rubiks.jpg")

# User color picker rectangles
white_rect = pygame.Rect(230, 400, 40, 40)
red_rect = pygame.Rect(280, 400, 40, 40)
green_rect = pygame.Rect(330, 400, 40, 40)
blue_rect = pygame.Rect(380, 400, 40, 40)
orange_rect = pygame.Rect(430, 400, 40, 40)
yellow_rect = pygame.Rect(480, 400, 40, 40)

# User color variables
user_color = white_image #default picked color from start is white
user_color_rect = pygame.Rect(150, 400, 40, 40)

# left view rectangles
l_rect1 = pygame.Rect(10, 40, 40, 40)
l_rect1col = white_image
l_rect2 = pygame.Rect(60, 40, 40, 40)
l_rect2col = white_image
l_rect3 = pygame.Rect(110, 40, 40, 40)
l_rect3col = white_image
l_rect4 = pygame.Rect(10, 90, 40, 40)
l_rect4col = white_image
l_rect5 = pygame.Rect(60, 90, 40, 40)
l_rect5col = red_image
l_rect6 = pygame.Rect(110, 90, 40, 40)
l_rect6col = white_image
l_rect7 = pygame.Rect(10, 140, 40, 40)
l_rect7col = white_image
l_rect8 = pygame.Rect(60, 140, 40, 40)
l_rect8col = white_image
l_rect9 = pygame.Rect(110, 140, 40, 40)
l_rect9col = white_image

# front view rectangles
f_rect1 = pygame.Rect(300, 40, 40, 40)
f_rect1col = white_image
f_rect2 = pygame.Rect(350, 40, 40, 40)
f_rect2col = white_image
f_rect3 = pygame.Rect(400, 40, 40, 40)
f_rect3col = white_image
f_rect4 = pygame.Rect(300, 90, 40, 40)
f_rect4col = white_image
f_rect5 = pygame.Rect(350, 90, 40, 40)
f_rect5col = rubiks_image
f_rect6 = pygame.Rect(400, 90, 40, 40)
f_rect6col = white_image
f_rect7 = pygame.Rect(300, 140, 40, 40)
f_rect7col = white_image
f_rect8 = pygame.Rect(350, 140, 40, 40)
f_rect8col = white_image
f_rect9 = pygame.Rect(400, 140, 40, 40)
f_rect9col = white_image

# right view rectangles
r_rect1 = pygame.Rect(600, 40, 40, 40)
r_rect1col = white_image
r_rect2 = pygame.Rect(650, 40, 40, 40)
r_rect2col = white_image
r_rect3 = pygame.Rect(700, 40, 40, 40)
r_rect3col = white_image
r_rect4 = pygame.Rect(600, 90, 40, 40)
r_rect4col = white_image
r_rect5 = pygame.Rect(650, 90, 40, 40)
r_rect5col = orange_image
r_rect6 = pygame.Rect(700, 90, 40, 40)
r_rect6col = white_image
r_rect7 = pygame.Rect(600, 140, 40, 40)
r_rect7col = white_image
r_rect8 = pygame.Rect(650, 140, 40, 40)
r_rect8col = white_image
r_rect9 = pygame.Rect(700, 140, 40, 40)
r_rect9col = white_image

# back view rectangles
ba_rect1 = pygame.Rect(10, 230, 40, 40)
ba_rect1col = white_image
ba_rect2 = pygame.Rect(60, 230, 40, 40)
ba_rect2col = white_image
ba_rect3 = pygame.Rect(110, 230, 40, 40)
ba_rect3col = white_image
ba_rect4 = pygame.Rect(10, 280, 40, 40)
ba_rect4col = white_image
ba_rect5 = pygame.Rect(60, 280, 40, 40)
ba_rect5col = yellow_image
ba_rect6 = pygame.Rect(110, 280, 40, 40)
ba_rect6col = white_image
ba_rect7 = pygame.Rect(10, 330, 40, 40)
ba_rect7col = white_image
ba_rect8 = pygame.Rect(60, 330, 40, 40)
ba_rect8col = white_image
ba_rect9 = pygame.Rect(110, 330, 40, 40)
ba_rect9col = white_image

# bottom view rectangles
b_rect1 = pygame.Rect(300, 230, 40, 40)
b_rect1col = white_image
b_rect2 = pygame.Rect(350, 230, 40, 40)
b_rect2col = white_image
b_rect3 = pygame.Rect(400, 230, 40, 40)
b_rect3col = white_image
b_rect4 = pygame.Rect(300, 280, 40, 40)
b_rect4col = white_image
b_rect5 = pygame.Rect(350, 280, 40, 40)
b_rect5col = blue_image
b_rect6 = pygame.Rect(400, 280, 40, 40)
b_rect6col = white_image
b_rect7 = pygame.Rect(300, 330, 40, 40)
b_rect7col = white_image
b_rect8 = pygame.Rect(350, 330, 40, 40)
b_rect8col = white_image
b_rect9 = pygame.Rect(400, 330, 40, 40)
b_rect9col = white_image

# top view rectangles
t_rect1 = pygame.Rect(600, 230, 40, 40)
t_rect1col = white_image
t_rect2 = pygame.Rect(650, 230, 40, 40)
t_rect2col = white_image
t_rect3 = pygame.Rect(700, 230, 40, 40)
t_rect3col = white_image
t_rect4 = pygame.Rect(600, 280, 40, 40)
t_rect4col = white_image
t_rect5 = pygame.Rect(650, 280, 40, 40)
t_rect5col = green_image
t_rect6 = pygame.Rect(700, 280, 40, 40)
t_rect6col = white_image
t_rect7 = pygame.Rect(600, 330, 40, 40)
t_rect7col = white_image
t_rect8 = pygame.Rect(650, 330, 40, 40)
t_rect8col = white_image
t_rect9 = pygame.Rect(700, 330, 40, 40)
t_rect9col = white_image

# init list to output
output_list = []

# init dictionaries for output
left_face = {}
front_face = {}

def showSavedText(image, rect):
	image_time = 840
	while image_time > 0:
		#print(image_time)
		solverDisplay.blit(image, rect)
		pygame.display.flip()
		image_time -= 1
	image_time = 840

def userColor(color):
	# Blits the picked color by user on the screen

	solverDisplay.blit(color, user_color_rect)

def drawFields():
	# draws lines on the screen to section off the front/top-left/down-left views

	#left view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (5, 30), (155, 30), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (5, 190), (155, 190), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (5, 30), (5, 190), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (155, 30), (155, 190), 2)

	#front view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (295, 30), (445, 30), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (295, 190), (445, 190), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (295, 30), (295, 190), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (445, 30), (445, 190), 2)

	#right view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (595, 30), (745, 30), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (595, 190), (745, 190), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (595, 30), (595, 190), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (745, 30), (745, 190), 2)

	#back view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (5, 220), (155, 220), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (5, 380), (155, 380), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (5, 220), (5, 380), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (155, 220), (155, 380), 2)

	#bottom view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (295, 220), (445, 220), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (295, 380), (445, 380), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (295, 220), (295, 380), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (445, 220), (445, 380), 2)

	#top view
	#top-left to top-right
	pygame.draw.line(solverDisplay, black, (595, 220), (745, 220), 2)
	#down-left to down-right
	pygame.draw.line(solverDisplay, black, (595, 380), (745, 380), 2)
	#top-left to down-left
	pygame.draw.line(solverDisplay, black, (595, 220), (595, 380), 2)
	#top-right to down-right
	pygame.draw.line(solverDisplay, black, (745, 220), (745, 380), 2)

	# draw fields where user can pick colors
	solverDisplay.blit(white_image, white_rect)
	solverDisplay.blit(red_image, red_rect)
	solverDisplay.blit(green_image, green_rect)
	solverDisplay.blit(blue_image, blue_rect)
	solverDisplay.blit(orange_image, orange_rect)
	solverDisplay.blit(yellow_image, yellow_rect)

def translateList(movelist):
	translated_list = []
	for item in movelist:
		sliced_list = list(item)

	count = 0

	try:
		for item in sliced_list[:-1]:
			if sliced_list[count + 1] == "'":
				translated_list.append(item.upper())
				#print (item.upper())
				count += 1
			elif item != "'":
				translated_list.append(item)
				#print(item)
				count += 1
			elif item == "'":
				count += 1

		if sliced_list[-1] != "'":
			translated_list.append(sliced_list[-1])
			#print (sliced_list[-1])
	except IndexError:
		print ("end of list reached")

	print(translated_list)

def resetFields():

	#init globals
	global user_color
	# Left view rects
	global l_rect1col
	global l_rect2col
	global l_rect3col
	global l_rect4col
	global l_rect5col
	global l_rect6col
	global l_rect7col
	global l_rect8col
	global l_rect9col
	# Front view rects
	global f_rect1col
	global f_rect2col
	global f_rect3col
	global f_rect4col
	global f_rect5col
	global f_rect6col
	global f_rect7col
	global f_rect8col
	global f_rect9col
	# Right view rects
	global r_rect1col
	global r_rect2col
	global r_rect3col
	global r_rect4col
	global r_rect5col
	global r_rect6col
	global r_rect7col
	global r_rect8col
	global r_rect9col
	# back view rects
	global ba_rect1col
	global ba_rect2col
	global ba_rect3col
	global ba_rect4col
	global ba_rect5col
	global ba_rect6col
	global ba_rect7col
	global ba_rect8col
	global ba_rect9col
	# Bottom view rects
	global b_rect1col
	global b_rect2col
	global b_rect3col
	global b_rect4col
	global b_rect5col
	global b_rect6col
	global b_rect7col
	global b_rect8col
	global b_rect9col
	# Top view rects
	global t_rect1col
	global t_rect2col
	global t_rect3col
	global t_rect4col
	global t_rect5col
	global t_rect6col
	global t_rect7col
	global t_rect8col
	global t_rect9col

	# Left view rects
	l_rect1col = white_image
	l_rect2col = white_image
	l_rect3col = white_image
	l_rect4col = white_image
	l_rect6col = white_image
	l_rect7col = white_image
	l_rect8col = white_image
	l_rect9col = white_image
	# Front view rects
	f_rect1col = white_image
	f_rect2col = white_image
	f_rect3col = white_image
	f_rect4col = white_image
	f_rect6col = white_image
	f_rect7col = white_image
	f_rect8col = white_image
	f_rect9col = white_image
	# Right view rects
	r_rect1col = white_image
	r_rect2col = white_image
	r_rect3col = white_image
	r_rect4col = white_image
	r_rect6col = white_image
	r_rect7col = white_image
	r_rect8col = white_image
	r_rect9col = white_image
	# Back view rects
	ba_rect1col = white_image
	ba_rect2col = white_image
	ba_rect3col = white_image
	ba_rect4col = white_image
	ba_rect6col = white_image
	ba_rect7col = white_image
	ba_rect8col = white_image
	ba_rect9col = white_image
	# Bottom view rects
	b_rect1col = white_image
	b_rect2col = white_image
	b_rect3col = white_image
	b_rect4col = white_image
	b_rect6col = white_image
	b_rect7col = white_image
	b_rect8col = white_image
	b_rect9col = white_image
	# Top view rects
	t_rect1col = white_image
	t_rect2col = white_image
	t_rect3col = white_image
	t_rect4col = white_image
	t_rect6col = white_image
	t_rect7col = white_image
	t_rect8col = white_image
	t_rect9col = white_image


def checkQuitandClicks():
	# Check for exit and event handling

	#init globals
	global user_color
	# Left view rects
	global l_rect1col
	global l_rect2col
	global l_rect3col
	global l_rect4col
	global l_rect5col
	global l_rect6col
	global l_rect7col
	global l_rect8col
	global l_rect9col
	# Front view rects
	global f_rect1col
	global f_rect2col
	global f_rect3col
	global f_rect4col
	global f_rect5col
	global f_rect6col
	global f_rect7col
	global f_rect8col
	global f_rect9col
	# Right view rects
	global r_rect1col
	global r_rect2col
	global r_rect3col
	global r_rect4col
	global r_rect5col
	global r_rect6col
	global r_rect7col
	global r_rect8col
	global r_rect9col
	# Bottom view rects
	global b_rect1col
	global b_rect2col
	global b_rect3col
	global b_rect4col
	global b_rect5col
	global b_rect6col
	global b_rect7col
	global b_rect8col
	global b_rect9col
	# Top view rects
	global t_rect1col
	global t_rect2col
	global t_rect3col
	global t_rect4col
	global t_rect5col
	global t_rect6col
	global t_rect7col
	global t_rect8col
	global t_rect9col
	# Back view rects
	global ba_rect1col
	global ba_rect2col
	global ba_rect3col
	global ba_rect4col
	global ba_rect5col
	global ba_rect6col
	global ba_rect7col
	global ba_rect8col
	global ba_rect9col
	# Init output list
	global output_list

	### THIS IS THE ACTUAL OUTPUT LIST OF PYGAME SURFACES THAT IS BEING SENT TO calcside.py and calc_rest.py ###
	output_list = [l_rect1col, l_rect2col, l_rect3col, l_rect4col, l_rect5col, \
				l_rect6col, l_rect7col, l_rect8col, l_rect9col, f_rect1col, f_rect2col, \
				f_rect3col, f_rect4col, f_rect5col, f_rect6col, f_rect7col, f_rect8col, \
				f_rect9col, r_rect1col, r_rect2col, r_rect3col, r_rect4col, r_rect5col, \
				r_rect6col, r_rect7col, r_rect8col, r_rect9col, ba_rect1col, ba_rect2col, \
				ba_rect3col, ba_rect4col, ba_rect5col, ba_rect6col, ba_rect7col, ba_rect8col, \
				ba_rect9col, b_rect1col, b_rect2col, b_rect3col, b_rect4col, b_rect5col, b_rect6col, \
				b_rect7col, b_rect8col, b_rect9col, t_rect1col, t_rect2col, t_rect3col, t_rect4col, \
				t_rect5col, t_rect6col, t_rect7col, t_rect8col, t_rect9col]
	#############################################################################################################
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = False
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:  # left mouse button
				#check confirm
				if confirmrect.collidepoint(event.pos):
					calcu_list = []

					for color in output_list:
						if color == white_image:
							calcu_list += "w"
						elif color == rubiks_image:
							calcu_list += "w"
						elif color == red_image:
							calcu_list += "r"
						elif color == green_image:
							calcu_list += "g"
						elif color == blue_image:
							calcu_list += "b"
						elif color == orange_image:
							calcu_list += "o"
						elif color == yellow_image:
							calcu_list += "y"
						else:
							calcu_list += "<no color>"
					
					### START SOLVING ALGORITHM IN OTHER FILE ###
					###
					###
					
					# Create cube object 
					cube = kubus.cube(calcu_list) # calcu list?
					ser = serial.Serial('/dev/tty.usbserial', 9600) #setup for pyserial
					while loopin == False 
						solve = cube.nextMove() # calls the cube.nextMove() function
						calc_rest(kubus, output_list)
						# nextMove() returns list of colors of all faces after a move
						# if it's solved, break out of this loop and ser.write(b solve)
						# if not, do the loop again and check for nextMove()
						if futureFunction(): 
							break
					#sends the move list to the arduino #check if this works
					# Check first algorithm/nextMove method? like cube.nextMove()
					# Do the move(cube.frontFaceCW() or something)
					# Check next algorithm etc etc
					# assemble movelist to send in calc_rest.py

					###
					###
					### END SOLVING ALGORITHM
					ser.write(bytes(movelist))
					# Reset rectangles to white and clear lists to solve another cube
					calcside.emptyList()
					calcu_list.clear()
					showSavedText(saved, inforect)
					resetFields()

				#reset rects
				if resetrect.collidepoint(event.pos):
					resetFields()

				#user color choice
				if white_rect.collidepoint(event.pos):
					user_color = white_image
				elif red_rect.collidepoint(event.pos):
					user_color = red_image
				elif green_rect.collidepoint(event.pos):
					user_color = green_image
				elif blue_rect.collidepoint(event.pos):
					user_color = blue_image
				elif orange_rect.collidepoint(event.pos):
					user_color = orange_image
				elif yellow_rect.collidepoint(event.pos):
					user_color = yellow_image

				#verander rect kleur van left view
				elif l_rect1.collidepoint(event.pos):
					l_rect1col = user_color
				elif l_rect2.collidepoint(event.pos):
					l_rect2col = user_color
				elif l_rect3.collidepoint(event.pos):
					l_rect3col = user_color
				elif l_rect4.collidepoint(event.pos):
					l_rect4col = user_color
				elif l_rect6.collidepoint(event.pos):
					l_rect6col = user_color
				elif l_rect7.collidepoint(event.pos):
					l_rect7col = user_color
				elif l_rect8.collidepoint(event.pos):
					l_rect8col = user_color
				elif l_rect9.collidepoint(event.pos):
					l_rect9col = user_color

				#verander rect kleur van front view
				elif f_rect1.collidepoint(event.pos):
					f_rect1col = user_color
				elif f_rect2.collidepoint(event.pos):
					f_rect2col = user_color
				elif f_rect3.collidepoint(event.pos):
					f_rect3col = user_color
				elif f_rect4.collidepoint(event.pos):
					f_rect4col = user_color
				elif f_rect6.collidepoint(event.pos):
					f_rect6col = user_color
				elif f_rect7.collidepoint(event.pos):
					f_rect7col = user_color
				elif f_rect8.collidepoint(event.pos):
					f_rect8col = user_color
				elif f_rect9.collidepoint(event.pos):
					f_rect9col = user_color

				#verander rect kleur van right view
				elif r_rect1.collidepoint(event.pos):
					r_rect1col = user_color
				elif r_rect2.collidepoint(event.pos):
					r_rect2col = user_color
				elif r_rect3.collidepoint(event.pos):
					r_rect3col = user_color
				elif r_rect4.collidepoint(event.pos):
					r_rect4col = user_color
				elif r_rect6.collidepoint(event.pos):
					r_rect6col = user_color
				elif r_rect7.collidepoint(event.pos):
					r_rect7col = user_color
				elif r_rect8.collidepoint(event.pos):
					r_rect8col = user_color
				elif r_rect9.collidepoint(event.pos):
					r_rect9col = user_color

				#verander rect kleur van back view
				elif ba_rect1.collidepoint(event.pos):
					ba_rect1col = user_color
				elif ba_rect2.collidepoint(event.pos):
					ba_rect2col = user_color
				elif ba_rect3.collidepoint(event.pos):
					ba_rect3col = user_color
				elif ba_rect4.collidepoint(event.pos):
					ba_rect4col = user_color
				elif ba_rect6.collidepoint(event.pos):
					ba_rect6col = user_color
				elif ba_rect7.collidepoint(event.pos):
					ba_rect7col = user_color
				elif ba_rect8.collidepoint(event.pos):
					ba_rect8col = user_color
				elif ba_rect9.collidepoint(event.pos):
					ba_rect9col = user_color

				#verander rect kleur van bottom view
				elif b_rect1.collidepoint(event.pos):
					b_rect1col = user_color
				elif b_rect2.collidepoint(event.pos):
					b_rect2col = user_color
				elif b_rect3.collidepoint(event.pos):
					b_rect3col = user_color
				elif b_rect4.collidepoint(event.pos):
					b_rect4col = user_color
				elif b_rect6.collidepoint(event.pos):
					b_rect6col = user_color
				elif b_rect7.collidepoint(event.pos):
					b_rect7col = user_color
				elif b_rect8.collidepoint(event.pos):
					b_rect8col = user_color
				elif b_rect9.collidepoint(event.pos):
					b_rect9col = user_color

				#verander rect kleur van top view
				elif t_rect1.collidepoint(event.pos):
					t_rect1col = user_color
				elif t_rect2.collidepoint(event.pos):
					t_rect2col = user_color
				elif t_rect3.collidepoint(event.pos):
					t_rect3col = user_color
				elif t_rect4.collidepoint(event.pos):
					t_rect4col = user_color
				elif t_rect6.collidepoint(event.pos):
					t_rect6col = user_color
				elif t_rect7.collidepoint(event.pos):
					t_rect7col = user_color
				elif t_rect8.collidepoint(event.pos):
					t_rect8col = user_color
				elif t_rect9.collidepoint(event.pos):
					t_rect9col = user_color

def showScreen():

	while True:

		mousepos = pygame.mouse.get_pos()

		# Fill background
		solverDisplay.fill((255,255,255))
		# Blit text
		solverDisplay.blit(front_text, (300, 10))
		solverDisplay.blit(left_text, (10, 10))
		solverDisplay.blit(right_text, (600, 10))
		solverDisplay.blit(back_text, (10, 200))
		solverDisplay.blit(bottom_text, (300, 200))
		solverDisplay.blit(top_text, (600, 200))
		solverDisplay.blit(usercolor_text, (10, 410))
		solverDisplay.blit(output_stringtext, (10, 550))
		# Blit front view rectangles with colors
		solverDisplay.blit(f_rect1col, f_rect1)
		solverDisplay.blit(f_rect2col, f_rect2)
		solverDisplay.blit(f_rect3col, f_rect3)
		solverDisplay.blit(f_rect4col, f_rect4)
		solverDisplay.blit(f_rect5col, f_rect5)
		solverDisplay.blit(f_rect6col, f_rect6)
		solverDisplay.blit(f_rect7col, f_rect7)
		solverDisplay.blit(f_rect8col, f_rect8)
		solverDisplay.blit(f_rect9col, f_rect9)
		# Blit left view rects with colors
		solverDisplay.blit(l_rect1col, l_rect1)
		solverDisplay.blit(l_rect2col, l_rect2)
		solverDisplay.blit(l_rect3col, l_rect3)
		solverDisplay.blit(l_rect4col, l_rect4)
		solverDisplay.blit(l_rect5col, l_rect5)
		solverDisplay.blit(l_rect6col, l_rect6)
		solverDisplay.blit(l_rect7col, l_rect7)
		solverDisplay.blit(l_rect8col, l_rect8)
		solverDisplay.blit(l_rect9col, l_rect9)
		# Blit right view rects with colors
		solverDisplay.blit(r_rect1col, r_rect1)
		solverDisplay.blit(r_rect2col, r_rect2)
		solverDisplay.blit(r_rect3col, r_rect3)
		solverDisplay.blit(r_rect4col, r_rect4)
		solverDisplay.blit(r_rect5col, r_rect5)
		solverDisplay.blit(r_rect6col, r_rect6)
		solverDisplay.blit(r_rect7col, r_rect7)
		solverDisplay.blit(r_rect8col, r_rect8)
		solverDisplay.blit(r_rect9col, r_rect9)
		# Blit back view rects with colors
		solverDisplay.blit(ba_rect1col, ba_rect1)
		solverDisplay.blit(ba_rect2col, ba_rect2)
		solverDisplay.blit(ba_rect3col, ba_rect3)
		solverDisplay.blit(ba_rect4col, ba_rect4)
		solverDisplay.blit(ba_rect5col, ba_rect5)
		solverDisplay.blit(ba_rect6col, ba_rect6)
		solverDisplay.blit(ba_rect7col, ba_rect7)
		solverDisplay.blit(ba_rect8col, ba_rect8)
		solverDisplay.blit(ba_rect9col, ba_rect9)
		# Blit bottom view rects with colors
		solverDisplay.blit(b_rect1col, b_rect1)
		solverDisplay.blit(b_rect2col, b_rect2)
		solverDisplay.blit(b_rect3col, b_rect3)
		solverDisplay.blit(b_rect4col, b_rect4)
		solverDisplay.blit(b_rect5col, b_rect5)
		solverDisplay.blit(b_rect6col, b_rect6)
		solverDisplay.blit(b_rect7col, b_rect7)
		solverDisplay.blit(b_rect8col, b_rect8)
		solverDisplay.blit(b_rect9col, b_rect9)
		# Blit top view rects with colors
		solverDisplay.blit(t_rect1col, t_rect1)
		solverDisplay.blit(t_rect2col, t_rect2)
		solverDisplay.blit(t_rect3col, t_rect3)
		solverDisplay.blit(t_rect4col, t_rect4)
		solverDisplay.blit(t_rect5col, t_rect5)
		solverDisplay.blit(t_rect6col, t_rect6)
		solverDisplay.blit(t_rect7col, t_rect7)
		solverDisplay.blit(t_rect8col, t_rect8)
		solverDisplay.blit(t_rect9col, t_rect9)

		if confirmrect.collidepoint(mousepos):
			solverDisplay.blit(confirm2, confirmrect)
		else:
			solverDisplay.blit(confirm1, confirmrect)

		if resetrect.collidepoint(mousepos):
			solverDisplay.blit(reset2, resetrect)
		else:
			solverDisplay.blit(reset1, resetrect)

		drawFields()
		# blit user color, must be before checkQuitandClicks!!
		userColor(user_color)
		# check for exit and clicks
		checkQuitandClicks()

		# update screen
		pygame.display.flip()

		# frames
		clock.tick(60)

while active:
	showScreen()