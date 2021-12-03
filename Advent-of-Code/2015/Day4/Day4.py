import hashlib

with open("day4.txt", "r") as f:
    line = f.readline()

#line = "abcdef"
#line = "pqrstuv"
counter = 0
found = False

TASK = 1

while True:
    temp = line + str(counter)
    result = hashlib.md5(temp.encode()).hexdigest()
    if TASK == 1:
        if result[0:5] == "00000":
            found = True
    if TASK == 2:
        if result[0:6] == "000000":
            found = True
    if found:
        print("Found! ")
        print(counter)
        break
    counter += 1
