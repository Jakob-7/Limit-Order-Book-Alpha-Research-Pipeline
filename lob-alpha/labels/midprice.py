from typing import List, Tuple


def midprice(bids: List[Tuple[float, float]], asks: List[Tuple[float, float]]) -> float:
    """
    Compute mid-price from best bid and ask.
    """
    if not bids or not asks:
        raise ValueError("Cannot compute midprice with empty book")

    return 0.5 * (bids[0][0] + asks[0][0])
