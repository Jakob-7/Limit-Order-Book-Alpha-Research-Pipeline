from book.events import Event
from features.queue import queue_depletion_score


def test_queue_depletion_upward_pressure():
    bids = [(100, 10)]
    asks = [(101, 2)]

    events = [
        Event(1, "trade", "ask", 101, 1),
        Event(2, "trade", "ask", 101, 1),
    ]

    score = queue_depletion_score(bids, asks, events)
    assert score > 0


def test_queue_depletion_downward_pressure():
    bids = [(100, 2)]
    asks = [(101, 10)]

    events = [
        Event(1, "trade", "bid", 100, 1),
        Event(2, "trade", "bid", 100, 1),
    ]

    score = queue_depletion_score(bids, asks, events)
    assert score < 0


def test_queue_depletion_empty_book():
    assert queue_depletion_score([], [], []) == 0.0


def test_queue_depletion_no_trades():
    bids = [(100, 5)]
    asks = [(101, 5)]

    assert queue_depletion_score(bids, asks, []) == 0.0
