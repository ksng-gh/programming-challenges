import sys

def Nodup():
    lon = input().split(' ')
    unique = []

    for x in lon:
        if x not in unique:
            unique.append(x)
    
    if len(unique) == len(lon):
        print("yes")
    else:
        print("no")

Nodup()