rows = 7

for i in range(rows):

    # First digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")  # Space between the two digits

    # Second digit 1
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
