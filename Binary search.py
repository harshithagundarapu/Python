lst = sorted(list(map(int, input("Enter list: ").split())))
key = int(input("Enter element: "))

low, high = 0, len(lst)-1
found = False

while low <= high:
    mid = (low + high) // 2
    if lst[mid] == key:
        found = True
        break
    elif lst[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print("Found" if found else "Not Found")
