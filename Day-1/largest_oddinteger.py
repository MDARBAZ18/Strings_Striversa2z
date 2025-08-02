# write a code for the largest odd integer
def largest_odd_integer(s):
    n = len(s)
    max_odd = ""
    for i in range(n):
        
        if s[i] == "0":
            continue
        for  j in range(n-1,i-1,-1):
            if int(s[j])%2 ==1:  # last digit check karo
                sub = s[i:j+1]
                if sub[0] != "0":
                    if max_odd == "" or int(sub) > int(max_odd):
                        max_odd = sub
                        
                    break
    return max_odd  # loop ke bahar
s ="007524"
print(largest_odd_integer(s))
         
         
# iska process boltu dekho 
"""
1) phele zero hai kya check karta then usku skip karta okay ?
2) phir se ek loop run hota edar j un backtrack karta aur udar tak elemenet banna tha jidar i ke value  
zero ni aari theek hian  , aur saath mein odd hian kya check karta bhi 
3) ek alag se substring baana re edar sub bolke
4) usme kidar se kidar tak ke elements hona we store in it
5) if sub[0] != 0  then it must be either max_odd = 0  or int(sub) > int(max_odd)
6 ) thats it bro game over 
"""               
            