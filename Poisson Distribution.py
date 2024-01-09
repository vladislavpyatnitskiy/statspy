from math import factorial
import numpy as np

def poisson_distribution(x, y): # Poisson Distribution
  
  return x ** y * np.exp(-x) / factorial(y)

poisson_distribution(3, 1) # Test
