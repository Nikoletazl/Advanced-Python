# file = open("file_opener.py")
#
# while True:
#     text = file.readlines(30)
#     print(text)
#     if not text:
#         break

def read_nth_line(file_path, n):
    file = open("file_reader.py")
    for i in range(n - 1):
        file.readline()
    return file.readline()


nth_line = 3
print(read_nth_line("file_reader.py", nth_line))
# i = 1
# for line in file.readlines():
#     print(f"{i}: {line}")
#     i += 1