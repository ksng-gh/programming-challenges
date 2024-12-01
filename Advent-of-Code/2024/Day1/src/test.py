with open("input.txt", "r") as f:
    lines = f.readlines()

left = []
right = []
c = 0
for line in lines:
    t = line.strip().split(' ')
    print(t)
    left.append(t[0])
    right.append(t[3])

left.sort()
right.sort()

for i in range(0, len(left)):
    c += abs(int(right[i]) - int(left[i]))

print(len(left))

print(c)