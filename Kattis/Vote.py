cases = int(input())

for i in range(cases):
    candidates = int(input())
    votes = []
    total = 0
    leaders = 0

    for i in range(candidates):
        v = int(input())
        votes.append(v)
        total += v

    max_v = max(votes)
    index_max = votes.index(max_v)
    half = sum(votes) / 2

    for i in votes:
        if i == max_v:
            leaders += 1

    if leaders > 1:
        print("no winner")
    elif max_v > half:
        print("majority winner {}".format(index_max + 1))
    else:
        print("minority winner {}".format(index_max + 1))

