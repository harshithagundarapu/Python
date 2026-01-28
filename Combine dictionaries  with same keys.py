d1 = {"a": 10, "b": 20}
d2 = {"a": 30, "b": 40}

result = {}

for key in d1:
    result[key] = d1[key] + d2[key]

print(result)
