d = {"a": 1, "b": 2, "c": 3}
inv = {}

for k, v in d.items():
    inv[v] = k

print(inv)
