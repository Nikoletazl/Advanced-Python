from collections import deque

price_bullet = int(input())
size_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())

counter = 0
shot_bullets = 0

while True:
    if locks and bullets:
        current_bullet = bullets.pop()
        if current_bullet <= locks[0]:
            locks.popleft()
            shot_bullets += 1
            counter += 1
            print("Bang!")
        elif current_bullet > locks[0]:
            shot_bullets += 1
            counter += 1
            print("Ping!")
        if counter == size_barrel:
            counter = 0
            if bullets:
                print("Reloading!")
            else:
                continue
    else:
        cost = shot_bullets * price_bullet
        total_money = intelligence - cost
        if len(bullets) >= 0 and not locks:
            print(f"{len(bullets)} bullets left. Earned ${total_money}")
            break
        else:
            print(f"Couldn't get through. Locks left: {len(locks)}")
            break



