def transaction_cost(
    half_spread: float = 0.5,
    fee: float = 0.1,
) -> float:
    """
    Fixed transaction cost per trade.
    """
    return half_spread + fee
