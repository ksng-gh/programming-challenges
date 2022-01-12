with open("day7.txt", "r") as f:
    lines = f.readlines()

#possible gates:
#AND NOT LSHIFT RSHIFT OR

#Python
# x & y bitwise and
# x | y bitwise or
# x << y lshift by y
# x >> y rshift by y
# ~a bitwise not

#CBA to learn regex atm...

commands = [line.strip().split(" ") for line in lines]
variables = {}
a = None
while a == None:
    for idx, instruction in enumerate(commands):
        if len(instruction) == 3 and instruction[0].isnumeric():
            print(instruction)
            variables.update({instruction[2]: int(instruction[0])})
            commands[idx] = ""
        if instruction[1] in variables or instruction[0] in variables and instruction[2] in variables:
            print(variables)
            print(instruction)
            for i in instruction:
                if i == "NOT":
                    variables.update({instruction[len(instruction) - 1]: ~int(instruction[1])})
                if i == "AND":
                    variables.update({instruction[len(instruction) - 1]: instruction[0] & instruction[2]})
                

b = 1
print(~b)



#print(commands)
print(variables)




maxnr = 65535

