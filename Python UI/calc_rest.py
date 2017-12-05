# /----------------------------------------------\
# |                   Reminders                  |
# \----------------------------------------------/

import datetime

#cube.faces[cube.facenames[0]].squares[0][0] left (red)
#cube.faces[cube.facenames[1]].squares[0][0] front (white)
#cube.faces[cube.facenames[2]].squares[0][0] right (orange)
#cube.faces[cube.facenames[3]].squares[0][0] back (yellow)
#cube.faces[cube.facenames[4]].squares[0][0] bottom (blue)
#cube.faces[cube.facenames[5]].squares[0][0] top (green)

# When holding the cube turning the cube 90 degrees left, right up or down to show another face the corner that is the in the top left is that face's [0][0], 
# this only applies to the back side if the rotation is done in a right or left motion but not for up / down tilting

#TODO: Check algo4, something is causing RB to go into (0, 1, 2) # Which section? 
#TODO: Line 302
#TODO: Line 310
#TODO: Look into why algo6 only occasionaly works, takes the wrong corner despite being told exactly which to pick. 
#TODO: Check why algo6 doesn't finish when it should
#TODO: Fix the issue with algo6 getting stuck in a loop.
#TODO: Please find a to stop the command line from becoming unresponsive.
#TODO: Add more conditions to algo6, can currently get stuck in several selectors without moves.
#TODO: Remove any commented code that isn't needed anymore.

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
	moveListBuffer = ""
	solved = False
	algos = []
	for i in range(7):
		algos.append(False)
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
				"r" : {"f" : "l",
							"r" : "u",
							"u" : "b",
							"b" : "r",
							"l" : "d",
							"d" : "f"},
				"g":{"f" : "u",
							"r" : "r",
							"u" : "b",
							"b" : "d",
							"l" : "l",
							"d" : "f"},
				"b": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"},
				"o":{"f": "r",
							"r" : "d",
							"u" : "b",
							"b" : "l",
							"l" : "u",
							"d" : "f"}
				}, 
				6: {	# Algo6
				"r" : {"f" : "l",
							"r" : "u",
							"u" : "b",
							"b" : "r",
							"l" : "d",
							"d" : "f"},
				"g":{"f" : "u",
							"r" : "r",
							"u" : "b",
							"b" : "d",
							"l" : "l",
							"d" : "f"},
				"b": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"},
				"o":{"f": "r",
							"r" : "d",
							"u" : "b",
							"b" : "l",
							"l" : "u",
							"d" : "f"}
				},7: {
				"r" : {"f" : "l",
							"r" : "u",
							"u" : "b",
							"b" : "r",
							"l" : "d",
							"d" : "f"},
				"g":{"f" : "u",
							"r" : "r",
							"u" : "b",
							"b" : "d",
							"l" : "l",
							"d" : "f"},
				"b": {"f" : "d",
							"r" : "l",
							"u" : "b",
							"b" : "u",
							"l" : "r",
							"d" : "f"},
				"o":{"f": "r",
							"r" : "d",
							"u" : "b",
							"b" : "l",
							"l" : "u",
							"d" : "f"}				   
					}}
				
	if (moves == "done"):
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
	print("Changed to face-{}, ".format(mod), moves, mvs)
	return(mvs)

def getInfo(i):
	coords = []
	colors = []
	if (i == 1):
		coords, colors = vars.cube.getCorners("w")
	elif (i == 2):
		miew = ["rb", "rg", "ob", "og"]
		coords1, colors1 = vars.cube.getEdge("r")
		coords2, colors2 = vars.cube.getEdge("o")
		coords1.extend(coords2)
		colors1.extend(colors2)
		for cor, col in zip(coords1, colors1):
			if (col in miew):
				coords.append(cor)
				colors.append(col)
	else:
		coords, colors = vars.cube.getEdge("w")
	print("coords: ", coords)
	print("colors: ", colors)
	return(coords, colors)

def algorithm():

	results = ""
	while not vars.solved and not vars.cube.stopSolving:
		count = 0
		for i in range(3):
			print("Start algo-" + str(i + 1))
			while not vars.algos[i] and not vars.cube.stopSolving:
				currentColor = ""
				count = 0
				coords, colors = getInfo(i)
				for j in range(len(coords)):
					if (i == 2):
						color = colors[j][0]
					else:
						color = colors[j][-1]
					moves = translateMoves(i + 1, color, vars.LUT[i][colors[j]][coords[j]])
					if (not moves == "done"):
						currentColor = colors[j]
						vars.cube.sendMoves(moves)
						vars.moveListBuffer += moves
						del(coords, colors)
						coords, colors = getInfo(i)
						k = colors.index(currentColor)
						if (not vars.LUT[i][colors[k]][coords[k]] == "done"):
							print("\n\nERROR!!!!!\n", coords, colors)
							debug = open("debug.txt", "a", newline = "\r\n")
							debug.write(str(colors[j]) + " algo-{} ".format(i+1) + str(coords[j]) + "\t")
							debug.write(" moves: {} - @{}\n".format(vars.LUT[i][colors[k]][coords[k]], datetime.datetime.now()))
							debug.close()
						else:
							print("\n{}\n{}\n".format(vars.LUT[i][colors[k]][coords[k]], currentColor))
						break
					else:
						count += 1
					if (count == 4):
						print(coords, colors)
						vars.algos[i] = True
		print(vars.moveListBuffer)
		
		cube = vars.cube  
	
		while not vars.algos[4-1] and not cube.stopSolving:
			print("Start algo-4")
			if cube.faces[cube.facenames[3]].squares[0][1] == "y":
				if cube.faces[cube.facenames[3]].squares[1][0] == "y":
					if cube.faces[cube.facenames[3]].squares[1][2] == "y":
						if cube.faces[cube.facenames[3]].squares[2][1] == "y":
							results = ""
							vars.algos[4-1] = True
						else:
							print("0whut?")
					else:
						results = translateMoves(4, "b", "fruRUF")
						print("Bleep1")
				elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
					results = translateMoves(4, "b", "U")
				else:
					print("1whut?")
					results = translateMoves(4, "b", "U")
			elif cube.faces[cube.facenames[3]].squares[1][0] == "y":
				if cube.faces[cube.facenames[3]].squares[1][2] == "y":
					results = translateMoves(4, "b", "fruRUF")
					print("Bleep2")
				elif cube.faces[cube.facenames[3]].squares[2][1] == "y":
					results = translateMoves(4, "b", "u")
				else:
					print("2whut?")
			elif cube.faces[cube.facenames[3]].squares[1][2] == "y":
				if cube.faces[cube.facenames[3]].squares[2][1] == "y":
					results = translateMoves(4, "b", "uu")
				else:
					print("3whut?")
			else:
				results = translateMoves(4, "b", "fruRUF")
				print("Bleep3")
			vars.cube.sendMoves(results)
			vars.moveListBuffer += results

		while not vars.algos[5-1] and not cube.stopSolving: 
			print("Start algo-5")
			if cube.faces[cube.facenames[0]].squares[1][0] is not "r":
				if cube.faces[cube.facenames[4]].squares[2][1] is not "b":
					if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "red"
							results = translateMoves(5, "r", "u") # Everything is wrong.
						elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
							front = "red"
							results = translateMoves(5, "r", "ruRuruuRu") # Green is right.
					elif cube.faces[cube.facenames[2]].squares[1][2] == "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "green"
							results = translateMoves(5, "g", "ruRuruuRu") # Orange is right.
						elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
							front = "red"
							results = translateMoves(5, "r", "ruRuruuRu") # Orange and green are right.
				elif cube.faces[cube.facenames[4]].squares[1][2] == "b":
					if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "orange"
							results = translateMoves(5, "o", "ruRuruuRu") # Blue is right.
						if cube.faces[cube.facenames[5]].squares[0][1] == "g":
							front = "orange"
							results = translateMoves(5, "g", "ruRuruuRu") # Blue and green are right. Opposites, move green (or blue) #!!!!!!!!!!!!!!
					elif cube.faces[cube.facenames[2]].squares[1][2] == "o":				
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "green"
							results = translateMoves(5, "g", "ruRuruuRu") # Blue and orange are right.
						if cube.faces[cube.facenames[5]].squares[0][1] == "g":
							results = "" # Blue, orange and green are right.
			elif cube.faces[cube.facenames[0]].squares[1][0] == "r":
				if cube.faces[cube.facenames[4]].squares[2][1] is not "b":
					if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "blue"
							results = translateMoves(5, "b", "ruRuruuRu") # Red is right.
						elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
							front = "blue"
							results = translateMoves(5, "b", "ruRuruuRu") # Red and Green are right.
					elif cube.faces[cube.facenames[2]].squares[1][2] == "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "blue"
							results = translateMoves(5, "o", "ruRuruuRu") # Red and orange are right. Opposites, move orange (or red) #!!!!!!!!!!!!!! # Doesn't seem to be doing what it should, maybe check the translation?
						elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
							results = ""
							print("Error 1: This shouldn't even trigger; algo5") # Red, orange and green are right.
				elif cube.faces[cube.facenames[4]].squares[2][1] == "b":
					if cube.faces[cube.facenames[2]].squares[1][2] is not "o":
						if cube.faces[cube.facenames[5]].squares[0][1] is not "g":
							front = "orange"
							results = translateMoves(5, "o", "ruRuruuRu") # Red and blue are right.
						elif cube.faces[cube.facenames[5]].squares[0][1] == "g":
							results = ""
							print("Error 2: This shouldn't event trigger; algo5") # Red, blue and green are right.
					elif cube.faces[cube.facenames[2]].squares[1][2] == "o": # everything is right
						results = ""
						vars.algos[5-1] = True
			vars.cube.sendMoves(results)
			vars.moveListBuffer += results
					
		i6 = 0
		while not vars.algos[6-1] and not cube.stopSolving:
			input("Start algo-6")
			fronts = ["r", "b", "g", "o"]
			flip = ["b", "o", "g"]

			correctPos = {"ygr" : ((0,0,0),(3,0,2),(5,0,0)),
								"ybo" : ((2,2,2),(3,2,0),(4,2,2)),
								"yog" : ((2,2,0),(3,0,0),(5,2,0)),
								"yrb" : ((0,0,2),(3,2,2),(4,2,0))} # Check all these co-ords for accuracy
			
			coords, colors = vars.cube.getCorners("y")
			if coords[colors.index("ygr")] in correctPos["ygr"]:
				if coords[colors.index("ybo")] in correctPos["ybo"]:
					vars.algos[6-1] = True
					break
			elif coords[colors.index("ybo")] in correctPos["ybo"]: # double check if these should be elifs 
				results = translateMoves(6, "o", "urULuRUl")
			elif coords[colors.index("yog")] in correctPos["yog"]:
				results = translateMoves(6, "g", "urULuRUl")
			elif coords[colors.index("yrb")] in correctPos["yrb"]:
				results = translateMoves(6, "b", "urULuRUl")

			vars.cube.sendMoves(results)
			vars.moveListBuffer += results

			coords, colors = vars.cube.getCorners("y")
			check = True
			for i in range(len(colors)):
				if (not coords[i] in correctPos[colors[i]]):
					check = False
			if (check):
				vars.algos[6-1] = True

		while not vars.algos[7-1] and not cube.stopSolving:
			input("Start algo-7")
			fronts = ["r", "b", "g", "o"]
			location = (0,0,0)
			edgeColor = ["ryg", "rby", "ogy", "oyb"]
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
			for i in range(4):
				pas = True
				for c in colors[i]:
					if (not c in edgeColor[i]):
						pas = False
				if pas:
					if (coords[i] == location): # Why the ()s
						for x in adjacent:
							if  colors3[:2] is not adjacent:
								results = translateMoves(2, "r", "RDrd")

			# Check rotation thingy !!!!
			while (not cube.faces["top_face"].squares[0][1] == "g"):
				results += "b"
			# Check rotation thingy !!!!

			vars.cube.sendMoves(results)
			vars.moveListBuffer += results
			vars.algos[7-1] = True


		cube.sendMoves(results) # Sends results to the cube updating it.
		vars.moveListBuffer += results # Adds this cycle's moves into the buffer.
		print(vars.moveListBuffer)

		if vars.cube.solved():
			return vars.moveListBuffer