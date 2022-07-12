cases = int(input())

#For all cases...
for i in range(cases):
    candidates = int(input())
    votes = []
    total = 0
    leaders = 0

    #Get the votes and total votes
    for i in range(candidates):
        v = int(input())
        votes.append(v)
        total += v

    #Get the relevant values, max value, where it is and half of votes.
    max_v = max(votes)
    index_max = votes.index(max_v)
    half = sum(votes) / 2

    #Find out if there are many votes has the same highest value
    for i in votes:
        if i == max_v:
            leaders += 1

    if leaders > 1:
        print("no winner")
    elif max_v > half:
        print("majority winner {}".format(index_max + 1))
    else:
        print("minority winner {}".format(index_max + 1))

