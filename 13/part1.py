TARGET_FILE = "exampleInput.txt"

# --------------------------------------------------------------------

def findAllBrackets(str):
	opening = []
	closing = []

	found = -2
	index = 0
	while found != -1:
		found = str.find('[', index)

		if found != -1:
			opening.append(found)
			index = found + 1
			found = -2

	found = -2
	index = 0
	while found != -1:
		found = str.find(']', index)

		if found != -1:
			closing.append(found)
			index = found + 1
			found = -2

	return [opening,closing]

# --------------------------------------------------------------------

file = open(TARGET_FILE, 'r')

rawFileInput = []
for line in file:
	if line.rstrip() != '':
		rawFileInput.append(line.rstrip())

for p in range(0, len(rawFileInput), 2):
	m1 = rawFileInput[p]
	m2 = rawFileInput[p+1]

	print(f"Pair {(p // 2) + 1} -> Member 1: {m1}, Member 2: {m2}")

	m1opening, m1closing = findAllBrackets(m1)
	m2opening, m2closing = findAllBrackets(m2)

	left = m1[m1opening[0]+1:m1closing[len(m1closing)-1]]
	right = m2[m2opening[0]+1:m2closing[len(m2closing)-1]]

	print(f"Left: {left}, Right: {right}")
