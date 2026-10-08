T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    left_sum = 0
    found = False

    for i in range(n):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            found = True
            break

        left_sum += arr[i]

    if found:
        print("YES")
    else:
        print("NO")
