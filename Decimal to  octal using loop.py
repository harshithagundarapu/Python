num = int(input("Enter decimal number: "))
octal = ""

while num > 0:
    octal = str(num % 8) + octal
    num //= 8

print("Octal:", octal)
