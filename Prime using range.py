n = int(input("Enter a number: "))

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "Yes")
    else:
        print(num, "No")
