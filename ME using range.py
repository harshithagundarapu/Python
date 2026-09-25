def find_missing(nums):
    n = len(nums)
    result = []

    for i in range(1, n + 1):
        if i not in nums:
            result.append(i)

    return result


# Example 1
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_missing(nums))

# Example 2
nums = [1, 1]
print(find_missing(nums))
