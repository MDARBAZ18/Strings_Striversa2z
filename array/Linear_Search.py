""" write a program for the linear search algorithm """
def Linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
array = [10,5,23,1,89,3]
target = 23
result = Linear_search(array,target)
if result != -1:
    print("element found at index",result)
    
else:
    print("element not found ")

