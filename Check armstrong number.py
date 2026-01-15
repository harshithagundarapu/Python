num = int(input("Enter number: "))
temp = num
n = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** n
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
