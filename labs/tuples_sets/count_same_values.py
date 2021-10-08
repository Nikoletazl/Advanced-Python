number_counts = {}

numbers = [float(x) for x in input().split()]

for number in numbers:
    if number not in number_counts:
        number_counts[number] = 0
    number_counts[number] += 1

for number, count in number_counts.items():
    print(f"{number} - {count} times")