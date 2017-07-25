

white_image = "w"
red_image = "r"
green_image = "g"
blue_image = "b"
orange_image = "o"
yellow_image = "y"

rubiks_image = "u"
offsetx = [10, 300, 600]
offsety = [40, 230]
img_size = 40
imgs = {"red" : "r",
		"white" : "w",
		"orange" : "o",
		"yellow" : "y",
		"blue" : "b",
		"green" : "g"}

rects = []
rects_col = []

for i , color in enumerate(imgs):

	if ((i - 3) >= 0):
		xoff = offsetx[i - 3]
	else:
		xoff = offsetx[i]
	if (i < 3):
		yoff = offsety[0]
	else:
		yoff = offsety[1]
	for y in range(3):
		for x in range(3):
			xpos = (xoff + (x * 50))
			ypos = (yoff + (y * 50))
			rects.append((xpos, ypos, img_size, img_size))
			if (color == "white" and x == 1 and y == 1):
				rects_col.append(rubiks_image)
			else:
				rects_col.append(color)
print(rects_col)

for i in range(len(rects_col)):
	if ((i + 5) % 9 == 0):
		continue
	rects_col[i] = "i"

print(rects_col)
edges = [[0,1], [1,0], [1,2], [2,1]]
for edge in edges:
	print(edge)
print(edges)