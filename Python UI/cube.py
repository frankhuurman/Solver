from collections import deque


class const:
	edges = [[0,1], [1,0], [1,2], [2,1]]
	corners = [[0,0], [0,2], [2,0], [2,2]]
	rotateOrder = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]]
	faceColorIndex = {"r": 0, "w": 1, "o": 2, "y": 3, "b": 4, "g": 5}
	facenames = ["left_face", "front_face", "right_face", "back_face", "bottom_face", "top_face"]

class cube(object):
	"""Object representing one rubik's cube."""
	
	connections = {
		const.facenames[0]: (5, 3, 4, 1),
		const.facenames[1]: (5, 0, 4, 2),
		const.facenames[2]: (5, 1, 4, 3),
		const.facenames[3]: (5, 2, 4, 0),
		const.facenames[4]: (1, 0, 3, 2),
		const.facenames[5]: (3, 0, 1, 2)
		}
	faces = {}
	facenames = const.facenames

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """

		moi = []
		for i in """rggrrwyyoyggrwbbboryyoobwwbggwyyboobwwgrboryyboorggrww""":
			moi.append(i)
		print(moi)
		sides = ["up", "left", "down", "right"]
		for i, f in enumerate(const.facenames):
			squares = moi[i*9 : i*9 + 9]
			face_color = squares[int(len(squares)/2)]
			name = const.facenames[const.faceColorIndex[face_color]]
			conns = {}
			for i, conn in enumerate(self.connections[name]):
				conns[const.facenames[conn]] = sides[i]
			self.faces[f] = face(squares, name, conns)

		
	def rotate(self, name, dir):
		"""Rotates the face along with the corresponding sides."""

		face = self.faces[name]
		face.rotateFace(dir)
		temp = deque()
		reverse = []
		for i in face.connections:
			reverse.append(i)
		if (dir):
			for f in face.connections:
				temp.append(self.faces[f].getSide(name))
		else:
			for f in reversed(reverse):
				temp.append(self.faces[f].getSide(name))
		temp.append(temp.popleft())
#		print(temp)
		if (dir):
			for f in face.connections:
				self.faces[f].setSide(name, temp.popleft())
		else:
			for f in reversed(reverse):
				self.faces[f].setSide(name, temp.popleft())

	def printFaces(self, name):
		"""Prints the current face with the 4 connecting sides, all properly oriented."""

		squares = {}
		middleSquares = []
		text = ""
		for i, f in enumerate(list(self.faces[name].connections.keys())):
			main = self.faces[name].connections[f]
			sec = self.faces[f].connections[name]
			squares["sq" + str(i)] = self.turnForPrint(main, sec, self.faces[f].squares, f)
#			print(main, sec)
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

	def sendMoves(self, moves):

		index = {"l": 0, "f": 1, "r": 2, "b": 3, "d": 4, "u": 5}
		for move in moves:
			dir = str(move).islower()
			self.rotate(const.facenames[index[str(move).lower()]], dir)

	def turnForPrint(self, relMain, relSec, squares, name):
		if (relMain == relSec):
			return(self.rotPrint(2, squares, name))
		elif ((relMain == "up" and relSec == "left") or
				(relMain == "left" and relSec == "down") or
				(relMain == "down" and relSec == "right") or
				(relMain == "right" and relSec == "up")):
			return(self.rotPrint(1, squares, name))
		elif ((relMain == "left" and relSec == "up") or
				(relMain == "up" and relSec == "right") or
				(relMain == "right" and relSec == "down") or
				(relMain == "down" and relSec == "left")):
			return(self.rotPrint(3, squares, name))
		return(squares)


	def rotPrint(self, turns, squares, name):
		print(str(turns), "moi")
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

	def solved(self):
		s = True
		for f in const.facenames:
			if (not self.faces[f].allTheSame()):
				s = False

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
			temp = []
			for j in range(3):
				temp.append(data[(i*3)+j])
			self.squares.append(temp)
			del(temp)

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
	
	def setSide(self, name, values):
		"""Sets the 3 squares on the side of the face with %name."""
		
		if (self.connections[name] == "up"):
			for i, value in enumerate(values):
				self.squares[0][i] = value
		if (self.connections[name] == "left"):
			for i, value in enumerate(values):
				self.squares[i][0] = value
		if (self.connections[name] == "right"):
			for i, value in enumerate(values):
				self.squares[i][2] = value
		if (self.connections[name] == "down"):
			for i, value in enumerate(values):
				self.squares[2][i] = value

	def getSide(self, name):
		"""Returns the 3 squares on the side of the named face."""
		colors = []
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