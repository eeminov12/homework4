def readfile(file, counter, write_list):
    with open(str(file), "r") as f:
        lines = f.readlines()
        line = lines[counter]
        if line.strip() == "$$$":
            while True:
                new_line = input("Enter a line:")
                if len(new_line.split(" ")) > 2:
                    write_list.append(new_line+"\n")
                    print(f"Line {new_line.strip()} was added manually.")
                    break
                else:
                    print("Print 3 words or more")
                    continue
        else:
            write_list.append(line)
            print(f"Line {line.strip()} was added automatically.")
        counter += 1
    return write_list, counter


def writefile(rewrite_list):
    with open("script.txt", "w") as f:
        for line in rewrite_list:
            f.write(line)

line_list = []
file_1 = "chapter1.txt"
file_2 = "chapter2.txt"
file_1_counter = 0
file_2_counter = 0


while True:
    with open(file_1, "r") as f1, open(file_2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    max_lines = max(len(lines1), len(lines2))
    for iteration in range(max_lines):
        if file_1_counter < len(lines1):
            line_list, file_1_counter = readfile(file_1, file_1_counter, line_list)
        else:
            pass
        if file_2_counter < len(lines2):
            line_list, file_2_counter = readfile(file_2, file_2_counter, line_list)
        else:
            pass
    break
writefile(line_list)






