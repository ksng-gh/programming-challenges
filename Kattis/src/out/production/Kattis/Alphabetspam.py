import sys

def Alphabetspam():
    string = input()

    toDivideWith = len(string)

    blank = 0
    lower = 0
    upper = 0
    symbol = 0

    for x in string:
        if x == "_":
            blank += 1
        elif x.islower():
            lower += 1
        elif x.isupper():
            upper += 1
        elif not(x.isalpha() and x.isdigit()):
            symbol += 1

    print(float(blank/toDivideWith))
    print(float(lower/toDivideWith))
    print(float(upper/toDivideWith))
    print(float(symbol/toDivideWith))

Alphabetspam()