import StratLab as sl
from . import conditions
from . import holdings


bt = sl.Backtest(to_excel=True)
conditions.add_moab_conditions(bt)
holdings.add_moab_holdings(bt)
bt.run()