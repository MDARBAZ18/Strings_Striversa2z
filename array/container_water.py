# write a code to find out the max area of water it can store in the container 
# using brute force karsakte but optimization is a concern so that the reason here i using 2 pointer
def max_water(container):
    left = 0
    right = len(container)-1 
    max_water = 0
    while left < right:
        width = right - left
        height = min(container[left],container[right])
        area = width * height
        max_water = max(max_water,area)
        
        if container[left] < container[right]:
            left += 1
        else:
            right -= 1
    return max_water
container = [1,8,6,2,5,4,8,3,7]
print(max_water(container))
        
        
# using brute force karenge ab theek hain 
def max_water(container):
    for i in range(len(container)):
        max_water = 0
        for j in range(i+1,len(container)):
            width = j -i
            height = min(container[i],container[j])
            area = width*height
            max_water = max(max_water,area)
    return max_water
container = [1,8,6,2,5,4,8,3,7]
print(max_water(container))
# leetcode 11 question hai yeh 
            
🔢 LeetCode Top 50 Array Questions List
✅ Level 1: Easy (Basics - Logic & Traversal)
Two Sum

Best Time to Buy and Sell Stock

Remove Duplicates from Sorted Array

Move Zeroes

Contains Duplicate

Intersection of Two Arrays

Plus One

Merge Sorted Array

Find the Difference

Maximum Subarray (Kadane's Algo)

🧠 Level 2: Medium (Greedy, Prefix, Sliding Window)
Product of Array Except Self

3Sum

Set Matrix Zeroes

Rotate Array

Find Minimum in Rotated Sorted Array

Search in Rotated Sorted Array

Subarray Sum Equals K

Longest Consecutive Sequence

Spiral Matrix

Jump Game

🧩 Level 3: Medium (Binary Search, Prefix + Suffix, Extra Space)
Minimum Size Subarray Sum

Merge Intervals

Insert Interval

Sort Colors (Dutch Flag)

Kth Largest Element in Array

Top K Frequent Elements

Majority Element

Maximum Product Subarray

Maximum Points You Can Obtain from Cards

Gas Station

🔥 Level 4: Hard (Advanced Patterns & Optimization)
Trapping Rain Water

Median of Two Sorted Arrays

First Missing Positive

Maximum Subarray Sum with One Deletion

Sliding Window Maximum

Count of Smaller Numbers After Self

Burst Balloons

Merge K Sorted Arrays

Largest Rectangle in Histogram

Find Median from Data Stream

💎 Bonus 10 – Real Interview Tricky/Useful
XOR Queries of Subarray

Find Pivot Index

Range Sum Query – Immutable

Count Inversions in Array

Random Pick with Weight

Minimum Number of Arrows to Burst Balloons

Number of Subarrays with Bounded Maximum

Max Area of Island (Matrix as array)

Monotonic Array

Longest Mountain in Array
    
   
        
    