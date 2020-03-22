import sys

def Symmetricorder():
    checkLoop = 1

    namelist = []
    nameA = []
    nameB = []

    counter = 1

    while checkLoop == 1:
        testcase = input()
        testcase = int(testcase)
        
        if testcase == 0:
            break

        for x in range(0, testcase):
            name = input()
            namelist.append(name)
        
        nameA = namelist[0:len(namelist):2]
        nameB = namelist[1:len(namelist):2]
        nameB = nameB[::-1]        
        
        print("SET {}".format(counter))
        nameTot = nameA + nameB
        for x in nameTot:
            print(x)
        namelist.clear()
        counter += 1
    


Symmetricorder()