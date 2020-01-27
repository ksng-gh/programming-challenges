import sys

def Hissingmicrophone():
    word = input()
    maybehiss = 1
    c = 0

    for x in word:
        if x == 's':
            if len(word) == c + 1:
                print("no hiss")
                maybehiss = 0
                break
            elif word[c + 1] == 's':
                print("hiss")
                maybehiss = 0
                break
        c = c + 1
    if maybehiss == 1:
        print("no hiss")

Hissingmicrophone()
