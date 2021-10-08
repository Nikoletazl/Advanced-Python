def read_matrix():
    n = int(input())
    matrix = []

    for _ in range(n):
        row = input()
        matrix.append(row)

    return matrix


matrix = read_matrix()
symbol = input()

is_found = False
row, col = None, None

for r in range(len(matrix)):
    if is_found:
        break
    for c in range(len(matrix[r])):
        if matrix[r][c] == symbol:
            row, col = r, c
            is_found = True
            break
if is_found:
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")