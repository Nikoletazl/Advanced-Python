punctuation_marks = {",", "?", "!", "'", "-", ":", ";", "_", '"'}

with open("text.txt", "r") as file, open("output.text", "w") as result:
    idx = 1
    for line in file:
        letters_count = 0
        punctuation_marks_count = 0
        for ch in line:
            if ch in punctuation_marks:
                punctuation_marks_count += 1
            elif ch.isalpha():
                letters_count +=1

        result.write(f"Line {idx}: {line.strip()} ({letters_count})({punctuation_marks_count})")
        result.write("\n")
        idx += 1



