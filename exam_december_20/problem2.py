def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


initial_string = input()
size = int(input())
matrix = []

for row in range(size):
    matrix.append([x for x in input()])

number_directions = int(input())
directions = []

for direction in range(number_directions):
    directions.append(input())

curr_row = 0
curr_col = 0
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "P":
            curr_row = row
            curr_col = col
            matrix[curr_row][curr_col] = "-"

directions_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

next_row = 0
next_col = 0
for command in directions:
    if command in directions_dict:
        next_row = curr_row + directions_dict[command][0]
        next_col = curr_col + directions_dict[command][1]
        if is_in_range(next_row, next_col, size):
            curr_position = matrix[next_row][next_col]
            if curr_position.isalpha():
                initial_string += curr_position
                matrix[next_row][next_col] = "-"
            curr_row = next_row
            curr_col = next_col
        else:
            if initial_string:
                initial_string = initial_string[:-1]

matrix[curr_row][curr_col] = "P"

print(initial_string)
for row in matrix:
    print(f"{''.join(row)}")