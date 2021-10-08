size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []


for row in range(size):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][size - 1 - row])

