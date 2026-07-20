rows = 7

for i in range(rows):

    # Digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
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
