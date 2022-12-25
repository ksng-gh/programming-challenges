#CR for improvement

with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2
sand = 0
rocks = set()
coords = []

#max y
abyss = 0

def fallingsand():
    global sand
    x = 500
    y = 0
    while True:
        if (x, y) in rocks:
            (x, y) = (500, 0)
        if (x, y + 1) not in rocks and y < abyss:
            y += 1
        elif (x - 1, y + 1) not in rocks and y < abyss:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in rocks and y < abyss:
            x += 1
            y += 1
        else:
            sand += 1
            rocks.add((x, y))
        if y >= abyss:
            break

def fallingsand2():
    global sand
    x = 500
    y = 0
    while True:
        if (x, y) in rocks:
            (x, y) = (500, 0)
        if (x, y + 1) not in rocks and y < abyss + 1:
            y += 1
        elif (x - 1, y + 1) not in rocks and y < abyss + 1:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in rocks and y < abyss + 1:
            x += 1
            y += 1
        else:
            sand += 1
            rocks.add((x, y))
        if (x, y) == (500, 0):
            break  

def fixrock(x1, y1, x2, y2):
    global abyss
    abyss = max(max(abyss, y1), y2)
    
    if x1 < x2:
        for x in range(x1, x2 + 1):
            rocks.add((x, y1))
    else:
        for x in range(x1, x2 - 1, -1):
            rocks.add((x, y1))
    if y1 < y2:
        for y in range(y1, y2 + 1):
            rocks.add((x1, y))
    else:
        for y in range(y1, y2 - 1, -1):
            rocks.add((x1, y))
    
for line in lines:
    data = line.strip().split()
    for i in data:
        if i == '->':
            continue
        coords.append(i)
    for i in range(len(coords) - 1):
        x1, y1 = map(int, coords[i].split(','))
        x2, y2 = map(int, coords[i + 1].split(','))
        fixrock(x1, y1, x2, y2)
    coords = []
if TASK == 1:
    fallingsand()
else:
    fallingsand2()
print(sand)