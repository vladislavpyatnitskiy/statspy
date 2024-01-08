from math import factorial

def permutation_coefficient(x, y): # Permutation Coefficient
    
    return factorial(x) / factorial(x - y)
    
print(permutation_coefficient(5, 2)) # Test
