import sys

class Volatility:

    def implied_vol(s, k, t, r, c, s_disc, k_disc):

        '''We must calculate the min and max of the possible
        implied volatlity values'''

        # Call bounds
        '''With no market uncertainty (vol = 0), the call price just 
        becomes the value of S(PV) - K(PV)'''
        in_lo = max(s_disc - k_disc, 0)
        '''With max market uncertanty (vol --> infinity), the call price becomes
        the value of S(PV) but never exceeds'''
        asym_hi = s_disc

        if c < in_lo or c > asym_hi:
            sys.exit("No valid implied volatlity due to market incosistency")

        # IL < C < AH
        # 1e-6 or 1/10^6 is our minimum difference in call price to accept the implied volatlity estimate
        tol = 1e-6
        

        

        





    