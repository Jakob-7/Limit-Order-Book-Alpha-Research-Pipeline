from dataclasses import dataclass
from typing import Literal


EventType = Literal["add", "cancel", "trade"]
Side = Literal["bid", "ask"]


@dataclass(frozen=True, slots=True)
class Event:
    timestamp: int
    event_type: EventType
    side: Side
    price: float
    size: float

    def __post_init__(self):
        if self.timestamp < 0:
            raise ValueError("timestamp must be non-negative")
        if self.event_type not in ("add", "cancel", "trade"):
            raise ValueError("invalid event_type")
        if self.side not in ("bid", "ask"):
            raise ValueError("invalid side")
        if self.price <= 0:
            raise ValueError("price must be positive")
        if self.size <= 0:
            raise ValueError("size must be positive")
