def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(el) for el in input().split()])

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

cells_count = 0
total_sum = 0

indexes_coordinates = input().split()
for el in indexes_coordinates:
    bomb_row, bomb_col = el.split(",")
    bomb_row = int(bomb_row)
    bomb_col = int(bomb_col)
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value <= 0:
        continue
    matrix[bomb_row][bomb_col] = 0
    for direction in direction_mapper:
        new_row = bomb_row + direction_mapper[direction][0]
        new_col = bomb_col + direction_mapper[direction][1]
        if is_in_range(new_row, new_col, n):
            if matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= bomb_value

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
            cells_count += 1
            total_sum += matrix[row][col]

print(f'Alive cells: {cells_count}')
print(f'Sum: {total_sum}')
for row in range(len(matrix)):
    print(" ".join(str(el) for el in matrix[row]))