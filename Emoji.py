n = 7

for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1 or
            j == 0 or j == n - 1):
            print("*", end=" ")
        elif i == 2 and (j == 2 or j == 4):
            print("*", end=" ")
        elif i == 4 and j in range(2, 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
