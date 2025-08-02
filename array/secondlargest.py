#write a code inorder to find out the second largest number in array
def secondlargest(nums):
    largest = second = float("-inf") # negative infinity 
    for elem in nums:
        if elem > largest:    # 1 > -infinity hain toh 
            second = largest
            largest = elem
        elif elem > second and elem != largest:
            second = elem
    return second
nums = [1,2,3,4]
print(secondlargest(nums))