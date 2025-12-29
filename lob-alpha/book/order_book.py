from collections import defaultdict
from typing import Dict, List, Tuple

from book.events import Event


class LimitOrderBook:
    def __init__(self):
        self.bids: Dict[float, float] = defaultdict(float)
        self.asks: Dict[float, float] = defaultdict(float)

    def process_event(self, event: Event) -> None:
        book = self._select_book(event.side)

        if event.event_type == "add":
            book[event.price] += event.size

        elif event.event_type == "cancel":
            self._cancel(book, event.price, event.size)

        elif event.event_type == "trade":
            self._trade(book, event.price, event.size)

        else:
            raise ValueError("unknown event type")

        self._cleanup(book)
        self._check_invariants()

    def snapshot(
        self, depth: int = 10
    ) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        bids = sorted(self.bids.items(), key=lambda x: -x[0])[:depth]
        asks = sorted(self.asks.items(), key=lambda x: x[0])[:depth]
        return bids, asks

    def midprice(self) -> float:
        if not self.bids or not self.asks:
            raise ValueError("empty book")
        return 0.5 * (max(self.bids) + min(self.asks))

    # -------- internals --------

    def _select_book(self, side: str) -> Dict[float, float]:
        if side == "bid":
            return self.bids
        if side == "ask":
            return self.asks
        raise ValueError("invalid side")

    def _cancel(self, book: Dict[float, float], price: float, size: float) -> None:
        if price not in book:
            return
        book[price] = max(0.0, book[price] - size)

    def _trade(self, book: Dict[float, float], price: float, size: float) -> None:
        if price not in book:
            return
        book[price] = max(0.0, book[price] - size)

    def _cleanup(self, book: Dict[float, float]) -> None:
        for p in list(book.keys()):
            if book[p] <= 0:
                del book[p]

    def _check_invariants(self) -> None:
        if self.bids and self.asks:
            if max(self.bids) >= min(self.asks):
                raise RuntimeError("crossed book")
