from collections import deque

cups = deque(int(x) for x in input().split())
bottles = list(int(x) for x in input().split())

wasted_water = 0

while True:
    if cups and bottles:
        current_cup = cups.popleft()
        current_bottle = bottles.pop()
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
        else:
            cups.appendleft(current_cup - current_bottle)
    else:
        break

if cups:
    result = ' '.join([str(x) for x in cups])
    print(f"Cups: {result}")
if bottles:
    res = ' '.join([str(x) for x in bottles])
    print(f"Bottles: {res}")

print(f"Wasted litters of water: {wasted_water}")