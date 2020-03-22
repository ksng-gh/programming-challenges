import sys

def Simonsays():
    tot = int(input())

    while tot > 0:
        sentence = input().split(' ')

        if sentence[0] == "Simon" and sentence[1] == "says":
            sentence.remove("Simon")
            sentence.remove("says")
            toprint = ' '.join(sentence)
            print(toprint)

        tot -= 1
Simonsays()