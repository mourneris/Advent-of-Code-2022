TARGET_FILE = "exampleInput.txt"

UPPER_LIMIT = 100000 # Upper limit we're looking for

class Stack:
	def __init__(self):
		self.__contents = []
		self.__size = 0
     
	def __repr__(self):
		return f"Contents: {self.__contents}"

	def push(self, content):
		self.__contents.append(content)
		self.__size += 1

	def pop(self):
		if self.__size != 0:
			self.__size -= 1
			return self.__contents.pop(self.__size - 1)

		return None

	def peek(self):
		return self.__contents[self.__size - 1]



class Folder:
	def __init__(self, name : str, parent : str = None):
		self.__name = name
		self.__parent = parent
		self.__children = {}
		self.__size = 0
	
	def hasChild(self, childName):
		try:
			children = list(self.__children.keys())
			childExists = children.index(childName)
			return bool(childExists)
		except ValueError:
			return False

	def addChild(self, childName):
		if not self.hasChild(childName):
			self.__children.update({childName : Folder(childName, self)})

	def getChild(self, childName):
		

	def getChildren(self):
		return self.__children

	def setSize(self, size):
		self.__size = size
	
	def incSize(self, amount):
		self.__size += amount

	def getSize(self):
		return self.__size
	
termOutput = []
with open(TARGET_FILE, 'r') as file:
	for line in file:
		termOutput.append(line.rstrip().split(' '))


# * The path stack will keep track of the folder structure
path = Stack()

root = Folder("/")

root.addChild("Apple")
root.addChild("Dog")
print(root.hasChild("Cat"))
print(root.hasChild("Apple"))
print(root.hasChild("Dog"))

print(root.getChild("Cat"))
print(root.getChild("Apple"))
print(root.getChild("Dog"))

# for output in termOutput[2:7]:
# 	if output[0] == "dir":
# 		currentFolder.addChild(output[1])
# 		print(f"Adding child {output[1]}")
# 	elif output[0] == '$':
# 		if output[1] == 'cd':
# 			if 
# 	else:
# 		print(f"Adding size {output[0]}")
# 		currentFolder.incSize(int(output[0]))