rows, cows = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
best_row = 0
best_col = 0
for r in range(rows - 2):
    for c in range(cows - 2):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r][c + 2] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1] + \
                      matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + \
                      matrix[r + 2][c + 1] + \
                      matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum, best_row, best_col = current_sum, r, c

print(f"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])
