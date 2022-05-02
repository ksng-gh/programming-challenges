import sys
import math

stars = int(input())

def cylindervolume(r, h):
    return math.pi * h * math.pow(r, 2)

def distance(v1, v2):
    x = (v1[0] - v2[0]) ** 2
    y = (v1[1] - v2[1]) ** 2
    z = (v1[2] - v2[2]) ** 2
    return math.sqrt(x + y + z)

def crossproduct(v1, v2):
    a = v1[1] * v2[2] - v1[2] * v2[1]
    b = -1 * (v1[0] * v2[2] - v1[2] * v2[0])
    c = v1[0] * v2[1] - v1[1] * v2[0]
    return (a, b, c)

def isInside(t, p, n):
    if distance(p, t[n][0]) < t[n][2] or distance(p, t[n][1]) < t[n][2]:
        return True
    else:
        return False

#Vector subtraction
def vectorsub(v1, v2):
    v = (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
    return v

#Vector addition
def vectoradd(v1, v2):
    v = (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
    return v

#Vector multiplication
def vectormul(a, v2):
    v = (a * v2[0], a * v2[1], a * v2[2])
    return v

#Vector division with value a
def vectordiv(a, v):
    v = (v[0] / a, v[1] / a, v[2] / a)
    return v

#Vector dotproduct
def vectorproduct(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def norm(v):
    n = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    return n

def normalize(v):
    normed = norm(v)
    n = (v[0] / normed, v[1] / normed, v[2] / normed)
    return n

#Checks if it's a zero vector
def isZero(v):
    if v[0] == 0 and v[1] == 0 and v[2] == 0:
        return True
    else:
        return False

#############################################################
#############################################################



starcoords = []
maxdistorig = 0
mindistpoints = [sys.maxsize, sys.maxsize]
dtoplane = 0
planebasepoints = [((0, 0, 0), False), ((0, 0, 0), False)]
maxdistperp = 0
maxdistoriglist = [0] * 2
maxdistperplist = [0] * 2
dispvectors = []
planepoints = []
zerov = False

#Extract coords
for i in range(stars):
    x, y, z = map(int, input().split(" "))
    starcoords.append((x, y, z))

#Get the max distance between 2 points.
for i in range(len(starcoords) - 1):
    for j in range(i + 1, len(starcoords)):
        d = distance(starcoords[i], starcoords[j])
        if d > maxdistorig:
            maxdistorig = d

            maxdistoriglist[0] = starcoords[i]
            maxdistoriglist[1] = starcoords[j]

#Make a plane from one of the points by getting the closest 2 points
for i in range(len(starcoords)):
    d = distance(starcoords[i], maxdistoriglist[0])
    if d < mindistpoints[0] and d != 0:
        if d < mindistpoints[1]:
            mindistpoints[1] = d
            planebasepoints[1] = starcoords[i]       
        else:
            mindistpoints[0] = d
            planebasepoints[0] = starcoords[i]



planenormal = normalize(crossproduct(vectorsub(planebasepoints[0], maxdistoriglist[]), vectorsub(planebasepoints[1], maxdistoriglist[0])))
        
#Find point furthest from the plane
#The biggest distance between 2 points in the beginning and point to plane can be different.
#Used to get the h in volumeformula
#ax + by + cz = d
a = planenormal[0]
b = planenormal[1]
c = planenormal[2]
x = maxdistoriglist[0][0]
y = maxdistoriglist[0][1]
z = maxdistoriglist[0][2]
d = (a * x + b * y + c * z)

for i in starcoords:
    dist = abs(a * i[0] + b * i[1] + c * i[2] - d) / math.sqrt(a ** 2 + b ** 2 + c ** 2)
    if dist > dtoplane:
        dtoplane = dist
        maxdistoriglist[1] = i

#Get point on plane closest to a given point for every point
for i in starcoords:
    dot = vectorproduct(planenormal, i)
    mwn = vectormul(dot, planenormal)
    p = vectorsub(i, mwn)
    planepoints.append(p)

planepoints = list(set(planepoints))
end = False
prev = []
rmax = 0

# Idea 1
#Make a circle from 3 points. Biggest circle -> all points in the circle. Use that radius to calc volume.
#i = p1, j = p2, k = p3
for i in range(len(planepoints) - 2):
    for j in range(i + 1, len(planepoints) - 1):
        for k in range(j + 1, len(planepoints)):

            if end:
                continue

            d21 = vectorsub(planepoints[j], planepoints[i])
            d31 = vectorsub(planepoints[k], planepoints[i])

            f2 = 1/2 * (d21[0] ** 2 + d21[1] ** 2 + d21[2] ** 2)
            f3 = 1/2 * (d31[0] ** 2 + d31[1] ** 2 + d31[2] ** 2)

            m23xy = d21[0] * d31[1] - d21[1] * d31[0]
            m23yz = d21[1] * d31[2] - d21[2] * d31[1]
            m23xz = d21[2] * d31[0] - d21[0] * d31[2]

            f23 = vectorsub(vectormul(f2, d31), vectormul(f3, d21))

            cx = planepoints[i][0] + (m23xy * f23[1] - m23xz * f23[2]) / (m23xy ** 2 + m23yz ** 2 + m23xz ** 2)
            cy = planepoints[i][1] + (m23yz * f23[2] - m23xy * f23[0]) / (m23xy ** 2 + m23yz ** 2 + m23xz ** 2)
            cz = planepoints[i][2] + (m23xz * f23[0] - m23yz * f23[1]) / (m23xy ** 2 + m23yz ** 2 + m23xz ** 2)

            cv = (cx, cy, cz)

            ri = norm(vectorsub(planepoints[i], cv))

            if ri > rmax:
                rmax = ri

#print(cylindervolume(rmax, dtoplane))

# Idea 2
#Get the largest difference that includes all other points, while decreasing the radius if possible
circledist = 0
distances = []
check = []
a = False

#Get distances between all projected points on the plane.
for i in range(len(planepoints) - 1):
    for j in range(1, len(planepoints)):
        d = distance(planepoints[i], planepoints[j])
        distances.append((planepoints[i], planepoints[j], d))

sortdistances = sorted(distances, key=lambda d: d[2])
sortdistances = sortdistances[::-1]

prev = []

#Gives the minimum distance to which all points are included.
for n in range(len(sortdistances)):
    if a:
        continue

    for i in planepoints:
        if isInside(sortdistances, i, n):
            check.append(True)
        else:
            check.append(False)
    
    if all(check) == False:
        a = True
        if n == 0:
            prev = sortdistances[0]
    else:
        prev = sortdistances[n]
    
circledist = prev[2]

print(cylindervolume(circledist/2, dtoplane))