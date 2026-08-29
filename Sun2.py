
for i in range(11):
    for j in range(11):

        if (i == 0 and j == 5) or \
           (i == 10 and j == 5) or \
           (j == 0 and i == 5) or \
           (j == 10 and i == 5) or \
           (i == 2 and j == 2) or \
           (i == 2 and j == 8) or \
           (i == 8 and j == 2) or \
           (i == 8 and j == 8) or \
           (3 <= i <= 7 and 3 <= j <= 7):

            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
