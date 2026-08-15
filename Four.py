for i in range(5):

    # F
    for j in range(5):
        if j == 0 or i == 0 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print("   ", end="")

    # O
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("   ", end="")

    # U
    for j in range(5):
        if j == 0 or j == 4 or i == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("   ", end="")

    # R
    for j in range(5):
        if j == 0 or i == 0 or i == 2 or (j == 4 and i == 1) or (i == 3 and j == 3) or (i == 4 and j == 4):
            print("*", end="")
        else:
            print(" ", end="")

    print()
