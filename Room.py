for i in range(15):
    for j in range(25):

        # Ceiling
        if i == 0:
            print("*", end=" ")

        # Walls
        elif j == 0 or j == 24:
            print("*", end=" ")

        # Window
        elif 3 <= i <= 6 and (j == 5 or j == 10):
            print("*", end=" ")
        elif (i == 3 or i == 6) and 5 <= j <= 10:
            print("*", end=" ")

        # Door
        elif 8 <= i <= 13 and (j == 15 or j == 20):
            print("*", end=" ")
        elif i == 8 and 15 <= j <= 20:
            print("*", end=" ")

        # Floor
        elif i == 14:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
