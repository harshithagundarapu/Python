for i in range(10):
    for j in range(17):

        # Candle
        if i == 0 and j == 8:
            print("*", end=" ")
        elif i == 1 and j == 8:
            print("*", end=" ")

        # Flame
        elif i == 2 and 7 <= j <= 9:
            print("*", end=" ")

        # Top layer
        elif i == 3 and 4 <= j <= 12:
            print("*", end=" ")
        elif i == 4 and (j == 4 or j == 12):
            print("*", end=" ")

        # Cake body
        elif 5 <= i <= 8 and (j == 2 or j == 14):
            print("*", end=" ")
        elif i == 5 and 2 <= j <= 14:
            print("*", end=" ")
        elif i == 8 and 2 <= j <= 14:
            print("*", end=" ")

        # Plate
        elif i == 9 and 1 <= j <= 15:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
