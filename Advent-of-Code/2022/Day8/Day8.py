with open("input.txt", "r") as f:
    lines = f.readlines()

visibletrees = 0
grid = [[int(h) for h in line.strip()] for line in lines]

TASK = 2

def isVisible(x, y):
    rV = False
    for i in range(x - 1, -1, -1):
        if grid[x][y][0] <= grid[i][y][0]:
            break
        if i == 0:
            rV = True

    for i in range(x + 1, len(grid[0])):
        if grid[x][y][0] <= grid[i][y][0]:
            break
        if i == len(grid[0]) - 1:
            rV = True
    
    for i in range(y - 1, -1, -1):
        if grid[x][y][0] <= grid[x][i][0]:
            break
        if i == 0:
            rV = True
    
    for i in range(y + 1, len(grid)):
        if grid[x][y][0] <= grid[x][i][0]:
            break
        if i == len(grid) - 1:
            rV = True
    return (grid[x][y][0], True) if rV else (grid[x][y][0], False)

def viewDistance(x, y):
    vD = 1
    vC = 0
    if x > 0:
        for i in range(x - 1, -1, -1):
            if grid[x][y][0] > grid[i][y][0]:
                vC += 1
            else:
                vC += 1
                break
        vD *= vC
        vC = 0
    if x < len(grid[0]) - 1:
        for i in range(x + 1, len(grid[0])):
            if grid[x][y][0] > grid[i][y][0]:
                vC += 1
            else:
                vC += 1
                break
        vD *= vC
        vC = 0
    if y > 0:
        for i in range(y - 1, -1, -1):
            if grid[x][y][0] > grid[x][i][0]:
                vC += 1
            else:
                vC += 1
                break
        vD *= vC
        vC = 0
    if y < len(grid) - 1:
        for i in range(y + 1, len(grid)):
            if grid[x][y][0] > grid[x][i][0]:
                vC += 1
            else:
                vC += 1
                break
        vD *= vC
        vC = 0
    
    return (grid[x][y][0], vD)

if TASK == 1:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                grid[i][j] = (grid[i][j], True)
            else:
                grid[i][j] = (grid[i][j], False)

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            grid[x][y] = isVisible(x, y)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][1] == True:
                visibletrees += 1
    print(visibletrees)

maxvd = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid[i][j] = (grid[i][j], 0)

for x in range(1, len(grid) - 1):
    for y in range(1, len(grid[0]) - 1):
        grid[x][y] = viewDistance(x, y)

for i in grid:
    for t in i:
        maxvd = max(maxvd, t[1])
print(maxvd)
