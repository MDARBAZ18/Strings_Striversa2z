# write a code to find out the majority element
# iska timecomplexity hain 0(n^2)
def majorityelement(array):
    for i in range(len(array)):
        count = 0 
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
            else :
                exit
        if count > len(array)//2:
            return array[i]
    return -1
        
array = [1,1,1,13,3]
print(majorityelement(array))
      
      
# using soritng karsakte aapan ? mlm let me show it  
# iska timecomplexity hain o(nlogn) agar sorting jidar use hora idar vo aata dekh yaad rakh le phatte 
def majorityelement(array):
    array.sort()
    return array[len(array)//2]
array = [1,2,2,1,1,1,1,13]
print("the majority element is : ",majorityelement(array))

# yeh optimze way hain dekho iska 
# iska tc hain 0(n)
def majroity_element(array):
    
    count  = 0
    candidate = None
    for ele in array:
        if count == 0:
            candidate = ele
        if candidate == ele:
            count   += 1
            
        else :
            count -= 1
    if array.count(candidate) > len(array)//2:
        return candidate
array = [3,3,4]
print (" the majority element is :",majroity_element(array))

