import copy

n, k = map(int, input().split(" "))

battlefield = []
ships = []

def matchshipX(ships, field, start):


    combinations = 0
    cship = ships.pop(0)
    count = 0
    startx = start[0]
    coords = []
    poppings = []

    for i in range(startx, startx + cship):
        coords.append((i, start[1]))

    for i in range(len(coords)):
        for j in range(len(field)):
            if coords[i][0] == field[j][0] and coords[i][1] == field[j][1]:
                poppings.append(j)
                count += 1


    poppings.sort(reverse=True)
    for i in poppings:
        field.pop(i)

    gatekeeper = False
    for i in field:
        if i[2] == "O":
            gatekeeper = True

    if count != cship or (gatekeeper and len(ships) == 0):
        return 0

    elif len(ships) == 0 and count == len(coords):
        return 1

    else:
        for i in field:
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(field), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(field), i)


    return combinations

def matchshipY(ships, field, start):

    combinations = 0
    cship = ships.pop(0)

    if cship == 1:
        return 0

    count = 0
    starty = start[1]
    coords = []
    poppings = []

    for i in range(starty, starty + cship):
        coords.append((start[0], i))

    for i in range(len(coords)):
        for j in range(len(field)):
            if coords[i][0] == field[j][0] and coords[i][1] == field[j][1]:
                poppings.append(j)
                count += 1


    poppings.sort(reverse=True)
    for i in poppings:
        field.pop(i)

    gatekeeper = False
    for i in field:
        if i[2] == "O":
            gatekeeper = True

    if count != cship or (gatekeeper and len(ships) == 0):
        return 0

    elif len(ships) == 0 and count == len(coords):
        return 1

    else:
        for i in field:
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(field), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(field), i)


    return combinations

def calculate(ships, field):
    combinations = 0

    for i in field:
        combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(battlefield), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(battlefield), i)

    return combinations

##
##
##

for i in range(n):
    line = input()
    for index, item in enumerate(line):
        if item != "X":
            battlefield.append((index, n - (i + 1), item))

for i in range(k):
    ships.append(int(input()))

ships.sort(reverse=True)

print(calculate(ships, battlefield))