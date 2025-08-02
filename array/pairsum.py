# write a code for the pair sum problem i need optimize code  tc = 0(n)
def pairsum(array,target):
    start = 0
    end = len(array)-1
    while start < end:
        if array[start]+array[end] == target:
            return ("the index value is ",start,end)
        elif array[start]+array[end] < target:
            start += 1
        else:
            end -= 1
    
array = [1,2,3,4,5]
target = 3
print(pairsum(array,target))


# agar brute force karke dekhenge bhai lets goo >> timecomplexity hain 0{n^2) 
def pairsumbf(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return i,j
            elif array[i]+array[j] < target:
                i+=1
            else:
                array[i]+array[j] > target
                j -= 1
array = [1,2,3,4,5]
target = 3
print(pairsumbf(array,target))