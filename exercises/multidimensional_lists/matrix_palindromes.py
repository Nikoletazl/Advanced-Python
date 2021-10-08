rows, cows = [int(x) for x in input().split()]

matrix = []

for r in range(rows):
    for c in range(cows):
        print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=" ")
    print()