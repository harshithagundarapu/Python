binary = input("Enter binary number: ")
decimal = int(binary, 2)

hex_digits = "0123456789ABCDEF"
hex_num = ""

while decimal > 0:
    hex_num = hex_digits[decimal % 16] + hex_num
    decimal //= 16

print("Hexadecimal:", hex_num)
