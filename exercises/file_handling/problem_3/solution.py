import os

while True:
    line = input()
    if line == "End":
        break
    args = line.split("-")
    command = args[0]
    file_name = args[1]
    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        content = args[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")
    elif command == "Replace":
        old_str = args[2]
        new_str = args[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                content = file.read().replace(old_str, new_str)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print("An error occurred")
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")


