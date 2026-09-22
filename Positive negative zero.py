n = int(input("Enter a number: "))

for num in range(-n, n + 1):
    if num > 0:
        print(num, "Positive")
    elif num < 0:
        print(num, "Negative")
    else:
        print(num, "Zero")
