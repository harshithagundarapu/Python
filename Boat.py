for i in range(11):
    for j in range(15):

        if (i == 0 and j == 7) or \
           (i == 1 and (j == 6 or j == 8)) or \
           (i == 2 and (j == 5 or j == 9)) or \
           (i == 3 and (j == 0 or j == 1 or j == 2 or j == 3 or
                        j == 4 or j == 5 or j == 6 or j == 7 or
                        j == 8 or j == 9 or j == 10 or j == 11 or
                        j == 12 or j == 13 or j == 14)) or \
           (i >= 4 and j == i - 4) or \
           (i >= 4 and j == 14 - (i - 4)):

            print("*", end="")
        else:
            print(" ", end="")

    print()
