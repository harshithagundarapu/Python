lst = [{"a": 1}, {"b": 2}, {"c": 3}]
result = {}

for item in lst:
    result.update(item)

print(result)
