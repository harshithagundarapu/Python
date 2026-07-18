rows = 7

for i in range(rows):

    # Digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between digits

    # Digit 3
    for j in range(5):
        if i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
