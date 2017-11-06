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
						mpos = (line.find("\t", cpos))
						if mpos == -1:
							mpos = -2
						m = line[(cpos + 2): mpos+1].strip()
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
	algo4 = True
	algo5 = True
	algo6 = True
	algo7 = True
#	algos[2] = True
	cube = None


def translateMoves(alg, mod, moves):


	tList = {2 :{	# Algo2
				"r" : {"u" : "f",
							"b" : "r",
							"l" : "u",
							"d" : "b",
							"f" : "l",
							"r" : "d"},
				"o":	{"u": "f",
							"f" : "r",
							"r" : "u",
							"d" : "b",
							"b" : "l",
							"l" : "d"},
				"g":	{"u" : "f",
							"l" : "r",
							"f" : "u",
							"d" : "b",
							"r" : "l",
							"b" : "d"},
				"b":	{"u" : "f",
							"r" : "r",
							"b" : "u",
							"d" : "b",
							"l" : "l",
							"f" : "d"}
				}, 3: {	# Algo3
				"r" : {"d" : "f",
							"b" : "r",
							"r" : "u",
							"u" : "b",
							"f" : "l",
							"l" : "d"},
				"o":	{"d": "f",
							"f" : "r",
							"l" : "u",
							"u" : "b",
							"b" : "l",
							"r" : "d"},
				}, 4: {	# Algo4
				"b": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"}
				}, 5: {	# Algo5
				"r" : {"f" : "d",
							"r" : "b",
							"u" : "r",
							"b" : "u",
							"l" : "f",
							"d" : "l"},
				"g":{"f" : "d",
							"r" : "r",
							"u" : "f",
							"b" : "u",
							"l" : "l",
							"d" : "b"},
				"b": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"},
				"o":{"f": "d",
							"r" : "f",
							"u" : "l",
							"b" : "u",
							"l" : "b",
							"d" : "r"}
				}}
				
	if (moves == ""):
		return(moves)
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
		print("Not changed. ", moves)
		return(moves)
	print("Changed ", moves, mvs)
	return(mvs)



def algorithm():

	results = ""
	while not vars.solved and not vars.cube.stopSolving: # Check if the cube is solved
		count = 0
		for i in range(3):
			input("Start algo-" + str(i + 1))
			while not vars.algos[i] and not vars.cube.stopSolving:# Check to see if the white edges are solved
				currentColor = ""
				coords = []
				colors = []
				count = 0
				if (i == 1):
					coords, colors = vars.cube.getCorners("w")
					print(coords, colors)
					print(vars.cube.printFaces("front_face"))
				elif (i == 2):
					miew = ["rb", "rg", "ob", "og"]
					coords1, colors1 = vars.cube.getEdge("r")
					coords2, colors2 = vars.cube.getEdge("o")
					coords1.extend(coords2)
					colors1.extend(colors2)
#					print("coords1: ", coords1)
#					print("colors1: ", colors1)
					for cor, col in zip(coords1, colors1):
						if (col in miew):
							coords.append(cor)
							colors.append(col)
					print("coords: ", coords)
					print("colors: ", colors)
					#vars.algos[i] = True
				else:
					coords, colors = vars.cube.getEdge("w")
					print(coords, colors)
				for j in range(len(coords)): #itterates through all colors until the first incorrectly placed color is found
					if (i == 2):
						color = colors[j][0]
					else:
						color = colors[j][-1]
#					print(i, j, colors, coords)
					moves = translateMoves(i + 1, color, vars.LUT[i][colors[j]][coords[j]])
					if (moves is not ""):
#						if (i == 1):
					#	for m in moves:
						input("\nNext move: " + colors[j] + str(coords[j]) + moves) 
						currentcolors = colors[j] # !
						vars.cube.sendMoves(moves)
#						else:
#						vars.cube.sendMoves(moves)
						vars.moveListBuffer += moves
						break	# Redo the while loop to get the current location of all white edges.
					else:
						count += 1	# If sqaure is correct, count it.
					if (count == 4):
						print(coords, colors)
						vars.algos[i] = True	# All white edges are resolved, end this step of algorithm.

					if (vars.LUT[i][colors[j]][coords[j]] is not ""): # ! 
						pass
		print(vars.moveListBuffer)
		vars.cube.stopSolving = True
		
	cube = vars.cube  
	
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
		edgeColor = ["ryg", "rby", "ogy", "oyb"]
		iter = 0
		coords, colors = cube.getCorners("o")
		coords2, colors2 = cube.getCorners("r")
		coords3 = []
		colors3 = []
		for cl, cr in zip(colors, coords):
			if cl in edgeColor:
				coords3.append(cr)
				colors3.append(cl)
		for cl, cr in zip(colors2, coords2):
			if cl in edgeColor:
				coords3.append(cr)
				colors3.append(cl)
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

	if not vars.algo7: # D035 th15 w0rk?
		fronts = ["r", "b", "g", "o"]
		location = (0,0,0)
		edgeColor = ["ryg", "rby", "ogy", "oyb"]
		iter = 0
		coords, colors = cube.getCorners("o")
		coords2, colors2 = cube.getCorners("r")
		coords3 = []
		colors3 = []
		adjacent = [cube.faces[cube.facenames[0]].squares[0][0], cube.faces[cube.facenames[5]].squares[0][0]]
		for cl, cr in zip(colors, coords):
			if cl in edgeColor:
				coords3.append(cr)
				colors3.append(cl)
		for cl, cr in zip(colors2, coords2):
			if cl in edgeColor:
				coords3.append(cr)
				colors3.append(cl)
		for iter in range(4):
			pas = True
			for c in colors[iter]:
				if (not c in edgeColor[iter]):
					pas = False
			if pas:
				if (coords[iter] == location): # Why the ()s
					iter += 1
					for x in adjacent:
						if  cl[:2] is not adjacent:
							results = translateMoves(2, "r", "RDrd")

	cube.sendMoves(results) # Sends results to the cube updating it.
	vars.moveListBuffer += results # Adds this cycle's moves into the buffer.
	print(vars.moveListBuffer)

	if vars.cube.solved():
		return vars.moveListBuffer