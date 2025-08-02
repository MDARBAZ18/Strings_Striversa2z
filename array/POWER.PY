# write a code to find out the code for the power value 
def pow(n,x):
    base = x
    power = n
    result = 1
    if base < 0 :
        base = 1/base
        power = -power
    while power > 0:
        if power % 2 == 1:
            result *= base
            
        base *= base
        power //= 2 
    return result
print (" the power of given number is :",pow(3,5))
        
           
# time complexity kya hogi ? iski? o(N) kya yeh sahi hai hain bilkul sahi hain bhai 