targetFile = "actualInput.txt"

UPPER_LIMIT = 100000 # Upper limit we're looking for

class Folder:
	def __init__(self,name, parent=[], files={}):
		self.name = name
		self.files = files
		self.parent = parent
		self.children = []
		self.size = 0

	def print(self):
		print(self.name)
		print(self.files)
		print(self.parent)
		print(self.children)
		print(self.size)

	def addFile(self, fileName, fileSize):
		self.files.update({fileName : fileSize})

# Open file and read from it
file = open(targetFile, "r") # Open file in read mode

# fileContents = file.read() # Read file contents in fileContents

fileContents = [] # Create empty list for fileContents

for line in file:
	line = line.rstrip('\n')
	fileContents.append(line)

file.close() # Close the file

# Playground

previousDirectory = ""
currentDirectory = ""
folderContents = []
for output in fileContents:
	if output.startswith('$ cd'):
		destDirectory = output.lstrip("$ cd ")
		# print(f"Detected change directory command: {output}")
		# print(f"Destination Directory: {destDirectory}")
	elif output.startswith('$ ls'):
		print(folderContents)
		folderContents = []
		print(f"Detected list contents command: {output}")
	else:
		folderContents.append(output)

