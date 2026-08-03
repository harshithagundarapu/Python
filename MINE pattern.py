rows = 7

for i in range(rows):

    # M
    for j in range(5):
        if j == 0 or j == 4 or (i == j and i <= 2) or (i + j == 4 and i <= 2):
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
    print("  ", end="")

    # N
    for j in range(5):
        if j == 0 or j == 4 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # E
    for j in range(5):
        if j == 0 or i == 0 or i == 3 or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
