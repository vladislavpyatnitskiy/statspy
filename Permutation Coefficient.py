from math import prod

def permutation_coefficient(x, y): # Permutation Coefficient
    
    return prod(range(1, x + 1)) / prod(range(1, x - y + 1))

result = permutation_coefficient(59, 6) # Test
print(result)
