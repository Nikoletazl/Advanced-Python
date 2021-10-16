from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees_capacity = [int(x) for x in input().split(", ")]
total_pizza = 0

while pizza_orders and employees_capacity:

    pizza = pizza_orders[0]
    employee = employees_capacity[-1]
    if pizza > 10:
        pizza_orders.popleft()
        continue
    if pizza <= 0:
        pizza_orders.popleft()
        continue

    if pizza <= employee:
        total_pizza += pizza
        pizza_orders.popleft()
        employees_capacity.pop()

    elif pizza > employee:
        pizza_orders[0] -= employee
        total_pizza += employee
        employees_capacity.pop()
        continue

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)} ")


