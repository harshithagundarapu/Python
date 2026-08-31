for i in range(8):
    for j in range(16):

        if i == 0 and 4 <= j <= 10:
            print("*", end=" ")

        elif i == 1 and (j == 3 or j == 11):
            print("*", end=" ")

        elif i == 2 and (j == 2 or j == 12):
            print("*", end=" ")

        elif i == 3 and (j == 1 or j == 5 or j == 9 or j == 13):
            print("*", end=" ")

        elif i == 4 and (j == 1 or j == 5 or j == 9 or j == 13):
            print("*", end=" ")

        elif i == 5 and (j == 1 or j == 5 or j == 9 or j == 13):
            print("*", end=" ")

        elif i == 6 and (j == 1 or j == 5 or j == 9 or j == 13):
            print("*", end=" ")

        elif i == 7 and 1 <= j <= 13:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
