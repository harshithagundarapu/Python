rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        elif j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
