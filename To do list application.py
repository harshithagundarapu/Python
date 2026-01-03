tasks = []

while True:
    print("1.Add Task  2.View  3.Exit")
    ch = input("Choose: ")

    if ch == '1':
        tasks.append(input("Task: "))
    elif ch == '2':
        print(tasks)
    elif ch == '3':
        break
