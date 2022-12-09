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






