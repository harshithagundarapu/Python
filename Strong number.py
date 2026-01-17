num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    fact = 1
    d = temp % 10
    for i in range(1, d+1):
        fact *= i
    sum += fact
    temp //= 10

print("Strong Number" if sum == num else "Not Strong")
