import discount

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

    # Discount stock at expiration to present value - i.e. the value of not being the holder during the dividend period
    s_disc = discount.Discount.principal_discount(s, q, t)

    # Discount strike at expiration to present value - i.e. the value that can grow to the full amount at expiration via risk-free rate instrument
    k_disc = discount.Discount.principal_discount(k, r, t)

    parity_params = {s_disc, p, c, k_disc}


if __name__ == "__main__":
    main()
