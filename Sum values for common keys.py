d1 = {"a": 10, "b": 20}
d2 = {"a": 30, "b": 40}
result = {}

for k in d1:
    result[k] = d1[k] + d2[k]

print(result)
