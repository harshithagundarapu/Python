number = int(input("Enter a number to print its multiplication table: "))
print("Multiplication table for {}:".format(number))
for i in range(1, 11):
print("{} x {} = {}".format(number, i, number * i))
