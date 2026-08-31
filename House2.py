# Roof
for i in range(5):
    for j in range(9):
        if j == 4 - i or j == 4 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# House
for i in range(6):
    for j in range(9):

        if j == 0 or j == 8:
            print("*", end=" ")

        elif i == 0 or i == 5:
            print("*", end=" ")

        elif i == 2 and (j == 2 or j == 3 or j == 5 or j == 6):
            print("*", end=" ")

        elif i == 3 and (j == 2 or j == 3 or j == 5 or j == 6):
            print("*", end=" ")

        elif i >= 3 and 4 <= j <= 5:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
