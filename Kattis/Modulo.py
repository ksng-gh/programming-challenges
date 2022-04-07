import sys

def Modulo():

    nom = []
    unique = []

    for x in range(0, 10):
        nom.append(int(input()) % 42)

    for x in nom:
        if x not in unique:
            unique.append(x)

    print(len(unique))

Modulo()