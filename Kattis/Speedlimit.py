stop = False
while not stop:
    cases = []
    sum = 0
    sets = int(input())
    if sets == -1:
        stop = True
    for i in range(sets):
        miles, hour = map(int, input().split(" "))
        cases.append((miles, hour))
    for i in range(len(cases)):
        if i < 1:
            sum += cases[i][0] * cases[i][1]
        else:
            sum += cases[i][0] * (cases[i][1] - cases[i - 1][1])
    if not stop:
        print("{} miles".format(sum))

