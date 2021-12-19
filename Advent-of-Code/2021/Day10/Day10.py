with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

#()
#[]
#{}
#<>

#) -> 3
#] -> 57
#} -> 1197
#> -> 25137

TASK = 2

stack = []
corrupt = False
sum = 0

if TASK == 1:

    for line in lines:
        for idx, symbol in enumerate(line):
            if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
                stack.append(symbol)
            else:
                curr = stack[-1]
                if curr == "(" and symbol == ")":
                    stack.pop()
                elif curr == "[" and symbol == "]":
                    stack.pop()
                elif curr == "{" and symbol == "}":
                    stack.pop()
                elif curr == "<" and symbol == ">":
                    stack.pop()
                else:
                    if symbol != "\n":
                        match symbol:
                            case ")":
                                v = 3
                            case "]":
                                v = 57
                            case "}":
                                v = 1197
                            case ">":
                                v = 25137
                        sum += v
                        break
        stack.clear()
    
    print(sum)


#) -> 1
#] -> 2
#} -> 3
#> -> 4

#23074090194
#too high

scores = []

if TASK == 2:
    for line in lines:
        for idx, symbol in enumerate(line):
            if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
                stack.append(symbol)
            else:
                curr = stack[-1]
                if curr == "(" and symbol == ")":
                    stack.pop()
                elif curr == "[" and symbol == "]":
                    stack.pop()
                elif curr == "{" and symbol == "}":
                    stack.pop()
                elif curr == "<" and symbol == ">":
                    stack.pop()
                else:
                    if symbol != "\n":
                        match symbol:
                            case ")":
                                v = 3
                            case "]":
                                v = 57
                            case "}":
                                v = 1197
                            case ">":
                                v = 25137
                        sum += v
                        corrupt = True
                        break

        if not corrupt:
            while len(stack) != 0:
                curr = stack[-1]
                sum = sum * 5
                match curr:
                    case "(":
                        sum += 1
                    case "[":
                        sum += 2
                    case "{":
                        sum += 3
                    case "<":
                        sum += 4
                stack.pop()
            scores.append(sum)
        
        sum = 0
        corrupt = False
        stack.clear()
    scores.sort()
    print(scores[int(len(scores)/2)])