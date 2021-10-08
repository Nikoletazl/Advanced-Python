rows, cols = [int(x) for x in input().split()]
word = input()

matrix = []
word_idx = 0

for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = word[word_idx]
        else:
            matrix[row][cols - 1 - col] = word[word_idx]
        word_idx = (word_idx + 1) % len(word)

for elements in matrix:
    print("".join(elements))