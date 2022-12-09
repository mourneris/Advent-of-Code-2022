targetFile = "exampleInput.txt"

# Functions -----------------------------------------------------------------------
def getListOfANum(numDesired, num):
	listOfNums = []

	for i in range(0, numDesired):
		listOfNums.append(num)

	return listOfNums

def pullColumn(matrix, column):
	col = []

	for row in matrix:
		col.append(row[column])
	
	return col

def arrayOr(a, b):
	array = []
	if len(a) == len(b):
		for i in range(0,len(a)):
			array.append(a[i] or b[i])
		return array
	else:
		print("Arrays don't match sizes...")
		return -1

def findVisibility(trees):
	vis = []
	tallestTree = -1

	for tree in trees:
		if tree > tallestTree:
			vis.append(1)
			tallestTree = tree
		else:
			vis.append(0)
	
	return vis

# Courtesy of OpenGPT AI
# Rotates 90 degrees clock-wise
def rotate(lst):
	# check if the input list is empty
	if not lst:
		return []

	# get the number of rows and columns in the list
	rows = len(lst)
	cols = len(lst[0])

	# calculate the center position of the list
	center_row = rows // 2
	center_col = cols // 2

	# create a new list with the same number of rows and columns
	# as the input list
	result = [[0 for _ in range(rows)] for _ in range(cols)]

	# loop through the rows and columns of the input list
	for i in range(rows):
		for j in range(cols):
			# get the value at the current position in the input list
			value = lst[i][j]

			# calculate the new row and column positions for the value
			# by rotating it around the center position of the list
			new_row = center_row + (j - center_col)
			new_col = center_col + (center_row - i)

			# assign the value to the corresponding position in the
			# result list
			result[new_row][new_col] = value

	return result


# ---------------------------------------------------------------------------------

# Prepare to open and read contents
file = open(targetFile, "r")

trees = []
for line in file:
	line = line.rstrip()
	trees.append(line)

file.close()
# ---------------------------------------------------------------------------------

# Prepare to chop the trees list into a by-tree matrix configuration
newTrees = []
for row in trees:
	newRow = []
	for tree in row:
		newRow.append(int(tree))
	newTrees.append(newRow)

trees = newTrees # Transfer the new by-tree matrix variant of the input

print(trees)

#-----------------------------------------------------------------------

# We need to create a matrix which tracks which trees are visible and which are not in order to prevent duplicates
# This matrix only really needs to track the core trees NOT on the perimeter
# 1. We need to check the visibility from every direction; left, top, right, bottom
# 	1a. We only need to check in one direction (i.e. top to bottom, left to right) since the input is reversable
# 2. As we move through we can track what's the highest tree to facilitate checking visilibity

hVis = []
for row in trees:
	left2right = findVisibility(row)
	right2left = findVisibility(reversed(row))
	right2left.reverse()

	finalVis = arrayOr(left2right, right2left)

	# print(f"{row}: L2R -> {left2right}, R2L -> {right2left}, Final -> {finalVis}")

	hVis.append(finalVis)

print("### Horizontal Visibility ###")
for row in hVis:
	print(row)

vVis = []
rotatedTrees = rotate(trees)

for row in rotatedTrees:
	left2right = findVisibility(row)
	right2left = findVisibility(reversed(row))
	right2left.reverse()

	finalVis = arrayOr(left2right, right2left)

	# print(f"{row}: L2R -> {left2right}, R2L -> {right2left}, Final -> {finalVis}")

	vVis.append(finalVis)

vVis = rotate(rotate(rotate(vVis)))

print("### Vertical Visibility ###")
for row in vVis:
	print(row)

# print("### Non-Rotated Trees ###")
# for row in trees:
# 	print(row)

# print("### Rotated Tree ###")
# for row in rotatedTrees:
# 	print(row)

fullVis = []
for r in range(len(hVis)):
	row = []
	for c in range(len(vVis)):
		row.append(int(hVis[r][c] or vVis[r][c]))
	
	fullVis.append(row)

print("### Full Visibility ###")
for row in fullVis:
	print(row)

numVisible = 0

for row in fullVis:
	numVisible += sum(row)

print(f"There are {numVisible} trees outside the plot.")
