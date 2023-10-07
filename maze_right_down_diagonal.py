# maze top left to bottom right with movements : right, down, diagonal



def findPath(processed, row, col):
	if row == 1 and col == 1:
        	return [processed]
	paths = list()
	if row > 1 and col > 1:
		diag = findPath(processed+"D", row-1, col-1)
		if diag:
			paths.extend(diag)
	if row > 1:
		down = findPath(processed+"V", row-1, col)
		if down:
			paths.extend(down)
	if col > 1:
		right = findPath(processed+"H", row, col-1)
		if right:
			paths.extend(right)
	return paths





paths = findPath("", 3, 3)
for path in paths:
	print(path)
