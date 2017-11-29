from collections import deque
import random


class const:
	"""The class has a few arrays and dicts to help map colors and faces, and general relations."""

	# edges, corners and rotateOrder are arrays with the x, y coordinates of squares of a face.
	# Edges is the collection of the edge elements of a face. Used in the solving algorithm.
	edges = [[0,1], [1,0], [1,2], [2,1]]

	# Corners is the collection of the corner elements of a face. Used in the solving algorithm.
	# [[x,y, xFace,yFace], [x,y, xFace,yFace]], xFace and yFace refer to sides[]
	corners = [[0,0, 1,0], [0,2, 0,3], [2,0, 2,1], [2,2, 3,2]]

	# rotateOrder is the collection of all the elements of a face that are moved
	# during a rotation of that face.
	rotateOrder = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]]

	# Dict with {color : index of facenames}. So you can get the right face when you only know the color.
	faceColorIndex = {"r": 0, "w": 1, "o": 2, "y": 3, "b": 4, "g": 5}

	# The names of the faces in the order presented used in the program.
	facenames = ["left_face", "front_face", "right_face", "back_face", "bottom_face", "top_face"]

	# Translation list to indicate which face must rotate for which move command. Use command.lower() when making queries in this dict.
	moveFaceIndex = {"l": 0, "f": 1, "r": 2, "b": 3, "d": 4, "u": 5}
	
	# Indicating the order for the args in connections{}. Only used during init.
	sides = ["up", "left", "down", "right"]

	# Translation list used when initiating a cube. From this, the relative links between faces are interpreted.
	# For example, face[5](top) is up from face[0](left)
	connections = {
		facenames[0]: (5, 3, 4, 1),
		facenames[1]: (5, 0, 4, 2),
		facenames[2]: (5, 1, 4, 3),
		facenames[3]: (5, 2, 4, 0),
		facenames[4]: (1, 0, 3, 2),
		facenames[5]: (3, 0, 1, 2)
		}

class cube(object):
	"""Object representing one rubik's cube."""
	
	stopSolving = False
	faces = {}
	facenames = const.facenames
	start = []	# Keep a record of the starting position.

	def __init__(self, outputlist):
		
		self.start = outputlist
#		dinges = "gyrrrbyrbyorywoowbgoggowwrwrborybbwgybogbyogrwowggwbyy"
#		for l in dinges:
#			self.start.append(l)
		self.setStart()
		self.randomSetStart()


	def setStart(self):
		"""Assigns the items from outputlist to their own face."""

		for i, f in enumerate(const.facenames):
			squares = self.start[i*9 : i*9 + 9]	# Picking 9 elements from the list
			face_color = squares[int(len(squares)/2)]	# Checking color of the 4th element.
			name = const.facenames[const.faceColorIndex[face_color]]
			conns = {}	# Dict {name : relative orientation} used for interactions between different faces.
			for i, conn in enumerate(const.connections[name]):
				conns[const.facenames[conn]] = const.sides[i]
			self.faces[f] = face(squares, name, conns)

	def randomSetStart(self):
		"""Use this method to get the cube to a random state."""

		moves = ["l", "f", "r", "b", "d", "u"]
		mvs = ""
		for i in range(30):
			j = moves[int(random.random() * 6)]
			if (random.random() > .5):
				j = j.upper()
			self.sendMoves(j)
			mvs += j
		print(mvs)
		
	def sendMoves(self, moves):
		"""Main method for manipulating the cube."""

#		print("sendMoves: ", moves)
		for move in moves:
			dir = str(move).islower()
			self.__rotate(const.facenames[const.moveFaceIndex[str(move).lower()]], dir)
			
	def solved(self):
		"""Returns True if all faces are unicolored, else False."""

		s = True
#		for f in const.facenames:
#			if (not self.faces[f].allTheSame()):
#				s = False
#				break
		if (s):
			self.stopSolving = True
		return(s)
	
	def printFaces(self, name):
		"""Prints the current face with the 4 connecting sides, all properly oriented.
		Kinda useless now that the GUI shows the current cube status."""

		print(name)
		squares = {}
		middleSquares = []
		text = ""
		for i, f in enumerate(list(self.faces[name].connections.keys())):
			main = self.faces[name].connections[f]
			sec = self.faces[f].connections[name]
			squares["sq" + str(i)] = self.__turnForPrint(main, sec, self.faces[f].squares, f)
		for a, b, c in zip(squares["sq1"], self.faces[name].squares, squares["sq3"]):
			line = []
			for s in a:
				line.append(s)
			for s in b:
				line.append(s)
			for s in c:
				line.append(s)
			middleSquares.append(line)
		for row in squares["sq0"]:
			text += "\n\t"
			for sq in row:
				text += sq + " "
		for row in middleSquares:
			text += "\n  "
			for sq in row:
				text += sq + " "
		for row in squares["sq2"]:
			text += "\n\t"
			for sq in row:
				text += sq + " "
		return(text + "\n")

	def getEdge(self, color):
		"""\t\tReturns the positions of all edge squares with the selected color
		as well as the color combination of that edge piece."""

		order = [0, 1, 3, 2]
		
		coords = []
		colors = []
		for f in self.faces.keys():
			for i, (x, y) in zip(order, const.edges):
				if (color == self.faces[f].squares[x][y]):
					otherSide = const.facenames[const.connections[f][i]]
					otherColor = self.faces[otherSide].getSide(f)[1]
					colorCombo = color + str(otherColor)
#					print(f, otherSide, otherColor)
#					print("moi", i, x, y)
					fIndex = const.facenames.index(f)
					coords.append((fIndex, x, y))
					colors.append(colorCombo)
		return(coords, colors)

	def getCorners(self, color, extraReturn = False):
		"""Returns a list with the coords of the corner squares that match the selected color."""
		
		
		blah = {(0,0):((0,2),(2,0)),
				  (0,2):((2,2),(0,0)),
				  (2,0):((0,0),(2,2)),
				  (2,2):((2,0),(0,2))
					}
		coords = []
		colors = []
		for f in self.faces.keys():
			for x, y, s1, s2 in const.corners:
				if (color == self.faces[f].squares[x][y]):
					side1 = const.facenames[const.connections[f][s1]]
					side2 = const.facenames[const.connections[f][s2]]
					main1 = self.faces[f].connections[side1]
					main2 = self.faces[f].connections[side2]
					sec1 = self.faces[side1].connections[f]
					sec2 = self.faces[side2].connections[f]
					sq1 = self.__turnForPrint(main1, sec1, self.faces[side1].squares, f)
					sq2 = self.__turnForPrint(main2, sec2, self.faces[side2].squares, f)
					# fIndex = face 1st, x,y = coords 1st
					c1 = blah[(x,y)][0]	# <-- coords of 2nd
					c2 = blah[(x,y)][1]	# <-- coords of 3rd
					fIndex = const.facenames.index(f)
		#			print(c1, c2, fIndex, side1, side2)
					if (extraReturn):
						coords.append({color : (fIndex, x, y),
							sq1[c1[0]][c1[1]] : (const.facenames.index(side1), c1[0], c1[1]),
							sq2[c2[0]][c2[1]] : (const.facenames.index(side2), c2[0], c2[1])})
					else:
						coords.append((fIndex, x, y))
						colors.append(color + sq1[c1[0]][c1[1]] + sq2[c2[0]][c2[1]])
		if (extraReturn):
			return(coords)
		else:
			return(coords, colors)
		"""
		[{ "y" : (2,0,2),
			"o" : (5,0,2),
			"g" : (3,0,0)}
			]
		"""
	def alg6coords(self):

		coo = []
		coords = self.getCorners("y", True)
		for c in coords:
			if (not c["y"][0] == 3):
				coo.append(c)


		return(coo)

	def __rotate(self, name, dir):
		"""Rotates the face along with the corresponding sides."""

		face = self.faces[name]
		# Rotate the squares of the face you want to rotate.
		face.rotateFace(dir)
		temp = deque()

		# Gathering the colors of other faces directly connected to the face in 1 direction or the other:
		if (dir):
			for f in face.connections:
				temp.append(self.faces[f].getSide(name))
		else:
			reverse = []	# Need a new var because you can't reverse a Dict.
			for f in face.connections:
				reverse.append(f)
			for f in reversed(reverse):
				temp.append(self.faces[f].getSide(name))

		# Move the colors of the left block in the array to the right side.
		# Equals rotating a circle.
		temp.append(temp.popleft())

		# Getting the colors back to the right faces.
		if (dir):
			for f in face.connections:
				self.faces[f].setSide(name, temp.popleft(), True)
		else:
			for f in reversed(reverse):
				self.faces[f].setSide(name, temp.popleft(), False)

	def __turnForPrint(self, relMain, relSec, squares, name):
		if (relMain == relSec):
			return(self.__rotPrint(2, squares, name))
		elif ((relMain == "up" and relSec == "left") or
				(relMain == "left" and relSec == "down") or
				(relMain == "down" and relSec == "right") or
				(relMain == "right" and relSec == "up")):
			return(self.__rotPrint(1, squares, name))
		elif ((relMain == "left" and relSec == "up") or
				(relMain == "up" and relSec == "right") or
				(relMain == "right" and relSec == "down") or
				(relMain == "down" and relSec == "left")):
			return(self.__rotPrint(3, squares, name))
		return(squares)
	
	def __rotPrint(self, turns, squares, name):
#		print(str(turns), "moi")
		temp = deque()
		blah = [["","",""],["","",""],["","",""]]
		for x, y in const.rotateOrder:
			temp.append(squares[x][y])
		for i in range(turns):
			temp.append(temp.popleft())
			temp.append(temp.popleft())
		for x, y in reversed(const.rotateOrder):
			blah[x][y] = temp.pop()
		blah[1][1] = self.faces[name].face_color
		return(blah)


class face(object):
	"""Object representing 1 side of a rubik's cube."""
	
	# squares
	@property
	def squares(self):
		return(self.__squares)
	@squares.setter
	def squares(self, squares):
		self.__squares = squares
	# conns
	@property
	def conns(self):
		return(self.__conns)
	@conns.setter
	def conns(self, conns):
		self.__conns = conns
	# face_color
	@property
	def face_color(self):
		return(self.__face_color)
	@face_color.setter
	def face_color(self, face_color):
		self.__face_color = face_color
	# face_name
	@property
	def face_name(self):
		return(self.__face_name)
	@face_name.setter
	def face_name(self, face_name):
		self.__face_name = face_name
	# connections
	@property
	def connections(self):
		return(self.__connections)
	@connections.setter
	def connections(self, connections):
		self.__connections = connections
	

	def __init__(self, data, face_name, conns):
		self.face_color = data[int(len(data)/2)]
		self.squares = []
		self.face_name = face_name
		self.connections = conns
		for i in range(3):
			self.squares.append(data[i*3 : i*3+3])


	def checkEdges(self, color):
		"""Returns a list with the coords of the edge square that matches the selected color."""
		ret = []
		for x, y in self.edges:
			if (color == self.squares[x][y]):
				ret.append((x, y))
		return(ret)

	def checkCorners(self, color):
		"""Returns a list with the coords of the corner square that matches the selected color."""
		ret = []
		for x, y in self.corners:
			if (color == self.squares[x][y]):
				ret.append((x, y))
		return(ret)
	
	def setSide(self, name, values, dir):
		"""Sets the 3 squares on the side of the face with %name."""
		
		if (self.connections[name] == "up"):
#			print("up " + name + " " + self.face_name)
			if (name == "back_face" and self.face_name == "top_face" and not dir
			or name == "front_face" and self.face_name == "bottom_face" and dir):
#				print("reversing-u!" + str(values))
				values = reversed(values)
			for i, value in enumerate(values):
				self.squares[0][i] = value

		if (self.connections[name] == "left"):
#			print("left " + name + " " + self.face_name)
			if (name == "right_face" and self.face_name == "back_face"# and dir
			or name == "back_face" and self.face_name == "left_face" and dir
			or name == "left_face" and self.face_name == "top_face" and dir
			or name == "front_face" and self.face_name == "right_face" and not dir
			or name == "left_face" and self.face_name == "bottom_face" and not dir):
#				print("reversing-l!" + str(values))
				values = reversed(values)
			for i, value in enumerate(values):
				self.squares[i][0] = value

		if (self.connections[name] == "right"):
#			print("right " + name + " " + self.face_name)
			if (name == "back_face" and self.face_name == "right_face" and dir
			or name == "right_face" and self.face_name == "bottom_face" and dir
			or name == "right_face" and self.face_name == "top_face" and not dir
			or name == "front_face" and self.face_name == "left_face" and not dir
			or name == "left_face" and self.face_name == "back_face"):# and dir):
#				print("reversing-r!" + str(values))
				values = reversed(values)
			for i, value in enumerate(values):
				self.squares[i][2] = value

		if (self.connections[name] == "down"):
#			print("down " + name + " " + self.face_name)
			if (name == "back_face" and self.face_name == "bottom_face" and not dir
			or name == "front_face" and self.face_name == "top_face" and dir):
#				print("reversing-d!" + str(values))
				values = reversed(values)
			for i, value in enumerate(values):
				self.squares[2][i] = value

	def getSide(self, name):
		"""Returns the 3 squares on the side of the named face."""
		colors = []
#		print(self.face_name, self.connections)
		if (self.connections[name] == "up"):
			for i in range(3):
				colors.append(self.squares[0][i])
		if (self.connections[name] == "left"):
			for i in range(3):
				colors.append(self.squares[i][0])
		if (self.connections[name] == "right"):
			for i in range(3):
				colors.append(self.squares[i][2])
		if (self.connections[name] == "down"):
			for i in range(3):
				colors.append(self.squares[2][i])
		return(colors)

	def rotateFace(self, dir):
		"""Rotate the face clockwise 'cw' or counter clockwise 'ccw'."""
		temp = deque()
		if (dir):
			for x, y in reversed(const.rotateOrder):
				temp.append(self.squares[x][y])
		else:
			for x, y in const.rotateOrder:
				temp.append(self.squares[x][y])
		temp.append(temp.popleft())
		temp.append(temp.popleft())
		if (dir):
			for x, y in const.rotateOrder:
				self.squares[x][y] = temp.pop()
		else:
			for x, y in reversed(const.rotateOrder):
				self.squares[x][y] = temp.pop()

	def allTheSame(self):
		"""Return True if all the colors of the square are the same color."""
		same = True
		for row in self.squares:
			for sq in row:
				if (not sq == self.face_color):
					same = False
		return(same)

	def getColors(self):
		"""Returns the colors of the face in a 3x3 grid."""
		
		colors = ""
		for row in self.squares:
			for sq in row:
				colors += str(sq)
		return(colors)