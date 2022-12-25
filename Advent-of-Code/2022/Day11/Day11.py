with open("input.txt", "r") as f:
    lines = f.readlines()

#monkeydata
#0: items
#1: operation
#2: test
#3: if true
#4: if false

#i = [[89, 95, 92, 64, 87, 68], ("*", 11), 2, 7, 4]
#Cheating...

monkeydata = [[[89, 95, 92, 64, 87, 68], ("*", 11), 2, 7, 4], [[87, 67], ("+", 1), 13, 3, 6], [[95, 79, 92, 82, 60], ("+", 6), 3, 1, 6], [[67, 97, 56], ("*", "old"), 17, 7, 0], [[80, 68, 87, 94, 61, 59, 50, 68], ("*", 7), 19, 5, 2], [[73, 51, 76, 59], ("+", 8), 7, 2, 1], [[92], ("+", 5), 11, 3, 0], [[99, 76, 78, 76, 79, 90, 89], ("+", 7), 5, 4, 5]]
monkeytestdata = [[[79, 98], ("*", 19), 23, 2, 3], [[54, 65, 75, 74], ("+", 6), 19, 2, 0], [[79, 60, 97], ("*", "old"), 13, 1, 3], [[74], ("+", 3), 17, 0, 1]]

magic = 1
for i in monkeydata:
    magic *= i[2]

monkeyinspectiondata = [0] * 8
TASK = 1

def printallitems(l):
    for i in l:
        print(i[0])

if TASK == 1:
    rounds = 20
else:
    rounds = 10000

for _ in range(rounds):
    for idx, i in enumerate(monkeydata): #i = data of monkey
        for item in i[0]:
            monkeyinspectiondata[idx] += 1
            if i[1][0] == "*":
                if i[1][1] == "old":
                    currworrylevel = item * item
                else:
                    currworrylevel = item * i[1][1]
            else:
                currworrylevel = item + i[1][1]
            if TASK == 1:
                currworrylevel = currworrylevel // 3
            else: 
                currworrylevel = currworrylevel % magic
            if currworrylevel % i[2] == 0:
                monkeydata[i[3]][0].append(currworrylevel)                    
            else:
                monkeydata[i[4]][0].append(currworrylevel)                
        monkeydata[idx][0] = []
max1 = max(monkeyinspectiondata)
monkeyinspectiondata.remove(max1)
print(max(monkeyinspectiondata) * max1)

    