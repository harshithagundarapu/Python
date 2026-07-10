rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if ((i == 0 or i == rows - 2) and (j > 0 and j < cols - 2)) or \
           ((j == 0 or j == cols - 2) and (i > 0 and i < rows - 2)) or \
           (i == j and i >= rows // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
