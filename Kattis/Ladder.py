import sys
import math

def Ladder():
    h, v = input().split(' ')
    h = float(h)
    v = float(v)

    ans = h / math.sin(math.radians(v))
    print(math.ceil(ans))

Ladder()