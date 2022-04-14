import sys
import math

stars = int(input())

starcoords = []

def cylindervolume(r, h):
    return math.pi * h * math.pow(r, 2)

lx = sys.maxsize
ly = sys.maxsize
lz = sys.maxsize

hx = -sys.maxsize - 1
hy = -sys.maxsize - 1
hz = -sys.maxsize - 1

for i in range(stars):
    x, y, z = input().split(" ")
    lx = min(int(x), lx)
    ly = min(int(y), ly)
    lz = min(int(z), lz)

    hx = max(int(x), hx)
    hy = max(int(y), hy)
    hz = max(int(z), hz)
    starcoords.append((int(x), int(y), int(z)))

    h = max(hx, (max(hy, hz))) - min(lx, (min(ly, lz)))
    r = max(hx, (max(hy, hz))) - min(lx, (min(ly, lz)))

print(cylindervolume(r, h))