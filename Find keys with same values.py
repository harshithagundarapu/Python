d = {"a": 10, "b": 20, "c": 10}
result = {}

for k, v in d.items():
    result.setdefault(v, []).append(k)

print(result)
