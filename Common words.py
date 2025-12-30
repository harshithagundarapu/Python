s1 = input("Enter sentence 1: ").split()
s2 = input("Enter sentence 2: ").split()

common = set(s1) & set(s2)
print("Common words:", common)
