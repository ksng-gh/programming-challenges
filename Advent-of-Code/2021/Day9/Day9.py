import math

with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

#with open("test2.txt", "r") as f:
#    lines = f.readlines()


heightmap = []
for line in lines:
    line = line.strip()
    heightmap.append(line)

def isLowest(l):
    return True if min(l) == l[0] and not l.count(l[0]) == len(l) else False

#mode = 0, all neighbours
#mode = 1, higher neighbours
def getNeighbours(x, y, heightmap):
    checkList = []
    if y == 0 and x == 0:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y + 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
    #(max, 0)
    elif y == 0 and x == len(heightmap[0]) - 1:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y][x - 1]))
        checkList.append(int(heightmap[y + 1][x]))
    #(top)
    elif y == 0:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y][x - 1]))
        checkList.append(int(heightmap[y + 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
    #(0, max)
    elif y == len(heightmap) - 1 and x == 0:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
    #left
    elif x == 0:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
        checkList.append(int(heightmap[y + 1][x]))
    #(max, max)
    elif y == len(heightmap) - 1 and x == len(heightmap[0]) - 1:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y][x - 1]))
    #bot
    elif y == len(heightmap) - 1:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y][x - 1]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
    #right
    elif x == len(heightmap[0]) - 1:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y + 1][x]))
        checkList.append(int(heightmap[y][x - 1]))
    else:
        checkList.append(int(heightmap[y][x]))
        checkList.append(int(heightmap[y - 1][x]))
        checkList.append(int(heightmap[y][x + 1]))
        checkList.append(int(heightmap[y + 1][x]))
        checkList.append(int(heightmap[y][x - 1]))
    
    return checkList

#Get neighbours of yourself and bigger
def getNeighbours2(x, y, heightmap):
    checkList = []
    if y == 0 and x == 0:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
    #(max, 0)
    elif y == 0 and x == len(heightmap[0]) - 1:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
    #(top)
    elif y == 0:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
    #(0, max)
    elif y == len(heightmap) - 1 and x == 0:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
    #left
    elif x == 0:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
    #(max, max)
    elif y == len(heightmap) - 1 and x == len(heightmap[0]) - 1:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
    #bot
    elif y == len(heightmap) - 1:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
    #right
    elif x == len(heightmap[0]) - 1:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
    else:
        checkList.append([int(heightmap[y][x]), (y, x)])
        checkList.append([int(heightmap[y - 1][x]), (y - 1, x)])
        checkList.append([int(heightmap[y][x + 1]), (y, x + 1)])
        checkList.append([int(heightmap[y + 1][x]), (y + 1, x)])
        checkList.append([int(heightmap[y][x - 1]), (y, x - 1)])
    center = checkList[0][0]
    r = [value for value in checkList if 9 not in value and center <= value[0]]
    return r

#remove duplicate
def cleanse(l):
    new = []
    for i in l:
        if i not in new:
            new.append(i)
    return new

TASK = 2

if TASK == 1:
    lowpoints = []
    for y, item in enumerate(heightmap):
        #print(item)
        for x in range(len(item)):
            checkList = getNeighbours(x, y, heightmap)
            if isLowest(checkList):
                lowpoints.append(checkList[0] + 1)
    print(sum(lowpoints))

if TASK == 2:
    max3 = []
    tubes = []
    for y, item in enumerate(heightmap):
        for x in range(len(item)):
            if int(heightmap[y][x]) != 9:
                neighbours = getNeighbours2(x, y, heightmap)
                curr = len(neighbours)
                i = 0
                while i < curr:
                    neighbours = neighbours + getNeighbours2(neighbours[i][1][1], neighbours[i][1][0], heightmap)
                    neighbours = cleanse(neighbours)
                    curr = len(neighbours)
                    i += 1
                if len(max3) < 3:
                    max3.append(len(neighbours))
                else:
                    max3.append(len(neighbours))
                    max3.remove(min(max3))
    print(math.prod(max3))
