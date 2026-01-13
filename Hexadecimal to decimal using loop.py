hex_num = input("Enter hexadecimal number: ").upper()
hex_digits = "0123456789ABCDEF"
decimal = 0
power = 0

for digit in hex_num[::-1]:
    decimal += hex_digits.index(digit) * (16 ** power)
    power += 1

print("Decimal:", decimal)
