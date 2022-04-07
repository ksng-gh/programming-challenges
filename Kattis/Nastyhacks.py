import sys

#1 Rev no ads
#2 Rev with ads
#3 Cost of ads

def Nastyhacks():
    n = input()
    n = int(n)
    for x in range(0, n):
        r, e, c = input().split(' ')
        r = int(r)
        e = int(e)
        c = int(c)
        
        costOfAd = e - c

        if costOfAd > r:
           print("advertise")
        elif costOfAd == r:
           print("does not matter")
        elif costOfAd < r:
           print("do not advertise")
Nastyhacks()