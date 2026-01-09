num = int(input("Enter number: "))
s = sum(int(d) for d in str(num))

if num % s == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
