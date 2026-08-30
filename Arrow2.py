for i in range(5):
    for j in range(9):

        if i == 2 and j <= 5:
            print("*", end=" ")

        elif i == 0 and j == 7:
            print("*", end=" ")

        elif i == 1 and (j == 6 or j == 7):
            print("*", end=" ")

        elif i == 3 and (j == 6 or j == 7):
            print("*", end=" ")

        elif i == 4 and j == 7:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
