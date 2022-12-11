#Cr

with open("input.txt", "r") as f:
    lines = f.readlines()

TASK = 2

def stackup():
    sizes.append(stack.pop(-1))
    if stack:
        stack[-1] += sizes[-1]

stack = []
sizes = []
for line in lines:
    line = line.strip()
    if line == "$ cd ..":
        stackup()
    elif line.startswith("$ cd "):
        stack.append(0)
    else:
        size = line.split()[0]
        if size.isdigit():
            stack[-1] += int(size)

while stack:
    stackup()

if TASK == 1:
    print(sum(i for i in sizes if i <= 100000))
else:
    print(min(i for i in sizes if (70000000 - max(sizes) + i) > 30000000))
