import sys

def FizzBuzz():
    c1, c2, inp1 = input().split(' ')

    c1 = int(c1)
    c2 = int(c2)
    inp1 = int(inp1)

    for x in range(1, inp1 + 1):
        if x % c1 == 0 and x % c2 == 0 :
            print("FizzBuzz")
        elif x % c1 == 0 :
            print("Fizz")
        elif x % c2 == 0 :
            print("Buzz")
        else:
            print(x)

FizzBuzz()
