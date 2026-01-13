binary = input("Enter binary number: ")
decimal = int(binary, 2)
octal = ""

while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal //= 8

print("Octal:", octal)
