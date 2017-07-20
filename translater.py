move_list = ["ff'bbd'b'btb'"]

def translateToArduino(movelist):
	translated_list = []
	for item in movelist:
		sliced_list = list(item)

	count = 0

	try:
		for item in sliced_list[:-1]:
			if sliced_list[count + 1] == "'":
				translated_list.append(item.upper())
				#print (item.upper())
				count += 1
			elif item != "'":
				translated_list.append(item)
				#print(item)
				count += 1
			elif item == "'":
				count += 1

		if sliced_list[-1] != "'":
			translated_list.append(sliced_list[-1])
			#print (sliced_list[-1])
	except IndexError:
		print ("end of list reached")

	print(translated_list)

translateToArduino(move_list)