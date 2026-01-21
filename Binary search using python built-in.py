import bisect

arr = sorted(list(map(int, input("Enter elements: ").split())))
key = int(input("Enter element: "))

index = bisect.bisect_left(arr, key)

if index < len(arr) and arr[index] == key:
    print("Element found at index", index)
else:
    print("Element not found")
