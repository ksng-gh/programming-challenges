hw = input().split(";")
sum = 0
for w in range(len(hw)):
    hw[w] = hw[w].split("-")  
for i in hw:
    if len(i) > 1:
        sum += int(i[1]) - int(i[0]) + 1
    else:
        sum += 1
print(sum)