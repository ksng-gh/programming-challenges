#Made earlier code that actually worked, became desperate when it didnt work,
#so I made this one, getting help with https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
#Turns out, I get the same result. It's a "bug", which basically means that 'E' -> 26 instead of 27
from queue import PriorityQueue
import math

TASK = 2

with open("input.txt", "r") as f:
    lines = f.readlines()

m = [list(line.strip().split()[0]) for line in lines]

allA = []

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x].islower():
            if(ord(m[y][x]) - 96 == 1):
                allA.append((x, y))
            m[y][x] = (ord(m[y][x]) - 96, (x, y))
        
        if m[y][x] == "S":
            start = (x, y)
            if TASK == 1:
                m[y][x] = (0, start)
            else:
                m[y][x] = (1, start)

        elif m[y][x] == "E":

            end = (x, y)
            m[y][x] = (26, end)

def getNeighbours(x, y):
    neighbours = []
    if x < len(m[0]) - 1:
        if ((m[y][x][0] + 1) >= m[y][x + 1][0]):
            neighbours.append(m[y][x + 1][1])
    if x > 0:
        if ((m[y][x][0] + 1) >= m[y][x - 1][0]):
            neighbours.append(m[y][x - 1][1])
    if y < len(m) - 1:
        if ((m[y][x][0] + 1) >= m[y + 1][x][0]):
            neighbours.append(m[y + 1][x][1])
    if y > 0:
        if ((m[y][x][0] + 1) >= m[y - 1][x][0]):
            neighbours.append(m[y - 1][x][1])
    return (x, y), neighbours

neighbour = {getNeighbours(x, y)[0]:getNeighbours(x, y)[1] for y in range(len(m)) for x in range(len(m[0]))}


def dijkstra(x, y):
    visited = []
    D = {}
    if TASK == 1:
        for i in range(len(m[0])):
            for j in range(len(m)):
                D[(i, j)] = math.inf
                if (i, j) == start:
                    D[(i, j)] = 0
    else:
        for i in range(len(m[0])):
            for j in range(len(m)):
                D[(i, j)] = math.inf
                if (i, j) == (x, y):
                    D[(i, j)] = 0
    queue = PriorityQueue()
    if TASK == 1:
        
        queue.put((0, start))
    else:
        queue.put((0, (x, y)))
    while not queue.empty():
        (dist, current) = queue.get()
        visited.append(current)

        nb = neighbour[current]
        for n in nb:
            if n not in visited:
                old_dist = D[n]
                new_dist = D[current] + 1
                if new_dist < old_dist:
                    queue.put((new_dist, n))
                    D[n] = new_dist
    return D


if TASK == 1:

    x, y = (start)
    res = dijkstra(x, y)
    print(res[end])
else:
    #This shitty solution (using Dijkstra from every a to E is veeeeeery slow, but lazy.
    #Better way is prob trying to filter all impossible A first before conducting Dijkstra for every A.
    #Alternatively start from end.
    allDist = []
    for i in allA:
        allDist.append(dijkstra(i[0], i[1])[end])
    print(min(allDist))
