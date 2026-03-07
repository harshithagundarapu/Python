marks = {"A": 85, "B": 70, "C": 90}

for name, m in marks.items():
    if m >= 75:
        print(name, "Pass")
    else:
        print(name, "Fail")
