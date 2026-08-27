for i in range(11):
    for j in range(21):

        if (i == 0 and j == 10) or \
           (i == 1 and (j == 9 or j == 10 or j == 11)) or \
           (i == 2 and (j == 8 or j == 9 or j == 10 or j == 11 or j == 12)) or \
           (i == 3 and (j == 7 or j == 8 or j == 9 or j == 10 or j == 11 or j == 12 or j == 13)) or \
           (i == 4 and j in range(21)) or \
           (i == 5 and 3 <= j <= 17) or \
           (i == 6 and 5 <= j <= 15) or \
           (i == 7 and 7 <= j <= 13) or \
           (i == 8 and 6 <= j <= 14) or \
           (i == 9 and (j == 5 or j == 15)) or \
           (i == 10 and (j == 4 or j == 16)):

            print("*", end="")
        else:
            print(" ", end="")

    print()
