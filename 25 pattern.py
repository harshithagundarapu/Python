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

    # Digit 5
    for j in range(5):
        if i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        elif i < rows // 2 and j == 0:
            print("*", end="")
        elif i > rows // 2 and j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
