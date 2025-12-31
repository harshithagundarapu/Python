a = int(input("Enter a: "))
b = int(input("Enter b: "))

while b:
    a, b = b, a % b

print("GCD:", a)
