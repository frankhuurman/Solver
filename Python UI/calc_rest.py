from pprint import pprint
from collections import OrderedDict

def printFace(facename, face):
	"""Prints the name of the face and the face that is given as an argument"""
	# example: printFace("left face: ", left_face)

	#TODO: Rewrite this part for a LIST item instead of Dict

	temp_dict = OrderedDict()
	count = 1
	for item, value in face.items():
		temp_dict[count] = value
		count += 1

	print(facename)
	print(temp_dict[1], temp_dict[2], temp_dict[3])
	print(temp_dict[4], temp_dict[5], temp_dict[6])
	print(temp_dict[7], temp_dict[8], temp_dict[9], "\n")
	1, ff
	2, bf



class cube(object):

	facesnames = ["left_face", "front_face", "right_face", "back_face", "bottom_face", "top_face"]
	faces = {}

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """
		print(outputlist)
		for i, f in enumerate(self.facesnames):
			self.faces[f] = face(outputlist[i*9 : i*9 + 9])

		for f in self.facesnames:
			print("Face: " + f)
			print(self.faces[f].squares)
			print(self.faces[f].face_color)
		
		
		
class face(object):
	
	# squares
	@property
	def squares(self):
		return(self.__squares)
	@squares.setter
	def squares(self, squares):
		self.__squares = squares
	# face_color
	@property
	def face_color(self):
		return(self.__face_color)
	@face_color.setter
	def face_color(self, face_color):
		self.__face_color = face_color
		
		
	def __init__(self, data):
		self.squares = []
		print(data)
		self.face_color = data[int(len(data)/2)]
		print("Face_color:", str(self.face_color))
		for i in range(3):
			moi = []
			for j in range(3):
				print(str(i), str(j), str((i*3)+j), str(data[(i*3)+j]))
				moi.append(data[(i*3)+j])
			self.squares.append(moi)
			del(moi)

	def allTheSame(self):
		moi = True
		for i in self.squares:
			if (not i == self.face_color):
				moi = False
		return(True)

	def printface(self):
		print(self.squares)