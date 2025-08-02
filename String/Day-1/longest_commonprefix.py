# write a function to find the longest common prefix string amount an array of strings
def lsp(s):
    n = len(s)
    if not s:
        return " "
    prefix = s[0]
    
    for ele in s[1:]:
        while not ele.startswith(prefix):
            prefix  = prefix[:-1]
            if not prefix:
                return " "
    return prefix

s = ["flower" , "flow","fly","flight"]
print(lsp(s))    

# process boltu dekh phatte
"""
1) step 1: agar string hein ni hain toh empty return karo 
step 2: start element ku prefix bolke fix kardo phele theek hain
step 3: iterate elements in s from ranges 1 index to n-1 
step 4: if prefix is not found or not match or mismatch then prefix ku chota karo 
step 5: vo kaisa bole toh flower -> flowe -> flow -> flo -> fl -> f yeh sab prefix[:-1] ke wajah se hota
step 6: agar prefix ke bara ni raha toh simple return empty 
step 7 : game over khatam milte hain nextt question ke saath   
  
  
    """