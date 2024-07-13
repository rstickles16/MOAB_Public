import StratLab as sl

def add_moab_conditions(
        bt: sl.Backtest
):

    bt.add_condition(
        name='volatility',
        ticker_1='^ndx',
        study_1='rsi',
        study_1_period=10,
        operator='>',
        value=80
    )

    bt.add_condition(
        name='long_rsi_bull',
        ticker_1='^ndx',
        study_1='rsi',
        study_1_period=10,
        operator='<',
        value=34,
    )

    bt.add_condition(
        name='short_rsi_bull',
        ticker_1='^ndx',
        study_1='rsi',
        study_1_period=2,
        operator='<',
        value=10,
    )

    bt.add_condition(
        name='long_sma_bull',
        ticker_1='^ndx',
        study_1='price',
        operator='>',
        ticker_2='^ndx',
        study_2='sma',
        study_2_period=200
    )

    bt.add_condition(
        name='short_sma_bull',
        ticker_1='^ndx',
        study_1='price',
        operator='>',
        ticker_2='^ndx',
        study_2='sma',
        study_2_period=21,
    )