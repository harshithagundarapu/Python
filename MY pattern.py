rows = 7

for i in range(rows):

    # M
    for j in range(5):
        if j == 0 or j == 4 or (i == j and i <= 2) or (i + j == 4 and i <= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Y
    for j in range(5):
        if (i == j and i <= 2) or (i + j == 4 and i <= 2) or (j == 2 and i >= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
