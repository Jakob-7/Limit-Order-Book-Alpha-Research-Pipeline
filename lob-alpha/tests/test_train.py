import numpy as np
from book.events import Event
from backtest.train import run_experiment


def test_training_pipeline_runs():
    snapshots = [
        ([(100, 5)], [(101, 5)]),
        ([(100, 4)], [(101, 6)]),
        ([(100, 6)], [(101, 4)]),
        ([(100, 3)], [(101, 7)]),
    ]

    event_windows = [
        [Event(1, "trade", "ask", 101, 1)],
        [Event(2, "trade", "bid", 100, 1)],
        [Event(3, "trade", "ask", 101, 2)],
        [Event(4, "trade", "bid", 100, 2)],
    ]

    midprices = [100.5, 100.4, 100.6, 100.3]

    model = run_experiment(snapshots, event_windows, midprices)
    assert model is not None
