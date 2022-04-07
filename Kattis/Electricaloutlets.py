import sys

def calc():
    n = int(input()) 
    for i in range(n):
        v = 0
        l = [int(i) for i in input().split(' ')]
        for j in l[1:]:
            v += j
        print(v - (l[0] - 1))
calc()