import sys

with open("day7.txt", "r") as f:
   line = f.readline()

#with open("test.txt", "r") as f:
#   line = f.readline()

crabs = line.strip().split(",")
crabs = [int(i) for i in crabs]

TASK = 2

least = sys.maxsize
totalfuel = 0
startposition = 0
maxposition = max(crabs)

def sumall(start, end):
    sum = 0
    h = max(end, start)
    l = min(end, start)
    for i in range(0, h - l + 1):
        sum = sum + i
    return sum

#Slow, but works!
while startposition < maxposition:
    for i in crabs:
        if TASK == 1:
            totalfuel += abs(i - startposition)
        else:
            totalfuel += sumall(startposition, i)
    least = totalfuel if totalfuel < least else least
    totalfuel = 0
    startposition += 1


print(least)