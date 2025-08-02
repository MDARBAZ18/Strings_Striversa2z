def maxSubArrayBruteForce(nums):
    n = len(nums)
    max_sum = float('-inf')
    start = end = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    return max_sum, start, end
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result, start, end = maxSubArrayBruteForce(nums)
print("Brute Force → Max Sum:", result)
print("Subarray:", nums[start:end+1])



