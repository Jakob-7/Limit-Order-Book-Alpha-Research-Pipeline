import csv
from collections import deque
from typing import Deque, Iterable, List, Tuple

from book.events import Event
from book.order_book import LimitOrderBook


def load_events_from_csv(
    path: str,
) -> List[Event]:
    """
    Load LOB events from a CSV file.

    Expected columns:
        timestamp,event_type,side,price,size
    """
    events: List[Event] = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            events.append(
                Event(
                    timestamp=int(row["timestamp"]),
                    event_type=row["event_type"],
                    side=row["side"],
                    price=float(row["price"]),
                    size=float(row["size"]),
                )
            )

    return events


def build_lob_samples(
    events: List[Event],
    depth: int = 10,
    window_size: int = 50,
) -> Tuple[
    List[Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]],
    List[List[Event]],
    List[float],
]:
    """
    Replay events through a limit order book and build samples.

    Returns:
        snapshots      : [(bids, asks), ...]
        event_windows  : [[Event, ...], ...]
        midprices      : [float, ...]
    """
    lob = LimitOrderBook()

    snapshots = []
    midprices = []
    event_windows: List[List[Event]] = []

    window: Deque[Event] = deque(maxlen=window_size)

    for e in events:
        try:
            lob.process_event(e)
        except RuntimeError:
            # skip events that would cause crossed book
            continue

        window.append(e)


        # skip until book is populated
        try:
            bids, asks = lob.snapshot(depth=depth)
            mid = lob.midprice()
        except Exception:
            continue

        snapshots.append((bids, asks))
        event_windows.append(list(window))
        midprices.append(mid)

    return snapshots, event_windows, midprices


def load_dataset(
    csv_path: str,
    depth: int = 10,
    window_size: int = 50,
):
    """
    High-level convenience function.
    """
    events = load_events_from_csv(csv_path)
    return build_lob_samples(
        events,
        depth=depth,
        window_size=window_size,
    )
