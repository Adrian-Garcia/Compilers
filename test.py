f = open("testt.txt")

while (True):

	line = f.readline()

	if (line):
		print(line)
	else:
		break
