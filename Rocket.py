for i in range(12):
    for j in range(11):

        # Rocket top
        if i == 0 and j == 5:
            print("*", end=" ")
        elif i == 1 and 4 <= j <= 6:
            print("*", end=" ")
        elif i == 2 and 3 <= j <= 7:
            print("*", end=" ")

        # Rocket body
        elif 3 <= i <= 7 and (j == 2 or j == 8):
            print("*", end=" ")
        elif 3 <= i <= 7 and 4 <= j <= 6:
            print("*", end=" ")

        # Rocket bottom
        elif i == 8 and 3 <= j <= 7:
            print("*", end=" ")

        # Flames
        elif i == 9 and 4 <= j <= 6:
            print("*", end=" ")
        elif i == 10 and 3 <= j <= 7:
            print("*", end=" ")
        elif i == 11 and 4 <= j <= 6:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
