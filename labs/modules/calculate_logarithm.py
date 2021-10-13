import math


def calculate_log(x, base):
    if base == "natural":
        return f"{math.log(x):.2f}"

    base = int(base)

    return math.log(x, base)


print(calculate_log(10, 10))
print(calculate_log(10, "natural"))