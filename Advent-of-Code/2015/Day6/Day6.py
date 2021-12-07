with open("day6.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

TASK = 1

size = 1000
lights = 0

#-1 = off, 1 = on
if TASK == 1:
    lightStatus = [[-1 for i in range(size)] for j in range(size)]
else:
    lightStatus = [[0 for i in range(size)] for j in range(size)]

def setLights(grid, x0, y0, x1, y1, status):
    #0 = on, 1 = off, 2 = toggle
    if status == 0:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = 1
    if status == 1:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = -1
    if status == 2:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                val = grid[x][y]
                grid[x][y] = val * -1
    return grid

def setLights2(grid, x0, y0, x1, y1, status):
    #0 = on, 1 = off, 2 = toggle
    if status == 0:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] += 1
    if status == 1:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if grid[x][y] > 0:
                    grid[x][y] -= 1
    if status == 2:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] += 2
    return grid


for line in lines:
    line = line.strip().split(" ")
    if line[0] != "toggle":
        x0 = int(line[2].split(",")[0])
        y0 = int(line[2].split(",")[1])

        x1 = int(line[4].split(",")[0])
        y1 = int(line[4].split(",")[1])
    else:
        x0 = int(line[1].split(",")[0])
        y0 = int(line[1].split(",")[1])

        x1 = int(line[3].split(",")[0])
        y1 = int(line[3].split(",")[1])
    if line[1] == "on":
        if TASK == 1:
            setLights(lightStatus, x0, y0, x1, y1, 0)
        else:
            setLights2(lightStatus, x0, y0, x1, y1, 0)
    if line[1] == "off":
        if TASK == 1:
            setLights(lightStatus, x0, y0, x1, y1, 1)
        else:
            setLights2(lightStatus, x0, y0, x1, y1, 1)
    if line[0] == "toggle":
        if TASK == 1:
            setLights(lightStatus, x0, y0, x1, y1, 2)
        else:
            setLights2(lightStatus, x0, y0, x1, y1, 2)

if TASK == 1:
    for i in lightStatus:
        for j in i:
            if j > 0:
                lights += 1
else:
    for i in lightStatus:
        for j in i:
                lights += j
print(lights)
        
        
        
    
    
        