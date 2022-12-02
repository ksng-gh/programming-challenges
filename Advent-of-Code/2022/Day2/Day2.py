with open("input.txt", "r") as f:
    lines = f.readlines()

#A, X
#B, Y 
#C, Z

#A = rock
#B = paper
#C = scizzor

#draw = 3
#win = 6

#p2:
#x = lose
#y = draw
#z = win

def checker(inp):
    if inp == 'A X':
        return 3 + 1
    if inp == 'A Y':
        return 6 + 2
    if inp == 'A Z':
        return 0 + 3
    if inp == 'B X':
        return 0 + 1
    if inp == 'B Y':
        return 3 + 2
    if inp == 'B Z':
        return 6 + 3
    if inp == 'C X':
        return 6 + 1
    if inp == 'C Y':
        return 0 + 2
    if inp == 'C Z':
        return 3 + 3

def checker2(a, b):
    if a == "A":
        if b == "X":
            return 3
        if b == "Y":
            return 3 + 1
        return 6 + 2
    
    if a == "B":
        if b == "Y":
            return 3 + 2
        if b == "Z":
            return 6 + 3
        return 1
    
    if a == "C":
        if b == "Z":
            return 6 + 1
        if b == "X":
            return 0 + 2
        return 3 + 3

score = 0

TASK = 1
if(TASK == 1):
    for line in lines:
        score += checker(line.strip())
    print(score)

else:
    for line in lines:
        op, out = line.split()
        score += checker2(op, out)
    print(score)