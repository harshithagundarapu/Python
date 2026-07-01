rows = 7

for i in range(rows):
    if i == 0:
        print("   *   ")
    elif i == rows // 2:
        print(" ***** ")
    else:
        print("*     *")
