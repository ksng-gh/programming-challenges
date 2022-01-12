with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

if TASK == 1:
    for i, idx in enumerate(lines[:-1]):
        for j, jdx in enumerate(lines, i):
            if int(idx) + int(jdx) == 2020:
                print(int(idx) * int(jdx))
                break

if TASK == 2:
    for i, idx in enumerate(lines[:-1]):
        for j, jdx in enumerate(lines, i):
            for k, kdx in enumerate(lines, j):
                if int(idx) + int(jdx) + int(kdx)== 2020:
                    print(int(idx) * int(jdx) * int(kdx)) 
                    break