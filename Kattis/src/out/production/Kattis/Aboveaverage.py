import sys

def Aboveaverage():
    testcases = int(input())
    c = 0

    while testcases > 0:
        lon = input().split(' ')
        lon = [int(x) for x in lon]
        lon.remove(lon[0])
        average = sum(lon[:])/len(lon)

        lon = sorted(lon)
        nonf = int(average)

        for x in lon:
            if x > nonf:
                c += 1

        print("{:,.3f}%".format(100 * c/len(lon)))

        c = 0
        testcases -= 1

Aboveaverage()
