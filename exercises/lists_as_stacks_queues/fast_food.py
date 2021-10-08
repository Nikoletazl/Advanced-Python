from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))

max_order = max(orders)

while orders:
    current_order = orders[0]
    if current_order > total_food:
        break
    else:
        total_food -= current_order
        orders.popleft()

print(max_order)
if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")