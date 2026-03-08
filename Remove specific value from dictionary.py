d = {"a": 10, "b": 20, "c": 30}
val = int(input("Enter value to remove: "))

for k in list(d.keys()):
    if d[k] == val:
        del d[k]

print(d)
