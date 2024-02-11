# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

import re

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def C(k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))

def list_to_string(terms, variable):
    result = []
    for coef, exp in reversed(terms):

        if coef == 1 and exp != 0:
            term = f"{variable}" if exp == 1 else f"{variable}^{exp}"
        elif coef == -1 and exp != 0:
            term = f"-{variable}" if exp == 1 else f"-{variable}^{exp}"
            
        else:
            if exp == 0:
                term = str(coef)
            elif exp == 1:
                term = f"{coef}{variable}"
            else:
                term = f"{coef}{variable}^{exp}"

        result.append(term)

    return "+".join(result).replace("+-", "-")
    

def expand(expr):
    x = re.findall(r'[a-z]', expr)[0]
    a = int(re.findall(r'\((\-?\d+)[a-z]', expr)[0] if re.findall(r'\((\-?\d+)[a-z]', expr) else (-1 if re.findall(r'\-[a-z]', expr)else 1))
    b = int(re.findall(r'[a-z]([\-\+]\d+)', expr)[0])
    n = int(re.findall(r'\^(\d+)', expr)[0])
    
    result = []
    
    for k in range(n+1)[::-1]:
        result.append((C(k, n) * (a**(n-k)) * (b**k), n-k))
        
    result = [(int(coef), exp) for coef, exp in result]
        
    return list_to_string(result, x)

print(expand(input()))