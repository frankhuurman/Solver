
import cube as kubus
import random
import sys
import time


dinges = "rggrrwyyoyggrwbbboryyoobwwbggwyyboobwwgrboryyboorggrww"
print(len(dinges))
moves = []
blah = ["D", "L", "B", "U", "R", "F"]
for i in blah:
	moves.append(i)
	moves.append(i.lower())
cube = kubus.cube("r"*9 + "w"*9 + "o"*9 + "y"*9 + "b"*9 + "g"*9)
t = 0
if (cube.solved()):
	print("moi")

#while(True):
i = 0
m = ""
x = time.time()
t = time.time()
for a in moves:
	for b in moves:
		for c in moves:
			for d in moves:
				for e in moves:
					for f in moves:
						cube.setStart()
						cube.sendMoves(a+b+c+d+e+f)
						i += 1
						colors = ""
						for face in cube.facenames:
							colors += cube.faces[face].getColors()
						if (i >= 10**4):
							i = 0
							print(a+b+c+d+e+f)
							print(colors)
							print(dinges)
							print((10 ** 4) / (time.time() - t))
							t = time.time()
						if (colors == dinges):
							print(m)
							print(time.time() - x)
							sys.exit()
print(time.time() - x)
"""
	for b in range(10 ** 4):
		m = ""
		cube.setStart()
		for i in range(6):
			move = moves[int(random.random() * 6)]
			if (random.random()*1 < 0.5):
				move = move.lower()
			cube.sendMoves(move)
			m += move
"""
"""
#		else:
#			print(m)
	print(m)
"""