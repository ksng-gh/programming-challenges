#with open("input.txt", "r") as f:
#    lines = f.readlines()

with open("test.txt", "r") as f:
    lines = f.readlines()

class Node:
    def __init__(self, l):
        self.data = l

connections = []

for line in lines:
    line = line.strip()
    a, b = line.split("-")
    n = Node((a, [b]))