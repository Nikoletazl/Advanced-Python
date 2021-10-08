expression = input()

stack = []
balanced = True
pair = {
    "{": "}",
    "[": "]",
    "(": ")",
}
for ch in expression:
    if ch in "{[(":
        stack.append(ch)
    else:
        if len(stack) == 0:
            balanced = False
        last_opening_bracket = stack.pop()
        if pair[last_opening_bracket] != ch:
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")