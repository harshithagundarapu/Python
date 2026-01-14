lst = list(map(int, input("Enter numbers: ").split()))
max_num = lst[0]

for i in lst:
    if i > max_num:
        max_num = i

print("Maximum:", max_num)
