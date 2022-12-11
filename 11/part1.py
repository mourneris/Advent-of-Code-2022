TARGET_FILE = "exampleInput.txt"
NUM_ROUNDS = 20 # Number of rounds over which we'll be observing behavior

# Monkey Business = Product of the two highest monkeys' number of items inspected

class Monkey:
	ID = -1 # ID of -1 means unassigned
	

# Grab Input from File
file = open(TARGET_FILE, "r")

fileInput = []
for line in file:
	fileInput.append(line.rstrip())

file.close()

