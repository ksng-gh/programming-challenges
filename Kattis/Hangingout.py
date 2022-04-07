safety, events = input().split(' ')
safety = int(safety)
events = int(events)

people = 0
denied = 0

for i in range(events):
    action, number = input().split(' ')
    number = int(number)

    if action == "enter":
        if number + people > safety:
            denied += 1
        else:
            people += number
    else:
        people -= number

print(denied)