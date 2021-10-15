from collections import deque


def are_fireworks_enough(fireworks):
    return all(x >= 3 for x in fireworks.values())


def solve(firework_effects, explosive_powers):
    firework_effects_queue = deque([x for x in firework_effects if x > 0])
    explosive_powers_stack = [x for x in explosive_powers if x > 0]

    fireworks = {
        "palm": 0,
        "willow": 0,
        "crossette": 0
    }

    while firework_effects_queue \
            and explosive_powers_stack \
            and not are_fireworks_enough(fireworks):
        firework_effect = firework_effects_queue.popleft()
        explosive_power = explosive_powers_stack.pop()

        current_sum = firework_effect + explosive_power

        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks["crossette"] += 1
        elif current_sum % 3 == 0:
            fireworks["palm"] += 1
        elif current_sum % 5 == 0:
            fireworks["willow"] += 1
        else:
            if firework_effect > 1:
                firework_effects_queue.append(firework_effect - 1)
            explosive_powers_stack.append(explosive_power)

    print(fireworks)


def print_success(fireworks):
    print()


def print_fail(fireworks, firework_eff, remaining_exp):
    print()


firework = [int(x) for x in input().split(", ")]
explosive = [int(x) for x in input().split(", ")]

if are_fireworks_enough(fireworks):
    print_success(fireworks)
else:
    print_fail(fairworks, remaining_firework_eff, remaining_explosive_powers)


solve(firework, explosive)
