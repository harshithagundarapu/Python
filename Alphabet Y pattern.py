rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if (i <= rows // 2 and (j == i or j == cols - 1 - i)) or \
           (i > rows // 2 and j == cols // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
