import sys


def Cetvrta():

    a, b = input().split(' ')
    c, d = input().split(' ')
    e, f = input().split(' ')

    x = [a, c, e]
    y = [b, d, f]

    for i in x:
        if a == e:
            retx = c
        elif a == c:
            retx = e
        else:
            retx = a
    for i in y:
        if b == d:
            rety = f
        elif b == f:
            rety = d
        else:
            rety = b

    print("{} {}" .format(retx, rety))


Cetvrta()
