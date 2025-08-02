#write a code to check whether its a valid anagram hain ya ni bas 
def isanagram(s,t)->bool:
    if len(s) != len(t):
        return False
    from collections import Counter
    return Counter(s) == Counter(t)

"""_summary_

step1: defination of anagram 
def: anagram is word / phrase  formed by rearranging the letter of different word/phrase typically using all the original
letters exactly onces is called as anagram 
step2: counter ek built in hain vo ke libraby / module hain collection ka
step3: counter count karta ek ek letter ka aisa 
step4: hello hain samhjo h:1 , l:2 , o:1 aisa count karta 
step 5: hello  == olleh aisa if sahi toh true aata 
step 6 : yeh ek important question hain medium level of string 
    """