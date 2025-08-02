def maxsubarray_kalgo(array):
    max_sum = current_sum = array[0]
    start = end = s = 0
    for i in range(1,len(array)):
        if array[i] > current_sum+array[i]:
            current_sum = array[i]
            s = i
        else:
            current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
    return max_sum, start,end
array = [-2,1,-3,4,-1,2,1,-5,4]
result,start,end = maxsubarray_kalgo(array)
print("kalgo using the result is : ",result)
print("subarray is:",array[start:end+1])