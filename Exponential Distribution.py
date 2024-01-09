import numpy as np

def exponential_distribution(x, y): # Exponential Distribution
  
  return 1 - np.exp(-x * y)

exponential_distribution(15, .05) # Test
