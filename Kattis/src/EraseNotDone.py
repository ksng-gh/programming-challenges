import sys

def Erase():
    n = int(input())
    str1 = input()
    str2 = input()

    if n % 2 == 0:
        if str1 == str2:
            print("Deletion succeeded")
        else:
            print("Deletion failed")
    else:
Erase()