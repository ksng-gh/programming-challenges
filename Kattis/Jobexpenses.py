thing = input()
valuables = map(int, input().split(" "))
sum = 0
for i in valuables:
    if i < 0:
        sum -= i
print(sum)