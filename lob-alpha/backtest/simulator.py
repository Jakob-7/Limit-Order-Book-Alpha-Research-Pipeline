import numpy as np
from typing import List

from backtest.costs import transaction_cost


def simulate_pnl(
    midprices: List[float],
    probs: np.ndarray,
    threshold: float = 0.51,
):
    """
    Simple PnL simulator.

    - Long if P(up) > threshold
    - Short if P(up) < 1 - threshold
    - Flat otherwise
    """
    pnl = []
    costs = transaction_cost()

    for t in range(len(probs) - 1):
        if probs[t] > threshold:
            ret = midprices[t + 1] - midprices[t]
            pnl.append(ret - costs)

        elif probs[t] < 1 - threshold:
            ret = midprices[t] - midprices[t + 1]
            pnl.append(ret - costs)

        else:
            pnl.append(0.0)

    return np.array(pnl)


def sharpe_ratio(pnl: np.ndarray) -> float:
    if pnl.std() == 0:
        return 0.0
    return pnl.mean() / pnl.std()
