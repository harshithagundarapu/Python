for i in range(9):
    for j in range(9):
        if j == i or j == 8 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
