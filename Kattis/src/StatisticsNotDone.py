import sys
import time

#min, max, range

def Statistics():
    token = True
    counter = 1

    while token:
        lon = input().split(' ')

        lon = [int(x) for x in lon]
        lon.remove(lon[0])

        mi = min(lon)
        ma = max(lon)
        ra = ma - mi

        print("Case {}: {} {} {}".format(counter, mi, ma, ra))
        counter += 1



Statistics()