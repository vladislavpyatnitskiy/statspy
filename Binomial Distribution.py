from math import comb

def binomial_distribution(x, y, p): # Binomial Distribution
    
    if isinstance(y, int):
        return comb(x, y) * p**y * (1 - p)**(x - y)
    
    return sum([comb(x, n) * p**n * (1 - p)**(x - n) for n in y])

binomial_distribution(4, 0, 0.1) # test
