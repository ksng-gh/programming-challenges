with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2
if TASK == 1:

    overlaps = 0
    for line in lines:
        a, b = line.split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        if a1 - b1 >= 0 and a2 - b2 <= 0:
            overlaps += 1
        elif a1 - b1 <= 0 and a2 - b2 >= 0:
            overlaps += 1
    print(overlaps)

else:
    overlaps = 0
    for line in lines:
        a, b = line.split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        l = [i for i in range(a1, a2 + 1)]
        for i in range(b1, b2 + 1):
            if i in l:
                overlaps += 1
                break     
    print(overlaps)