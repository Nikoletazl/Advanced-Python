def get_turn():
    turn_str = input()
    vals = turn_str[1:-1].split(", ")
    return [int(val) for val in vals]


def in_range(val, max_value):
    return 0 <= val < max_value


def get_value(board, row_index, col_index, n, m):
    if not in_range(row_index, n) or not in_range(col_index, m):
        return 0

    value_str = board[row_index][col_index]

    if value_str.isdigit():
        return int(value_str)

    value = int(board[row_index][0]) + int(board[row_index][-1]) + \
        int(board[0][col_index]) + int(board[-1][col_index])

    if value_str == "D":
        return 2 * value

    if value_str == "T":
        return 3 * value

    return 501


def solve(board, player_names, n, m):
    curr_player = player_names[0], 501, 0
    other_player = player_names[1], 501, 0

    while True:
        name, total_points, turns = curr_player
        row_index, col_index = get_turn()

        curr_points = get_value(board, row_index, col_index, n, m)
        total_points -= curr_points
        turns += 1

        curr_player = name, total_points, turns

        if total_points <= 0:
            break

        curr_player, other_player = other_player, curr_player

    name, _, turns = curr_player
    print(f"{name} won the game with {turns} throws!")


player_names = input().split(", ")
n = 7
m = 7
board = [input().split() for _ in range(n)]

solve(board, player_names, n, m)