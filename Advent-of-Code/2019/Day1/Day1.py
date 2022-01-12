with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

sum = 0
if TASK == 1:
    for i in lines:
        v = int(i)
        sum += (v // 3) - 2

if TASK == 2:
    for i in lines:
        v = int(i)
        while v > 0:
            v = (v // 3) - 2
            if v > 0:
                sum += v
        
print(sum)