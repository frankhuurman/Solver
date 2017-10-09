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
						m = line[cpos + 2:].strip()
						f = line[cpos - 9]
						x = line[cpos - 6]
						y = line[cpos - 3]
						lut[alg][cc][(f, x, y)] = m

		return(lut)

	LUT = getLUT()
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

def ifBulk(colorCombo, pos):
	#TODO: Start mirroring the algorithm, be mindfull that there are still a few positions that will require solving.
	#TODO: Translate the RDrd sequence to work for all four sides using each side's respective stepper motors (RDrd refers to two specific stepper motors, which would mean one corner would constantly be moved when passing RDrd to the move list.) <-- PRIORITY
	#TODO: Look into making a function that adds 'RDrd' s depending on the position of the white surface relative to the white face when in the correct vertical row (Algo2) <-- important
	#TODO: Remove the pass statements once a section is finished
	#TODO: Fix algo1 "wr", has the algorithm for two edges for some reason # seems to be for the white - green edge aswell as the white - red edge.
#TODO: Decide which face to use as the front for algo4 (honestly doesn't matter since the end result is symetrical from all for sides)
	cube = vars.cube  
	results = ""
	
	for i, a in enumerate(vars.algos):
		if (not a):
			results = vars.LUT[i][cc][pos]
			break
			
	if not vars.algo4: # Blue considered front 
		if cube.faces[cube.facenames[3]].squares[0][1] == "y":
			if cube.faces[cube.facenames[3]].squares[1][0] == "y":
				if cube.faces[cube.facenames[3]].squares[1][2] == "y":
					if cube.faces[cube.facenames[3]].squares[2][1] == "y":
						results = "" 
				else:
					results = "fruRUF"                                               
			elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
				results = "U"
		elif cube.faces[cube.facenames[3]].squares[1][0] == "y":
			if cube.faces[cube.facenames[3]].squares[1][2] == "y":
				results = "fruRUF"
			elif cube.faces[cube.facenames[3]].squares[2][1] == "y":
				results = "u"
		elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
			if cube.faces[cube.facenames[3]].squares[2][1] == "y":
				results = "uu"
		else:
			results = "fruRUF"
	if not vars.algo5: 
		if cube.faces[cube.facenames[0]].squares[1][0] is not "r":
			if cube.faces[cube.facenames[4]].squares[2][1] is not "b":
				if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
					if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
						front = "red"
						results = "u"
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
	if not vars.algo6: pass# List algo 6
		# Not even going to bother attempting to write pseudo code for this one at present.
	'''if not vars.algo7: # List algo 7
		if colorCombo == yellowOrangeBlue: pass
			# Code goes here.
		if colorCombo == yellowBlueRed: pass
			# Code goes here.
		if colorCombo == yellowRedGreen: pass
			# Code goes here.
		if colorCombo == yellowGreenOrange: pass
			# Code goes here. '''
	cube.sendmoves(results) # Sends results to the cube updating it.
	vars.moveListBuffer += results # Adds this cycle's moves into the buffer. 

def algorithm():
	count = 0
	while not vars.solved: # Check if the cube is solved
		while not vars.algos[0]:# Check to see if the white edges are solved
			for name in vars.cube.facenames: # Check each face for edges # name comes from where?
				print(name)
				edges, colorCombo = vars.cube.getEdge(name, "w") # Check each block asociated with an edge to see if it is white
				"""^^ updated this line for the new cube code."""
				while (len(edges) > 0): # Don't need to go further if there are no white edges.
					edges, colorCombo = vars.cube.getEdge(name, "w") # Check each block asociated with an edge to see if it is white
					pos = edges[0]
					ifBulk(colorCombo[0], pos[0])
					count += 1 # Used to indicate a edge has been solved
					if count == 4: 
						count = 0 # reset count to 0
						algo1 = True
		'''while not vars.algo2:  # Check to see if the white face is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check each corner block for the color white
				count += 1
				if count == 4:# Increase a counter that keeps track of the amount of correct corners.
					count = 0 # If the counter indicates 3, meanig all four corners are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
					algo2 = True
				# Check the two other blocks of the corner for their color
					# Take the number asociated with the white block and run it through a list to see what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer.
		while not vars.algo3: pass # Check to see if the middle layer is solved, simple Boolean TRUE / FALSE (LOOP)
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
		while not vars.algo6: pass # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
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
	if vars.cube.solved():
		return vars.moveListBuffer