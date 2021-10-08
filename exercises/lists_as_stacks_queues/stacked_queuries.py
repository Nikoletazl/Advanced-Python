n = int(input())

stack = []

for _ in range(n):
    line_parts = input().split()
    command = line_parts[0]
    if command == "1":
        number = int(line_parts[1])
        stack.append(number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))
