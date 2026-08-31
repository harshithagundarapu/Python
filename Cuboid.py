for i in range(10):
    for j in range(20):

        if i == 0 and 5 <= j <= 14:
            print("*", end="")

        elif i == 1 and (j == 4 or j == 15):
            print("*", end="")

        elif i == 2 and (j == 3 or j == 16):
            print("*", end="")

        elif i == 3 and (j == 2 or j == 17):
            print("*", end="")

        elif 3 <= i <= 8 and (j == 2 or j == 11 or j == 17):
            print("*", end="")

        elif i == 8 and 2 <= j <= 17:
            print("*", end="")

        else:
            print(" ", end="")

    print()
