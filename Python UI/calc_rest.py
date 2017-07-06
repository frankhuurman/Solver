from pprint import pprint
from collections import OrderedDict

# TODO: Define which blocks are edges, doesn't need to be defined for each face individualy, just itterate through the faces and asign 2, 4, 6 and eight as edges
# TODO: Link the sides of individual edges and corners so they move with one another

def printFace(facename, face):
	"""Prints the name of the face and the face that is given as an argument"""
	# example: printFace("left face: ", left_face)

	#TODO: Rewrite this part for a LIST item instead of Dict

	temp_dict = OrderedDict()
	count = 1
	for item, value in face.items():
		temp_dict[count] = value
		count += 1

	print(facename)
	print(temp_dict[1], temp_dict[2], temp_dict[3])
	print(temp_dict[4], temp_dict[5], temp_dict[6])
	print(temp_dict[7], temp_dict[8], temp_dict[9], "\n")
	1, ff
	2, bf



class cube(object):

	facesnames = ["left_face", "front_face", "right_face", "back_face", "bottom_face", "top_face"]
	faces = {}

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """
		print(outputlist)
		for i, f in enumerate(self.facesnames):
			self.faces[f] = face(outputlist[i*9 : i*9 + 9])

		for f in self.facesnames:
			print("Face: " + f)
			print(self.faces[f].printFace())
			print(self.faces[f].face_color)
			print(self.faces[f].allTheSame())
		
		
		
class face(object):
	
	# squares
	@property
	def squares(self):
		return(self.__squares)
	@squares.setter
	def squares(self, squares):
		self.__squares = squares
	# face_color
	@property
	def face_color(self):
		return(self.__face_color)
	@face_color.setter
	def face_color(self, face_color):
		self.__face_color = face_color
		
		
	def __init__(self, data):
		self.squares = []
		print(data)
		self.face_color = data[int(len(data)/2)]
		print("Face_color:", str(self.face_color))
		for i in range(3):
			moi = []
			for j in range(3):
				print(str(i), str(j), str((i*3)+j), str(data[(i*3)+j]))
				moi.append(data[(i*3)+j])
			self.squares.append(moi)
			del(moi)

	def allTheSame(self):
		"""Return True if all the colors of the square are the same color."""
		same = True
		for color in self.squares:
			if (not color == self.face_color):
				same = False
		return(same)

	def printFace(self):
		display = ""
		for row in self.squares:
			for sq in row:
				display += "\t" + str(sq)
			display += "\n"

def list(colorCombo, pos)
	#TODO: Add booleans for selecting which algorithm need to be picked
	#TODO: Define moveListBuffer somewhere 
	if algo1 == True:
		if colorCombo == whiteRed: # skip front 4
			if pos == cube.front_face(2): # V 
				moveListBuffer += "uubllb'u'u'"
			if pos == cube.front_face(6): # V 
				moveListBuffer += "r'ddl'd'd'r"
			if pos == cube.front_face(8): # V 
				movelistBuffer += "ddb'llbd'd'"
			if pos == cube.left_face(2): # V
				moveListBuffer += "ubllb'u'"
			if pos == cube.left_face(4): # V
				moveListBuffer += "bdl'd'b'"
			if pos == cube.left_face(6): # V
				moveListBuffer += "fulu'f'"
			if pos == cube.left_face(8): # V
				moveListBuffer += "l'fulu'f'l"
			if pos == cube.top_face(2): # V
				moveListBuffer += "u'lu"
			if pos == cube.top_face(4): # V
				moveListBuffer += "l"
			if pos == cube.top_face(6): # V
				moveListBuffer += "uulu'u'"
			if pos == cube.top_face(8): # V
				moveListBuffer += "ulu'"
			if pos == cube.right_face(2): # V 
				moveListBuffer += "u'bllb'u"
			if pos == cube.right_face(4): # V 
				moveListBuffer += "ru'bllb'ur'"
			if pos == cube.right_face(6): # V
				moveListBuffer += "bdl'd'b'"
			if pos == cube.right_face(8): # V
				moveListBuffer += "r'b'dl'd'br"
			if pos == cube.bottom_face(2): # V 
				moveListBuffer += "d'l'd"
			if pos == cube.bottom_face(4): # V
				moveListBuffer += "l'"
			if pos == cube.bottom_face(6): # V
				moveListBuffer += "ddl'd'd'"
			if pos == cube.bottom_face(8): # V
				moveListBuffer += "d'l'd"
			if pos == cube.back_face(2): # V
				moveListBuffer += "bllb'"
			if pos == cube.back_face(4): # V
				moveListBuffer += "bbllb'b'"
			if pos == cube.back_face(6): # V
				moveListBuffer += "ll"
			if pos == cube.back_face(8): # V
				moveListBuffer += "b'llb"
		if colorCombo == whiteBlue: # skip front 2
			if pos == cube.front_face(4):
				moveListBuffer += 

		# EXAMPLE
		# If colorCombo = (whiteRed) 
			# If pos = face(number)
			# If pos = face(number)
		# If colorCombo = (whiteBlue)
			# If pos = face(number) !&*NHDSW*&!DJ*(SQJ*(DAMUSUI(!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!))) 24 edges
			# If pos = face(number)
		# if colorCombo = (whiteOrange)
			# If pos = face(number)
			# If pos = face(number)
		# if colorCombo = (WhiteGreen)
			# If pos = face(number)
			# If pos = face(number)
		# EXAMPLE
	# List algo 2
	# List algo 3
	# List algo 4
	# List algo 5 
	# List algo 6 
	# List algo 7 """


def Algorithm
	solved = False
	algo1 = False
	algo2 = False
	algo3 = False
	algo4 = False
	algo5 = False
	algo6 = False
	while solved == False: # Check if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
		while algo1 == False:# Check to see if the white edges are solved, done through a simple Boolean TRUE / FALSE (LOOP)
			# Check each block asociated with a edge to see if it is white
				# If a white edge is found and it is already in, or has been moved to a correct position then ignore it.
					# Increase a counter that keeps track of the amount of correct edges.
					# If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
				# Check the other side of the edge to see what color it is
					# Take the number asociated with the white block and run it through a list to check what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer
				# Move to the next edge block
		while algo2 == False: # Check to see if the white face is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check each corner block for the color white
				# If a white Corner is found and it is already in, or has been moved to a correct position then ignore it.
					# Increase a counter that keeps track of the amount of correct corners.
					# If the counter indicates 3, meanig all four corners are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
				# Check the two other blocks of the corner for their color
					# Take the number asociated with the white block and run it through a list to see what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer.
		while algo3 == False: # Check to see if the middle layer is solved, simple Boolean TRUE / FALSE (LOOP) @##$U*@$*(!@($#!U@$ !@#$!@*U$NJSAU*!&$(!@#(!@#NCAISKDQ !@#*@$!@&(#*SDAS DAS d)) CHECK IF THIS BLOCK WORKS (IN THEORY ANYWAYS)
			# Check each edge on the middle and back layer of the cube for a orange color
				# If a orange edge is found then check the other side of the edge 
					# Check if the block is in the correct position
						# If the block is in the correct position then mark it as completed
							# Increase a counter that keeps track of the amount of correct edges
							# If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
						# Else check the color combination in combination with it's position in the list.
							# Store the corresponding moves in moveListBuffer
		while algo4 == False: # Check to see if the yellow cross exists, simple Boolean TRUE / FALSE (LOOP)
			#Check each edge that is still not in the correct position (Back) for yellow
				# Check if the edge is in the correct position already
					# If the block is in the correct position then mark it as completed (Can be one of four spots. aslong as it is at a edge on the yellow face it counts as a correct position)
						# Increase a counter that keeps track of the amount of correct edges
						# If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
					# Else go through the list using the position of the yellow edge.
						# Store the corresponding moves required to put the edge in the correct position in moveListBuffer
		while algo5 == False # Check to see if the yellow edges are solved, simple Boolean TRUE / FALSE (LOOP)
			# Check the color of the color on the non yellow sides of the edges.
				# If the color matches the color of the center of the face (5)
					# Increase a counter that keeps track of the amount of correct edges.
					# If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
				# Else check the color of the adjacent edge, going clockwise
					# If the color of the adjacent edge matches the color of the center block of their respective face
						# Go back to looking for a unsolved block skipping this one for the next round
					# Else go through the list 
						# Store the moves in moveListBuffer #@!$!*@$*!@)#!@$(!@$)!@)#!@)_%()!@# KEEP IN MIND THAT THIS DOES NOT FOLLOWS THE STANDARD ALGORITHM AND IT NEEDS TO BE ADAPTED TO WORK FOR EACH OF THE FOUR SIDES!
		while algo6 == False # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
		while solved == False # Check to see if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
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
	# Send moveListBuffer back to solverfinal2.py