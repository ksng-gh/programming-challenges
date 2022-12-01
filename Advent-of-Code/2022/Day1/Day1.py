with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

if(TASK == 1):

    loc = []
    calories = 0
    for line in lines:
        if line in ['\n', '\r\n']:
            loc.append(calories)
            calories = 0
            continue
        calories += int(line)
    print(max(loc))

if(TASK == 2):
    loc = []
    calories = 0
    for line in lines:
        if line in ['\n', '\r\n']:
            loc.append(calories)
            calories = 0
            continue
        calories += int(line)
    
    one = max(loc)
    loc.remove(one)
    two = max(loc)
    loc.remove(two)
    three = max(loc)
    print(one + two + three)