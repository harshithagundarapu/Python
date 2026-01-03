score = 0

if input("Python is interpreted? (yes/no): ").lower() == "yes":
    score += 1
if input("Python supports OOP? (yes/no): ").lower() == "yes":
    score += 1

print("Score:", score)
