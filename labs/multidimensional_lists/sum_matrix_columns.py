def read_matrix():
    (n, m) = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()

n = len(matrix)
m = len(matrix[0])

column_sums = [0] * m

for r in range(n):
    for c in range(m):
        value = matrix[r][c]
        column_sums[c] += value

[print(x) for x in column_sums]
