#Sort Characters by Frequency
"""
You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.

If two or more characters have same frequency then arrange them in alphabetic order. """

def sort_character_frequency(s):
    from collections import Counter
    freq = Counter(s)
    return sorted(freq,key = lambda ch:(-freq[ch],ch))

"""_summary_

step1: counter ke through count karna kounsa alphabet kitne baar aaya theek hian 

step2: edar aapne ku alphabeetic ni uske frequencey matlab un kitne baar aaya uske hisab se sort karna 

hello h:1,e:1,l:2,0:1  isme phele l aaya uske bad sab 1 hain ryt
alphabetic ke hisab se aate 

step3: aur yeh -freq isliye lekh bcz ( desceending == bade se chota elements hona aappne ku )








    """