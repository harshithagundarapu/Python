for i in range(11):
    for j in range(21):

        if i == 0 and 6 <= j <= 14:
            print("*", end=" ")

        elif i == 1 and (j == 4 or j == 16):
            print("*", end=" ")

        elif 2 <= i <= 8 and (j == 3 or j == 17):
            print("*", end=" ")

        elif i == 9 and (j == 4 or j == 16):
            print("*", end=" ")

        elif i == 10 and 6 <= j <= 14:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
