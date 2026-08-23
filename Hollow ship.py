for i in range(10):
    for j in range(21):

        if i == 0 and j == 10:
            print("*", end=" ")

        elif i == 1 and j == 10:
            print("*", end=" ")

        elif i == 2 and 7 <= j <= 13:
            print("*", end=" ")

        elif i == 3 and (j == 7 or j == 13):
            print("*", end=" ")

        elif i == 4 and (j == 7 or j == 13):
            print("*", end=" ")

        elif i == 5 and (j == 7 or j == 13):
            print("*", end=" ")

        elif i == 6 and 4 <= j <= 16:
            print("*", end=" ")

        elif i == 7 and (j == 3 or j == 17):
            print("*", end=" ")

        elif i == 8 and (j == 4 or j == 16):
            print("*", end=" ")

        elif i == 9 and 5 <= j <= 15:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
