# maze top left to bottom right with movements : right, down, diagonal with obstacles



def findPath(processed, row, col, maze):
	if not maze[row][col]:
		return []
	if row == len(maze)-1 and col == len(maze[0])-1:
        	return [processed]
	paths = list()
	if row < len(maze)-1 and col < len(maze[0])-1:
		diag = findPath(processed+"D", row+1, col+1, maze)
		if diag:
			paths.extend(diag)
	if row < len(maze)-1:
		down = findPath(processed+"V", row+1, col, maze)
		if down:
			paths.extend(down)
	if col < len(maze[0])-1:
		right = findPath(processed+"H", row, col+1, maze)
		if right:
			paths.extend(right)
	return paths




maze = [
	[True, True, True],
	[True, False, True],
	[True, True, True]
]
paths = findPath("", 0, 0, maze)
for path in paths:
	print(path)
