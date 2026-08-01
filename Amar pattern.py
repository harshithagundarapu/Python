rows = 7

for i in range(rows):

    # A
    for j in range(7):
        if ((j == 0 or j == 6) and i != 0) or \
           (i == 0 and j == 3) or \
           (i == 3 and j > 0 and j < 6):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # M
    for j in range(7):
        if j == 0 or j == 6 or \
           (i == j and i <= 3) or \
           (i + j == 6 and i <= 3):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # A
    for j in range(7):
        if ((j == 0 or j == 6) and i != 0) or \
           (i == 0 and j == 3) or \
           (i == 3 and j > 0 and j < 6):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # R
    for j in range(6):
        if j == 0 or \
           (i == 0 and j < 5) or \
           (i == 3 and j < 5) or \
           (j == 5 and i > 0 and i < 3) or \
           (i - j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
