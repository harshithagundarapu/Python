from collections import defaultdict

d = defaultdict(int)
items = ["apple", "banana", "apple", "orange"]

for item in items:
    d[item] += 1

print(dict(d))
