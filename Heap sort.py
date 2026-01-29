import heapq

arr = list(map(int, input("Enter elements: ").split()))
heapq.heapify(arr)

sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
print("Sorted list:", sorted_arr)
