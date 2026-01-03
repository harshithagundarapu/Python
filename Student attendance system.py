students = []

while True:
    print("1.Add Student  2.View  3.Exit")
    ch = input("Choose: ")

    if ch == '1':
        students.append(input("Student name: "))
    elif ch == '2':
        print("Students:", students)
    elif ch == '3':
        break
