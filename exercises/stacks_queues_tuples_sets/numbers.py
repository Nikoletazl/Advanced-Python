first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    command_parameter = line_args[1]

    if command == "Add" and command_parameter == "First":
        [first.add(int(x)) for x in line_args[2:]]
    elif command == "Add" and command_parameter == "Second":
        [second.add(int(x)) for x in line_args[2:]]
    elif command == "Remove" and command_parameter == "First":
        current_set = set([(int(x)) for x in line_args[2:]])
        first = first.difference(current_set)
    elif command == "Remove" and command_parameter == "Second":
        current_set = set([(int(x)) for x in line_args[2:]])
        second = second.difference(current_set)
    else:
        print(first.issubset(second) or second.issubset(first))

print(", ".join([str(x) for x in sorted(first)]))
print(", ".join([str(x) for x in sorted(second)]))

