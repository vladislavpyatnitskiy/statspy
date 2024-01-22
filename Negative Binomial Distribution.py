from math import factorial

def binomial_distribution_negative(x, y, p): # Negative Binomial Distribution
    if y == 0:
        print("Use Geometric Distribution Please")
    else:
        r=(factorial(x-1)/(factorial(y-1)*factorial(x-y-1)))*p**y*(1-p)**(x-y)
        return r

print(binomial_distribution_negative(4, 1, 0.9)) # Test
