with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

TASK = 2

sum = 0
found = True
keys = []
if TASK == 1:
    for i in lines:
        s = i.strip()
        if s[0] == "+":
            sum += int(s[1:])
        else:
            sum -= int(s[1:])
if TASK == 2:
    while found:
        for i in lines:
            s = i.strip()
            if s[0] == "+":
                sum += int(s[1:])
            else:
                sum -= int(s[1:])
            if sum in keys:
                found = False
                break
            else:
                keys.append(sum)
            #print(keys)
        #if len(keys) > 10:
        #    break
            
print(sum)