move_list = ["ff'bbd'b'btb'"]

for item in move_list:
	sliced_list = list(item)

count = 0

try:
	for item in sliced_list[:-1]:
		#print (count)
		if sliced_list[count + 1] == "'":
			#print ("I found a thing")
			print (item.upper())
			count += 1
		elif item != "'":
			print(item)
			count += 1
		elif item == "'":
			count += 1
	if sliced_list[-1] != "'":
		print (sliced_list[-1])
except IndexError:
	print ("end of list reached")