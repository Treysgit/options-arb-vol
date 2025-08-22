


class Arbitrage:
    
    # min_diff defaults to 0.15 if user doesn't provide a minimum difference
    @staticmethod
    def put_call_parity(s_disc, p, c, k_disc, min_diff): 

        # Calculate "same payoff"
        diff = Arbitrage.same_payoff(s_disc, p, c, k_disc)

        # Check for arbitrage opportunity
        if diff >= min_diff:
            print(f"Sell side: stock and put.\nShort the stock by selling now +${s_disc}, write and sell put +${p}.\n"
                  f"Buy side: call and bond.\nBuy the call -${c}, invest in the bond (PV of strike) -${k_disc}\n"
                  f"Locked in arbitrage: {s_disc} + {p} - {c} - {k_disc} = +${diff}")
            
        elif diff <= -min_diff:
            print(f"Sell side: call and bond.\nSell bond (PV of strike) +${k_disc}, write and sell call +${c}.\n"
                  f"Buy side: stock and put.\nBuy the stock -${s_disc}, buy the put -${p}\n"
                  f"Locked in arbitrage: {c} + {k_disc} - {s_disc} - {p} = +${-diff}")
        else:
            print(f"The same payoff relationship holds between the variables, leaving no put-call parity arbitrage opportunity.")

    @staticmethod
    def same_payoff(s_disc, p, c, k_disc):
        left = s_disc + p
        right = c + k_disc
        return left - right

        