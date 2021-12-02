with open("day3.txt", "r") as f:
    line = f.readline()

TASK = 2

presents = 1
checker = [(0, 0)]
posX = 0
posY = 0
roboposX = 0
roboposY = 0

def checkPresents(tuple):
    if tuple in checker:
        return True
    else: 
        return False


#line = ">"
#line = "^v"
#line = "^>v<"
#line = "^v^v^v^v^v"

if TASK == 1:
    for i in line:
        if i == "^":
            posY += 1
        if i == ">":
            posX += 1
        if i == "v":
            posY -= 1
        if i == "<":
            posX -= 1

        position = (posX, posY)

        if not checkPresents(position):
            presents += 1
            checker.append(position)

if TASK == 2:

    for idx, i in enumerate(line):
        roboOrSanta = int(idx) % 2

        if roboOrSanta == 0:
            if i == "^":
                posY += 1
            if i == ">":
                posX += 1
            if i == "v":
                posY -= 1
            if i == "<":
                posX -= 1

            position = (posX, posY)
        else:
            if i == "^":
                roboposY += 1
            if i == ">":
                roboposX += 1
            if i == "v":
                roboposY -= 1
            if i == "<":
                roboposX -= 1

            position = (roboposX, roboposY)
            
            
        if not checkPresents(position):
            presents += 1
            checker.append(position)

print(presents)