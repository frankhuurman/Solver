from collections import deque


"""
Connections betweeen the faces:
dict:
	{"up": %face, "left": %face, "right": %face, "down": %face}
	left	[top, back, front, bottom]
	1 [(6,row,norm), (4), (2), (5)]
	front	[top, left, right, bottom]
	2 [6,1,3,5]
	right	[top, front, back, bottom]
	3 [6,2,4,5]
	back	[top, right, left, bottom]
	4 [6,3,1,5]
	bottm	[front, left, right, back]
	5 [2,1,3,4]
	top	[back, left, right, front]
	6 [4,1,3,2]

links = rood
boven = groen
rechts oranje
voor = wit
achter = geel
onder = blauw
"""


class cube(object):
	"""Object representing one rubik's cube."""
	
	
	facenames = ["left_face", "front_face", "right_face", "back_face", "bottom_face", "top_face"]
	connections = {
		facenames[0]: (5, 3, 1, 4),
		facenames[1]: (5, 0, 2, 4),
		facenames[2]: (5, 1, 3, 4),
		facenames[3]: (5, 2, 0, 4),
		facenames[4]: (1, 0, 2, 3),
		facenames[5]: (3, 0, 2, 1)
		}

	faces = {}
	faceColorIndex = {"r": 0, "w": 1, "o": 2, "y": 3, "b": 4, "g": 5}

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """

		sides = ["up", "left", "right", "down"]
		for i, f in enumerate(self.facenames):
			squares = outputlist[i*9 : i*9 + 9]
			face_color = squares[int(len(squares)/2)]
			name = self.facenames[self.faceColorIndex[face_color]]
			conns = {}
			for i, conn in enumerate(self.connections[name]):
				conns[sides[i]] = self.facenames[conn]
			self.faces[f] = face(squares, name, conns)

		for f in self.facenames:
			print("Face: " + f)
			print(self.faces[f].printFace())
			print(self.faces[f].connections)
		
		"""
		for f in self.facenames:
			print("Face: " + f)
			print(self.faces[f].face_name)
			print(self.faces[f].printFace())
			print(self.faces[f].face_color)
			print(self.faces[f].allTheSame())
#			self.faces[f].rotateFace(True)
			self.rotate(f, True)
			print(self.faces[f].printFace())
#			self.faces[f].rotateFace(True)
			self.rotate(f, True)
			print(self.faces[f].printFace())
#			self.faces[f].rotateFace(False)
			self.rotate(f, False)
			print(self.faces[f].printFace())
#			self.faces[f].rotateFace(True)
			self.rotate(f, True)
			print(self.faces[f].printFace())
		print(len(self.faces[self.facenames[2]].checkEdges("w")))
		"""

	def rotate(self, name, dir):
		face = self.faces[name]
		face.rotateFace(dir)
		temp = deque()
		for f, j in face.connections.items():
			print(f, j, self.faces[j].face_name)
			temp.append(self.faces[j].getSide(name))
		temp.append(temp.popleft())
		for f, j in face.connections.items():
			self.faces[j].setSide(name, temp.popleft())
		
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
	
	edges = [[0,1], [1,0], [1,2], [2,1]]
	corners = [[0,0], [0,2], [2,0], [2,2]]
	rotateOrder = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]]

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
		
		if (self.connections["up"] == name):
			for value, i in enumerate(values):
				self.squares[0][i] = value
		if (self.connections["left"] == name):
			for value, i in enumerate(values):
				self.squares[i][0] = value
		if (self.connections["right"] == name):
			for value, i in enumerate(values):
				self.squares[i][2] = value
		if (self.connections["down"] == name):
			for value, i in enumerate(values):
				self.squares[2][i] = value

	def getSide(self, name):
		"""Returns the 3 squares on the side of the named face."""
#		side = self.connections[name]
		colors = []
		if (self.connections["up"] == name):
			for i in range(3):
				colors.append(self.squares[0][i])
		if (self.connections["left"] == name):
			for i in range(3):
				colors.append(self.squares[i][0])
		if (self.connections["right"] == name):
			for i in range(3):
				colors.append(self.squares[i][2])
		if (self.connections["down"] == name):
			for i in range(3):
				colors.append(self.squares[2][i])
		return(colors)

	def rotateFace(self, dir):
		"""Rotate the face clockwise 'cw' or counter clockwise 'ccw'."""
		temp = deque()
		if (dir):
			for x, y in reversed(self.rotateOrder):
				temp.append(self.squares[x][y])
		else:
			for x, y in self.rotateOrder:
				temp.append(self.squares[x][y])
		temp.append(temp.popleft())
		temp.append(temp.popleft())
		if (dir):
			for x, y in self.rotateOrder:
				self.squares[x][y] = temp.pop()
		else:
			for x, y in reversed(self.rotateOrder):
				self.squares[x][y] = temp.pop()

	def allTheSame(self):
		"""Return True if all the colors of the square are the same color."""
		same = True
		for row in self.squares:
			for sq in row:
				if (not sq == self.face_color):
					same = False
		return(same)

	def printFace(self):
		"""Returns the colors of the face in a 3x3 grid."""
		display = ""
		for row in self.squares:
			for sq in row:
				display += "\t" + str(sq)
			display += "\n"
		return(display)