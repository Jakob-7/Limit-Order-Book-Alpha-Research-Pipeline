from book.events import Event
from features.flow import (
    trade_imbalance,
    trade_intensity,
    cancel_pressure,
)


def test_trade_imbalance_buy_dominant():
    events = [
        Event(1, "trade", "ask", 101, 3),
        Event(2, "trade", "ask", 101, 2),
        Event(3, "trade", "bid", 100, 1),
    ]
    assert trade_imbalance(events) == (5 - 1) / 6


def test_trade_imbalance_empty():
    assert trade_imbalance([]) == 0.0


def test_trade_intensity():
    events = [
        Event(1, "trade", "ask", 101, 3),
        Event(2, "add", "bid", 100, 5),
        Event(3, "trade", "bid", 100, 2),
    ]
    assert trade_intensity(events) == 5


def test_cancel_pressure_bid_dominant():
    events = [
        Event(1, "cancel", "bid", 100, 4),
        Event(2, "cancel", "ask", 101, 1),
    ]
    assert cancel_pressure(events) == (4 - 1) / 5


def test_cancel_pressure_empty():
    assert cancel_pressure([]) == 0.0
