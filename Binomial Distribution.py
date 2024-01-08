from math import factorial

def binomial_distribution(x, y, p): # Binomial Distribution
    
    return (factorial(x)/(factorial(y)*factorial(x-y)))*p**y*(1-p)**(x-y)
    
print(binomial_distribution(4, 0, 0.1)) # Test
