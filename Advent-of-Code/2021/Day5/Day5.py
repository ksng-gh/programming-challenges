with open("day5.txt", "r") as f:
   lines = f.readlines()

coordinates = []
for line in lines:
    line = line.strip()
    pos = line.split(" -> ")
    coordinates.append(pos)

for coordinate in coordinates:
    position1 = coordinate[0].split(",")
    position2 = coordinate[1].split(",")

    print(position1)