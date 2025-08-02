"""_summary_
  Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.



Return a string with the words in reverse order, concatenated by a single space.

example:
Input: s = "welcome to the jungle"

Output: "jungle the to welcome"
    """
def reverse_string(s):
    words = s.split()  
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
 
s = "hello world"
print(reverse_string(s))    
"""_summary_
step 1:# haar ek word ku list banna deta ya aur extra spacae remove karta    
# eg: " hello world "   if we use split() == ["hello","world"]  aisa aata 
step 2: # agar rang emein kuch bhi ni diye toh last number leta un theek hian 
step 3: # in kya karta bole toh reversed_words ke list mein jo elements hai na phatte
    # unku join karta un with a single space in between words of list 
    #theek hain ?
    """