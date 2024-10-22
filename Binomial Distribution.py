from math import factorial

def binomial_distribution(x, y, p): # Binomial Distribution
    
    if isinstance(y, int):
        return math.comb(x, y) * p**y * (1 - p)**(x - y)
    else:
        return sum([math.comb(x, n) * p**n * (1 - p)**(x - n) for n in y])

binomial_distribution(4, 0, 0.1) # test
