lst = list(map(int, input("Enter numbers: ").split()))
lst = list(set(lst))
lst.sort()

print("Second largest:", lst[-2])
