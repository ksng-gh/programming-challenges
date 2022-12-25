import re
#with open("input.txt", "r") as f:
#    lines = f.readlines()

with open("test.txt", "r") as f:
    lines = f.readlines()

a = ["a", "b"]
print(a.items())

scanned = set()

"""
def scan(x, y, bx, by):
    dist = 0
    scanned.add((x, y))
    
    while (bx, by) not in scanned:
        #right
        for r in range(dist + 1):
            scanned.add((x + r, y))
            if r == dist:
                right = (x + r, y)
        #down
        for d in range(dist + 1):
            scanned.add((x, y + d))
            if d == dist:
                down = (x, y + d)
        #up
        for u in range(dist + 1):
            scanned.add((x, y - u))
            if u == dist:
                up = (x, y - u)
        #left
        for l in range(dist + 1):
            scanned.add((x - l, y))
            if l == dist:
                left = (x - l, y)
        #print(x)
        #Go clockwise

        for inv in range(dist):
            #print(right)
            #print(down)
            #print(up)
            #print(left)
            scanned.add((right[0] - inv, right[1] + inv)) # -, +
            scanned.add((down[0] - inv, down[1] - inv)) # -, -
            scanned.add((up[0] + inv, up[1] + inv)) # +, +
            scanned.add((left[0] + inv, left[1] - inv)) # +, -

        dist += 1
"""

def scan(x, y, bx, by):
    dist = 0
    


#print(teest)
for line in lines:
    d = re.findall(r'\d+', line)
    sx, sy, bx, by = map(int, d)
    #print((bx, by))
    #scan(0, 0, 10, 10)
    scan(sx, sy, bx, by)

c = 0
c1 = 0
for i in scanned:
    if i[1] == 10:
        c1 += 1 
    if i[1] == 20000:
        c += 1

print(scanned)
#print(c)
print(c1)
