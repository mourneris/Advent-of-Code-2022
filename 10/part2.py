TARGET_FILE = "actualInput.txt"

NUM_CYCLES = 240
CRT_ROWS = 6
CRT_COLS = 40

# Prepare to open and read contents
file = open(TARGET_FILE, "r")

instructions = []
for line in file:
	line = line.rstrip()

	instructions.append(line)

file.close()

# Fill the corresponding x values at a given cycle
xAtCycle = []
for i in range(NUM_CYCLES):
	xAtCycle.append(1)

cycle = 0
x = 1
for ins in instructions:		
	if ins[0:4] == "noop":
		xAtCycle[cycle] = x
		cycle += 1
	elif ins[0:4] == "addx":
		xAtCycle[cycle] = x
		xAtCycle[cycle+1] = x
		
		cycle += 2
		x += int(ins[5:len(ins)]) # Pull the argument of addx as an integer and add it to x
		xAtCycle[cycle] = x
		# print(f"Assigned x = {x} at cycle {cycle}.")

print(xAtCycle)

# Write the screen printing algorithm
for row in range(CRT_ROWS):
	for pixel in range(CRT_COLS):
		charToPrint = ' '

		if abs(xAtCycle[row*40 + pixel] - int(pixel)) <= 1:
			charToPrint = '#'

		print(charToPrint, end='')
	
	print('')









