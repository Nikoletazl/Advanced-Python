def read_matrix():
    n = int(input())
    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()

print(
    [x for row in matrix for x in row]
)
