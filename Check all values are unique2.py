d = {"a": 10, "b": 20, "c": 30}
values = list(d.values())

if len(values) == len(set(values)):
    print("All values are unique")
else:
    print("Duplicate values found")
