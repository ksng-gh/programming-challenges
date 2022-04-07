import sys


def Tri():
    lon = [int(x) for x in input().split()]

    if lon[0] + lon[1] == lon[2]:
        print("{}+{}={}".format(lon[0], lon[1], lon[2]))
    elif lon[0] - lon[1] == lon[2]:
        print("{}-{}={}".format(lon[0], lon[1], lon[2]))
    elif lon[0] * lon[1] == lon[2]:
        print("{}*{}={}".format(lon[0], lon[1], lon[2]))
    elif lon[0] / lon[1] == lon[2]:
        print("{}/{}={}".format(lon[0], lon[1], lon[2]))

    elif lon[1] + lon[2] == lon[0]:
        print("{}={}+{}".format(lon[0], lon[1], lon[2]))
    elif lon[1] - lon[2] == lon[0]:
        print("{}={}-{}".format(lon[0], lon[1], lon[2]))
    elif lon[1] * lon[2] == lon[0]:
        print("{}={}*{}".format(lon[0], lon[1], lon[2]))
    elif lon[1] / lon[2] == lon[0]:
        print("{}={}/{}".format(lon[0], lon[1], lon[2]))

Tri()
