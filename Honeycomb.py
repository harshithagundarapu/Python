n = int(input("Enter a number: "))

for num in range(1, n + 1):
    if num % 2 == 0 and num % 3 == 0:
        print("honey comb")
    elif num % 2 == 0:
        print("honey")
    elif num % 3 == 0:
        print("comb")
    else:
        print(str(num))
