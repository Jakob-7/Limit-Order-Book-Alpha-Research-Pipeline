import numpy as np
from backtest.simulator import simulate_pnl, sharpe_ratio


def test_simulate_pnl_runs():
    midprices = [100, 101, 100, 102]
    probs = np.array([0.6, 0.4, 0.7, 0.5])

    pnl = simulate_pnl(midprices, probs)
    assert len(pnl) == len(probs) - 1


def test_sharpe_ratio():
    pnl = np.array([1.0, -0.5, 1.5, -0.2])
    s = sharpe_ratio(pnl)
    assert isinstance(s, float)
