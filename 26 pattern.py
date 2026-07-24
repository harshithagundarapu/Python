rows = 7

for i in range(rows):

    # Digit 2
    for j in range(5):
        if i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        elif i < rows // 2 and j == 4:
            print("*", end="")
        elif i > rows // 2 and j == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between digits

    # Digit 6
    for j in range(5):
        if (i == 0 and j > 0) or \
           (i == rows // 2) or \
           (i == rows - 1 and j > 0) or \
           (j == 0 and i > 0 and i < rows - 1) or \
           (j == 4 and i > rows // 2 and i < rows - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
