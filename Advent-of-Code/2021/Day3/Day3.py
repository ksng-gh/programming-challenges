with open("day3.txt", "r") as f:
   lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

#Python clear() removes from memory

#max = mostCommon, min = leastCommon
def filterDesired(minOrMax, list):
    zeroList = []
    oneList = []
    index = 1

    while True:
        for item in list:
            if item[index] == "0":
                zeroList.append(item)
            else:
                oneList.append(item)
        if minOrMax == "max":
            if len(zeroList) > len(oneList):
                list = zeroList
                zeroList = []
                oneList = []
            elif len(oneList) > len(zeroList):
                list = oneList
                zeroList = []
                oneList = []
            else:
                if zeroList[0][index] == "1":
                    list = zeroList
                else:
                    list = oneList
                zeroList = []
                oneList = []
        else:
            if len(oneList) > len(zeroList):
                list = zeroList
                zeroList = []
                oneList = []
            elif len(zeroList) > len(oneList):
                list = oneList
                zeroList = []
                oneList = []
            else:
                if zeroList[0][index] == "0":
                    list = zeroList
                else:
                    list = oneList
                zeroList = []
                oneList = []

        if list.count(list[0]) == len(list):
            return int(list[0], 2)

        index += 1
        
storage = [None] * 12
zeroes = 0
ones = 0

gamma = ""
epsilon = ""

TASK = 2

oxygenRating = 0
CO2Rating = 0

#Sorting in different indices (i.e. first index in [0], second index in [1]...)
#Prob a better way to do it in Python
for line in lines:
    for idx, i in enumerate(line):
        position = idx % 12
        string = storage[position]
        if string == None:
            string = ""
        string = string + i
        storage[position] = string

if TASK == 1:
    #Counting the ones and zeroes (gamma/epsilon)
    for i in storage:
        for items in i:
            if items == "1":
                ones += 1
            else: 
                zeroes += 1
        
        if ones > zeroes:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        
        ones = 0
        zeroes = 0

    print(int(gamma, 2) * int(epsilon, 2))

if TASK == 2:
    t1 = []
    t0 = []
    for line in lines:
        if line[0] == "1":
            t1.append(line)
        else:
            t0.append(line)

    if len(t1) > len(t0):
        oxygenRating = filterDesired("max", t1)
        CO2Rating = filterDesired("min", t0)
    else: 
        #I'm dumb. Oxygen is always max, never min eksdee
        oxygenRating = filterDesired("max", t0)
        CO2Rating = filterDesired("min", t1)
    
    print(oxygenRating * CO2Rating)
