def islandPerimeter(grid):
    perimeter = 0
    for row in grid:
        for element in row:
            if element == '0':
                continue
            elif element == '1':



grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
islandPerimeter(grid)
