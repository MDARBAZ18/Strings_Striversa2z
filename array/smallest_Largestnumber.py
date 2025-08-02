"""find the largest and smallest number in array using loops """
arr = [10,5,23,1,89,3]
smallest = largest = arr[0] # edar kounsa bhi assume karlo chalta zarruri ni ha index o lena bolke
for num in arr:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("smallest number is :",smallest )
print("largest number is :",largest )

# yeh dsa ke liye bhut acha hai , min , max dono bhi use karsakte for cp heapq laga sakte , sorting bhi use karsakte



#using min aur max array 
arr = [10,5,23,1,89,3]
print ("smallest number ",min(arr))
print("largest number",max(arr))




# using sorting in order to find the largest and smallest 
arr = [10,5,23,1,89,3]
arr.sort()
print("smallest number:",arr[0])
print("largeest number:",arr[-1])



# isme mein hein find the index for the smallest and largest values of the array 
arr = [10,5,23,1,89,3]
smallest = largest = arr[0] 
smallest_index = largest_index = 0

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i
    if arr[i] > largest:
        largest = arr[i]
        largest_index = i
        
        
print("smallest number is :",smallest ,"at index ",smallest_index )
print("largest number is :",largest ,"at index ",largest_index )