from labels.midprice import midprice
from labels.targets import midprice_direction


def test_midprice():
    bids = [(100, 5)]
    asks = [(102, 3)]

    assert midprice(bids, asks) == 101.0


def test_midprice_direction_basic():
    mids = [100.0, 101.0, 100.5]

    labels = midprice_direction(mids, horizon=1, epsilon=0.0)
    assert labels == [1, -1, 0]


def test_midprice_direction_with_epsilon():
    mids = [100.0, 100.01, 100.02]

    labels = midprice_direction(mids, horizon=1, epsilon=0.05)
    assert labels == [0, 0, 0]


def test_midprice_direction_long_horizon():
    mids = [100.0, 100.5, 101.0]

    labels = midprice_direction(mids, horizon=2)
    assert labels == [1, 0, 0]
