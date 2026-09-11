number = 7092007

while number >= 10:
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    number = total

print("Digital Root:", number)
