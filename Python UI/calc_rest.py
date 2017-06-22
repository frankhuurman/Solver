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

class cube(object):

	def __init__(self, outputlist):
		""" Assigns the items from outputlist to their own face """
		left_face = []
		front_face = []
		right_face = []
		back_face = []
		bottom_face = []
		top_face = []
		count = 1

		for item in outputlist:
			if count <= 9:
				left_face += item
				count += 1
			elif count > 9 and count <= 18:
				front_face += item
				count += 1
			elif count > 18 and count <= 27:
				right_face += item
				count += 1
			elif count > 27 and count <= 36:
				back_face += item
				count += 1
			elif count > 36 and count <= 45:
				bottom_face += item
				count += 1
			elif count > 45 and count <= 54:
				top_face += item
				count += 1

		print (left_face)
		print (front_face)
		print (right_face)


