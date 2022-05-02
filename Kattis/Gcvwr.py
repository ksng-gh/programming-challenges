g, t, n = map(int, input().split(" "))
w = (g - t) * 0.9
items = input().split(" ")
items = [int(i) for i in items]
print(int(w - sum(items)))