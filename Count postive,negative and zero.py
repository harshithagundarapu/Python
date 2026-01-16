lst = list(map(int, input("Enter numbers: ").split()))
pos = neg = zero = 0

for i in lst:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
