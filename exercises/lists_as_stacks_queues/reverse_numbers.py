stack = input().split()

result = []

while stack:
    el = stack.pop()
    result.append(el)

print(" ".join(result))