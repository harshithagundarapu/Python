marks = {"A": 80, "B": 70, "C": 90}
avg = sum(marks.values()) / len(marks)

for s, m in marks.items():
    if m > avg:
        print(s)
