def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = [el for el in input().split()]
values = []

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "d_right_up": (-1, 1),
    "d_left_up": (-1, -1),
    "d_right_down": (1, 1),
    "d_left_down": (1, -1)
}

for el in bombs:
    data = el.split(",")
    r = int(data[0])
    c = int(data[1])
    current_value = matrix[r][c]
    if current_value <= 0:
        continue
    matrix[r][c] = 0
    for direction in direction_mapper:
        new_row = r + direction_mapper[direction][0]
        new_col = c + direction_mapper[direction][1]
        if is_in_range(new_row, new_col, size):
            if matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= current_value

alive_cells = 0
sum = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] <= 0:
            continue
        else:
            sum += matrix[row][col]
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")

for row in range(len(matrix)):
    print(" ".join(str(el) for el in matrix[row]))