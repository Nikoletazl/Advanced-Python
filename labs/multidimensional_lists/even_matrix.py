def read_matrix():
    n = int(input())
    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()
even_matrix = []

for row in matrix:
    even = [x for x in row if x % 2 == 0]
    even_matrix.append(even)

print(even_matrix)