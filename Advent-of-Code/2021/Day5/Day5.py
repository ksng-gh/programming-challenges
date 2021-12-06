#Note, I should read the text more carefully :^)

with open("day5.txt", "r") as f:
   lines = f.readlines()

#with open("test.txt", "r") as f:
#   lines = f.readlines()

# position1: [x0, y0], position2: [x1, y1]
def isVerticalOrHorizontal(x0, y0, x1, y1):
    return True if x0 == x1 or y0 == y1 else False

def diagonalsCheck(x0, y0, x1, y1):
    vx = 1
    vy = 1
    if x1 < x0:
        vx = -1
    if y1 < y0:
        vy = -1
    return vx, vy

TASK = 2

coordinates = []
for line in lines:
    line = line.strip()
    pos = line.split(" -> ")
    coordinates.append(pos)

overlapCounter = 0
#List too slow
overlapDict = {}

for coordinate in coordinates:
    position1 = coordinate[0].split(",")
    position2 = coordinate[1].split(",")

    # position1: [x0, y0], position2: [x1, y1]
    x0 = int(position1[0])
    x1 = int(position2[0])

    y0 = int(position1[1])
    y1 = int(position2[1])
    if TASK == 1:
        if isVerticalOrHorizontal(x0, y0, x1, y1):
            startx = min(x0, x1)
            endx = max(x0, x1)

            starty = min(y0, y1)
            endy = max(y0, y1)

            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    newPos = (str(x), str(y))
                    if overlapDict.get(newPos) is None:
                        overlapDict[newPos] = 1
                    else:
                        overlapDict.update({newPos: overlapDict.get(newPos) + 1})
    if TASK == 2:
        if isVerticalOrHorizontal(x0, y0, x1, y1):
            startx = min(x0, x1)
            endx = max(x0, x1)

            starty = min(y0, y1)
            endy = max(y0, y1)

            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    newPos = (str(x), str(y))
                    if overlapDict.get(newPos) is None:
                        overlapDict[newPos] = 1
                    else:
                        overlapDict.update({newPos: overlapDict.get(newPos) + 1})
        else:
            startx = min(x0, x1)
            endx = max(x0, x1)

            resd = diagonalsCheck(x0, y0, x1, y1)
            for x in range(startx, endx + 1):
                newPos = (str(x0), str(y0))
                x0 += resd[0]
                y0 += resd[1]
                if overlapDict.get(newPos) is None:
                    overlapDict[newPos] = 1
                else:
                    overlapDict.update({newPos: overlapDict.get(newPos) + 1})

for i in overlapDict:
    if overlapDict.get(i) > 1:
        overlapCounter += 1

print(overlapCounter)