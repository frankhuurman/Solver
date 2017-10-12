#cube.faces[cube.facenames[0]].squares[0][0] left (red)
#cube.faces[cube.facenames[1]].squares[0][0] front (white)
#cube.faces[cube.facenames[2]].squares[0][0] right (orange)
#cube.faces[cube.facenames[3]].squares[0][0] back (yellow)
#cube.faces[cube.facenames[4]].squares[0][0] bottom (blue)
#cube.faces[cube.facenames[5]].squares[0][0] top (green)

# kleur waar je op zoekt met getCorners("kleur") zit op de coordinaten die je krijgt. (face, y, x)
# Green first, then red, then yellow.
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
			for x in adjacent
				if  cl[:2] is not adjacent:
					results = translateMoves(2, "r", "RDrd")
					