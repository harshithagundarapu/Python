rows = 7

for i in range(rows):

    # H
    for j in range(5):
        if j == 0 or j == 4 or i == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # A
    for j in range(5):
        if (i == 0 and j != 0 and j != 4) or \
           (i == 3) or \
           ((j == 0 or j == 4) and i != 0):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # N
    for j in range(5):
        if j == 0 or j == 4 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # I
    for j in range(5):
        if i == 0 or i == rows - 1 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
