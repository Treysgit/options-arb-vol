import discount
import arbitrage
import sys
import strategy
import volatility

'''Note - We presuppose that the options are European when using put-call 
parity, long straddle, and implied volatility - meaning the options
of the underlying assets can only be exercised at expiration.'''

def main():
    print("This program checks for put-call parity arbitrage, long straddle\n strategy,"
          " and also returns the implied volatility of the underlying asset.\n"
          "\nEnter the values for the stock, put, call, "
          "strike (shared), time to expiration (shared),\n" 
          "dividend yield, and risk-free rate."
    )

    # Receive stock, put, call, strike, expiration, dividend yield, 
    # and risk-free rate values from user
    s = abs(float(input("S: "))) # stock price
    p = abs(float(input("P: "))) # put premium
    c = abs(float(input("C: "))) # call premium
    k = abs(float(input("K: "))) # strike price
    t = abs(float(input("T (years): "))) # time to expiration
    q = abs(float(input("q: "))) # dividend yield
    r = abs(float(input("r: "))) # risk-free rate
    flag = str(input("Do you want to enter a minimum difference "
                       "for the put-call parity check (y/n): "))
    if flag.lower() == "y":
        min_diff = abs(float(input("Enter minimum difference: ")))
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
    if flag.lower() != "y":
        sys.exit()

    # Run long straddle strategy and print result to user
    strategy.Strategy.long_straddle(c, p, t, k)

    print("\n" + "_" * 40 + "\n")
    # Return implied volatility 
    flag = str(input("\nDo you want to calculate the implied volitility (y/n)? "))
    if flag.lower() != "y":
        sys.exit()
    imp_vol = volatility.Volatility.implied_vol(s, k, t, r, c, s_disc, k_disc)
    print(f"The implied volatility of the underlying asset (S = {s}): {imp_vol:.2f}")



if __name__ == "__main__":
    main()
