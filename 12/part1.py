TARGET_FILE = "exampleInput.txt"

file = open(TARGET_FILE, "r")

topoMap = []
for line in file:
	topoMap.append(line.rstrip())

file.close()
del file

for row in topoMap:
     print(row)