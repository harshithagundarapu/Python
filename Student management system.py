students = []

while True:
    print("1.Add  2.View  3.Delete  4.Exit")
    ch = input("Choose: ")

    if ch == '1':
        students.append(input("Student name: "))
    elif ch == '2':
        print(students)
    elif ch == '3':
        students.remove(input("Name to delete: "))
    elif ch == '4':
        break
