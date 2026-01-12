num = int(input("Enter decimal number: "))
hex_digits = "0123456789ABCDEF"
hex_num = ""

while num > 0:
    hex_num = hex_digits[num % 16] + hex_num
    num //= 16

print("Hexadecimal:", hex_num)
