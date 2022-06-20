tests = int(input())

for i in range(tests):
    s = input()[::-1]
    sum = 0
    for i in range(len(s)):
        inti = int(s[i])
        if i % 2 == 1:
            inti = inti * 2
            if inti > 9:
                sint = str(inti)
                inti = int(sint[0]) + int(sint[1])
        sum += inti
    if sum % 10 == 0:
        print("PASS")
    else:
        print("FAIL")
