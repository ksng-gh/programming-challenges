import sys

#n = length of side cake
#h = length of horizontal cut
#v = length of vertical cut

def Calc():
    n, h, v = input().split(' ')
    n = int(n)
    h = int(h)
    v = int(v)
    #Cave man method

    #piece 1
    p1 = v * h * 4
    p2 = (n - v) * h * 4
    p3 = v * (n - h) * 4
    p4 = (n - v) * (n - h) * 4

    print(max((max(p1, p2), max(p3, p4))))

Calc()