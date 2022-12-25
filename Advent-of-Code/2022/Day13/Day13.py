from ast import literal_eval
import copy

TASK = 1

with open("input.txt", "r") as f:
    lines = f.readlines()

order = 1
orders = []

def process(m1, m2):
    ml = max(len(m1), len(m2))
    counter = 0
    while counter < ml:
        if m1 == [] and m2 == []:
            return False
        if m1 == []:
            return True
        if m2 == []:
            return False
        c1 = m1[0]
        m1.pop(0)
        c2 = m2[0]
        m2.pop(0)
        if isinstance(c1, int) and isinstance(c2, int):
            if c1 < c2:
                return True
            elif c1 > c2:
                return False
            else:
                continue
        if isinstance(c1, list) and isinstance(c2, list):
            r = process(c1, c2)
            if r == True or r == False:
                return r
            else:
                continue
        if isinstance(c1, list):
            if isinstance(c2, int):
                return process(c1, [c2])
        if isinstance(c2, list):
            if isinstance(c1, int):
                return process([c1], c2)

        counter += 1

if TASK == 1:

    while lines:
        if lines[0] == '\n':
            lines.pop(0)
            continue
        first = literal_eval(lines[0].strip())
        lines.pop(0)
        second = literal_eval(lines[0].strip())
        lines.pop(0)

        res = process(first, second)
        if res == True:
            orders.append(order)
        order += 1

    print(sum(orders))

if TASK == 2:
    decodekey1 = [[2]]
    decodekey2 = [[6]]
    toSort = []
    toSort.append(decodekey1)
    toSort.append(decodekey2)
    while lines:
        if lines[0] == '\n':
            lines.pop(0)
            continue
        m = literal_eval(lines[0].strip())
        lines.pop(0)
        for idx, i in enumerate(toSort):
            mc = copy.deepcopy(m[:]) #Item from read
            ic = copy.deepcopy(i[:]) #Item in sorted list
            res = process(mc, ic)
            if res == True:
                toSort.insert(idx, m)
                break
            elif idx == len(toSort) - 1:
                toSort.append(m)
                break
            else:
                continue
    one = 0
    two = 0
    for idx, i in enumerate(toSort):
        if i == [[2]]:
            one = idx + 1
        if i == [[6]]:
            two = idx + 1
    print(one * two)
