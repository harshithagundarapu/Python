for i in range(5):

    # F
    for j in range(5):
        if j == 0 or i == 0 or i == 2:
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

    # V
    for j in range(5):
        if (i < 3 and (j == 0 or j == 4)) or (i == 3 and (j == 1 or j == 3)) or (i == 4 and j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print("   ", end="")

    # E
    for j in range(5):
        if j == 0 or i == 0 or i == 2 or i == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
