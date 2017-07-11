from collections import deque


"""
Connections betweeen the faces:
dict:
	{"up": %face, "left": %face, "right": %face, "down": %face}
	left	[top, back, front, bottom]
	1 [6,4,2,5]
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
	faces = {}

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """
		print(outputlist)
		for i, f in enumerate(self.facenames):
			self.faces[f] = face(outputlist[i*9 : i*9 + 9])

		for f in self.facenames:
			self.faces[f].rotateFace("cw")
			print("Face: " + f)
			print(self.faces[f].printFace())
			print(self.faces[f].face_color)
			print(self.faces[f].allTheSame())
#		print(self.faces["top_face"].printFace())
#		self.faces["top_face"].rotateFace("cw")
#		print(self.faces["top_face"].printFace())
		print(self.faces[self.facenames[2]].checkEdges("w"))
		
		
		
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
	
	edges = [[0,1], [1,0], [1,2], [2,1]]
	corners = [[0,0], [0,2], [2,0], [2,2]]
	order = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]]
		
		
	def __init__(self, data):
		self.face_color = data[int(len(data)/2)]
		self.squares = []
		for i in range(3):
			temp = []
			for j in range(3):
				temp.append(data[(i*3)+j])
			self.squares.append(temp)
			del(temp)

	def checkEdges(self, color):
		"""Returns a list with the coords of the square that matches the selected color."""
		ret = []
		for e in self.edges:
			if (color == self.squares[e[0]][e[1]]):
				ret.append(e)
		return(ret)

	def rotateFace(self, dir):
		"""Rotate the face clockwise 'cw' or counter clockwise 'ccw'."""
		temp = deque()
		for row in self.squares:
			for sq in row:
				if (not row == 1 and not sq == 1):
					temp.append(sq)
		temp.append(temp.popleft())
		temp.append(temp.popleft())
		print(temp)
		for row in self.squares:
			for sq in row:
				if (not row == 1 and not sq == 1):
					sq = temp.pop()

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
