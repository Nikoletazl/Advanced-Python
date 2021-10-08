clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
current_rack = rack_capacity
while clothes:
    cloth = clothes[-1]
    if cloth > current_rack:
        used_racks += 1
        current_rack = rack_capacity
    else:
        current_rack -= cloth
        clothes.pop()

print(used_racks)