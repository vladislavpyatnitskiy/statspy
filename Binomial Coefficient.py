from math import factorial

def binom_coefficient(x, y): # Binomial Coefficient
    
    return factorial(x) / (factorial(y) * factorial(x - y))

print(binom_coefficient(59, 6)) # Test
