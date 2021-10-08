def is_invalid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]
    if is_invalid_position(size, row, col):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row_elements in matrix:
    print(" ".join([str(x) for x in row_elements]))