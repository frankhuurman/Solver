import cube as kubus

#cube.faces[cube.facenames[0]].squares[0][0] left
#cube.faces[cube.facenames[1]].squares[0][0] front
#cube.faces[cube.facenames[2]].squares[0][0] right
#cube.faces[cube.facenames[3]].squares[0][0] back
#cube.faces[cube.facenames[4]].squares[0][0] bottom
#cube.faces[cube.facenames[5]].squares[0][0] top

class vars:
	moveListBuffer = ""
	solved = False
	algo1 = False
	algo2 = False
	algo3 = False
	algo4 = False
	algo5 = False
	algo6 = False
	cube = None

def ifBulk(cube, colorCombo, pos):
	#TODO: Add booleans for selecting which algorithm need to be picked
	if not vars.algo1: #NOTE: Check the position of the WHITE side of the edge
		if colorCombo == whiteRed: # correct pos == cube.faces[cube.facenames[1]].squares[1][0]
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				return # 7h15 w0rk5 :p
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: 
				vars.moveListBuffer += "uubllb'u'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: 
				vars.moveListBuffer += "r'ddl'd'd'r"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: 
				vars.moveListBuffer += "ddb'llbd'd'"
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				vars.moveListBuffer += "ubllb'u'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				vars.moveListBuffer += "bdl'd'b'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				vars.moveListBuffer += "fulu'f'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				vars.moveListBuffer += "l'fulu'f'l"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				vars.moveListBuffer += "u'lu"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				vars.moveListBuffer += "l"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				vars.moveListBuffer += "uulu'u'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				vars.moveListBuffer += "ulu'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: 
				vars.moveListBuffer += "u'bllb'u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: 
				vars.moveListBuffer += "ru'bllb'ur'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				vars.moveListBuffer += "bdl'd'b'"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				vars.moveListBuffer += "r'b'dl'd'br"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: 
				vars.moveListBuffer += "d'l'd"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				vars.moveListBuffer += "l'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				vars.moveListBuffer += "ddl'd'd'"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				vars.moveListBuffer += "d'l'd"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				vars.moveListBuffer += "bllb'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				vars.moveListBuffer += "bbllb'b'"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				vars.moveListBuffer += "ll"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				vars.moveListBuffer += "b'llb"
		if colorCombo == whiteBlue: # correct pos == cube.faces[cube.facenames[1]].squares[2][1]:
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: 
				vars.moveListBuffer += "uubbddb'b'u'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				vars.moveListBuffer += "llbddl'l'b'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				vars.moveListBuffer += "rrb'ddbr'r'"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: 
				vars.moveListBuffer += "lldl'l'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				vars.moveListBuffer += "l'dl"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				vars.moveListBuffer += "ldl'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: 
				vars.moveListBuffer += "d"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				vars.moveListBuffer += "bl'dlb'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				vars.moveListBuffer += "l'bddb'l"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				vars.moveListBuffer += "rb'ddbr'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				vars.moveListBuffer += "ul'bddb'lu'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				vars.moveListBuffer += "rrd'r'r'"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				vars.moveListBuffer += "r'd'r"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				vars.moveListBuffer += "rd'r"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				vars.moveListBuffer += "d'"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				vars.moveListBuffer += "dr'b'ddbr"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				vars.moveListBuffer += "lbddb'l'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				vars.moveListBuffer += "r'b'ddbr"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				vars.moveListBuffer += "brd'"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				vars.moveListBuffer += "rrd'r'r'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				vars.moveListBuffer += "r'd'r"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				vars.moveListBuffer += "rdr'"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				vars.moveListBuffer += "d'"
		if colorCombo == whiteOrange: # correct pos == cube.faces[cube.facenames[1]].squares[1][2]:
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				vars.moveListBuffer += "l'bd'rrdb'l"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				vars.moveListBuffer += "bd'rrdb'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				vars.moveListBuffer += "ld'brrb'dl'"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				vars.moveListBuffer += "d'brrb'd"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]:
				vars.moveListBuffer += "uub'rrbu'u'"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				vars.moveListBuffer += "lddrd'd'l'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				vars.moveListBuffer += "ddbrrb'd'd'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				vars.moveListBuffer += "rb'd'rdb"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				vars.moveListBuffer += "r'dbrrb'd'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				vars.moveListBuffer += "b'd'rdb"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				vars.moveListBuffer += "r'b'd'rdb"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				vars.moveListBuffer += "brrb'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				vars.moveListBuffer += "rr"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				vars.moveListBuffer += "bbrrb'b'"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				vars.moveListBuffer += "drd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				vars.moveListBuffer += "ddrd'd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				vars.moveListBuffer += "r"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				vars.moveListBuffer += "d'rd"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				vars.moveListBuffer += "brrb'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				vars.moveListBuffer += "ubrrb'u'"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				vars.moveListBuffer += "r'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				vars.moveListBuffer += "u'r'u"
		if colorCombo == whiteGreen: # correct pos == cube.faces[cube.facenames[1]].squares[0][1]:
			if pos == cube.faces[cube.facenames[0]].squares[0][1]:
				vars.moveListBuffer += "u'"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]:
				vars.moveListBuffer += "lu'l'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]:
				vars.moveListBuffer += "l'u'l"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]:
				vars.moveListBuffer += "llu'l'l'"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]:
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[1][0]:
				vars.moveListBuffer += "llb'uubl'l'"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]:
				vars.moveListBuffer += "rrbuub'r'r'"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]:
				vars.moveListBuffer += "ddbbuub'b'd'd'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]:
				vars.moveListBuffer += "u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]:
				vars.moveListBuffer += "rur'"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]:
				vars.moveListBuffer += "r'ur"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]:
				vars.moveListBuffer += "rrur'r'"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]:
				vars.moveListBuffer += "uu"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]:
				vars.moveListBuffer += "buub'"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]:
				vars.moveListBuffer += "b'uub"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]:
				vars.moveListBuffer += "bbuub'b'"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]:
				vars.moveListBuffer += "dr'buub'rd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]:
				vars.moveListBuffer += "lb'uubl'"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]:
				vars.moveListBuffer += "r'buub'r"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]:
				vars.moveListBuffer += "br'urb'"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]:
				vars.moveListBuffer += "blu'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]:
				vars.moveListBuffer += "l'b'uubl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]:
				vars.moveListBuffer += "rbuub'r'"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]:
				vars.moveListBuffer += "u'rbuub'r'u"
	if not algo2: pass
	if not algo3: pass
	if not algo4: pass
	if not algo5: pass
	if not algo6: pass


def algorithm():
	count = 0
	while not vars.solved: # Check if the cube is solved
		while not vars.algo1:# Check to see if the white edges are solved
			for name in vars.cube.facenames: # Check each face for edges?
				whiteEdges = vars.cube.faces[name].checkEdges("w") # Check each block asociated with an edge to see if it is white
				if (len(whiteEdges) > 0): # Don't need to go further if there are no white edges.
					for pos in whiteEdges:
						colorCombo = otherSide # Check the other side of the edge to see what color it is
						# ^^^^ What data is needed here?
						ifBulk(vars.cube, colorCombo, pos)
					"""
					This isn't needed anymore I think?
					count += 1 # increase the counter that keeps track of correct edges
					if count == 4:
						count = 0 # reset count to 0
						algo1 = True # means the first of the algorithm is done (hopefully) 
					"""
		while not algo2:  # Check to see if the white face is solved, simple Boolean TRUE / FALSE (LOOP)
			# Check each corner block for the color white
				# If a white Corner is found and it is already in, or has been moved to a correct position then ignore it.
					count += 1
					if count == 4:# Increase a counter that keeps track of the amount of correct corners.
						count = 0 # If the counter indicates 3, meanig all four corners are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
						algo2 = True
				# Check the two other blocks of the corner for their color
					# Take the number asociated with the white block and run it through a list to see what moves should be performed to get it into it's proper position.
						# Store these moves in moveListBuffer.
		while not algo3:  # Check to see if the middle layer is solved, simple Boolean TRUE / FALSE (LOOP) @##$U*@$*(!@($#!U@$ !@#$!@*U$NJSAU*!&$(!@#(!@#NCAISKDQ !@#*@$!@&(#*SDAS DAS d)) CHECK IF THIS BLOCK WORKS (IN THEORY ANYWAYS)
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
		while not algo4:  # Check to see if the yellow cross exists, simple Boolean TRUE / FALSE (LOOP)
			#Check each edge that is still not in the correct position (Back) for yellow
				# Check if the edge is in the correct position already
					# If the block is in the correct position then mark it as completed (Can be one of four spots. aslong as it is at a edge on the yellow face it counts as a correct position)
						count += 1 # Increase a counter that keeps track of the amount of correct edges
						if count == 4: # If the counter indicates 3, meaning all four edges are in the correct position then break out of this loop and move onto the next part of the algorithm after setting a Boolean to TRUE
							count = 0
							algo4 = True
					# Else go through the list using the position of the yellow edge.
						# Store the corresponding moves required to put the edge in the correct position in moveListBuffer
		while not algo5:  # Check to see if the yellow edges are solved, simple Boolean TRUE / FALSE (LOOP)
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
		while not algo6: pass # Check to see if the yellow corners are prepared correctly, simple Boolean TRUE / FALSE (LOOP)
			# Check if the side on the yellow face is NOT yellow
				# If the other colors on the corner DO NOT match the color at the center of their respective face
					# Go into the list using the position of this corner
						# Calculate how many times the attached moves need to be executed to make all corners be correct.
							# Store the attached moves in moveListBuffer as many times as is needed to react a correct cube state
							# Set the Boolean to TRUE and break out of this loop.
			# Else move onto the next corner
		while not solved: pass # Check to see if the cube is solved, simple Boolean TRUE / FALSE (LOOP)
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
		loopin = True
	if vars.cube.solved() == True:
		return moveListBuffer#, loopin <-- what is this supposed to do?
# Send moveListBuffer back to solverfinal2.py