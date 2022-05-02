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
    #print((a, b, c))
    return (a, b, c)

def isInside(t, p, n):
    if distance(p, t[n][0]) < t[n][2] or distance(p, t[n][1]) < t[n][2]:
        return True
    else:
        return False

def trianglearea(b, h):
    return norm(b) * norm(h) / 2

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
    starcoords.append((int(x), int(y), int(z)))

print(starcoords)

#starcoords = [(0, 0, 0), (1, 1, 1)]

#Get the max distance between 2 points.
for i in range(len(starcoords) - 1):
    for j in range(i + 1, len(starcoords)):
        d = distance(starcoords[i], starcoords[j])
        if d > maxdistorig:
            maxdistorig = d
            if not isZero(starcoords[i]):
                maxdistoriglist[0] = starcoords[i]
                maxdistoriglist[1] = starcoords[j]
            else:
                zerov = True
                maxdistoriglist[1] = starcoords[i]
                maxdistoriglist[0] = starcoords[j]

#Check base plane points

#Make a plane from one of the points by getting the closest 2 points
for i in range(len(starcoords)):
    d = distance(starcoords[i], maxdistoriglist[0])
    if d < mindistpoints[0] and d != 0:
        if d < mindistpoints[1]:
            mindistpoints[1] = d
            planebasepoints[1] = starcoords[i]       
        #elif d > mindistpoints[1]:
        else:
            mindistpoints[0] = d
            planebasepoints[0] = starcoords[i]

#print("planebase")
#print(planebasepoints)
#print("maxdistorig")
#print(maxdistoriglist)
planenormal = normalize(crossproduct(vectorsub(planebasepoints[0], maxdistoriglist[0]), vectorsub(planebasepoints[1], maxdistoriglist[0])))
print("points for plane:")
print(planebasepoints[0])
print(planebasepoints[1])
print(maxdistoriglist[0])

print("planenormal")
print(planenormal)
        
#Find point furthest from the plane
#The biggest distance between 2 points and point to plane can be different.
#Used to get the h in volumeformula
a = planenormal[0]
b = planenormal[1]
c = planenormal[2]
x = maxdistoriglist[0][0]
y = maxdistoriglist[0][1]
z = maxdistoriglist[0][2]
d = (a * x + b * y + c * z)

for i in range(len(starcoords)):
    dist = abs(a * starcoords[i][0] + b * starcoords[i][1] + c * starcoords[i][2] - d) / math.sqrt(a ** 2 + b ** 2 + c ** 2)
    #print(dist)
    if dist > dtoplane:
        dtoplane = dist
        #if not zerov:
        maxdistoriglist[1] = starcoords[i]
        #else:
        #    maxdistoriglist[1] = starcoords[i]



print("furthest point")
print(maxdistoriglist[1])
print("d")
print(d)


#Get point on plane closest to a given point for every point

for i in starcoords:
    dot = vectorproduct(planenormal, i)
    mwn = vectormul(dot, planenormal)
    p = vectorsub(i, mwn)
    planepoints.append(p)

"""
pinp = []
for p in starcoords:
    #print((d - p[0] - p[1] - p[2]))
    #print((a + b + c))
    t = (d - p[0] * a - p[1] * b - p[2] * c) / (a ** 2 + b ** 2 + c ** 2)
    #print(t)
    nv = (a * t + p[0], b * t + p[1], c * t + p[2])
    pinp.append(nv)
"""

print("planepoints")
print(planepoints) #Has all points projected onto the plane
"""
print("pinpnew")
print(pinp)
"""

planepoints = list(set(planepoints))
tp = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
rvec = (0, 0, 0)
end = False
prev = []
info = []
rmax = 0


#print(forcircle)

#Make a circle from 3 points, get center, then check radius. If all points within radius, we gucci.
#Make a circle from 3 points. Biggest circle -> all points in the circle. Use that radius to calc volume.
#https://math.stackexchange.com/questions/1076177/3d-coordinates-of-circle-center-given-three-point-on-the-circle
#i = p1, j = p2, k = p3
for i in range(len(planepoints) - 2):
    for j in range(i + 1, len(planepoints) - 1):
        for k in range(j + 1, len(planepoints)):
            #pn1 = normalize(vectorsub(forcircle[k], forcircle[i]))
            #pn2 = normalize(vectorsub(forcircle[j], forcircle[i]))
            #pn3 = crossproduct(pn1, pn2)
            #ca = norm(vectorsub(forcircle[i], forcircle[k]))
            #ab = norm(vectorsub(forcircle[j], forcircle[i]))
            #bc = norm(vectorsub(forcircle[k], forcircle[j]))

            
            #print(pn1)
            #print(pn2)
            #print(pn3)

            

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
            rj = norm(vectorsub(planepoints[j], cv))
            rk = norm(vectorsub(planepoints[k], cv))
            print(ri)
            print(rj)
            print(rk)
            info.append((cv, ri))

            #if r > rmax:
            #    rmax = r
            #    rvec = cv
            #    tp[0] = planepoints[i]
            #    tp[1] = planepoints[j]
            #    tp[2] = planepoints[k]
checker = []
pr = 0
sortinfo = sorted(info, key=lambda d: d[1])
sortinfo = sortinfo[::-1]
for i in range(len(sortinfo)):
    if end:
        continue
    for j in planepoints:
        if distance(info[i][0], j) < info[i][1]:
            checker.append(True)
        else:
            checker.append(False)
    
    if all(checker) == False:
        end = True
        if i == 0:
            pr = sortinfo[0][1]
    else:
        pr = sortinfo[i][1]

print("pr")
print(pr)
#print("sortinfo")
#print(sortinfo)
print("sortinfo length")
print(len(sortinfo))


print("info")
print(info)
print("tp")
print(tp)
print("rmax") 
print(rmax)
print("rvec")
print(rvec)
#print(cv)
print("d to plane")
print(dtoplane)
#202428.85386984056
print("FINALLY??!??!!")
print(cylindervolume(pr, dtoplane))
#Get the largest difference that includes all other points, while decreasing the radius if possible
circledist = 0
center = (0, 0, 0)
bigdiff = [0] * 2
distances = []
checkl = []
check2 = []
a = False

for i in range(len(planepoints) - 1):
    for j in range(1, len(planepoints)):
        d = distance(planepoints[i], planepoints[j])
        distances.append((planepoints[i], planepoints[j], d))

#print(distances)
sortdistances = sorted(distances, key=lambda d: d[2])
sortdistances = sortdistances[::-1]

prev = []
print("sort dista")
print(sortdistances)
#print(len(sortdistances))
#print(sortdistances[0])

for n in range(len(sortdistances)):
    if a:
        continue

    for i in planepoints:
        if isInside(sortdistances, i, n):
            check2.append(True)
        else:
            check2.append(False)
    
    if all(check2) == False:
        a = True
        if n == 0:
            prev = sortdistances[0]
    else:
        prev = sortdistances[n]
    
#print(prev)
circledist = prev[2]
print("circledist")
print(circledist)
#print("dtoplane")
#print(dtoplane)

print(cylindervolume(circledist/2, dtoplane))
#print(math.pi * ((circledist ** 2) / 4) * dtoplane)
"""
vs = vectorsub(maxdistoriglist[0], maxdistoriglist[1])

#Get perpendicular displacement vectors
for i in starcoords:
    #dia = 1.7320508075688772
    #vol = 4.081048569526989
    #c = crossproduct(vs, vectorsub(i, maxdistoriglist[1]))
    #n = norm(vs)
    #nv = (c[0] / n, c[1] / n, c[2] / n)
    #dispvectors.append(nv)

    v = vectorproduct(i, vs) / vectorproduct(vs, vs)
    projv = (v * vs[0], v * vs[1], v * vs[2])
    dispvectors.append(vectoradd(vs, projv))

#print(dispvectors)

#Get max dist for the displacement vectors
for i in range(len(dispvectors)):
    for j in range(1, len(dispvectors)):
        d = distance(dispvectors[i], dispvectors[j])
        if d > maxdistperp:
            maxdistperp = d
            #maxdistperplist[0] = starcoords[i]
            #maxdistperplist[1] = starcoords[j]
            
            maxdistperplist[0] = dispvectors[i]
            maxdistperplist[1] = dispvectors[j]
            
#print(maxdistperplist)
#print(maxdistoriglist)

diameter = norm(vectorsub(maxdistperplist[0], maxdistperplist[1]))

    #dia = 1.7320508075688772
    #vol = 4.081048569526989

#print(diameter)

#print(math.pi * ((diameter ** 2) / 4) * distance(maxdistoriglist[0], maxdistoriglist[1]))
#print(cylindervolume(diameter/2, norm(vectorsub(maxdistoriglist[0], maxdistoriglist[1]))))

#print(checkplanar(crossproduct((1, 0, 0), (0, 0, 1)), (0, 0, 0), (1, 1, 1)))
#print(checkplanar(crossproduct((1, 1, -1), (1, 1, 1)), (1, 1, 2), (1, 1, 7)))
#print(cylindervolume(r, h))
"""