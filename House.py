# Roof
for i in range(5):
    for j in range(9):
        if j == 4 - i or j == 4 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# House body
for i in range(5):
    for j in range(9):
        if i == 0 or i == 4 or j == 0 or j == 8:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
