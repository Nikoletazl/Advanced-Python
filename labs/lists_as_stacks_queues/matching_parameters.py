
expression = input()
parenthesis_indices = []

for index, ch in enumerate(expression):
    if ch == "(":
        parenthesis_indices.append(index)
    elif ch == ")":
        closing_index = index
        opening_index = parenthesis_indices.pop()
        print(expression[opening_index:closing_index + 1])

