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
		if (coords[iter] == location[iter])
			iter += 1
			front = fronts[iter]
			results = "urULuRUl"