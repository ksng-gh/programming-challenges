s = input()
storage = []
for i in range(len(s) - 1):
    if s[i] == ":" or s[i] == ";":
        if s[i + 1] == ")":
            storage.append(i)
        elif s[i + 1] == "-" and i != (len(s) - 1):
           if s[i + 2] == ")":
               storage.append(i)

for i in storage:
    print(i)