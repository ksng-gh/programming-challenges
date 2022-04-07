import sys

def Babybites():
    size = input()
    lon = input().split(' ')
    counter = 1

    token = True

    for x in lon:
        if x.isdigit():
            x = int(x)
            if x == 'mumble':
                continue
            elif x != counter:
                print("something is fishy")
                token = False
                break
        counter += 1
    if token == True:
        print("makes sense")

Babybites()