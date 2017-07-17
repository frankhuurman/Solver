

#TODO: Update all the calls to cube
#cube.faces[cube.facenames[0]].squares[0][0] left
#cube.faces[cube.facenames[1]].squares[0][0] front
#cube.faces[cube.facenames[2]].squares[0][0] right
#cube.faces[cube.facenames[3]].squares[0][0] back
#cube.faces[cube.facenames[4]].squares[0][0] bottom
#cube.faces[cube.facenames[5]].squares[0][0] top

def ifBulk(moveListBuffer, colorCombo, pos, cube, algo1, algo2, algo3, algo4, algo5, algo6, algo7):
	#TODO: Add booleans for selecting which algorithm need to be picked
	#TODO: Define moveListBuffer somewhere 
	if algo1 == False: #NOTE: Check the position of the WHITE side of the edge
		if colorCombo == whiteRed: # correct pos == cube.faces[cube.facenames[1]].squares[1][0]
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				break # Ch3ck 1f th15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: # V 
				moveListBuffer += "uubllb'u'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: # V 
				moveListBuffer += "r'ddl'd'd'r"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: # V 
				movelistBuffer += "ddb'llbd'd'"
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				moveListBuffer += "ubllb'u'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				moveListBuffer += "bdl'd'b'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				moveListBuffer += "fulu'f'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				moveListBuffer += "l'fulu'f'l"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				moveListBuffer += "u'lu"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				moveListBuffer += "l"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				moveListBuffer += "uulu'u'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				moveListBuffer += "ulu'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: # V 
				moveListBuffer += "u'bllb'u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: # V 
				moveListBuffer += "ru'bllb'ur'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				moveListBuffer += "bdl'd'b'"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				moveListBuffer += "r'b'dl'd'br"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: # V 
				moveListBuffer += "d'l'd"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				moveListBuffer += "l'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				moveListBuffer += "ddl'd'd'"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				moveListBuffer += "d'l'd"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				moveListBuffer += "bllb'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				moveListBuffer += "bbllb'b'"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				moveListBuffer += "ll"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				moveListBuffer += "b'llb"
		if colorCombo == whiteBlue: # correct pos == cube.faces[cube.facenames[1]].squares[2][1]:
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: 
				moveListBuffer += "uubbddb'b'u'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				moveListBuffer += "llbddl'l'b'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				moveListBuffer += "rrb'ddbr'r'"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				break # ch3ck 1f th15 w0rk5
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: 
				moveListBuffer += "lldl'l'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				moveListBuffer += "l'dl"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				moveListBuffer += "ldl'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: 
				moveListBuffer += "d"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				moveListBuffer += "bl'dlb'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				moveListBuffer += "l'bddb'l"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				moveListBuffer += "rb'ddbr'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				moveListBuffer += "ul'bddb'lu'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				moveListBuffer += "rrd'r'r'"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				moveListBuffer += "r'd'r"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				moveListBuffer += "rd'r"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				movelistBuffer += "d'"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				moveListBuffer += "dr'b'ddbr"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				moveListBuffer += "lbddb'l'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				moveListBuffer += "r'b'ddbr"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				moveListBuffer += "brd'"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				moveListBuffer += "rrd'r'r'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				moveListBuffer += "r'd'r"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				moveListBuffer += "rdr'"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				moveListBuffer += "d'"
		if colorCombo == whiteOrange: # correct pos == cube.faces[cube.facenames[1]].squares[1][2]:
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				movelistBuffer += "l'bd'rrdb'l"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				moveListBuffer += "bd'rrdb'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				movelistBuffer += "ld'brrb'dl'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				moveListBuffer += "d'brrb'd"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]:
				moveListBuffer += "uub'rrbu'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				moveListBuffer += "lddrd'd'l'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				break # ch3ck 1f th15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				moveListBuffer += "ddbrrb'd'd'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				moveListBuffer += "rb'd'rdb"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				moveListBuffer += "r'dbrrb'd'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				moveListBuffer += "b'd'rdb"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				moveListBuffer += "r'b'd'rdb"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				moveListBuffer += "brrb'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				moveListBuffer += "rr"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				moveListBuffer += "bbrrb'b'"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				moveListBuffer += "drd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				moveListBuffer += "ddrd'd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				moveListBuffer += "r"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				moveListBuffer += "d'rd"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				moveListBuffer += "brrb'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				moveListBuffer += "ubrrb'u'"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				moveListBuffer += "r'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				moveListBuffer += "u'r'u"
		if colorCombo == whiteGreen: # correct pos == cube.faces[cube.facenames[1]].squares[0][1]:
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				movelistBuffer += "u'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				moveListBuffer += "lu'l'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				movelistBuffer += "l'u'l"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				moveListBuffer += "llu'l'l'"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]:
				break # ch3ck 1f th15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				moveListBuffer += "llb'uubl'l'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				moveListBuffer += "rrbuub'r'r'"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				moveListBuffer += "ddbbuub'b'd'd'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				moveListBuffer += "u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				moveListBuffer += "rur'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				moveListBuffer += "r'ur"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				moveListBuffer += "rrur'r'"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				moveListBuffer += "uu"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				moveListBuffer += "buub'"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				moveListBuffer += "b'uub"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				moveListBuffer += "bbuub'b'"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				moveListBuffer += "dr'buub'rd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				moveListBuffer += "lb'uubl'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				moveListBuffer += "r'buub'r"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				moveListBuffer += "br'urb'"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				moveListBuffer += "blu'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				moveListBuffer += "l'b'uubl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				moveListBuffer += "rbuub'r'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				moveListBuffer += "u'rbuub'r'u"
	# List algo 2
	# List algo 3
	# List algo 4
	# List algo 5 
	# List algo 6 
	# List algo 7 """

	for name in cube.facenames:
		cube.faces[name]

def Algorithm(cube):
	solved = False
	algo1 = False
	algo2 = False
	algo3 = False
	algo4 = False
	algo5 = False
	algo6 = False
	count = 0
	moveListBuffer = []
	while solved == False: # Check if the cube is solved
		while algo1 == False:# Check to see if the white edges are solved
			for name in cube.facenames:
				whiteEdges = cube.faces[name].checkEdges("w") # Check each block asociated with a edge to see if it is white
				for name in whiteEdges:
					pos = whiteEdges[name]
					colorCombo = otherSide # Check the other side of the edge to see what color it is
					ifBulk(moveListBuffer, colorCombo, pos, cube, algo1, algo2, algo3, algo4, algo5, algo6, algo7)
						count += 1 # increase the counter that keeps track of correct edges
						if count == 4:
							count = 0 # reset count to 0
							algo1 = True # means the first of the algorithm is done (hopefully) 
				# Move to the next edge block
		while algo2 == False: pass # Check to see if the white face is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check each corner block for the color white
				# If a white Corner is found and it is already in, or has been moved to a correct position then ignore it.
					count += 1
					if count == 4:# Increase a counter that keeps track of the amount of correct corners.
						count = 0 # If the counter indicates 3, meanig all four corners are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
						algo2 = True
				# Check the two other blocks of the corner for their color
					# Take the number asociated with the white block and run it through a list to see what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer.
		while algo3 == False: pass # Check to see if the middle layer is solved, simple Boolean TRUE / FALSE (LOOP) @##$U*@$*(!@($#!U@$ !@#$!@*U$NJSAU*!&$(!@#(!@#NCAISKDQ !@#*@$!@&(#*SDAS DAS d)) CHECK IF THIS BLOCK WORKS (IN THEORY ANYWAYS)
			# Check each edge on the middle and back layer of the cube for a orange color
				# If a orange edge is found then check the other side of the edge 
					# Check if the block is in the correct position
						# If the block is in the correct position then mark it as completed
							count += 1 # Increase a counter that keeps track of the amount of correct edges
							if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
								count = 0 
								algo3 = True
						# Else check the color combination in combination with it's position in the list.
							# Store the corresponding moves in moveListBuffer
		while algo4 == False: pass # Check to see if the yellow cross exists, simple Boolean TRUE / FALSE (LOOP)
			#Check each edge that is still not in the correct position (Back) for yellow
				# Check if the edge is in the correct position already
					# If the block is in the correct position then mark it as completed (Can be one of four spots. aslong as it is at a edge on the yellow face it counts as a correct position)
						count += 1 # Increase a counter that keeps track of the amount of correct edges
						if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
							count = 0
							algo4 = True
					# Else go through the list using the position of the yellow edge.
						# Store the corresponding moves required to put the edge in the correct position in moveListBuffer
		while algo5 == False: pass # Check to see if the yellow edges are solved, simple Boolean TRUE / FALSE (LOOP)
			# Check the color of the color on the non yellow sides of the edges.
				# If the color matches the color of the center of the face (5)
					count += 1# Increase a counter that keeps track of the amount of correct edges.
					if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
						count = 0
						algo5 = True
				# Else check the color of the adjacent edge, going clockwise
					# If the color of the adjacent edge matches the color of the center block of their respective face
						# Go back to looking for a unsolved block skipping this one for the next round
					# Else go through the list 
						# Store the moves in moveListBuffer #@!$!*@$*!@)#!@$(!@$)!@)#!@)_%()!@# KEEP IN MIND THAT THIS DOES NOT FOLLOWS THE STANDARD ALGORITHM AND IT NEEDS TO BE ADAPTED TO WORK FOR EACH OF THE FOUR SIDES!
		while algo6 == False: pass # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
		while solved == False: pass # Check to see if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
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
	if solved == True:
		return moveListBuffer
# Send moveListBuffer back to solverfinal2.py