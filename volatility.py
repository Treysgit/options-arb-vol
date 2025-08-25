import sys
import math

class Volatility:

    # Calculates implied volatility of underlying stock
    @staticmethod
    def implied_vol(s, k, t, r, c, s_disc, k_disc):

        '''We must calculate the min and max of the possible
        implied volatlity values to employ a binary search'''

        # Call option bounds
        '''With no market uncertainty (vol = 0), the call price just 
        becomes the value of S(PV) - K(PV)'''
        intrin_lo = max(s_disc - k_disc, 0)
        '''With max market uncertanty (vol --> infinity), the call price becomes
        the value of S(PV) but never exceeds'''
        asym_hi = s_disc

        # Input validation - market inconsistency
        if c < intrin_lo or c >= asym_hi:
            sys.exit("No valid implied volatlity due to market incosistency")

        vol_lo = 0.0
        vol_hi = 1.0 # Conservative guess
        call_guess = Volatility.black_scholes_call(s, k, t, r, vol_hi, s_disc, k_disc) # Get call price at vol_hi
        vol_cap = 10.0 # Improbable cap

        # Increase vol_hi until its call price is greater than or equal to market call price
        while call_guess < c:
            vol_hi *= 2
            call_guess = Volatility.black_scholes_call(s, k, t, r, vol_hi, s_disc, k_disc) # Get call price at vol_hi

            # Sanity check
            if vol_hi > vol_cap:
                sys.exit("Implied volatility is improbably high - input error likely")

        # IL < C < AH
        # 1e-6 or 1/10^6 is our minimum difference in call price (market and estimate) to accept the implied volatlity estimate
        tol = 1e-6
        sigma = (vol_hi + vol_lo) / 2 # First guess is just the midpoint

        # Binary search to find implied volatlilty 
        while vol_hi - vol_lo > tol:
            sigma = (vol_hi + vol_lo) / 2 # Midpoint estimate
            call_guess = Volatility.black_scholes_call(s, k, t, r, sigma, s_disc, k_disc)

            # Increase call_est to call by increasing vol.
            # We shift up lower vol bound to midpoint (sigma)
            if call_guess < c : 
                vol_lo = sigma

            # Decrease call_est to call by decreasing vol.
            # We shift down upper vol bound to midpoint (sigma)
            else:
                vol_hi = sigma 
            
        return sigma
            

    # Calculates a call option price using the Black-Scholes model
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

        




        

        





    