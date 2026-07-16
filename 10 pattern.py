rows = 7

for i in range(rows):
    # Digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between 1 and 0

    # Digit 0
    for j in range(5):
        if ((i == 0 or i == rows - 1) and (j > 0 and j < 4)) or \
           ((j == 0 or j == 4) and (i > 0 and i < rows - 1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
