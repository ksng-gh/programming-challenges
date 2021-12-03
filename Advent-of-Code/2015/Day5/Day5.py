with open("day5.txt", "r") as f:
    lines = f.readlines()

niceStrings = 0

#For test1
#test = "ugknbfddgicrmopn"
test = "aaa"
#test = "jchzalrnumimnmhp"
#test = "haegwjzuvuyypxyu"

#For test2
#test = "qjhvhtzxzqqjkmpb"
#test = "xxyxx"
#test = "uurcxstgmygtbstg"
#test = "ieodomkazucvgmuy"
TASK = 2

def niceRules(string):
    counter = 0
    nicecounter = 0

    vowels = ["a", "e", "i", "o", "u"]

    #Good

    for i in string:
        if i in vowels:
            counter += 1
            if counter == 3:
                nicecounter += 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            nicecounter += 1
            break

    #Bad
    
    bad = ["ab", "cd", "pq", "xy"]
    for i in range(len(string) - 1):
        if string[i] + string[i + 1] in bad:
            return False
    nicecounter += 1
    if nicecounter == 3:
        return True
    return False  

def niceRules2(string):
    nice = 0
    found = False
    #First test
    for item in range(len(string) - 1):
        together = string[item] + string[item + 1]
        #print(together)
        for current in range(item + 2, len(string) - 1):
            together2 = string[current] + string[current + 1]
            #print(together2)
            if together == together2:
                #print("woo")
                nice += 1
                found = True
                break
        if found:
            break

    #Second test

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            nice += 1
            break
    return True if nice == 2 else False


#print(niceRules(test))


for line in lines:
    if TASK == 1: 
        if niceRules(line):
            niceStrings += 1
    if TASK == 2:
        if niceRules2(line):
            niceStrings += 1

#print(niceRules2(lines))
#print(niceRules2)
print(niceStrings)