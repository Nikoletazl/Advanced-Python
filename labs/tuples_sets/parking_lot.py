n = int(input())

parking_lot = set()

for _ in range(n):
    direction, car = input().split(", ")
    if direction == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")