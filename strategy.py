


class Strategy:

    @staticmethod
    def long_straddle(c, p, t, k):

        premiums = c + p 
        print(f"You need to make a net profit of +${premiums} from either option to break even.")

        s_predict = float(input(f"Enter the stock price prediction at T (years) = {t} : "))
        call_payoff = max(s_predict - k, 0) # Call option wouldn't be exercised if s - k wasn't positive
        put_payoff = max(k - s_predict, 0) # Put option wouldn't be exercise if k - s wasn't postive

        pnl = (call_payoff + put_payoff) - premiums

        if(pnl > 0):
            print(f"If the stock moves to ${s_predict}, your pnl will be +${pnl:.2f}")
        else:
            print(f"If the stock moves to ${s_predict}, your pnl will be -${-pnl:.2f}")


        

