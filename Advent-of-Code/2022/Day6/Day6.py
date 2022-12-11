with open("input.txt", "r") as f:
    lines = f.readlines()

lines = lines[0].strip()

TASK = 2

if TASK == 1:
    for i in range(3, len(lines)):
        s = lines[i-4:i]
        if len(set(s)) == 4:
            print(i)
            break
else:
    for i in range(13, len(lines)):
        s = lines[i-14:i]
        if len(set(s)) == 14:
            print(i)
            break