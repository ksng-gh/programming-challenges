import sys

dom = {
        "A":11,
        "K":4,
        "Q":3,
        "J":20,
        "T":10,
        "9":14,
        "8":0,
        "7":0,
    }

nondom = {
    
        "A":11,
        "K":4,
        "Q":3,
        "J":2,
        "T":10,
        "9":0,
        "8":0,
        "7":0,
    }

def Func():
    h, d = input().split(' ')
    h = int(h) * 4
    p = 0
    i = 0
    while i < h:
        txt = list(input())
        if txt[1] == d:
            for j in dom:
                if j == txt[0]:
                    p = p + dom[j]
        else:
            for j in nondom:
                if j == txt[0]:
                    p = p + nondom[j]
        i = i + 1

    print(str(p))

Func()