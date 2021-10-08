from collections import deque

water_quantity = int(input())

people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break

    people_queue.appendleft(command)

while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        params = command.split(" ")
        liters_to_add = int(params[1])
        water_quantity += liters_to_add
    else:
        name = people_queue.pop()
        water_wanted = int(command)
        if water_wanted <= water_quantity:
            print(f"{name} got water")
            water_quantity -= water_wanted
        else:
            print(f"{name} must wait")

print(f"{water_quantity} liters left")

