n = int(input())

c = 0
for i in range(n):
    w = input().lower()
    if "rose" in w or "pink" in w:
        c += 1
if c == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(c)