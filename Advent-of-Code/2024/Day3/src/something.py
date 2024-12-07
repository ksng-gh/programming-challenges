from re import findall

with open("input.txt", "r") as f:
    lines = f.readlines()

c = 0
enable = True
for line in lines:
    for f, s, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
        if do:
            enable = True
        elif dont:
            enable = False
        else:
            if enable:
                c += int(f) * int(s)

print(c)