rows, cows = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

count = 0

for r in range(rows - 1):
    for c in range(cows - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            count += 1

print(count)
