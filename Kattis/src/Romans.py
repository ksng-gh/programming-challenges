import sys
import math

def Romans():
    engmile = float(input())
    engtorom = float(engmile * 1000 * (5280/4854))
    checkdec = (engtorom - int(engtorom))

    if checkdec > 0.4:
        print(math.ceil(engtorom))
    else:
        print(math.floor(engtorom))

Romans()
