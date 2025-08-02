""" write a program for the array inorder to reverse it """
# using 2 pointers hai yeh phatte samjha na 
array = [1,2,3,4,5,6]
left = 0
right = len(array)-1

while left < right :
    array[left],array[right] = array[right],array[left]
    left += 1
    right -= 1
print ("reversed array ",array)

# using direct reverse se karsakte aapan 
array = [1,2,3,4,5,6]
array.reverse()
print("reversed array is : ",array)

# using slicing karsakte aapan edar ek new array banta unchanged the real one 
array = [1,2,3,4,5,6]
reversed_array = array[::-1]
print("reversed array is ",reversed_array )