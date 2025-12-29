from typing import Iterable, List, Tuple

from book.events import Event


def queue_depletion_score(
    bids: List[Tuple[float, float]],
    asks: List[Tuple[float, float]],
    events: Iterable[Event],
) -> float:
    """
    Queue depletion pressure at the best level.

    Score > 0  → ask more likely to deplete (upward pressure)
    Score < 0  → bid more likely to deplete (downward pressure)

    Formula:
        score = (buy_flow / best_ask_size) - (sell_flow / best_bid_size)

    Returns 0.0 if book is incomplete.
    """
    if not bids or not asks:
        return 0.0

    best_bid_size = bids[0][1]
    best_ask_size = asks[0][1]

    if best_bid_size <= 0 or best_ask_size <= 0:
        return 0.0

    buy_flow = 0.0
    sell_flow = 0.0

    for e in events:
        if e.event_type != "trade":
            continue

        # trade on ask = aggressive buy
        if e.side == "ask":
            buy_flow += e.size

        # trade on bid = aggressive sell
        elif e.side == "bid":
            sell_flow += e.size

    return (buy_flow / best_ask_size) - (sell_flow / best_bid_size)
