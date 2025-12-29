import pytest

from book.order_book import LimitOrderBook
from book.events import Event


def test_add():
    lob = LimitOrderBook()
    lob.process_event(Event(1, "add", "bid", 100, 5))
    lob.process_event(Event(2, "add", "ask", 101, 3))

    bids, asks = lob.snapshot()
    assert bids == [(100, 5)]
    assert asks == [(101, 3)]


def test_cancel():
    lob = LimitOrderBook()
    lob.process_event(Event(1, "add", "bid", 100, 5))
    lob.process_event(Event(2, "cancel", "bid", 100, 2))

    bids, _ = lob.snapshot()
    assert bids == [(100, 3)]


def test_trade():
    lob = LimitOrderBook()
    lob.process_event(Event(1, "add", "ask", 101, 5))
    lob.process_event(Event(2, "trade", "ask", 101, 5))

    _, asks = lob.snapshot()
    assert asks == []


def test_midprice():
    lob = LimitOrderBook()
    lob.process_event(Event(1, "add", "bid", 99, 1))
    lob.process_event(Event(2, "add", "ask", 101, 1))

    assert lob.midprice() == 100


def test_crossed_book():
    lob = LimitOrderBook()
    lob.process_event(Event(1, "add", "bid", 101, 1))

    with pytest.raises(RuntimeError):
        lob.process_event(Event(2, "add", "ask", 100, 1))
