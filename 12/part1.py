TARGET_FILE = "exampleInput.txt"

# --------------------------------------------------------------------------

class Tile:
	Symbol = ''
	SymbolValue = -1
	XPos = -1
	YPos = -1
	isHiker = False
	isExit = False

	def __init__(self, Symbol = '', Pos = (-1,-1)):
		self.Symbol = Symbol
		self.SymbolValue = ord(self.Symbol)
		self.XPos, self.YPos = Pos

		self.updateStatus()

	def __str__(self):
		return f"Tile at {self.XPos}, {self.YPos} with symbol {self.Symbol}. Is it the hiker? {self.isHiker}. Is it the exit? {self.isExit}"

	def updateStatus(self):
		match(self.Symbol):
			case 'S':
				self.isHiker = True
				self.isExit = False
			case 'E':
				self.isExit = True
				self.isHiker = False
			case _:
				self.isHiker = False
				self.isExit = False

	def updateTile(self, newSymbol):
		self.Symbol = newSymbol
		self.SymbolValue = ord(self.Symbol)
		self.updateStatus()

class TopoMap:
	TopoMap = []
	lenBestRoute = -1

	def __init__(self, inputMap):
		for r in range(len(inputMap)):
			newRow = []
			for c in range(len(inputMap[r])):
				newRow.append(Tile(inputMap[r][c], (r, c)))
			
			self.TopoMap.append(newRow)

	# Define function which takes two Tile objects and returns the height difference between them
	def heightDiff(self, tile1, tile2):
		return tile2.SymbolValue - tile1.SymbolValue
	
	


# --------------------------------------------------------------------------

# Reading from file
file = open(TARGET_FILE, "r")

mapInput = []
for line in file:
	mapInput.append(line.rstrip())

file.close()
del file

# Note: Need ord() to turn chars into numbers

# Creating our topographic map object
topoMap  = TopoMap(mapInput)
del mapInput


