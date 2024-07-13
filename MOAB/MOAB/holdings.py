import StratLab as sl

def add_moab_holdings(
        bt: sl.Backtest
):
        
    bt.add_holding(
        conditions=['volatility'],
        flags=['True'],
        holdings_list=['uvxy']
    )

    bt.add_holding(
        conditions=['long_rsi_bull'],
        flags=['True'],
        holdings_list=['tqqq']
    )

    bt.add_holding(
        conditions = ['short_rsi_bull'],
        flags=['True'],
        holdings_list=['tqqq']
    )

    bt.add_holding(
        conditions=['long_sma_bull'],
        flags=['True'],
        holdings_list=['tqqq'],
        dca_period=2
    )

    bt.add_holding(
        conditions=['short_sma_bull'],
        flags=['True'],
        holdings_list=['tqqq']
    )

    bt.add_holding(
        conditions=['short_sma_bull'],
        flags=['False'],
        holdings_list=['sqqq']
    )