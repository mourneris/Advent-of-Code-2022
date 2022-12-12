import math

TARGET_FILE = "exampleInput.txt"
NUM_ROUNDS = 20 # Number of rounds over which we'll be observing behavior
DIVIDE_BY = 3 # What it divides by after inspection

# Monkey Business = Product of the two highest monkeys' number of items inspected

class Monkey:
	ID = -1 # ID of -1 means unassigned
	Items = []
	Operation = ' ' # Space equals null operation
	Argument = None # No Argument by Default
	Divisor = 0 # 0 by Default
	isTrueTarget = -1 # -1 means no target (default)
	isFalseTarget = -1 # -1 means no target (default)
	itemsCounted = 0 # Tracker for number of items counted

	# Takes the inputList of inputs and will parse what it needs from it
	def __init__(self, inputList):
		# Line 0 of Input for ID
		self.ID = int(((inputList[0].rstrip(':')).split(' '))[1])
		
		# Line 1 of Input for Starting Items
		self.Items = list(map(int,inputList[1][18:len(inputList[1])].split(', ')))

		# Line 2 of Input for Operation and Argument
		self.Operation = inputList[2][23]
		if self.Operation not in ['*', '+', '/', '-']:
			print("Operation is invalid. Found {self.Operation} as operation.")
		
		self.Argument = inputList [2][25:len(inputList[2])]

		# Line 3 of Input for Divisor
		self.Divisor = int(inputList[3][21:len(inputList[3])])

		# Line 4 of Input for isTrueTarget
		self.isTrueTarget = int(inputList[4][29:len(inputList[4])])

		# Line 5 of Input for isFalseTarget
		self.isFalseTarget = int(inputList[5][30:len(inputList[5])])

	def __str__(self):
		return f"Monkey {self.ID} with items {self.Items} performs {self.Operation} {self.Argument} on old. Checks if divisible by {self.Divisor} and if true it throws to monkey {self.isTrueTarget}, otherwise to monkey {self.isFalseTarget}. This monkey has counted {self.itemsCounted} items at this time."

	def throwItem(self, target, itemNum):
		return (target, itemNum)

	def catchItem(self, itemNum):
		self.Items.append(itemNum)

	def perfOp(self, old, arg):
		match(self.Operation):
			case '*':
				return old * arg
			case '+':
				return old + arg
			case '-':
				return old - arg
			case '/':
				return old / arg

	def inspect(self, itemNum):
		self.itemsCounted += 1
		worryLevel = 0

		if self.Argument == "old":
			worryLevel = self.perfOp(itemNum, itemNum)
		else:
			worryLevel = self.perfOp(itemNum, int(self.Argument))

		worryLevel = math.floor(worryLevel / DIVIDE_BY)

		self.Items.remove(itemNum)
		
		if worryLevel % self.Divisor == 0:
			return self.throwItem(self.isTrueTarget, worryLevel)
		else:
			return self.throwItem(self.isFalseTarget, worryLevel)
		
# Grab Input from File
file = open(TARGET_FILE, "r")

fileInput = []
for line in file:
	if line != chr(10):
		fileInput.append(line.rstrip())

file.close()

monkeys = []
for m in range(0,len(fileInput),6):
	monkeyInput = fileInput[m:m+6]
	# print(monkeyInput)
	monkeys.append(Monkey(monkeyInput))

for i in range(20):
	for monkey in monkeys:
		# print(monkey)
		
		for item in monkey.Items.copy():
			# print(f"Current item is {item}")
			thrown = monkey.inspect(item)
			target = thrown[0]
			itemThrown = thrown[1]
			# print(f"Monkey {monkey.ID} threw {itemThrown} to monkey {target}.")
			monkeys[target].catchItem(itemThrown)

monkeyBusiness = []

for monkey in monkeys:
	monkeyBusiness.append(monkey.itemsCounted)
 
monkeyBusiness.sort(reverse=True)

maxMonkeyBusiness = monkeyBusiness[0] * monkeyBusiness[1]

print(f"Answer is {maxMonkeyBusiness}")