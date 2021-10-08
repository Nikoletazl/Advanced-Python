def find_sum(numbers_list):
    result = 1
    for i in range(len(numbers_list)):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif number <= 10:
            result /= number
    return f"{result:.0f}"


print(find_sum([int(x) for x in input().split(", ")]))