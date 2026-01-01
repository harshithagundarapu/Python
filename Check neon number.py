num = int(input("Enter number: "))
sq = num * num
s = sum(int(d) for d in str(sq))

if s == num:
    print("Neon Number")
else:
    print("Not a Neon Number")
