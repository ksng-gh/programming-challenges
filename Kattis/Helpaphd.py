import sys

def Helpaphd():
    times = int(input())
    for x in range(0, times):
        string = input()
        if string[0].isdigit():
            one, two = string.split('+')
            print(int(one) + int(two))
        else:
            print("skipped")



Helpaphd()