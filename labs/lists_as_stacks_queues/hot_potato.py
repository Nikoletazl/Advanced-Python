from collections import deque

potatoes = input().split()
potatoes_queue = deque()
for p in potatoes:
    potatoes_queue.appendleft(p)
step = int(input())

while potatoes_queue:
    for _ in range(step - 1):
        potatoes_queue.appendleft(potatoes_queue.pop())
    potato_to_remove = potatoes_queue.pop()
    if potatoes_queue:
        print(f"Removed {potato_to_remove}")
    else:
        print(f"Last is {potato_to_remove}")

