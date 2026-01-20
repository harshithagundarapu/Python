lst = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

found = False
for i in range(len(lst)):
    if lst[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
