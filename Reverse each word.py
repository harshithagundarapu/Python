s = input("Enter sentence: ")
words = s.split()

for w in words:
    print(w[::-1], end=" ")
