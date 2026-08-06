rows = 5

# Upper half
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
