def perform_operation(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "/":
        return num_1 / num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "^":
        return num_1 ** num_2
    else:
        raise ValueError("Operation must be one of the following: '+', '-', ..")
