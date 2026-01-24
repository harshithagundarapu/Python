grades = ["A", "B", "A", "C", "B", "A"]
result = {}

for g in grades:
    result[g] = result.get(g, 0) + 1

print(result)
