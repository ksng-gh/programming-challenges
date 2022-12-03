with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

duplicates = []
score = 0
if TASK == 1:
    for line in lines:
        stripline = line.strip()
        halfway = int(len(stripline) / 2)
        for i in range(halfway):
            if stripline[i] in stripline[halfway:len(stripline)]:
                duplicates.append(stripline[i])
                break
    for i in duplicates:
        score += (ord(i) - 64) + 26 if i.isupper() else (ord(i) - 96)
    print(score)
else:
    for line in lines:
        duplicates.append(line.strip())
        if len(duplicates) == 3:
            for i in duplicates[0]:
                if i in duplicates[1] and i in duplicates[2]:
                    score += (ord(i) - 64) + 26 if i.isupper() else (ord(i) - 96)
                    break
            duplicates = []
    print(score)