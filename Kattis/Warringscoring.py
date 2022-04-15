scores = int(input())

def notnomde(l):
    s = [0] * 2
    n = 0
    y = 0
    current = l[0]

    w = ""

    for i in l:
        if i == "Notnomde" and current == "Notnomde":
            n += 1
        if i == "Yraglac" and current == "Yraglac":
            y += 1
        
        if current != i:
            if current == "Notnomde":
                if s[0] < n:
                    s[0] = n
                n = 0
                y += 1
            if current == "Yraglac":
                if s[1] < y:
                    s[1] = y
                y = 0
                n += 1
            
            current = i
        
    if current == "Notnomde":
        if s[0] < n:
            s[0] = n
            
    if current == "Yraglac":
        if s[1] < y:
            s[1] = y

    if s[0] == s[1]:
        w = "tie"
    elif s[0] > s[1]:
        w = "Notnomde"
    else:
        w = "Yraglac"

    return w

def yraglac(l):
    store = [0] * 2
    current = l[0]
    count = 0
    w = ""

    for n in l:
        if n == "Notnomde" and current == "Notnomde":
            count += 1
            
        if n == "Yraglac" and current == "Yraglac":
            count -= 1

        if current != n:
            if current == "Notnomde":
                if count > store[0]:
                    store[0] = count
                count -= 1
            if current == "Yraglac":
                if count < store[1]:
                    store[1] = count
                count += 1
            
        current = n

    if current == "Notnomde":
        if count > store[0]:
            store[0] = count
    if current == "Yraglac":
        if count < store[1]:
            store[1] = count

    if store[0] > abs(store[1]):
        w = "Notnomde"
    elif store[0] < abs(store[1]):
        w = "Yraglac"
    else:
        w = "tie"
    
    
    return w

winners = []
for i in range(scores):
    winners.append(input())

n = notnomde(winners)
y = yraglac(winners)

#print("N: " + str(n))
#print("Y: " + str(y))

print("Agree") if n == y else print("Disagree")


