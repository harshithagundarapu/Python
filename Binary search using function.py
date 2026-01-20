def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = sorted(list(map(int, input("Enter elements: ").split())))
key = int(input("Enter element: "))

result = binary_search(arr, key)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")
