import re
def surfacearea(list):
    list.sort()
    a = 2 * list[0] * list[1]
    b = 2 * list[1] * list[2]
    c = 2 * list[0] * list[2]
    return a + b + c + list[0] * list[1]

def ribbonlength(list):
    list.sort()
    return 2 * list[0] + 2 * list[1] + list[0] * list[1] * list[2]

with open("day2.txt", "r") as f:
    lines = f.readlines()

total = 0

TASK = 2

#test1 = [2, 3, 4]
#test2 = [1, 1, 10]

if TASK == 1:

    for line in lines:
        values = [int(v) for v in line.split('x')]
        total += surfacearea(values)

if TASK == 2:
    for line in lines:
        values = [int(v) for v in line.split('x')]
        total += ribbonlength(values)

print(total)






