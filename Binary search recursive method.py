def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = sorted(list(map(int, input("Enter elements: ").split())))
key = int(input("Enter element: "))

result = binary_search(arr, 0, len(arr) - 1, key)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")
