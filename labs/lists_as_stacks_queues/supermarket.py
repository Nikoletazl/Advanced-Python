from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)
