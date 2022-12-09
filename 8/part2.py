targetFile = "actualInput.txt"

# Functions -----------------------------------------------------------------------
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

print("### Plot ###")
for row in trees:
	print(row)

#-----------------------------------------------------------------------

ROWS = len(trees)
COLS = len(trees[0])

sceneryScores = []
for r in range(ROWS):
	sceneryScoreRow = []
	for c in range(COLS):
		# West Sightline
		if c == 0:
			west = 0
		else:
			west = 0
			for i in range(c-1,-1,-1):
				if trees[r][c] <= trees[r][i]:
					west += 1
					break
				else:
					west +=1
		
		# print(f"Western sightline at tree [{r},{c}] is {west}.")
		
		# East Sightline
		if c == COLS-1:
			east = 0
		else:
			east = 0
			for i in range(c+1,COLS):
				if trees[r][c] <= trees[r][i]:
					east += 1
					break
				else:
					east += 1

		# print(f"Eastern sightline at tree [{r},{c}] is {east}.")
		
		# North Sightline
		if r == 0:
			north = 0
		else:
			north = 0
			for i in range(r-1,-1,-1):
				if trees[r][c] <= trees[i][c]:
					north += 1
					break
				else:
					north += 1

		# print(f"Northern sightline at tree [{r},{c}] is {north}.")
		
		# South Sightline
		if r == ROWS-1:
			south = 0
		else:
			south = 0
			for i in range(r+1,ROWS):
				if trees[r][c] <= trees[i][c]:
					south += 1
					break
				else:
					south += 1

		# print(f"Southern sightline at tree [{r},{c}] is {south}.")

		# Calculate Scenery Score

		sceneryScoreRow.append(north * south * west * east)
	
	sceneryScores.append(sceneryScoreRow)

print("### Scenery Scores ###")
for rows in sceneryScores:
	print(rows)

# Find the highest scenary score

optimalSpotScore = 0;

for row in sceneryScores:
	maxOnRow = max(row)
	if maxOnRow > optimalSpotScore:
		optimalSpotScore = maxOnRow

print(f"The highest attainable scenary score is {optimalSpotScore}.")
