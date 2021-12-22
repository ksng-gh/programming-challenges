with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

#with open("test2.txt", "r") as f:
#    lines = f.readlines()

octo = [[int(i) for i in line if i != "\n"] for line in lines]

flash = 0
all = len(octo) * len(octo[0])

def resetFlash(l):
    counter = 0
    for x, r in enumerate(l):
        for y, o in enumerate(r):
            if o > 9:
                l[x][y] = 0
                counter += 1
    return True if counter == all else False

def increaseAdjacent(l, x, y):
    if x - 1 >= 0:
        l[x - 1][y] += 1
        
    if x < len(l[x]) - 1:
        l[x + 1][y] += 1

    if y - 1 >= 0:
        l[x][y - 1] += 1

    if y < len(l[y]) - 1:
        l[x][y + 1] += 1

    if y - 1 >= 0 and x - 1 >= 0:
        l[x - 1][y - 1] += 1
    
    if y < len(l[y]) - 1 and x < len(l[x]) - 1:
        l[x + 1][y + 1] += 1

    if x - 1 >= 0 and y < len(l[y]) - 1:
        l[x - 1][y + 1] += 1
        
    if x < len(l[x]) - 1 and y - 1 >= 0:
        l[x + 1][y - 1] += 1

def getAdjacent(l, x, y):
    r = []
    if x - 1 >= 0:
        r.append((x - 1, y))
        
    if x < len(l[x]) - 1:
        r.append((x + 1, y))

    if y - 1 >= 0:
        r.append((x, y - 1))

    if y < len(l[y]) - 1:
        r.append((x, y + 1))

    if y - 1 >= 0 and x - 1 >= 0:
        r.append((x - 1, y - 1))
    
    if y < len(l[y]) - 1 and x < len(l[x]) - 1:
        r.append((x + 1, y + 1))

    if x - 1 >= 0 and y < len(l[y]) - 1:
        r.append((x - 1, y + 1))
        
    if x < len(l[x]) - 1 and y - 1 >= 0:
        r.append((x + 1, y - 1))
    
    return r

n = []
n2 = []
#Access the stupid list.

s = 0
finished = False
TASK = 2

if TASK == 1:
    STEPS = 100
    while s < STEPS:
        for x, line in enumerate(octo):
            for y, o in enumerate(line):
                octo[x][y] += 1
                if octo[x][y] > 9:
                    n.append((x, y))
                    flash += 1
        while not finished:
            for i in n:
                increaseAdjacent(octo, i[0], i[1])
                adj = getAdjacent(octo, i[0], i[1])
                for a in adj:
                    if octo[a[0]][a[1]] == 10:
                        n2.append(a)
                        flash += 1
            n = n2
            n2 = []
            if n == []:
                resetFlash(octo)
                finished = True
        finished = False
        s += 1
    print(flash)

        
if TASK == 2:
    while True:
        for x, line in enumerate(octo):
            for y, o in enumerate(line):
                octo[x][y] += 1
                if octo[x][y] > 9:
                    n.append((x, y))
                    flash += 1
        while not finished:
            for i in n:
                increaseAdjacent(octo, i[0], i[1])
                adj = getAdjacent(octo, i[0], i[1])
                for a in adj:
                    if octo[a[0]][a[1]] == 10:
                        n2.append(a)
                        flash += 1
            n = n2
            n2 = []
            if n == []:
                c = resetFlash(octo)
                finished = True
        finished = False
        s += 1

        if c == True:
            print(s)
            break
    
