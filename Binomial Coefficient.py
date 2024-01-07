from math import prod

def binom_coefficient(x, y): # Binomial Coefficient
    
    return prod(range(1, x + 1))/(prod(range(1,y+1))*prod(range(1, x - y + 1)))

binom_coefficient(59, 6) # Test
