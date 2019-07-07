import sys
import math

#percentage of pizza has cheese
#pizz cheese / pizz tot


def Pizza2():
    r, c = input().split(' ')
    r = int(r)
    c = int(c)

    radpizz = r * r * math.pi

    radcheese = (r - c) * (r - c) * math.pi

    print(100 * radcheese/radpizz)

Pizza2()




