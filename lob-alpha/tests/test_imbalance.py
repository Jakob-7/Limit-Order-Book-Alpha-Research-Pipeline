from features.imbalance import (
    volume_imbalance,
    depth_imbalance,
    best_level_imbalance,
)


def test_volume_imbalance_balanced():
    bids = [(100, 5)]
    asks = [(101, 5)]
    assert volume_imbalance(bids, asks) == 0.0


def test_volume_imbalance_bid_dominant():
    bids = [(100, 8)]
    asks = [(101, 2)]
    assert volume_imbalance(bids, asks) == 0.6


def test_volume_imbalance_empty():
    assert volume_imbalance([], []) == 0.0


def test_depth_imbalance_top_levels():
    bids = [(100, 5), (99, 3)]
    asks = [(101, 2), (102, 1)]
    assert depth_imbalance(bids, asks, levels=2) == (8 - 3) / (8 + 3)


def test_best_level_imbalance():
    bids = [(100, 7)]
    asks = [(101, 3)]
    assert best_level_imbalance(bids, asks) == 0.4


def test_best_level_imbalance_missing_side():
    assert best_level_imbalance([], [(101, 3)]) == 0.0
