def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        for i in range(*args):
            args = i * 1
        return args
    elif operator == "/":
        for i in range(*args):
            args = i / 1
        return args
    elif operator == "-":
        for i in range(*args):
            args = i - 1
        return args


print(operate("*", 3, 4))