import numpy as np
from typing import Iterable, List, Tuple

from book.events import Event
from labels.targets import midprice_direction
from models.baselines import build_feature_vector
from models.logistic import LogisticLOBClassifier
from backtest.simulator import simulate_pnl, sharpe_ratio

from sklearn.metrics import accuracy_score, roc_auc_score


def build_dataset(
    snapshots: List[Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]],
    event_windows: List[Iterable[Event]],
    midprices: List[float],
    horizon: int = 1,
    epsilon: float = 0.0,
):
    """
    Build feature matrix X and label vector y.
    Neutral labels (0) are removed.
    """
    X = []
    y = midprice_direction(midprices, horizon=horizon, epsilon=epsilon)

    for (bids, asks), events in zip(snapshots, event_windows):
        X.append(build_feature_vector(bids, asks, events))

    X = np.asarray(X)
    y = np.asarray(y)

    mask = y != 0
    return X[mask], y[mask]


def train_test_split_time(
    X: np.ndarray,
    y: np.ndarray,
    test_frac: float = 0.3,
):
    """
    Chronological (time-based) train/test split.
    """
    split = int(len(X) * (1 - test_frac))
    return X[:split], X[split:], y[:split], y[split:]


def run_experiment(
    snapshots,
    event_windows,
    midprices,
    horizon: int = 1,
    epsilon: float = 0.0,
):
    """
    Full end-to-end experiment:
    - build features
    - build labels
    - train logistic regression
    - evaluate accuracy & AUC
    - simulate PnL with costs
    """
    X, y = build_dataset(
        snapshots,
        event_windows,
        midprices,
        horizon=horizon,
        epsilon=epsilon,
    )

    X_train, X_test, y_train, y_test = train_test_split_time(X, y)

    model = LogisticLOBClassifier()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)

    acc = accuracy_score(y_test, preds)
    auc = roc_auc_score(y_test, probs)

    print("Test accuracy:", round(acc, 4))
    print("Test AUC:", round(auc, 4))

    # --- PnL backtest ---
    test_midprices = midprices[-len(probs) - 1 :]
    pnl = simulate_pnl(test_midprices, probs)
    sharpe = sharpe_ratio(pnl)

    print("Sharpe ratio:", round(sharpe, 4))

    return model, pnl
