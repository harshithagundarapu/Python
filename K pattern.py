rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0 or i + j == rows // 2 or i - j == rows // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
