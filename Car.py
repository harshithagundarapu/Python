for i in range(9):
    for j in range(25):

        if i == 0 and 8 <= j <= 16:
            print("*", end=" ")

        elif i == 1 and (j == 7 or j == 17):
            print("*", end=" ")

        elif i == 2 and (j == 6 or j == 7 or j == 17 or j == 18):
            print("*", end=" ")

        elif i == 3 and (j == 5 or j == 6 or j == 18 or j == 19):
            print("*", end=" ")

        elif i == 4 and 3 <= j <= 21:
            print("*", end=" ")

        elif i == 5 and (j == 2 or j == 22):
            print("*", end=" ")

        elif i == 6 and (j == 2 or j == 5 or j == 6 or
                         j == 18 or j == 19 or j == 22):
            print("*", end=" ")

        elif i == 7 and (j == 3 or j == 4 or j == 20 or j == 21):
            print("*", end=" ")

        elif i == 8 and 3 <= j <= 21:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
