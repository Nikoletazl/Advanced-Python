from collections import deque


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


size = int(input())
commands = deque([x for x in input().split()])

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

expected_coals = 0
coals = 0

for row in range(size):
    field.append(input().split())

for row2 in range(len(field)):
    for col2 in range(len(field)):
        if field[row2][col2] == "c":
            expected_coals += 1

while commands:
    for r in range(len(field)):
        for c in range(len(field)):
            if field[r][c] == "s":
                if commands:
                    current_command = commands.popleft()
                    new_row = r + directions[current_command][0]
                    new_col = c + directions[current_command][1]
                    if is_in_range(new_row, new_col, size):
                        if field[new_row][new_col] == "*":
                            field[r][c], field[new_row][new_col] = "*", "s"
                            break
                        elif field[new_row][new_col] == "e":
                            print(f"Game over! ({new_row}, {new_col})")
                            break
                        elif field[new_row][new_col] == "c":
                            coals += 1
                            field[r][c], field[new_row][new_col] = "*", "s"
                            break
                else:
                    if coals == expected_coals:
                        print(f"You collected all coal! ({r}, {c})")
                    else:
                        print(f"{expected_coals - coals} pieces of coal left. ({r}, {c})")





