for i in range(5):

    # N
    for j in range(5):
        if j == 0 or j == 4 or j == i:
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

    # N
    for j in range(5):
        if j == 0 or j == 4 or j == i:
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
