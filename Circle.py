for i in range(13):
    for j in range(25):

        x = j - 12
        y = (i - 6) * 2

        if 130 <= x*x + y*y <= 180:
            print("*", end="")
        else:
            print(" ", end="")

    print()
