d = {"a": 10, "b": 40, "c": 20}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_d)
