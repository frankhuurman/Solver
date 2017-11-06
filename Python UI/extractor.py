


cc = False

#	dict algo* {colorCombo : ccdict}

#	ccdict = dict {pos : moves}

#	pos = [face, x, y]

algo1 = {"wr" : {	(0, 0, 1) : "U",
						(0, 1, 0) : "lUL",
						(0, 1, 2) : "LUl",
						(0, 2, 1) : "llULL",
						(1, 0, 1) : None
						},
			"wb" : {	(0, 0, 1) : "U",
						(0, 1, 0) : "lUL",
						(0, 1, 2) : "LUl",
						(0, 2, 1) : "llULL",
						(1, 0, 1) : None
						}
			
			}



curAlgo = 0
curCC = ""
temp = None

algos = []


with open("calc_rest.py", "r") as file:
	for i, line in enumerate(file):

		if (i < 35):
			continue

		# Get the algorithm:
		if (line.find("vars.alg") is not -1):
			curAlgo = int(line[line.find("vars.alg") + 9]) - 1
			algos.append({})


		# Get the colorcombo:
		if (line.find("colorCombo") is not -1):
			print("ccline: ", i)
			piep = False
			curCC = ""
			for char in line:
				if (char == "\""):
					piep = not piep
				elif (piep):
					curCC += char
			print(curCC)
			algos[curAlgo][curCC] = {}

		# Get position data
		if (line.find("cube.faces[cube.facenames[") is not -1):
			a = int(line.find("faces[cube.facenames[") + 21)
			face = line[a]
			x = line[a + 12]
			y = line[a + 15]
			temp = (int(face), int(x), int(y))

		elif (temp is not None):
			moves = ""
			piep = False
			for char in line:
				if (char == "\""):
					piep = not piep
				elif (piep):
					moves += char

			algos[curAlgo][curCC][temp] = moves
			temp = None

		if (i == 705):
			break


with open("output.txt", "w", newline = "\r\n") as file:
	for i, piep in enumerate(algos):
		file.write("algo" + str(i + 1) + "\n")
		for meh, blaat in piep.items():
			file.write("\t" + meh + "\n")
			for a, b in blaat.items():
				file.write("\t\t{} : {}\n".format(a, b))
