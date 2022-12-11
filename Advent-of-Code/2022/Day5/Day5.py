import re

#s1 = ['W', 'R', 'F']
#s2 = ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P']
#s3 = ['P', 'M', 'Z', 'N', 'L']
#s4 = ['J', 'C', 'H', 'R']
#s5 = ['C', 'P', 'G', 'H', 'Q', 'T', 'B']
#s6 = ['G', 'C', 'W', 'L', 'F', 'Z']
#s7 = ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C']
#s8 = ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C']
#s9 = ['J', 'W', 'H', 'G', 'R', 'S', 'V']

s = [[], ['W', 'R', 'F'], ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'], ['P', 'M', 'Z', 'N', 'L'], ['J', 'C', 'H', 'R'], ['C', 'P', 'G', 'H', 'Q', 'T', 'B'], ['G', 'C', 'W', 'L', 'F', 'Z'], ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'], ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'], ['J', 'W', 'H', 'G', 'R', 'S', 'V']]

with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

def moveCrate(amount, stackFrom, stackTo):
    if TASK == 1:
        for i in range(amount):
            s[stackTo].append(s[stackFrom].pop())
    else:
        amount = amount * -1
        s[stackTo] += s[stackFrom][amount:]
        del s[stackFrom][amount:]

for line in lines:
    ins = list(map(int, re.findall(r'\d+', line)))
    moveCrate(ins[0], ins[1], ins[2])
for i in range(1, 10):
    print(s[i][-1], end="")
