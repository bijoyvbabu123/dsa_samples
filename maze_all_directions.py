# maze top left to bottom right with movements : left, right, down, up  with obstacles



def findPath(processed, row, col, maze):
    if not maze[row][col]:
        return []

    if row == len(maze)-1 and col == len(maze[0])-1:
        return [processed]
    maze[row][col] = False


    paths = list()

    if row < len(maze)-1:
        down = findPath(processed+"D", row+1, col, maze)
        paths.extend(down)
    if col < len(maze[0])-1:
        right = findPath(processed+"R", row, col+1, maze)
        paths.extend(right)
    if row > 0:
        up = findPath(processed+"U", row-1, col, maze)
        paths.extend(up)
    if col > 0:
        left = findPath(processed+"L", row, col-1, maze)
        paths.extend(left)
    
    maze[row][col] = True

    return paths




maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
paths = findPath("", 0, 0, maze)
for path in paths:
    print(path)
