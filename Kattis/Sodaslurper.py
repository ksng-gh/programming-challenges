empty, found, require = map(int, input().split(" "))

soda = 0
total = empty + found
r = 0

while total >= require:
    total -= require
    soda += 1
    if total < require:
        total += soda
        r += soda
        soda = 0
print(r)
