def write_to_file(file_path, mode, text):
    file = open(file_path, mode)
    file.write(text)
    file.close()

write_to_file("files/numbers.txt", "w", """
NEW 5""")
