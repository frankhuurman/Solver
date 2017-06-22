# init list to calculate
calclist = []

def emptyList():
	""" clears the calclist so it can be used again for a new cube """

	global calclist
	calclist.clear()

def addList(colors):
	""" Extracts colors from calcu_list from solverfinal.py"""

	global calclist
	calclist += colors

	if len(calclist) == 54:
		print ("list complete: ")
		print (calclist)
		print ("\n")

	return colors

