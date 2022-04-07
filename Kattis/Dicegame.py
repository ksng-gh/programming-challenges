import sys

def Dicegame():
    c1, c2, c3, c4 = input().split(' ')
    d1, d2, d3, d4 = input().split(' ')

    c1 = int(c1)
    c2 = int(c2)
    c3 = int(c3)
    c4 = int(c4)
    d1 = int(d1)
    d2 = int(d2)
    d3 = int(d3)
    d4 = int(d4)

    cTot = c1 + c2 + c3 + c4
    dTot = d1 + d2 + d3 + d4

    if cTot == dTot:
        print("Tie")
    elif cTot > dTot:
        print("Gunnar")
    else:
        print("Emma")

Dicegame()    