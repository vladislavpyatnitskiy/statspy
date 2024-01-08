def binomial_distribution(x, y, p): # Binomial Distribution
    
    if y == 0: # When y = 0 => 0! = 1
        
        result = (prod(range(1, x + 1)) /
                  (prod(range(1,1))*prod(range(1,x-y+1))))*p**y*(1-p)**(x-y)
    else:
        # For other cases
        result = (prod(range(1, x + 1)) /
                  (prod(range(1,y+1))*prod(range(1,x-y+1))))*p**y*(1-p)**(x-y)
    
    return result

print(binomial_distribution(4, 0, 0.1)) # Test
