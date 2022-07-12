r, c = map(int, input().split(" "))

m = [[c for c in input()] for _ in range(r)]
cm = [[-1 for _ in range(c)] for _ in range(r)]

cases = int(input())

def seek(start, end, i):

    check_queue = []

    sx, sy = (start)
    ex, ey = (end)

    t = m[sy][sx]

    label = "binary" if t == "0" else "decimal"

    if cm[sy][sx] == -1:

        check_queue.append(start)

        if start == end:
            print(label)
            return

        while(check_queue):
            p = check_queue.pop(0)


            cm[p[1]][p[0]] = i
            # x + 1
            if p[0] + 1 < c:
                if m[p[1]][p[0] + 1] == t and cm[p[1]][p[0] + 1] != i:
                    check_queue.append((p[0] + 1, p[1]))
                    cm[p[1]][p[0] + 1] = i

            # x - 1
            if p[0] - 1 > 0:
                if m[p[1]][p[0] - 1] == t and cm[p[1]][p[0] - 1] != i:
                    check_queue.append((p[0] - 1, p[1]))
                    cm[p[1]][p[0] - 1] = i

            # y + 1
            if p[1] + 1 < r:
                if m[p[1] + 1][p[0]] == t and cm[p[1] + 1][p[0]] != i:
                    check_queue.append((p[0], p[1] + 1))
                    cm[p[1] + 1][p[0]] = i

            # y - 1
            if p[1] - 1 > 0:
                if m[p[1] - 1][p[0]] == t and cm[p[1] - 1][p[0]] != i:
                    check_queue.append((p[0], p[1] - 1))
                    cm[p[1] - 1][p[0]] = i
            


    if cm[sy][sx] == cm[ey][ex]:
        print(label)
    else:
        print("neither")

for i in range(cases):
    sy, sx, ey, ex = map(int, input().split(" "))
    s = (sx - 1, sy - 1)
    e = (ex - 1, ey - 1)

    seek(s, e, i)
        