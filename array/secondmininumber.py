# write the code to find the 2 min number in hte array
def secondmininumber(nums):
    smallest = second = float("inf")
    for elem in nums:
        if elem < smallest:
            second  = smallest
            smallest = elem
        elif elem == second and  second != smallest:
            second  = elem
    return second
nums = [1,2,3,4]
print(secondmininumber(nums))