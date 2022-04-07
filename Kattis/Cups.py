import sys

def Cups():
    times = int(input())
    nr = []
    clr = []

    for x in range(0, times):
        one, two = input().split(' ')

        if one.isdigit():
            one = int(one)/2
                    
            nr.append(int(one))
            clr.append(two)

        else:
                    
            nr.append(int(two))
            clr.append(one)

    while times > 0:
        ind = nr.index(min(nr))
        
        print(clr[ind])
        nr.remove(nr[ind])
        clr.remove(clr[ind])

        times -= 1

Cups()