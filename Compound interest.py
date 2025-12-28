p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

ci = p * (1 + r/100) ** t - p
print("Compound Interest:", ci)
