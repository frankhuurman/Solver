
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
		if (coords[iter] == location[iter])
			iter += 1
			front = fronts[iter]
			results = "urULuRUl"