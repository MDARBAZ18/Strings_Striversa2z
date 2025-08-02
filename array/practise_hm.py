""" practise questions hai phatte karo isme """
# write a function  code to calculate the sum and product of array
def sum_and_product(array):
    total_sum = 0
    total_product = 1
    
    for element in array :
        total_sum += element
        total_product *= element
    return total_sum,total_product
array = [1,2,3,4,5,6]
print (sum_and_product(array))


# waf to swap the max and min number of array 
def swap_max_min(array):
    smallest_num = array[0]
    largest_num = array[0]
    smallest_index = 0
    largest_index = 0
    
    for i in range(len(array)):
        if array[i] < smallest_num:
            smallest_num = array[i]
            smallest_index = i
        elif array[i] > largest_num:
            largest_num = array[i]
            largest_index = i
    
    array[smallest_index],array[largest_index] = array[largest_index],array[smallest_index]
    return array
array = [1,2,3,4,5,6]
print("after swaping the max and min values",swap_max_min(array))

#waf to print all the unique values in an array 
def unique_values(array):
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count == 1:
            print (array[i])
array = [1,2,2,3,3,3,5]
unique_values(array)
        
        
        
# or using sets bhi karsakte aapan 
def unique_values(array):
    unique_array = set(array)
    for element in unique_array:
        print (element)
array = [1,2,2,3,3,3,5]
unique_values(array)
        
        
#waf to print intersection of 2 arrays
    
            