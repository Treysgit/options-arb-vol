import math
# If dividend paid before expiration:
#  S_adj = S * exp(-q * T)
# or S_adj = S - D (fixed dividend)

# Discount strike with risk-free rate:
# K_adj = K * exp(-r * T)



class Discount:
    
    # Basic continuous compound formula
    @staticmethod
    def principal_discount(principal, rate, expiration):
        discount = principal *  math.exp(-rate * expiration)
        return discount
    
    # Implement later on
    def discount_pandas():
        pass
    


