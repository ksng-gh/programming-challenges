import sys

def Isithalloween():
    month, day = input().split(' ')
    day = int(day)

    if (month == 'OCT' and day == 31) or (month == 'DEC' and day == 25):
        print("yup")
    else:
        print("nope")
Isithalloween()        

