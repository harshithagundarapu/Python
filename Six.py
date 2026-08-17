for i in range(5):

    # S
    for j in range(5):
        if i == 0 or i == 2 or i == 4:
            print("*", end="")
        elif i == 1 and j == 0:
            print("*", end="")
        elif i == 3 and j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("   ", end="")

    # I
    for j in range(5):
        if i == 0 or i == 4 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("   ", end="")

    # X
    for j in range(5):
        if j == i or j == 4 - i:
            print("*", end="")
        else:
            print(" ", end="")

    print()
