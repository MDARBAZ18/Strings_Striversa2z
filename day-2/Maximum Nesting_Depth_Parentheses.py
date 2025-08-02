#Maximum Nesting Depth of the Parentheses

"""A string s is a valid parentheses string (VPS) if it meets the following conditions:

It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
The parentheses are balanced and correctly nested.


Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string"""
def maxndp(s):
    max_depth = 0
    current_depth = 0
    for ele in s:
        if ele == "(":
            current_depth += 1
            max_depth = max(current_depth,max_depth)
        else:
            if ele == ")":
                current_depth -= 1
    return max_depth
s = "(((())))"
print(maxndp(s))

"""_summary_
step1: isme max-depth aur current -depth bolke 2 vairables leere acha samjh aana bolke yeh liye
warna kuch bhi le sakte theek hian ? 
aur usku zero initilaize karna theek hian 

step2: haar ek element iterate karna in string 

step3: agar (  aaya toh current_depht +=1 lena value theek hian aur max_depth find karna 
edar questin diya aapne ku max find karo bolke 

current_depth aur max_depth mein max leke == max_depht mein add kare aapan 

step4: agar ) hain toh -=1 kro khatam    
    
    
    
    """
 