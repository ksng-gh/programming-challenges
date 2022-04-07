import sys

def Detaileddifferences():
    inps = input()
    inps = int(inps)

    check = ''
    counter = 0

    for x in range(0, inps):
        s1 = input()
        s2 = input()

        for y in range(0, len(s1)): 
            if s1[counter] == s2[counter]:
                check += '.'
            else:
                check += '*'
            counter += 1
        
        counter = 0
        print(s1)
        print(s2)
        print(check)
        check = ''


Detaileddifferences()