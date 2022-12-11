with open("input.txt", "r") as f:
    lines = f.readlines()

occurrance = 0
occurance2 = 0
TASK = 2
occ = []
for line in lines:
    line = line.replace("-", " ")
    line = line.replace(":", "")
    d = line.strip().split()

    if TASK == 1:

        counter = 0
        for i in d[3]:
            if i == d[2]:
                counter += 1
        if counter >= int(d[0]) and counter <= int(d[1]):
            occurrance += 1

    if TASK == 2:
        for idx, i in enumerate(d[3]):
            if i == d[2]:
                if (idx + 1) == int(d[0]) and (idx + 1) != int(d[1]):
                        occ.append(i)
                elif (idx + 1) == int(d[1]) and (idx + 1) != int(d[0]):
                        occ.append(i)
        if len(occ) > 0:
            if occ.count(occ[0]) == 1:
                occurance2 += 1
    occ = []
print(occurrance)
print(occurance2)