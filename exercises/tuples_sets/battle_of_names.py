n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    sum_name = sum([ord(x) for x in name]) // row
    if sum_name % 2 == 0:
        even.add(sum_name)
    else:
        odd.add(sum_name)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()
if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(", ".join([str(x) for x in result]))