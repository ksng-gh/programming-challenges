import math
import sys

#Get input
cases = int(input())

#Calculates dist between 2 islands
def distance(c0, c1):
    return math.sqrt(math.pow(c0[0] - c1[0], 2) + math.pow(c0[1] - c1[1], 2))

while cases > 0:
    islands = int(input())
    
    #Hold all distances
    distances = [[0] * islands for r in range(islands)]

    coords = []

    #Process the islands (The coordinates)
    for i in range(islands):
        a, b = input().split(' ')
        coord = (float(a), float(b))
        coords.append(coord)

    #Fill the distance 2D array
    for i in range(islands):
        for j in range(islands):
            distances[i][j] = distance(coords[i], coords[j])

    lowest = distances[0]
    visited = [False] * islands
    visited[0] = True
    count = 0
    cost = 0.0

    #While we don't have all the islands yet...
    while count < islands - 1:
        lowestpos = -1
        mindist = sys.maxsize

        #Get the lowest cost island and non-visited
        for i in range(islands):
            if visited[i] == False and mindist > lowest[i]:
                mindist = lowest[i]
                lowestpos = i

        #Replace all lowest cost island distances with new lowest of the new island distance (MST-esque)
        for i in range(islands):
            lowest[i] = min(lowest[i], distances[lowestpos][i])

        #Add cost
        cost += mindist
        #Set the island as visited
        visited[lowestpos] = True

        count += 1

    cases -= 1

    print(cost)