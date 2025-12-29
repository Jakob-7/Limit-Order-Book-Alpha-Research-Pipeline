from typing import List, Tuple


def volume_imbalance(
    bids: List[Tuple[float, float]],
    asks: List[Tuple[float, float]],
) -> float:
    """
    Compute volume imbalance between bid and ask sides.

    Imbalance = (V_bid - V_ask) / (V_bid + V_ask)

    Returns 0.0 if both sides are empty.
    """
    bid_volume = sum(size for _, size in bids)
    ask_volume = sum(size for _, size in asks)

    total = bid_volume + ask_volume
    if total == 0:
        return 0.0

    return (bid_volume - ask_volume) / total


def depth_imbalance(
    bids: List[Tuple[float, float]],
    asks: List[Tuple[float, float]],
    levels: int = 5,
) -> float:
    """
    Compute depth imbalance using only top-N price levels.
    """
    bid_depth = sum(size for _, size in bids[:levels])
    ask_depth = sum(size for _, size in asks[:levels])

    total = bid_depth + ask_depth
    if total == 0:
        return 0.0

    return (bid_depth - ask_depth) / total


def best_level_imbalance(
    bids: List[Tuple[float, float]],
    asks: List[Tuple[float, float]],
) -> float:
    """
    Imbalance at the best bid / ask only.
    """
    if not bids or not asks:
        return 0.0

    bid_size = bids[0][1]
    ask_size = asks[0][1]

    total = bid_size + ask_size
    if total == 0:
        return 0.0

    return (bid_size - ask_size) / total
