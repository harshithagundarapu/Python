d = {"a": 10, "b": 20, "c": 10}
result = {}

for k, v in d.items():
    if v not in result.values():
        result[k] = v

print(result)
