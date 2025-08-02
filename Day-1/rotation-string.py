#write a code to check whether s and goal , return true if na only if it can become goal after some no of shifts n s
# note isme leftmost se rightmost order mein changes karsakte bas 
# abcde -> bcdea -> cdeab aisa isku bolte leftmost to rightmost okay?

def rotationstring(s,goal)->bool:
    if len(s) != len(goal):
        return False
    return goal in (s+s)
    
    
s = "abcde"
goal = "cdeab"
print(rotationstring(s,goal))    

# process ku boltu wait 
"""
step1: phele length check karo iska if not same return false 
step2: check karo goal kya s+s add kare toh usme exist karta kya 
step3: abcdeabcde  ab ache se dekho isme goal already exist karta simple
step4: cdeab aara toh true result aata simple    
    """
    
# yeh strings ka medium question hain 
