def printPath(processed, row, col, maze, level=1):
    if maze[row][col] == "-" or maze[row][col] != '.':
        return

    maze[row][col] = level

    if row == len(maze)-1 and col == len(maze[0])-1:
        print()
        for r in maze:
            for c in r:
                print(c, end=" ")
            print()


    if row < len(maze)-1:
        printPath(processed+"D", row+1, col, maze, level+1)
    if col < len(maze[0])-1:
        printPath(processed+"R", row, col+1, maze, level+1)
    if row > 0:
        printPath(processed+"U", row-1, col, maze, level+1)
    if col > 0:
        printPath(processed+"L", row, col-1, maze, level+1)
    
    maze[row][col] = '.'

    return 



# - is obstacle
# . is free path
maze = [
    ['.', '.', '.'],
    ['.', ".", '.'],
    ['.', '.', '.']
]
paths = printPath("", 0, 0, maze)