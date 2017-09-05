# /----------------------------------------------\
# !                   Reminders                  !
# \----------------------------------------------/

#cube.faces[cube.facenames[0]].squares[0][0] left (red)
#cube.faces[cube.facenames[1]].squares[0][0] front (white)
#cube.faces[cube.facenames[2]].squares[0][0] right (orange)
#cube.faces[cube.facenames[3]].squares[0][0] back (yellow)
#cube.faces[cube.facenames[4]].squares[0][0] bottom (blue)
#cube.faces[cube.facenames[5]].squares[0][0] top (green)

import cube as kubus # <-- IMPORTANT

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
#TODO: Add code for keeping cube object up to date
#TODO: Write code to take the up to date version of the cube from the cube object.
#TODO: Translate the RDrd sequence to work for all four sides using each side's respective stepper motors (RDrd refers to two specific stepper motors, which would mean one corner would constantly be moved when passing RDrd to the move list.) <-- PRIORITY
#TODO: Fill in the section of algo2 involving the white - red - green corner. Simply fill in the positions as they appear rather than wasting time trying to force it into (possibly) impossible positions.
	if not vars.algo1: #NOTE: White surface of the edge used for position.
		if colorCombo == whiteRed: # correct pos == cube.faces[cube.facenames[1]].squares[1][0] White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				vars.moveListBuffer += "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				vars.moveListBuffer += "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "bRurB"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "blU"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "LBuubl"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "rbuuBR"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "UrbuuBRu"
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]:
				return # 7h15 w0rk5 :p
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V 
				vars.moveListBuffer += "uubllBUU"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V 
				vars.moveListBuffer += "RddLDDr"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V 
				vars.moveListBuffer += "ddBllbDD"
			elif pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "ubllBu'"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "bdLDB"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "fulUF"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "LfulUFl"
			elif pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "Ulu"
			elif pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "l"
			elif pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "uulUU"
			elif pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "ulU"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V 
				vars.moveListBuffer += "UbllBu"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V 
				vars.moveListBuffer += "rUbllBuR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "bdLDB"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "RBdLDbr"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V 
				vars.moveListBuffer += "DLd"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "L"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "ddLDD"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "DLd"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "bllB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "bbllBB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "ll"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "Bllb"
		if colorCombo == whiteBlue: # correct pos == cube.faces[cube.facenames[1]].squares[2][1]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "U"
			elif pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "lUL"
			elif pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "LUl"
			elif pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "llULL"
			elif pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			elif pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "llBuubLL"
			elif pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				vars.moveListBuffer += "rrbuuBRR"
			elif pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				vars.moveListBuffer += "ddbbuuBBDD'"
			elif pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "u"
			elif pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "ruR"
			elif pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "Rur"
			elif pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "rruRR"
			elif pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "uu"
			elif pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "buuB"
			elif pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "Buub"
			elif pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "bbuuBB"
			elif pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "dRbuuBrd'"
			elif pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "lBuubL"
			elif pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "RbuuBr"
			elif pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "bRurB"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "blU"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "LBuubl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "rbuuBR"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "UrbuuBRu"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				vars.moveListBuffer += "uubbddBBUU"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "llbddLLB"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				vars.moveListBuffer += "rrBddbRR"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V 
				vars.moveListBuffer += "lldLL"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "Ldl"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "ldL"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "d"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "bLdlb'"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "LbddBl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "rBddbR"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "uLbddBlU"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "rrDRR"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "RDr"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "rDr"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "D"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "dRBddbr"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "lbddDL"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "RBddbr"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "brD"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "rrDRR"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "RDr"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "rdR"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "D"
		if colorCombo == whiteOrange: # correct pos == cube.faces[cube.facenames[1]].squares[1][2]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "U"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "lUL"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "LUl"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "llULL"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "llBuubLL"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				vars.moveListBuffer += "rrbuuBRR"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				vars.moveListBuffer += "ddbbuuBBDD'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "ruR"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "Rur"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "rruRR"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "uu"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "buuB"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "Buub"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "bbuuBB"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "dRbuuBrd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "lBuubL"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "RbuuBr"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "bRurB"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "blU"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "LBuubl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "rbuuBR"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "UrbuuBRu"
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "LbDrdBl"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "bDrrdb'"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "lDbrrBdL"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "DbrrBd"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				vars.moveListBuffer += "uuBrrbUU"
			if pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "lddrDDL"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				vars.moveListBuffer += "ddbrrBDD"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "rBDrdb"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "RdbrrBD"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "BDrdb"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "RBDrdb"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "brrb'"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "rr"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "bbrrBB"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "Dr"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "drD"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "ddrDD"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "r"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "Drd"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "brrB"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "ubrrBU"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "R"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "URu"
		if colorCombo == whiteGreen: # correct pos == cube.faces[cube.facenames[1]].squares[0][1]: White surface used for position # V
			if pos == cube.faces[cube.facenames[0]].squares[0][1]: # V
				vars.moveListBuffer += "U"
			if pos == cube.faces[cube.facenames[0]].squares[1][0]: # V
				vars.moveListBuffer += "lUL"
			if pos == cube.faces[cube.facenames[0]].squares[1][2]: # V
				vars.moveListBuffer += "LUl"
			if pos == cube.faces[cube.facenames[0]].squares[2][1]: # V
				vars.moveListBuffer += "llULL"
			if pos == cube.faces[cube.facenames[1]].squares[0][1]: # V
				return # 7h15 w0rk5
			if pos == cube.faces[cube.facenames[1]].squares[1][0]: # V
				vars.moveListBuffer += "llBuubLL"
			if pos == cube.faces[cube.facenames[1]].squares[1][2]: # V
				vars.moveListBuffer += "rrbuuBRR"
			if pos == cube.faces[cube.facenames[1]].squares[2][1]: # V
				vars.moveListBuffer += "ddbbuuBBDD'"
			if pos == cube.faces[cube.facenames[2]].squares[0][1]: # V
				vars.moveListBuffer += "u"
			if pos == cube.faces[cube.facenames[2]].squares[1][0]: # V
				vars.moveListBuffer += "ruR"
			if pos == cube.faces[cube.facenames[2]].squares[1][2]: # V
				vars.moveListBuffer += "Rur"
			if pos == cube.faces[cube.facenames[2]].squares[2][1]: # V
				vars.moveListBuffer += "rruRR"
			if pos == cube.faces[cube.facenames[3]].squares[0][1]: # V
				vars.moveListBuffer += "uu"
			if pos == cube.faces[cube.facenames[3]].squares[1][0]: # V
				vars.moveListBuffer += "buuB"
			if pos == cube.faces[cube.facenames[3]].squares[1][2]: # V
				vars.moveListBuffer += "Buub"
			if pos == cube.faces[cube.facenames[3]].squares[2][1]: # V
				vars.moveListBuffer += "bbuuBB"
			if pos == cube.faces[cube.facenames[4]].squares[0][1]: # V
				vars.moveListBuffer += "dRbuuBrd'"
			if pos == cube.faces[cube.facenames[4]].squares[1][0]: # V
				vars.moveListBuffer += "lBuubL"
			if pos == cube.faces[cube.facenames[4]].squares[1][2]: # V
				vars.moveListBuffer += "RbuuBr"
			if pos == cube.faces[cube.facenames[4]].squares[2][1]: # V
				vars.moveListBuffer += "bRurB"
			if pos == cube.faces[cube.facenames[5]].squares[0][1]: # V
				vars.moveListBuffer += "blU"
			if pos == cube.faces[cube.facenames[5]].squares[1][0]: # V
				vars.moveListBuffer += "LBuubl"
			if pos == cube.faces[cube.facenames[5]].squares[1][2]: # V
				vars.moveListBuffer += "rbuuBR"
			if pos == cube.faces[cube.facenames[5]].squares[2][1]: # V
				vars.moveListBuffer += "UrbuuBRu"
	if not vars.algo2: # List algo2
		if colorCombo == whiteRedGreen: # Placeholder variable name # The position is the position of the white surface of the edge. <-- IMPORTANT
			if pos == cube.faces[cube.facenames[0]].squares[0][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[0]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[0]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[0]].squares[2][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[1]].squares[0][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[1]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[1]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[1]].squares[2][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[2]].squares[0][0]:
				vars.moveListBuffer += "" #rbRB (works for this side)
			if pos == cube.faces[cube.facenames[2]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[2]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[2]].squares[2][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[3]].squares[0][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[3]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[3]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[3]].squares[2][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[0][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[4]].squares[2][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[5]].squares[0][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[5]].squares[0][2]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[5]].squares[2][0]:
				vars.moveListBuffer += ""
			if pos == cube.faces[cube.facenames[5]].squares[2][2]:
				vars.moveListBuffer += ""


	if algo3 == False: pass # List algo 3
	if algo4 == False: pass # List algo 4
	if algo5 == False: pass # List algo 5 
	if algo6 == False: pass # List algo 6 
	if algo7 == False: pass # List algo 7

	for name in cube.facenames:
		cube.faces[name]

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