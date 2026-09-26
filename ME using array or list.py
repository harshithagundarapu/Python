def find_missing(nums):
    n = len(nums)
    result = []

    for i in range(1, n + 1):
        if i not in nums:
            result.append(i)

    return result


nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
nums2 = [1, 1]

print("Example 1:", find_missing(nums1))
print("Example 2:", find_missing(nums2))
