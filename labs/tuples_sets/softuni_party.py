n = int(input())
guest_list = {input() for _ in range(n)}

while True:
    command = input()
    if command == "END":
        break
    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in guest_list if is_vip(g)])
regular_guests = sorted([g for g in guest_list if not is_vip(g)])

print(len(guest_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]
