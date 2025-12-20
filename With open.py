    with open("sample.txt", "r") as file:
    first_line = file.readline()       # Read the first line
    words = first_line.split()         # Split into words

    print("Words in the first line:")
    for word in words:
        print(word)
