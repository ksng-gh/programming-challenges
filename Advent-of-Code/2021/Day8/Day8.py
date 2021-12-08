with open("input.txt", "r") as f:
    lines = f.readlines()

#with open("test.txt", "r") as f:
#    lines = f.readlines()

segments = []
for line in lines:
    segments.append(line.strip().split(" "))

#0 = length 6 abcdeg
#2 = length 5 acdfg
#3 = length 5 abcdf
#5 = length 5 bcdef
#6 = length 6 bcdefg
#9 = length 6 abcdef

#1 = length 2 ab 
#4 = length 4 abef
#7 = length 3 abd
#8 = length 7 abcdefg

#Sorts the strings in the segments before the "|"
#Prob better way to do it...


def searchLength(segment, length):
    for idx, item in enumerate(segment):
        if len(item) == length:
            segment[idx] = ""
            return item
    return -1

#Check if segment is in another segment
def isInSegment(retseg, otherseg):
    start = 0
    stop = len(otherseg)
    for item in otherseg:
        if item in retseg:
            start += 1
        if start == stop:
            return True
    return False            

#Remove duplicate
def trimSegment(retseg, otherseg):
    for i in otherseg:
        retseg = retseg.replace(i, "")
    return retseg

#Takes the segment and maps them into parts
def whySoAnnoying(segment):
    #    0
    #1       2
    #    3
    #4       5
    #    6
    #m = all 7 segments
    m = [None] * 7

    #1
    obj = searchLength(segment, 2)
    m[2] = obj
    m[5] = obj

    #7
    obj2 = searchLength(segment, 3)
    obj2 = trimSegment(obj2, obj)
    m[0] = obj2

    #4
    obj3 = searchLength(segment, 4)
    obj3 = trimSegment(obj3, obj)
    m[1] = obj3
    m[3] = obj3

    #9
    nine = ""
    for idx, item in enumerate(segment):
        obj4 = trimSegment(item, obj2)
        obj4 = trimSegment(obj4, obj3)
        obj4 = trimSegment(obj4, obj)
        if len(obj4) == 1:
            m[6] = obj4
            if isInSegment(item, obj) and isInSegment(item, obj2) and isInSegment(item, obj3):
                nine = item
                segment[idx] = ""

    #0
    zero = ""
    for idx, item in enumerate(segment):
        if isInSegment(item, obj) and len(item) == 6:
            zero = item
            obj5 = trimSegment(item, obj)
            obj5 = trimSegment(obj5, obj2)
            obj5 = trimSegment(obj5, obj3)
            obj5 = trimSegment(obj5, m[6])
            m[4] = obj5
            segment[idx] = ""

    #6
    for idx, item in enumerate(segment):
        if len(item) == 6:
            obj6 = trimSegment(nine, item)
            m[2] = obj6
            segment[idx] = ""

    m[5] = trimSegment(m[5], m[2])

    for item in segment:
        if len(item) == 7:
            m[3] = trimSegment(item, zero)
    
    m[1] = trimSegment(m[1], m[3])

    return m

def segmentDictionary(segments):
    mapped = whySoAnnoying(segments)
    numberDict = {}
    #0
    numberDict.update({"".join(sorted([mapped[0], mapped[2], mapped[5], mapped[6], mapped[1], mapped[4]])):"0"})
    #1
    numberDict.update({"".join(sorted([mapped[2], mapped[5]])):"1"})
    #2
    numberDict.update({"".join(sorted([mapped[0], mapped[2], mapped[3], mapped[4], mapped[6]])):"2"})
    #3
    numberDict.update({"".join(sorted([mapped[0], mapped[2], mapped[3], mapped[5], mapped[6]])):"3"})
    #4
    numberDict.update({"".join(sorted([mapped[1], mapped[2], mapped[3], mapped[5]])):"4"})
    #5
    numberDict.update({"".join(sorted([mapped[0], mapped[1], mapped[3], mapped[5], mapped[6]])):"5"})
    #6
    numberDict.update({"".join(sorted([mapped[0], mapped[1], mapped[3], mapped[4], mapped[5], mapped[6]])):"6"})
    #7
    numberDict.update({"".join(sorted([mapped[0], mapped[2], mapped[5]])):"7"})
    #8
    numberDict.update({"".join(sorted([mapped[0], mapped[1], mapped[2], mapped[3], mapped[4], mapped[5], mapped[6]])):"8"})
    #9
    numberDict.update({"".join(sorted([mapped[0], mapped[1], mapped[2], mapped[3], mapped[5], mapped[6]])):"9"})
    return numberDict

TASK = 1

one = 0
four = 0
seven = 0
eight = 0

if TASK == 1:
    for segment in segments:
        for item in range(11, 15):
            if len(segment[item]) == 2:
                one += 1
            if len(segment[item]) == 4:
                four += 1
            if len(segment[item]) == 3:
                seven += 1
            if len(segment[item]) == 7:
                eight += 1
    print(one + four + seven + eight)

if TASK == 2:
    t = []
    sum = 0
    delimiter = False
    for segment in segments:
        for item in segment:
            if item == "|":
                delimiter = True
            if item != "|" and delimiter == False:
                s = "".join(sorted(item))
                t.append(s)
        d = segmentDictionary(t)
        items = segment[-4:]
        s = ""
        for i in items:
            s += d.get("".join(sorted(i)))
        sum += int(s)
        delimiter = False
    print(sum)
