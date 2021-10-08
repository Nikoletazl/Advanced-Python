def get_player_choice(player):
    choice = input(f"Player {player}, please choose a column\n")
    return int(choice) - 1


def apply_player_choice(board, player_choice, player):
    row_index = 0
    while row_index < len(board) and board[row_index][player_choice] is None:
        row_index += 1

    board[row_index - 1][player_choice] = player
    return row_index - 1, player_choice


def get_right_win_values(board, row_index, col_index, max_count_index):
    right_win_condition = [board[row_index][c] for c in range(col_index, max_count_index)]
    return right_win_condition


def get_left_win_values(board, row_index, col_index, min_count_index):
    left_win_condition = [board[row_index][c] for c in range(col_index, min_count_index, -1)]
    return left_win_condition


def get_up_win_values(board, row_index, col_index, min_row_index):
    values = [board[r][col_index] for r in range(row_index, min_row_index, -1)]
    return values


def get_down_win_values(board, row_index, col_index, max_row_index):
    values = [board[r][col_index] for r in range(row_index, max_row_index)]
    return values


def get_down_right_win_values(board, row_index, col_index, max_row_index, max_col_index):
    # values = [board[row_index + d][col_index + d] for d in range(max_row_index - col_index)]
    # return values
    values = []
    max_d = min(
        max_row_index - row_index,
        max_col_index - col_index
    )
    for d in range(max_d):
        r = row_index + d
        c = col_index + d
        values.append(board[r][c])
    return values


def get_down_left_win_values(board, row_index, col_index, max_row_index, min_col_index):
    values = []
    max_d = min(
        max_row_index - row_index,
        abs(min_col_index - col_index)
    )
    for d in range(max_d):
        r = row_index + d
        c = col_index - d
        values.append(board[r][c])
    return values


def get_up_right_win_values(board, row_index, col_index, min_row_index, max_col_index):
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        max_col_index - col_index
    )
    for d in range(max_d):
        r = row_index - d
        c = col_index + d
        values.append(board[r][c])
    return values


def get_up_left_win_values(board, row_index, col_index, min_row_index, min_col_index):
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        abs(min_col_index - col_index)
    )
    for d in range(max_d):
        r = row_index - d
        c = col_index - d
        values.append(board[r][c])
    return values


def check_win_condition(board, row_index, col_index, win_count):
    max_col_index = min(col_index + win_count, len(board[row_index]))
    min_col_index = max(col_index - win_count, -1)

    min_row_index = max(row_index - win_count, -1)
    max_row_index = min(row_index + win_count, len(board))

    right_win_value = get_right_win_values(board, row_index, col_index, max_col_index)
    left_win_condition = get_left_win_values(board, row_index, col_index, min_col_index)
    up_win_condition = get_up_win_values(board, row_index, col_index, min_row_index)
    down_win_condition = get_down_win_values(board, row_index, col_index, max_row_index)

    up_left_win_condition = get_up_left_win_values(board, row_index, col_index, min_row_index, min_col_index)
    up_right_win_condition = get_up_right_win_values(board, row_index, col_index, min_row_index, max_col_index)
    down_left_win_condition = get_down_left_win_values(board, row_index, col_index, max_row_index, min_col_index)
    down_right_win_condition = get_down_right_win_values(board, row_index, col_index, max_row_index, max_col_index)

    possible_win_condition = [
        right_win_value,
        left_win_condition,
        up_win_condition,
        down_win_condition,
        up_right_win_condition,
        up_left_win_condition,
        down_right_win_condition,
        down_left_win_condition
    ]

    # return len(up_win_condition) == win_count and len(set(up_win_condition)) == 1
    for values in possible_win_condition:
        if len(values) == win_count and len(set(values)) == 1:
            return True
    return False


def is_player_choice_valid(board, player_choice):
    is_col_index_valid = 0 <= player_choice < len(board[0])
    has_col_space = is_col_index_valid and board[0][player_choice] is None
    return is_col_index_valid and has_col_space


def play(board):
    current_player, other_player = 1, 2
    while True:
        player_choice = get_player_choice(current_player)
        if not is_player_choice_valid(board, player_choice):
            print("Wrong column, try again!")
            continue
        row_index, col_index = apply_player_choice(board, player_choice, current_player)
        if check_win_condition(board, row_index, col_index, 4):
            print(f"Player {current_player} wins!")
            break

        print_board(board)
        current_player, other_player = other_player, current_player


def create_board(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def print_board(board):
    def get_value(value):
        if value in None:
            return 0
        return value

    for row in board:
        print([x if x is not None else 0 for x in row])


board = create_board(6, 7)

play(board)
