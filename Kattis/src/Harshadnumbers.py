import sys

def Harshadnumbers():
    lon = int(input())

    while True:
        if Checkharshad(str(lon)):
            print(lon)
            return
        else:
            lon += 1

def Checkharshad(numb):
    n = int(numb)
    ntot = 0

    for x in numb:
        ntot += int(x)
    
    if n % ntot == 0:
        return True
    else:
        return False

Harshadnumbers()