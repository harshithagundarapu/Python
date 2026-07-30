rows = 7

for i in range(rows):

    # Digit 3
    for j in range(5):
        if i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between digits

    # Digit 7
    for j in range(5):
        if i == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
