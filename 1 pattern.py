rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == cols // 2 or (i == rows - 1) or (i == 1 and j == cols // 2 - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
