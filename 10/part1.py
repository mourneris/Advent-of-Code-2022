targetFile = "actualInput.txt"

# Prepare to open and read contents
file = open(targetFile, "r")

instructions = []
for line in file:
	line = line.rstrip()

	instructions.append(line)

file.close()

# Start working the problem

def sigStrAtCycle(instructions, desiredCycle):
	cycle = 1
	x = 1
	for ins in instructions:
		if cycle >= desiredCycle - 1:
			break
		
		if ins[0:4] == "noop":
			cycle += 1
		elif ins[0:4] == "addx":
			cycle += 2
			x += int(ins[5:len(ins)]) # Pull the argument of addx as an integer and add it to x

	return desiredCycle * x

runningTotal = 0
for desired in range(20, 221, 40):
	runningTotal += sigStrAtCycle(instructions, desired)

print(f"Total is {runningTotal}")

