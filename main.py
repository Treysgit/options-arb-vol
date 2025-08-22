import discount
import arbitrage

def main():
    print("This program checks for put-call parity arbitrage.\n"
    "Enter the prices for the stock, put, call, "
    "strike (shared), time to expiration (shared),\n" 
    "dividend yield, and risk-free rate."
    )

    # Receive stock, put, call, strike, expiration, dividend yield, 
    # and risk-free rate values from user
    s = float(input("S: "))
    p = float(input("P: "))
    c = float(input("C: "))
    k = float(input("K: "))
    t = float(input("T: "))
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

    arbitrage.Arbitrage.put_call_parity(s_disc, p, c, k_disc, min_diff)




if __name__ == "__main__":
    main()
