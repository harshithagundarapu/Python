rows = 7

for i in range(rows):

    # Digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between digits

    # Digit 4
    for j in range(5):
        if (j == 0 and i < rows // 2) or j == 4 or i == rows // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
