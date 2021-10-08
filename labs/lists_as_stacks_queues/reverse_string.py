s = input()

ss = []

for ch in s:
    ss.append(ch)

result = ""

while len(ss) > 0:
    result += ss.pop()

print(result)