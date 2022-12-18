TARGET_FILE = "actualInput.txt"

UPPER_LIMIT = 100000 # Upper limit we're looking for

termOutput = []
with open(TARGET_FILE, 'r') as file:
	for line in file:
		termOutput.append(line.rstrip().split(' '))

# * The path stack will keep track of the folder structure
path = "/home"

folders = {"/home" : 0}

for output in termOutput[2:]:
	if output[0] == '$':
		if output[1] == "cd":
			match(output[2]):
				case "..":
					size = folders[path]
					prevPath = path
					path = path[:path.rfind('/')]
					# print(f"Moved Up to Folder: {path}")

					# Update Size of the Parent
					# print(f"Increasing size of {path} by {size} of folder {prevPath}")
					folderSize = folders[path] + size
					folders.update({path : folderSize})
				case Default:
					path += ('/' + output[2])
					folders.update({path : 0})
					# print(f"Moved Down to Folder: {path}")
		elif output[1] == "ls":
			pass
			# print("List (ls) command ignored...")
	elif output[0] != "dir":
		# print(f"Increasing size of {path} by {output[0]} of file {output[1]}")
		folderSize = folders[path] + int(output[0])
		folders.update({path : folderSize})

validSizes = []
for key, value in folders.items():
	if value < UPPER_LIMIT:
		validSizes.append(value)

validSizes.sort()
print(validSizes)

print(sum(validSizes))