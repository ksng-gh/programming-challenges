import sys

def Everywhere():
    arr = []
    unique = []

    inps = input()
    inps = int(inps)
    for x in range(0, inps):
        inp2 = input()
        inp2 = int(inp2)
        for y in range(0, inp2):
            city = input()
            arr.append(city)
            for z in arr:
                if z not in unique:
                    unique.append(z)
        print(len(unique))
        unique.clear()
        arr.clear()
Everywhere()