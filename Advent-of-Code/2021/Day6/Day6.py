with open("day6.txt", "r") as f:
   line = f.readline()

#with open("test.txt", "r") as f:
#   line = f.readline()

def movefish(l):
    newFish = l[0]
    for i in range(0, len(l) - 1):
        l[i] = l[i + 1]
    l[8] = 0
    l[8] += newFish
    l[6] += newFish
    return(l)

TASK = 2
DUMB = 1

if TASK == 1:
    SIMULATION_DAYS = 80
elif TASK == 2:
    SIMULATION_DAYS = 256

lanternfish = line.strip().split(",")
lanternfish = [int(i) for i in lanternfish]

days = 0
#Dumb approach, since it's gonna take forever with 256 days
#Worked well in the first one tho
if DUMB == 1:
    while days < SIMULATION_DAYS:
        for idx, i in enumerate(lanternfish):
            lanternfish[idx] = lanternfish[idx] - 1
            if lanternfish[idx] < 0:
                lanternfish.append(int(9))
                lanternfish[idx] = lanternfish[idx] + 7
        days += 1

lf = [0] * 9

for i in lanternfish:
    lf[i] += 1

#New solution
while days < SIMULATION_DAYS:
    movefish(lf)
    days += 1

print(sum(lf))
#print(len(lanternfish))