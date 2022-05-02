s = input()
o = ""
t = False
for i in s:
    if i == "a":
        t = True
    if t:
        o = o + i
print(o)