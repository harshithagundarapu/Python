name = input("Enter your name: ").upper()

for row in range(7):
    for ch in name:
        if ch == 'A':
            if ((row == 0 and ch != ' ') or row == 3 or row == 6):
                print("* ", end="")
            else:
                print("* ", end="")
        else:
            print("* ", end="")
    print()
