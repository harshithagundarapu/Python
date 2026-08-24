for i in range(6):
    for j in range(11):
        if j >= 5-i and j <= 5+i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(3):
    for j in range(11):
        if 4 <= j <= 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
