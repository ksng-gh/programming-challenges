#Mistake: process and cycle not in correct order

with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

#with open("test2.txt", "r") as f:
#    lines = f.readlines()

TASK = 2

x = 1
cycle = 1
stack = []
total = 0
CRT1 = []
CRT2 = []
CRT3 = []
CRT4 = []
CRT5 = []
CRT6 = []

currentCRT = CRT1

def printcycle(cycle):
    global total
    match cycle:
        case 20:
            total += cycle * x
        case 60:
            total += cycle * x
        case 100:
            total += cycle * x
        case 140:
            total += cycle * x
        case 180:
            total += cycle * x
        case 220:
            total += cycle * x

def getCRT(cycle):
    global currentCRT
    match cycle:
        case 41:
            currentCRT = CRT2
        case 81:
            currentCRT = CRT3
        case 121:
            currentCRT = CRT4
        case 161:
            currentCRT = CRT5
        case 201:
            currentCRT = CRT6

def process():
    global x
    getCRT(cycle)

    if (cycle % 40) == x or (cycle % 40) == (x + 1) or (cycle % 40) == (x + 2):
        currentCRT.append("#")
    else:
        currentCRT.append(".")
    printcycle(cycle)
    if stack:
        stack[0] = (stack[0][0], stack[0][1] - 1)
        if stack[0][1] == 0:
            x += stack[0][0]
            stack.pop(0)

for line in lines:
    cmd = line.split()
    if len(cmd) == 2:
        stack.append((int(cmd[1]), 2))
    else:
        stack.append((0, 1))
    process()
    cycle += 1

while stack:
    process()
    cycle += 1

if TASK == 1:
    print(total)
else:
    print(CRT1)
    print(CRT2)
    print(CRT3)
    print(CRT4)
    print(CRT5)
    print(CRT6)