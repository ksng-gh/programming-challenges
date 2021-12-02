with open("day2.txt", "r") as f:
    lines = f.readlines()

depth = 0
aim = 0
forward = 0
#lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

TASK = 2

if TASK == 1: 

    for line in lines:
        content = line.split(" ", 1)
        if content[0] == "forward":
            forward += int(content[1])
        if content[0] == "down":
            depth += int(content[1])
        if content[0] == "up":
            depth -= int(content[1])

if TASK == 2:

    for line in lines:
        content = line.split(" ", 1)
        if content[0] == "down":
            aim += int(content[1])
        if content[0] == "up":
            aim -= int(content[1])
        if content[0] == "forward":
            value = int(content[1])
            depth += value * aim
            forward += value
    
print(depth * forward)