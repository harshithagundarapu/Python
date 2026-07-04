rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if (j == i and i < rows - 1) or (j == cols - 1 - i and i < rows - 1):
            print("*", end="")
        elif i == rows - 1 and j == cols // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
