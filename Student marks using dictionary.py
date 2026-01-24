marks = {}
n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Subject name: ")
    score = int(input("Marks: "))
    marks[sub] = score

print(marks)
