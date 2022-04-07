import sys

def Oddities():
    times = input()
    times = int(times)
    for x in range(0, times):
        inp = input()
        inp = int(inp)
        if inp % 2 == 0:
            print("{0} is even" .format(inp))
        else:
            print("{0} is odd" .format(inp))

Oddities()