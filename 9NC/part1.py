targetFile = "exampleInput.txt"

# Prepare to open and read contents
file = open(targetFile, "r")

instructions = []
for line in file:
	line = line.rstrip()
	instructions.append(line)

file.close()
# -----------------------------------------------------------------------------------------------------------------------------

# Break instructions into directions and amounts
directions = []
amounts = []
for instruction in instructions:
	directions.append((instruction.split(' '))[0])
	amounts.append(int((instruction.split(' '))[1]))
# -----------------------------------------------------------------------------------------------------------------------------

# Find the boundaries for the field as well as the starting position of the head to keep values positive

# We're going to do this by tracking just the head through the list of instructions
xPos = 0
yPos = 0

rMax = 0 # Maximum boundary rightward
lMax = 0 # Maximum boundary leftward
uMax = 0 # Maximum boundary upward 
dMax = 0 # Maximum boundary downward

for i in range(len(directions)):
	# print(f"Command: Move {directions[i]} {amounts[i]} spots...")
	match directions[i]:
		case 'R':
			xPos += amounts[i]
			if xPos > rMax:
				rMax = xPos
		case 'L':
			xPos -= amounts[i]
			if xPos < lMax:
				lMax = xPos
		case 'U':
			yPos += amounts[i]
			if yPos > uMax:
				uMax = yPos
		case 'D':
			yPos -= amounts[i]
			if yPos < dMax:
				dMax = yPos
		case _:
			print("Command unrecognized. Exiting...")
			break

	# print(f"New position is {xPos},{yPos}...")
	# print(f"Boundaries: U = {uMax}, R = {rMax}, D = {dMax}, L = {lMax}")
	
# Calculate the distances traversed on the x-axis and y-axis
xDist = rMax - lMax + 1
yDist = uMax - dMax + 1

print(f"Playing field has to be {xDist} wide by {yDist} tall.")

# The starting position is the absolute value of the leftward max and the downward max, x and y, respectively.
xStarting = abs(lMax)
yStarting = abs(dMax)

print(f"Head should start at {xStarting},{yStarting}.")

# Create the playfield and corresponding visited field

playField = []
visitedField = []

for r in range(yDist):
	newRow = []
	newRowVisited = []
	for c in range(xDist):
		newRow.append('-')
		newRowVisited.append(0)
	
	playField.append(newRow)
	visitedField.append(newRowVisited)

EMPTY_FIELD = playField # Keep a copy of the empty field with nothing on it.

# yStarting has to be adjusted to move it relative to the bottom of the field
yStarting = len(playField) - yStarting - 1

playField[yStarting][xStarting] = 'H'
visitedField[yStarting][xStarting] = 1

print("### Starting Playfield ###")
for row in playField:
	print(row)

print("### Starting Tail Visited Field ###")
for row in visitedField:
	print(row)

# Track x and y positions of the tail and head respectively
xTail = xStarting
yTail = yStarting
xHead = xStarting
yHead = yStarting

for i in range(len(directions)):
	for s in range(amounts[i]):
		match directions[i]:
			case 'R':
				xHead += 1
			case 'L':
				xHead -= 1
			case 'U':
				yHead += 1
			case 'D':
				yHead -= 1

		# Tail checks here






