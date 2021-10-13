from triangle import print_line, print_triangle
from mathematical_operations import perform_operation
from fibonacci_sequence import create_sequence, locate

# print_triangle(6)
#
# print(perform_operation(1.23, 4, "^"))

print(create_sequence(10))
print(locate(13))

try:
    print(create_sequence(3))
    print(locate(10))
except IndexError as err:
    print(err)