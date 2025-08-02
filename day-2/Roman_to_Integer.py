"""_summary_
Roman numerals are represented by seven different symbols:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Roman numerals are typically written from largest to smallest, left to right. However, in specific cases, a smaller numeral placed before a larger one indicates subtraction.

The following subtractive combinations are valid:

I before V (5) and X (10) → 4 and 9
X before L (50) and C (100) → 40 and 90
C before D (500) and M (1000) → 400 and 900

Given a Roman numeral, convert it to an integer
    """
    
def Roman_to_Integer(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev = 0
    for ele in reversed(s):
        value = roman[ele]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total
s = "VVV"
print(Roman_to_Integer(s))

"""_summary_


STEP 1: Phele ek dicitionary banno ke diya un toh direct aapan inut lere usku theek hian 
step 2: total aur prev value count karna asia 

step3:ek loop chala do aur reversed kyu ? 🧠 Roman Numeral Rule:
Roman numerals mein right to left read karna useful hota hai, kyunki:

Jab chhota symbol bada ke left me hota hai → Subtraction hoti hai

step 4:
assgin kro roman ke char ku value ke saath 

step5:
agar value < prev ke chota rehi toh - karo 

step6: agar zayada hain toh + karo 




    """