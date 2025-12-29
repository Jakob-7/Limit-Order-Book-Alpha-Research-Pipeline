from data.loader import load_dataset
from backtest.train import run_experiment


def main():
    csv_path = "/Users/jakoblutz/Documents/Jakob/Uni/Projekte/lob-alpha/data/raw/BTCUSDT_l2_sample.csv"

    snapshots, event_windows, midprices = load_dataset(csv_path)

    model, pnl = run_experiment(
        snapshots,
        event_windows,
        midprices,
        horizon=5,
    )

    print("Total PnL:", pnl.sum())
    print("Number of trades:", (pnl != 0).sum())


if __name__ == "__main__":
    main()

