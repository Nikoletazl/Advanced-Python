def read_matrix():
    (n, m) = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

sums = []
n = len(matrix)
m = len(matrix[0])

for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1]
        sums.append((
            current_sum, r, c
        ))

max_sum = max(sums)
max_number = max_sum[0]
row = max_sum[1]
col = max_sum[2]

first_match = (matrix[row][col], matrix[row][col + 1])
second_match = (matrix[row + 1][col], matrix[row + 1][col + 1])

print(' '.join(str(x) for x in first_match))
print(' '.join(str(x) for x in second_match))
print(max_number)
