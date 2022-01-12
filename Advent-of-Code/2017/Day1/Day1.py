with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

TASK = 2
sum = 0
t = lines[0].strip()
#t = "1111"
#t = "1234"
#t = "91212129"

if TASK == 1:

    for i, idx in enumerate(t[:-1]):
        if t[i] == t[i + 1]:
            sum += int(t[i])

    if t[-1] == t[0]:
        print(t[0])
        sum += int(t[0])

if TASK == 2:
    half = len(t) // 2
    for i, idx in enumerate(t[:half]):
        if t[i] == t[(len(t) // 2) + i]:
            sum += int(t[i])
    sum *= 2

print(sum)