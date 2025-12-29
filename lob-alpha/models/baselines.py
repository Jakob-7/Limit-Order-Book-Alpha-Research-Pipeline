import numpy as np
from typing import Iterable, List, Tuple

from book.events import Event
from features.imbalance import (
    volume_imbalance,
    depth_imbalance,
    best_level_imbalance,
)
from features.flow import (
    trade_imbalance,
    trade_intensity,
    cancel_pressure,
)
from features.queue import queue_depletion_score


def build_feature_vector(
    bids: List[Tuple[float, float]],
    asks: List[Tuple[float, float]],
    events: Iterable[Event],
) -> np.ndarray:
    """
    Construct a single feature vector from LOB state and order flow.
    """
    return np.array(
        [
            volume_imbalance(bids, asks),
            depth_imbalance(bids, asks),
            best_level_imbalance(bids, asks),
            trade_imbalance(events),
            trade_intensity(events),
            cancel_pressure(events),
            queue_depletion_score(bids, asks, events),
        ],
        dtype=float,
    )
