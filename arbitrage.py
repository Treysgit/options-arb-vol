


class Arbitrage:
    
    # min_diff defaults to 0.15 if user doesn't provide a minimum difference
    @staticmethod
    def put_call_parity(s_disc, p, c, k_disc, min_diff): 

        # Calculate "same payoff"
        diff = Arbitrage.same_payoff(s_disc, p, c, k_disc)

        # Check for arbitrage opportunity
        if diff >= min_diff:
            print("\n" + "_" * 40 + "\n")
            print(f"Sell side: stock and put\nShort the stock by selling now +${s_disc:.2f}, write and sell put +${p:.2f}\n"
                  f"\nBuy side: call and bond.\nBuy the call -${c:.2f}, invest in the bond (PV of strike) -${k_disc:.2f}\n"
                  f"\nLocked in arbitrage: {s_disc:.2f} + {p:.2f} - {c:.2f} - {k_disc:.2f} = +${diff:.2f}")
            
        elif diff <= -min_diff:
            print("\n" + "_" * 40 + "\n")
            print(f"Sell side: call and bond\nSell bond (PV of strike) +${k_disc:.2f}, write and sell call +${c:.2f}.\n"
                  f"\nBuy side: stock and put.\nBuy the stock -${s_disc:.2f}, buy the put -${p:.2f}\n"
                  f"\nLocked in arbitrage: {c:.2f} + {k_disc:.2f} - {s_disc:.2f} - {p:.2f} = +${-diff:.2f}")
        else:
            print("\n" + "_" * 40 + "\n")
            print(f"The same payoff relationship holds between the variables, leaving no put-call parity arbitrage opportunity.")

    @staticmethod
    def same_payoff(s_disc, p, c, k_disc):
        left = s_disc + p
        right = c + k_disc
        return left - right

        