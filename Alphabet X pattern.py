rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if i == j or i + j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
