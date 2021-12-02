with open("day1.txt", "r") as f:
    lines = f.readline()

floor = 0
position = 0

#lines = ")"
#lines = "()())"

TASK = 2

if TASK == 1:
    for i in lines:
        if i == "(":
            floor += 1
        else:
            floor -= 1

    print(floor)

if TASK == 2:
    for i in lines:
        if i == "(":
            floor += 1
        else:
            floor -= 1
        
        position += 1

        if floor == -1:
            break

    print(position)
