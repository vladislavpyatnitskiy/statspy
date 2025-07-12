from math import factorial
import numpy as np

def poisson_distribution(x, y): # Poisson Distribution
  
  if isinstance(y, int):
      return x ** y * np.exp(-x) / factorial(y)
  
  return sum([x ** n * np.exp(-x) / factorial(n) for n in y])

poisson_distribution(3, 1) # Test
