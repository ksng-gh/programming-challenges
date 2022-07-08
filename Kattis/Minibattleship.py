import copy
from itertools import combinations

n, k = map(int, input().split(" "))

battlefield = []
ships = []

def matchshipX(ships, field, start):

    print("==========================")
    print("start X")
    print("==========================")

    print("field start")
    print(start)

    print("curr field")
    print(field)


    print("ships")
    print(ships)



    combinations = 0
    cship = ships.pop(0)
    count = 0
    startx = start[0]
    coords = []
    poppings = []

    for i in range(startx, startx + cship):
        coords.append((i, start[1]))

    print("coords")
    print(coords)


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

    print("field")
    print(field)

    if len(ships) == 0 and count == len(coords):
        print("returns 1")
        return 1
    elif (len(ships) == 0 and len(field) != 0) or count != cship or (gatekeeper and len(ships) == 0):
        print("returns 0")
        return 0
    else:
        #deepcopyfield = copy.deepcopy(field)
        #deepcopyships = copy.deepcopy(ships)
        for i in field:
            #combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(field), i)# + matchshipY(copy.deepcopy(ships), copy.deepcopy(field), i)
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(field), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(field), i)


    return combinations

def matchshipY(ships, field, start):

    print("==========================")
    print("start Y")
    print("==========================")

    print("field start")
    print(start)

    print("curr field")
    print(field)


    print("ships")
    print(ships)



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

    print("coords")
    print(coords)

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

    print("field")
    print(field)

    if len(ships) == 0 and count == len(coords):
        print("returns 1")
        return 1
    elif (len(ships) == 0 and len(field) != 0) or count != cship or gatekeeper:
        print("returns 0")
        return 0
    else:
        #deepcopyfield = copy.deepcopy(field)
        #deepcopyships = copy.deepcopy(ships)
        for i in field:
            combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(field), i) + matchshipY(copy.deepcopy(ships), copy.deepcopy(field), i)
            #combinations += matchshipY(copy.deepcopy(ships), copy.deepcopy(battlefield), i)


    return combinations

def calculate(ships, field):
    combinations = 0

    for i in field:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("NEW")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #combinations += matchshipX(copy.deepcopy(ships), copy.deepcopy(battlefield), i)# + matchshipY(copy.deepcopy(ships), copy.deepcopy(battlefield), i)
        #combinations += matchshipY(copy.deepcopy(ships), copy.deepcopy(battlefield), i)
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