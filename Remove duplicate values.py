data = {"a": 10, "b": 20, "c": 10}
unique = {}

for k, v in data.items():
    if v not in unique.values():
        unique[k] = v

print(unique)
