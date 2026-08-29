for i in range(11):
    for j in range(11):

        if (i == 0 and 3 <= j <= 7) or \
           (i == 1 and (j == 2 or j == 8)) or \
           (2 <= i <= 8 and (j == 1 or j == 9)) or \
           (i == 9 and (j == 2 or j == 8)) or \
           (i == 10 and 3 <= j <= 7) or \
           (i == 3 and (j == 3 or j == 7)) or \
           (i == 5 and j == 5) or \
           (i == 7 and 4 <= j <= 6):

            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
