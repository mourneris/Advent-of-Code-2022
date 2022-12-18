TARGET_FILE = "exampleInput2.txt"

LEN_ROPE = 10 # 9 Segments + Head

commands = ""

def toFString(x, y):
	return f"{x},{y}"

def fromFString(fStr):
	return list(map(int, fStr.split(',')))

direction = []
amount = []
with open(TARGET_FILE, 'r') as file:
	for line in file:
		dir, amt = line.rstrip().split(' ')
		
		direction.append(dir)
		amount.append(int(amt))
	
print(f"The Commands (For Reference): {commands}")

# Set these 2 to 0 if no offset to avoid negative numbers is needed
X_OFFSET = 11
Y_OFFSET = 5

rope = []

for tail in range(10):
	rope.append([X_OFFSET, Y_OFFSET])

# Indexing Constants for Readability
X = 0
Y = 1 
HEAD = 0
TAIL = LEN_ROPE - 1

visited = {toFString(rope[TAIL][X], rope[TAIL][Y]) : True}

for dir, amt in zip(direction, amount):
	for _ in range(amt):
		# * Head Logic
		match(dir):
			case 'R':
				rope[HEAD][X] += 1
			case 'L':
				rope[HEAD][X] -= 1
			case 'U':
				rope[HEAD][Y] += 1
			case 'D':
				rope[HEAD][Y] -= 1
		
		# print(f"Head @ ({rope[HEAD][X]},{rope[HEAD][Y]})")

		# * Tail Logic
		for seg in range(1,LEN_ROPE):
			prevSeg = seg - 1 # For readability

			xDiff = rope[prevSeg][X] - rope[seg][X]
			yDiff = rope[prevSeg][Y] - rope[seg][Y]
			
			# print(f"Segment {seg+1} Starting @ ({rope[seg][X]},{rope[seg][Y]})")
			# print(f"Dist. from Head to Tail is ({xDiff},{yDiff})")

			if xDiff >= 2:
				rope[seg][X] += 1
				rope[seg][Y] = rope[seg][Y] if rope[seg][Y] == rope[prevSeg][Y] else rope[prevSeg][Y]
			elif xDiff <= -2:
				rope[seg][X] -= 1
				rope[seg][Y] = rope[seg][Y] if rope[seg][Y] == rope[prevSeg][Y] else rope[prevSeg][Y]
			if yDiff >= 2:
				rope[seg][Y] += 1
				rope[seg][X] = rope[seg][X] if rope[seg][X] == rope[prevSeg][X] else rope[prevSeg][X]
			elif yDiff <= -2:
				rope[seg][Y] -= 1
				rope[seg][X] = rope[seg][X] if rope[seg][X] == rope[prevSeg][X] else rope[prevSeg][X]

			# print(f"Segment {seg+1} Ending @ ({rope[seg][X]},{rope[seg][Y]})")

		print(f"Tail @ ({rope[TAIL][X]},{rope[TAIL][Y]})")
		visited.update({toFString(rope[TAIL][X], rope[TAIL][Y]) : True})

print(f"The tail visited {len(visited)} tiles at least once.")

# TODO: Fix that output is falling lone. Perhaps resort to graphing the solution like suggested on exampleInput2.txt -> Write graphing function (offset finished)
