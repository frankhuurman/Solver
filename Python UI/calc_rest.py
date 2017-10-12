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

class vars:
	
	def getLUT():
		"""Method to extract data from the LUT.txt file."""

		lut = []
		alg = -1
		cc = ""
		with open("lut.txt", "r") as file:
			for i, line in enumerate(file):
				
				# Find current algorithm
				if (line.find("algo") is not -1):
					alg += 1
					lut.append({})

				# Find color combo.
				elif (len(line.strip()) <= 5):
					cc = line.strip()
					lut[alg][cc] = {}

				# Find actual data.
				else:
					cpos = (line.find(":"))
					if (cpos is not -1):
						m = line[(cpos + 2):].strip()
						f = int(line[cpos - 9])
						x = int(line[cpos - 6])
						y = int(line[cpos - 3])
						lut[alg][cc][(f, x, y)] = m

		return(lut)

	LUT = getLUT()
	translist = []
	moveListBuffer = ""
	solved = False
	algos = []
	for i in range(3):
		algos.append(False)
	algo4 = False
	algo5 = False
	algo6 = False
	aglo7 = False
	cube = None


def translateMoves(alg, mod, *moves):


	tList = {2 :{	# Algo2
				"red" : {"f" : "u",
							"r" : "b",
							"u" : "l",
							"b" : "d",
							"l" : "f",
							"d" : "r"},
				"orange":{"f": "u",
							"r" : "f",
							"u" : "r",
							"b" : "d",
							"l" : "b",
							"d" : "l"},
				"green":{"f" : "u",
							"r" : "l",
							"u" : "f",
							"b" : "d",
							"l" : "r",
							"d" : "b"},
				"blue": {"f" : "u",
							"r" : "r",
							"u" : "b",
							"b" : "d",
							"l" : "l",
							"d" : "f"}
				}, 3: {	# Algo3
				"red" : {"f" : "d",
							"r" : "b",
							"u" : "r",
							"b" : "u",
							"l" : "f",
							"d" : "l"},
				"red" : {"f" : "d",
							"r" : "f",
							"u" : "l",
							"b" : "u",
							"l" : "b",
							"d" : "r"}
				}, 4: {	# Algo4
				"blue": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"}
				}, 5: {	# Algo5
				"red" : {"f" : "d",
							"r" : "b",
							"u" : "r",
							"b" : "u",
							"l" : "f",
							"d" : "l"},
				"green":{"f" : "d",
							"r" : "r",
							"u" : "f",
							"b" : "u",
							"l" : "l",
							"d" : "b"},
				"blue": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"},
				"orange":{"f": "d",
							"r" : "f",
							"u" : "l",
							"b" : "u",
							"l" : "b",
							"d" : "r"}
				}}
				

	mvs = ""
	try:
		for m in moves:
			up = False
			if (m.isupper()):
				up = True
			new = tList[alg][mod][m.lower()]
			if (up):
				new = new.upper()
			mvs += new
	except:
		return(moves)
	return(mvs)



def ifBulk(colorCombo, pos):
	#TODO: Start mirroring the algorithm, be mindfull that there are still a few positions that will require solving.
	#TODO: Translate the RDrd sequence to work for all four sides using each side's respective stepper motors (RDrd refers to two specific stepper motors, which would mean one corner would constantly be moved when passing RDrd to the move list.) <-- PRIORITY
	#TODO: Look into making a function that adds 'RDrd' s depending on the position of the white surface relative to the white face when in the correct vertical row (Algo2) <-- important
	#TODO: Remove the pass statements once a section is finished
	#TODO: change colorcombo's. see line 37
	#TODO: Decide which face to use as the front for algo4 (honestly doesn't matter since the end result is symetrical from all for sides)
	cube = vars.cube  
	results = ""
	
	if not vars.algo4: # Blue considered front 
		if cube.faces[cube.facenames[3]].squares[0][1] == "y":
			if cube.faces[cube.facenames[3]].squares[1][0] == "y":
				if cube.faces[cube.facenames[3]].squares[1][2] == "y":
					if cube.faces[cube.facenames[3]].squares[2][1] == "y":
						results = ""
				else:
					results = translateMoves(4, "b", "fruRUF")
			elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
				results = translateMoves(4, "b", "U")
		elif cube.faces[cube.facenames[3]].squares[1][0] == "y":
			if cube.faces[cube.facenames[3]].squares[1][2] == "y":
				results = translateMoves(4, "b", "fruRUF")
			elif cube.faces[cube.facenames[3]].squares[2][1] == "y":
				results = translateMoves(4, "b", "u")
		elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
			if cube.faces[cube.facenames[3]].squares[2][1] == "y":
				results = translateMoves(4, "b", "uu")
		else:
			results = translateMoves(4, "blue", "fruRUF")

	if not vars.algo5: 
		if cube.faces[cube.facenames[0]].squares[1][0] is not "r":
			if cube.faces[cube.facenames[4]].squares[2][1] is not "b":
				if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "red"
						results = translateMoves(5, "r", "u")
					elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
						front = "red"
						results = "ruRuruuRu"
				elif cube.faces[cube.facenames[2]].squares[1][2] == "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "green"
						results = "ruRuruuRu"
					elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
						front = "red"
						results = "ruRuruuRu"
			elif cube.faces[cube.facenames[4]].squares[1][2] == "b":
				if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "orange"
						results = "ruRuruuRu"
					if cube.faces[cube.facenames[5]].squares[0][1] == "g":
						front = "orange"
						results = "ruRuruuRu"
				elif cube.faces[cube.facenames[2]].squares[1][2] == "o":				
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "green"
						results = "ruRuruuRu"
					if cube.faces[cube.facenames[5]].squares[0][1] == "g":
						results = ""
		elif cube.faces[cube.facenames[0]].squares[1][0] == "r":
			if cube.faces[cube.facenames[4]].squares[2][1] is not "b":
				if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "blue"
						results = "ruRuruuRu"
					elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
						front = "blue"
						results = "ruRuruuRu"
				elif cube.faces[cube.facenames[2]].squares[1][2] == "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "blue"
						results = "ruRuruuRu"
					elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
						results = ""
						print("Error 1: This shouldn't even trigger; algo5")
			elif cube.faces[cube.facenames[4]].squares[2][1] == "b":
				if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "orange"
						results = "ruRuruuRu"
					elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
						results = ""
						print("Error 2: This shouldn't event trigger; algo5")
				elif cube.faces[cube.facenames[2]].squares[1][2] == "o":
					results = ""
					print("Error 3: This shouldn't even trigger; algo5")

	if not vars.algo6:
		fronts = ["r", "b", "g", "o"]
		location = [(0,0,0), (0,2,0), (2,0,2), (2,2,2)]
		edgeColor = ["rgy", "rby", "ogy", "oby"]
		iter = 0
		coords, colors = cube.getCorners("r")
		for iter in range(4):
			pas = True
			for c in colors[iter]:
				if (not c in edgeColor[iter]):
					pas = False
			if pas:
				if (coords[iter] == location[iter]):
					iter += 1
					front = fronts[iter]
					results = "urULuRUl"

	'''if not vars.algo7: # List algo 7
		if colorCombo == yellowOrangeBlue: pass
			# Code goes here.
		if colorCombo == yellowBlueRed: pass
			# Code goes here.
		if colorCombo == yellowRedGreen: pass
			# Code goes here.
		if colorCombo == yellowGreenOrange: pass
			# Code goes here. '''

	cube.sendMoves(results) # Sends results to the cube updating it.
	vars.moveListBuffer += results # Adds this cycle's moves into the buffer.
	print(vars.moveListBuffer)
	

def algorithm():

	input("Start solving.")
	results = ""
	while not vars.solved and not vars.cube.stopSolving: # Check if the cube is solved
		count = 0
		for i in range(3):
			while not vars.algos[i] and not vars.cube.stopSolving:# Check to see if the white edges are solved
				count = 0
				if (i == 1):
					coords, colors = vars.cube.getCorners("w")
				else:
					coords, colors = vars.cube.getEdge("w")
				for j in range(len(coords)):
					moves = vars.LUT[0][colors[j]][coords[j]]
					if (moves is not ""):
						vars.cube.sendMoves(moves)
						vars.moveListBuffer += moves
						break	# Redo the while loop to get the current location of all white edges.
					else:
						count += 1	# If sqaure is correct, count it.
					if (count == 4):
						print(coords, colors)
						vars.algos[i] = True	# All white edges are resolved, end this step of algorithm.
		print(vars.moveListBuffer)
		vars.cube.stopSolving = True

#		whiteRedGreen:		Green considered front
#		whiteBlueRed:		Red considered front
#		whiteOrangeBlue:	Blue considered front
#		whiteGreenOrange:	Orange considered front

		
		"""
		while not vars.algo4: pass # Check to see if the yellow cross exists, simple Boolean TRUE / FALSE (LOOP)
			#Check each edge that is still not in the correct position (Back) for yellow
				# Check if the edge is in the correct position already
					# If the block is in the correct position then mark it as completed (Can be one of four spots. aslong as it is at a edge on the yellow face it counts as a correct position)
						count += 1 # Increase a counter that keeps track of the amount of correct edges
						if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
							count = 0
							algo4 = True
					# Else go through the list using the position of the yellow edge.
						# Store the corresponding moves required to put the edge in the correct position in moveListBuffer
		"""
		"""
		while not vars.algo5:  pass# Check to see if the yellow edges are solved, simple Boolean TRUE / FALSE (LOOP)
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
		"""
		"""
		while not vars.algo6: pass # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
		"""
		"""
		while not vars.solved: pass# Check to see if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
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
				# Break out of this loop (This is under the assumption everything up until now has worked)'''
			"""
	if vars.cube.solved():
		return vars.moveListBuffer