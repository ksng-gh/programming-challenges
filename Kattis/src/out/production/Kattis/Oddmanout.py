import sys


def Oddmanout():
    testcases = input()
    testcases = int(testcases)

    counter = 0
    unique = []

    for x in range(0, testcases):
        noneed = input()

        args = input().split(' ')

        for z in args:
            if z not in unique:
                unique.append(z)
            elif z in unique:
                unique.remove(z)
            
        print("Case #{}: {}".format(counter + 1, unique[0]))
        unique.clear()
        counter += 1
    

Oddmanout()
