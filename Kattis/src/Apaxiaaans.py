import sys

def Filter():
    wo = input()
    ret = ''
    prev = ""
    for ch in wo:
        if ch != prev:
            ret += ch
        prev = ch
    
    print(ret)
Filter()