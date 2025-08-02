# write a jo similar ke usse replace karna 
def isomorphicstring(s,t) -> bool:
    
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    mapped_to_t = set()
    
    for cs,ct in zip(s,t):
        if cs in map_s_to_t:
            if map_s_to_t[cs] != ct:
                return False
        else:
            if ct in mapped_to_t:
                return False
            map_s_to_t[cs] = ct
            mapped_to_t.add(ct)
    return True

s = ["egg"]
t = ["add"]
print(isomorphicstring(s,t))

# process kya hain iska let me explain it
"""
step1: phele check kro two strings ke len if equal hain toh theekhain if not reeturn false
step2: mapping karna (dictionary ) 
step3: map_s_to_t -> { 'e':'a','g':'d'}
step4: mapped_ct isme setbanra edar duplicatae values allow ni hote matlab g -> d aaya samjh g->j aisa ni aata 
isliye set lere aapan okay 
step5: element in s,t aur zip ka matlab dono ku ek saath iterate kare matalb 
loop dono ku ek saath chala re bole jaisa uska matlab okay ??
step6:check kare element/char of s string ka map_s_to_t mein hain 
step7: agar cs != ct raha toh false return kro 
step 8: ab ct ku chek karo in mapped_to_t return false 
matlab g ke ek unique value rehan haar cheez ke ek uniquq value rehna ais a
step9:(dicitinary ) cs = ct isme assign kardena then 
step 10: set mein add karna char of t string 
step 11: problem over bhut easy tha bas  
    """