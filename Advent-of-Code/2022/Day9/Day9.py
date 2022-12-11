#Cr
#Mistake: P1: calculated tail = headpos. Changed tail -> calculate next pos instead.

with open("input.txt", "r") as f:
    lines = f.readlines()

def move(head, dir):
    match dir:
        case "L":
            return (head[0] - 1, head[1])
        case "R":
            return (head[0] + 1, head[1])
        case "U":
            return (head[0], head[1] + 1)
        case "D":
            return (head[0], head[1] - 1)

def toofar(head, tail):
    if head == tail:
        return False

    if tail[0] + 1 == head[0] and tail[1] + 1 == head[1]:
        return False

    if tail[0] - 1 == head[0] and tail[1] + 1 == head[1]:
        return False

    if tail[0] + 1 == head[0] and tail[1] - 1 == head[1]:
        return False

    if tail[0] - 1 == head[0] and tail[1] - 1 == head[1]:
        return False


    if abs(max(head[0], tail[0]) - min(head[0], tail[0]) + max(head[1], tail[1]) - min(head[1], tail[1])) == 1:
        return False

    return True

def movetail(head, tail):
    hx, hy = head
    tx, ty = tail
    if toofar(head, tail):
        if hx - tx > 0:
            x = 1
        elif hx == tx:
            x = 0
        else:
            x = -1
        if hy - ty > 0:
            y = 1
        elif hy == ty:
            y = 0
        else:
            y = -1
        tx = tx + x
        ty = ty + y
    return (tx, ty)

TASK = 2

if TASK == 1:

    visited = set()
    tail = (0, 0)
    head = (0, 0)
    for line in lines:
        dir, step = line.split()
        for i in range(int(step)):
            head = move(head, dir)
            tail = movetail(head, tail)
            visited.add(tail)
    print(len(visited))


if TASK == 2:
    visited = set()
    rope = [(0, 0) for i in range(10)]
    for line in lines:
        dir, step = line.split()
        for i in range(int(step)):
            rope[0] = move(rope[0], dir)
            for r in range(len(rope) - 1):
                rope[r + 1] = movetail(rope[r], rope[r + 1])
                if r == len(rope) - 2:
                    visited.add(rope[r + 1])
    print(len(visited))