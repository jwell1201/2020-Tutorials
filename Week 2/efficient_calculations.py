# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fact(n):
    """Calculate n!"""
    if n == 0:
        return 1
    return n * fact(n-1)


print(f"5! is equal to {fact(5)}")

def oldExpTaylor(n, x):
    """Calculate exp(x) with n terms.
    
    1.19ms <- Run `%timeit oldExpTaylor(100, 5)` in iPython
    """
    output = 0
    for k in range(n):
        output += x**k / fact(k)
        
    return output


def expTaylor(n, x):
    """Calculate exp(x) with n terms.
    
    10.3us <- Run `%timeit expTaylor(100, 5)` in iPython
    
    Rationale
    ---------
    Term 1. x**1 / fact(1) = x / 1
    Term 2. x**2 / fact(2) = x*x / (1*2) = Term 1 * x/2
    Term 3. x**3 / fact(3) = x*x*x / (1*2*3) = Term 2 * x/3
    Term 4. x**4 / fact(4) = x*x*x*x / (1*2*3*4) = Term 3 * x/n
    ...
    Term k. x**k / fact(k) = Term (k-1) * x/k
    """
    term   = 1
    output = term  # Start with the first term, to avoid ZeroDivisionError
    for k in range(1, n):
        term   *= x / k
        output += term        
    return output


print(f"exp(2) is approximately {expTaylor(100, 2)}")
