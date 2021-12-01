with open("day1.txt", "r") as f:
    lines = f.readlines()
#depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
#depths = [607, 618, 618, 617, 647, 716, 769, 792]
depths = [int(j.strip()) for j in lines]

#comparison of depths without int() -> 1297
#comparison of depths with int() -> 1298
#...

increased = 0

VARIABLE = 2

#
# Part 1 - basic solution
#

if VARIABLE == 1:

    for i in range(len(depths) - 1):

        if depths[i] <= depths[i + 1]:
            increased += 1

#
# Part 2 - another basic solution
#

if VARIABLE == 2:

    for i in range(len(depths) - 3):
        a = depths[i] + depths[i + 1] + depths[i + 2]
        b = depths[i + 1] + depths[i + 2] + depths[i + 3]

        #... < != <= fml

        if a < b:
            increased += 1

print(increased)

