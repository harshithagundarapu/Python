rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if (j == 0 or
            j == cols - 1 or
            (i == j and i <= cols // 2) or
            (i + j == cols - 1 and i <= cols // 2)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
