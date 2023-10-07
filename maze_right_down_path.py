# moving from the top right corner to the bottom left corner of a maze
# can move only right or down
# print all paths

def printPath(processed, row, col):
    if row == 1 and col == 1:
        print(processed)
    if row > 1:
        printPath(processed+"D", row-1, col)
    if col > 1:
        printPath(processed+"R", row, col-1)

def listOfPaths(processed, row, col):
    # print("row", row, "col", col, "processed", processed)
    if row == 1 and col == 1:
        return [processed]

    overall_paths = list()

    if row > 1:
        d_processed = processed.copy()
        d_processed.append('D')
        down = listOfPaths(d_processed, row-1, col)
        if down:
            overall_paths.extend(down)

    if col > 1:
        r_processed = processed.copy()
        r_processed.append('R')
        right = listOfPaths(r_processed, row, col-1)
        if right:
            overall_paths.extend(right)

    if overall_paths:
        return overall_paths
    return


printPath("", 4, 3)
processed = list()
paths = listOfPaths(processed, 4, 3)
for path in paths:
	print(path)
