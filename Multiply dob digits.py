dob = "07092007"

product = 1

for digit in dob:
    product *= int(digit)

print("Product of DOB digits:", product)
