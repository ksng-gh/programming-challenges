s = input()
t = False
c = 0
for i in s:
    if not t:
        c += 1
    if i == ")":
        t = not t
        c -= 1
    if t:
        c -= 1

if c != 0:
    print("fix")
else:
    print("correct")