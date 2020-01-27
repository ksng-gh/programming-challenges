import sys

def Abc():
    lon = [int(x) for x in input().split()]
    order = input()
    lon = sorted(lon)

    counter = 0
    
    for x in order:
        if order[counter] == 'A':
            print(lon[0], end=' ')
        elif order[counter] == 'B':
            print(lon[1], end=' ')
        elif order[counter] == 'C':
            print(lon[2], end=' ')
        counter += 1

Abc()
