TARGET_FILE = "exampleInput.txt"

# --------------------------------------------------------------------------

class Tile:
	Symbol = ''
	XPos = -1
	YPos = -1
	ValidMoves = []
	isHiker = False
	isExit = False

	def __init__(self, Symbol = '', Pos = (-1,-1), ValidMoves = []):
		self.Symbol = Symbol
		self.XPos, self.YPos = Pos
		self.ValidMoves = ValidMoves

		self.updateStatus()

	def __str__(self):
		return f"Tile at {self.XPos}, {self.YPos} with symbol {self.Symbol} and valid moves {self.ValidMoves}. Is it the hiker? {self.isHiker}. Is it the exit? {self.isExit}"

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
		self.updateStatus()

	def updateValidMoves(self, validMoves):
		self.ValidMoves = validMoves

class TopoMap:
	TopoMap = []
	lenBestRoute = -1

	def __init__(self, inputMap):
		for r in range(len(inputMap)):
			newRow = []
			for c in range(len(inputMap[r])):
				newRow.append(Tile(inputMap[r][c], (r, c)))
			
			self.TopoMap.append(newRow)

	def defineValidMoves(self):
		print("Temporary Print To Keep Python From Freaking Out") 

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


