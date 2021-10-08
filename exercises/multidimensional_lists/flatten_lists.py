sublist = input().split("|")

result = []

for idx in range(len(sublist) -1, -1, -1):
    elements = sublist[idx].split()
    result += elements

print(" ".join(result))