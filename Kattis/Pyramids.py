blocks = int(input())
i = 1
height = 0
while blocks > 0:
    if blocks - i ** 2 < 0:
        break
    blocks -= i ** 2
    height += 1
    i += 2
print(height)
