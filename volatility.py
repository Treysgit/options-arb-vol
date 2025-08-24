import sys
import math

class Volatility:

    @staticmethod
    def implied_vol(s, k, t, r, c, s_disc, k_disc):

        '''We must calculate the min and max of the possible
        implied volatlity values'''

        # Call bounds
        '''With no market uncertainty (vol = 0), the call price just 
        becomes the value of S(PV) - K(PV)'''
        vol_lo = max(s_disc - k_disc, 0)
        '''With max market uncertanty (vol --> infinity), the call price becomes
        the value of S(PV) but never exceeds'''
        vol_hi = s_disc

        # Input validation - market inconsistency
        if c < vol_lo or c > vol_hi:
            sys.exit("No valid implied volatlity due to market incosistency")

        # IL < C < AH
        # 1e-6 or 1/10^6 is our minimum difference in call price to accept the implied volatlity estimate
        tol = 1e-6
        sigma = (vol_hi + vol_lo) / 2 # First guess is just the midpoint
        c_est = Volatility.black_scholes_call(s, k, r, sigma, s_disc, k_disc)
        



    @staticmethod
    def black_scholes_call(s, k, t, r, sigma, s_disc, k_disc):
        # Edge cases - sigma = 0 instrinsic low, t = 0 option is exercised now
        if sigma <= 0.0 or t <= 0.0:
            return max(s_disc - k_disc, 0.0) 
        
        d1 = Volatility.d1(s, k, t, r, sigma) # How far the stock is above the strike today - adjusting for time and vol
        d2 = Volatility.d2(s, k, t, r, sigma) # How likely the stock is to finish above the strike at expiration
        n_d1 = Volatility.N(d1) # Fraction of today's stock price that matters in the value of the call option
        n_d2 = Volatility.N(d2) # Fraction of the PV of the strike that matters in the value of the call option

        # Return estimated call price
        return s * n_d1 - k_disc * n_d2
        
    # Higher vol, Higher d1
    @staticmethod
    def d1(s, k, t, r, sigma):
        return (math.log(s/k) + (r + 0.5 * sigma**2) * t)/(sigma * math.sqrt(t))

    # Higher vol, Lower d2
    @staticmethod
    def d2(s, k, t, r, sigma):
        return (math.log(s/k) + (r - 0.5 * sigma**2) * t)/(sigma * math.sqrt(t))
    
    '''The cumulative distribution function - of the standard normal distribution.
    i.e., the probability that a random variable is less than or equal to x on 
    a normal distribution'''
    @staticmethod
    def N(x):
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

        




        

        





    