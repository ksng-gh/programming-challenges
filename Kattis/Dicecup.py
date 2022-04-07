import sys

def Calc():
    d1, d2 = input().split(' ')
    d1 = int(d1)
    d2 = int(d2)

    for i in range(min(d1 + 1, d2 + 1), max(d1 + 2, d2 + 2)):
        print(i)

Calc()