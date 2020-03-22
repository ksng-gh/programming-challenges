import sys

#n = length of side cake
#h = length of horizontal cut
#v = length of vertical cut

def Calc():
    n, h, v = input().split(' ')
    n = int(n)
    h = int(h)
    v = int(v)
    #big cake
    areabig = n * n

    #area of mid and small cake
    if(n - v) > n/2:
        if(n - h) > n/2:
            s = v * h
            m = 2 * h * (n - v)
        else:
            s = v * (n - h)
            m = h * v + ((n - h) * (n - v))
    else:
        if(n - h) > n/2:
            s = (n - v) * h
            m = h * v + ((n - v) * (n - h))
        else:
            s = (n - v) * (n - h)
            m = 2 * (n - h) * v

    res = (areabig - s - m) * 4
    print(res)

Calc()




