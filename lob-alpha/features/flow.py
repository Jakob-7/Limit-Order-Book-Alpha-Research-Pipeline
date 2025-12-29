from typing import Iterable

from book.events import Event


def trade_imbalance(events: Iterable[Event]) -> float:
    """
    Aggressive trade imbalance over a window of events.

    Imbalance = (buy_volume - sell_volume) / (buy_volume + sell_volume)

    - trade on ask  -> aggressive buy
    - trade on bid  -> aggressive sell
    """
    buy_vol = 0.0
    sell_vol = 0.0

    for e in events:
        if e.event_type != "trade":
            continue

        if e.side == "ask":
            buy_vol += e.size
        elif e.side == "bid":
            sell_vol += e.size

    total = buy_vol + sell_vol
    if total == 0:
        return 0.0

    return (buy_vol - sell_vol) / total


def trade_intensity(events: Iterable[Event]) -> float:
    """
    Total traded volume in the window.
    """
    return sum(e.size for e in events if e.event_type == "trade")


def cancel_pressure(events: Iterable[Event]) -> float:
    """
    Cancel pressure imbalance.

    Measures whether liquidity is being pulled more
    from bids or asks.
    """
    bid_cancel = 0.0
    ask_cancel = 0.0

    for e in events:
        if e.event_type != "cancel":
            continue

        if e.side == "bid":
            bid_cancel += e.size
        elif e.side == "ask":
            ask_cancel += e.size

    total = bid_cancel + ask_cancel
    if total == 0:
        return 0.0

    return (bid_cancel - ask_cancel) / total
