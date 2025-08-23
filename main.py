import discount
import arbitrage
import sys
import strategy

'''Note - We presuppose that the options are European when using put-call 
parity, long straddle, and implied volatility - meaning the options
of the underlying assets can only be exercised at expiration.'''

def main():
    print("This program checks for put-call parity arbitrage, long straddle\n strategy,"
          " and returns implied volatility of the call/put option.\n"
          "\nEnter the prices for the stock, put, call, "
          "strike (shared), time to expiration (shared),\n" 
          "dividend yield, and risk-free rate."
    )

    # Receive stock, put, call, strike, expiration, dividend yield, 
    # and risk-free rate values from user
    s = float(input("S: "))
    p = float(input("P: "))
    c = float(input("C: "))
    k = float(input("K: "))
    t = float(input("T (years): "))
    q = float(input("q: "))
    r = float(input("r: "))
    flag = str(input("Do you want to enter a minimum difference "
                       "for the put-call parity check (y/n): "))
    if flag == "y" or flag == "Y":
        min_diff = float(input("Enter minimum difference: "))
    else:
        min_diff = 0.15 # default

    # Discount stock at expiration to present value - i.e. the value of not being the holder during the dividend period
    s_disc = discount.Discount.principal_discount(s, q, t)

    # Discount strike at expiration to present value - i.e. the value that can grow to the full amount at expiration via risk-free rate instrument
    k_disc = discount.Discount.principal_discount(k, r, t) 

    # Run put-call arbitrage test and print result to the user
    arbitrage.Arbitrage.put_call_parity(s_disc, p, c, k_disc, min_diff)

    print("\n" + "_" * 40 + "\n")
    flag = str(input("Do you want to run a long straddle strategy (y/n)? "))
    if flag != "y" and flag != "Y":
        sys.exit()

    # Run long straddle strategy
    strategy.Strategy.long_straddle(c, p, t, k)



    
    






if __name__ == "__main__":
    main()
