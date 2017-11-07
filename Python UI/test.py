

import datetime

def write(args):
	debug = open("debug.txt", "a", newline = "\r\n") # opens debug.txt
	debug.write(str(args) + "\t") # writes all the info on te defective moves to debug.txt
	debug.write(str(datetime.datetime.now()) + "\n") # adds a timestamp
	debug.close() # closes debug.txt


write("moi")
write("blah")
write("Piep")