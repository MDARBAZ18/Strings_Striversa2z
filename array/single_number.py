# single number identify karna hain matlab ek list ya array mein twice elelment sku chod ke jo sirf ek baar aate
# usku single numbers bolte theek hain na 

def single_numbers(array):
    result = 0
    for elements in array:
        result ^= elements
    return result
array = [1,2,2]
print("the single numbers is :",single_numbers(array))
# yeh bhut efficient hai isliye yeh use kro acha rehta? okay ?