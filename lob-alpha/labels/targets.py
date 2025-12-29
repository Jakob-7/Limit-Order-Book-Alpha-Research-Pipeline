from typing import List


def midprice_direction(
    midprices: List[float],
    horizon: int = 1,
    epsilon: float = 0.0,
) -> List[int]:
    """
    Compute mid-price direction labels.

    Returns:
        +1  upward move
        -1  downward move
         0  no move
    """
    labels = []

    for t in range(len(midprices)):
        if t + horizon >= len(midprices):
            labels.append(0)
            continue

        diff = midprices[t + horizon] - midprices[t]

        if diff > epsilon:
            labels.append(1)
        elif diff < -epsilon:
            labels.append(-1)
        else:
            labels.append(0)

    return labels
