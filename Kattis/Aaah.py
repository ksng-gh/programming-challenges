import sys

def Aaah():
    pat = input()
    doc = input()

    if len(pat) >= len(doc):
        print("go")
    else:
        print("no")

Aaah()