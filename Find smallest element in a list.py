lst = list(map(int, input("Enter numbers: ").split()))
s = 0

for i in lst:
    if i % 2 == 0:
        s += i

print("Sum of even numbers:", s)
