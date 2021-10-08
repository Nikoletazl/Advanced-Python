# def is_knight_placed(board, row, col):
#     board_size = len(board)
#     if row < 0 or col < 0 or row > board_size or col > board_size:
#         return False
#     return board[row][col] == "K"
#
#
# def count_affected_knights(board, row, col):
#     result = 0
#     if is_knight_placed(board, row - 2, col - 1):
#         result += 1
#     elif is_knight_placed(board, row - 2, col + 1):
#         result += 1
#     elif is_knight_placed(board, row + 2, col - 1):
#         result += 1
#     elif is_knight_placed(board, row + 2, col + 1):
#         result += 1
#     elif is_knight_placed(board, row - 1, col - 2):
#         result += 1
#     elif is_knight_placed(board, row - 1, col + 2):
#         result += 1
#     elif is_knight_placed(board, row + 1, col - 2):
#         result += 1
#     elif is_knight_placed(board, row + 1, col + 2):
#         result += 1
#     return result
#
#
# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append(list(input()))
#
# removed_knights = 0
#
# while True:
#     max_count, knight_row, knight_col = 0, 0, 0
#     for r in range(size):
#         for c in range(size):
#             if matrix[r][c] == "0":
#                 continue
#             count = count_affected_knights(matrix, r, c)
#             if count > max_count:
#                 max_count, knight_row, knight_col = count, r, c
#     if max_count == 0:
#         break
#     matrix[knight_row][knight_col] = "0"
#     removed_knights += 1
#
# print(removed_knights)

rows = int(input())

matrix = []
horses = 0

for i in range(rows):
    row = input()
    matrix.append([])
    for char in range(len(row)):
        matrix[i].append(row[char])

for row in range(1, len(matrix)):
    while ' ' in matrix[row]:
        matrix[row].remove(' ')
    if row == 1:
        for index in range(len(matrix[row])):
            if index - 2 >= 0 and matrix[row - 1][index - 2] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1
            if index + 2 <= len(matrix[row]) - 1 and matrix[row - 1][index + 2] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1
    else:
        for index in range(len(matrix[row])):
            if index - 2 >= 0 and matrix[row - 1][index - 2] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1
            if index + 2 <= len(matrix[row]) - 1 and matrix[row - 1][index + 2] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1
            if index - 1 >= 0 and matrix[row - 2][index - 1] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1
            if index + 1 <= len(matrix[row]) - 1 and matrix[row - 2][index + 1] == matrix[row][index] == 'K':
                matrix[row][index] = 0
                horses += 1

print(horses)