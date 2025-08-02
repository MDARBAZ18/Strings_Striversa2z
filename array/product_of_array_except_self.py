# write a code inorder to find the product of array except itself
def product(nums):
    n = len(nums)
    res = [i]*n
    left = 1
    for i in range(n):
        
        res[i] = left
        left *= nums[i]
    
    right = 1
    for i in reversed(range(n)):
        right
        right *= nums[i]