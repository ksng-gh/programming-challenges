import sys

def Vote():
    times = int(input())
    lon = []
    votetot = 0

    while times > 0:
        votes = int(input())
        
        while votes > 0:
            v = int(input())
            lon.append(v)
            votetot += v

            votes -= 1
        
        ma = max(lon)
        index = lon.index(ma)

        ratio = ma/votetot

        if ratio > 0.5 and not all(elem == lon[0] for elem in lon):
            print("majority winner {}".format(index + 1))            
        elif ratio <= 0.5 and not all(elem == lon[0] for elem in lon):
            print("minority winner {}".format(index + 1))
        elif len(lon) == 1:
            print("majority winner {}".format(index + 1))
        else: 
            print("no winner")
        
        lon.clear()
        votetot = 0

        times -= 1

Vote()