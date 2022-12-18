TARGET_FILE = "actualInput.txt"

commands = ""

def toFString(x, y):
	return f"{x},{y}"

def fromFString(fStr):
	return list(map(int, fStr.split(',')))

with open(TARGET_FILE, 'r') as file:
	for line in file:
		dir, amt = line.rstrip().split(' ')
		commands += (dir * int(amt))
        
xTail = 0
yTail = 0

xHead = 0
yHead = 0

print(f"The Commands (For Reference): {commands}")

visited = {toFString(xTail, yTail) : True}

for cmd in commands:
	# * Head Logic
	match(cmd):
		case 'R':
			xHead += 1
		case 'L':
			xHead -= 1
		case 'U':
			yHead += 1
		case 'D':
			yHead -= 1
	
	print(f"Head @ ({xHead},{yHead})")
	
	# * Tail Logic
	xDiff = xHead - xTail
	yDiff = yHead - yTail
	
	print(f"Tail Starting @ ({xTail},{yTail})")
	print(f"Dist. from Head to Tail is ({xDiff},{yDiff})")

	if xDiff == 2:
		xTail += 1
		yTail = yTail if yTail == yHead else yHead
	elif xDiff == -2:
		xTail -= 1
		yTail = yTail if yTail == yHead else yHead
	if yDiff == 2:
		yTail += 1
		xTail = xTail if xTail == xHead else xHead
	elif yDiff == -2:
		yTail -= 1
		xTail = xTail if xTail == xHead else xHead

	visited.update({toFString(xTail, yTail) : True})

	print(f"Tail Ending @ ({xTail},{yTail})")

print(f"The tail visited {len(visited)} tiles at least once.")
	

