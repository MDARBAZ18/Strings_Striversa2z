# write the code for the remove all the outermost paranthesis
def outermost(s):
    count = 0 
    n = len(s)
    result = ""
    for element in s:
        if element == "(":
            if count > 0 :
                result += element
            count += 1
        elif element == ")":
            count -= 1
            if count > 0 :
                result += element
    return result
s = "(()())(())"
print(outermost(s))

"""_summary_
step1: ek flag create kare aapan count bolke (kuch bhi lekh sakte flag matlab aapne understanding ke liye samjho )
lekh liye okay??
step2: result starting mein empty rehti okay 
step3: iteration kare ek ek element in s string mein check kare agar ( yeh mila toh     
step4: count > 0 han kya check kro if not vo udhar break hota ,if count > 0 hain toh (  yeh result mein add hota 
step5: count ke value 0 -> 1 hoti 
step6: ek char hogaya ab sab aisi pura string check karna okay ?? 
step7: string = "(()())(())"
step8: iske index 2 pe ) yeh aaya toh count ke value -1 karo 
step9: phir check karo count ke value if zero se zayada hian toh ) yeh add kro result mein    
    
    
    
    """