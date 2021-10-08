def generate_combination(values, index, count, comb):
    if len(comb) == count:
        print(", ".join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combination(values, i + 1, count, comb)
        comb.pop()


generate_combination(input().split(", "), 0, int(input()), [])
