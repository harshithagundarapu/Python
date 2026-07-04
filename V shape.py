rows = 5

for i in range(rows):
    print(" " * i + "*" + " " * (2 * (rows - i) - 3), end="")
    if i != rows - 1:
        print("*")
    else:
        print()
