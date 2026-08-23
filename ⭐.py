for i in range(7):
    for j in range(13):

        if (i == 0 and j == 6) or \
           (i == 1 and 5 <= j <= 7) or \
           (i == 2 and 4 <= j <= 8) or \
           (i == 3) or \
           (i == 4 and 2 <= j <= 10) or \
           (i == 5 and 4 <= j <= 8) or \
           (i == 6 and 3 <= j <= 9):
            print("*", end="")
        else:
            print(" ", end="")

    print()
