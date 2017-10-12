# Add code for executing "urULuRUl" if 0 or 1 corners are correct, taking the corresponding face as front if 1 is correct.
# Add something to finish algo6 if more than 1 corner is correct since there can only ever be either 0, 1 or 4 correctly placed corners there is no use in checking more than two
# Does this work?

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
		if (coords[iter] == location[iter]):
			iter += 1
			front = fronts[iter]
			results = "urULuRUl"