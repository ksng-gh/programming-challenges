import copy

n, k = map(int, input().split(" "))

battlefield = []
ships = []

#Function to see if there are empty rows on x-axis
def matchshipX(ships, field, start):

    combinations = 0
    cship = ships.pop(0)
    #Coords for the ship which it occupies
    coordsX = [(i, start[1]) for i in range(start[0], start[0] + cship)]
    #Coords for which the ship does not occupy.
    newfieldX = [i for i in field if (i[0], i[1]) not in coordsX]

    #If there are "O" left, then not valid.
    gatekeeper = False
    for i in newfieldX:
        if i[2] == "O":
            gatekeeper = True

    count = len(field) - len(newfieldX)

    if count != cship or (gatekeeper and len(ships) == 0):
        return 0

    elif len(ships) == 0:
        return 1

    else:
        for i in newfieldX:
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(newfieldX), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(newfieldX), i)


    return combinations

#Function to see if there are empty rows on y-axis
def matchshipY(ships, field, start):

    combinations = 0
    cship = ships.pop(0)

    #If cship == 1, it has been seen in matchshipX, and thus returns 0.
    if cship == 1:
        return 0

    count = 0
    coordsY = [(start[0], i) for i in range(start[1], start[1] + cship)]
    newfieldY = [i for i in field if (i[0], i[1]) not in coordsY]

    gatekeeper = False
    for i in newfieldY:
        if i[2] == "O":
            gatekeeper = True

    count = len(field) - len(newfieldY)

    if count != cship or (gatekeeper and len(ships) == 0):
        return 0

    elif len(ships) == 0:
        return 1

    else:
        for i in newfieldY:
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(newfieldY), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(newfieldY), i)


    return combinations

def calculate(ships, field):
    combinations = 0

    for i in field:
        y = matchshipY(copy.deepcopy(ships), copy.deepcopy(battlefield), i)
        x = matchshipX(copy.deepcopy(ships), copy.deepcopy(battlefield), i)

        combinations += x + y

    return combinations

for i in range(n):
    line = input()
    for index, item in enumerate(line):
        if item != "X":
            battlefield.append((index, n - (i + 1), item))

for i in range(k):
    ships.append(int(input()))

ships.sort(reverse=True)

print(calculate(ships, battlefield))