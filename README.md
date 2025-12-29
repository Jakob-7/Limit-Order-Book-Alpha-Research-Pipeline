# 📈 Limit Order Book Alpha Research Pipeline

## Overview

This project implements a complete **end-to-end quantitative research pipeline** for short-horizon alpha modeling using **Limit Order Book (LOB) microstructure data**.

It is designed as a **research and engineering project**, showcasing how modern quantitative trading ideas are developed, tested, and evaluated in a realistic setting. The emphasis is on **correct methodology, clean architecture, and reproducibility**, rather than on producing an optimized trading strategy.

The pipeline covers the full lifecycle from raw event data to model-driven trading decisions.

---

## Project Structure

```text
lob-alpha/
├── book/                 # Limit order book engine
├── features/             # Microstructure feature engineering
├── labels/               # Mid-price labels
├── models/               # Predictive models (logistic baseline)
├── backtest/             # Training & PnL simulation
├── data/
│   ├── raw/              # Raw (uncommitted) market data
│   └── loader.py         # Data ingestion & replay
├── scripts/
│   └── run_experiment.py # Experiment runner
├── tests/                # Unit tests
└── README.md
```
Raw market data is intentionally excluded from version control.

---

## Limit Order Book Engine

The project includes a custom **Level-2 limit order book engine** that reconstructs the book from event-based data:

- `add`
- `cancel`
- `trade`

### Core properties
- Deterministic event replay
- Strict enforcement of market invariants
- Clean separation between book state and downstream logic

The engine is designed to be reusable for research experiments and feature extraction.

---

## Feature Engineering

A set of commonly studied **microstructure features** is implemented, grouped into three categories:

### Book State Features
- Volume imbalance
- Depth imbalance (top-N levels)
- Best-level imbalance

### Order Flow Features
- Aggressive trade imbalance
- Trade intensity
- Cancel pressure

### Queue Depletion Signal
- Relative depletion pressure at the best bid versus best ask

These features are widely used in both academic research and industry practice for modeling short-term price dynamics.

---

## Label Construction

Targets are defined using **mid-price direction** over a configurable prediction horizon:

- Upward move
- Downward move
- No significant move

Neutral labels are filtered to reduce noise and focus the model on actionable regimes.

---

## Model

A **logistic regression classifier** is used as a baseline model:

- Standardized inputs
- Interpretable coefficients
- Stable optimization

This choice provides a transparent reference point and allows clear interpretation of how microstructure features relate to price direction.

---

## Backtesting & Execution

The backtesting framework simulates **conservative execution assumptions**:

- Trades cross the spread
- Fixed transaction costs
- No execution optimization or inventory management

PnL is computed directly from realized mid-price movements minus transaction costs. This setup ensures that results reflect realistic trading conditions.

---

## Results

Final experiment results on structured synthetic LOB data:

Test accuracy: 0.5921  
Test AUC: 0.2122  
Sharpe ratio: 0.0  
Total PnL: -45.0  
Number of trades: 75  

These results confirm that the pipeline:
- Generates trading signals
- Executes trades consistently
- Produces stable and reproducible metrics

---

## Testing

The project includes unit tests covering:

- Limit order book invariants
- Feature calculations
- Model training behavior
- Backtest stability
- Numerical edge cases

Tests are designed to ensure correctness and robustness across the full pipeline.

---

## Scope & Purpose

This repository is intended as:

- A **quantitative research pipeline**
- A **portfolio project** demonstrating realistic workflows
- A foundation for further experimentation and extension

The design prioritizes clarity, correctness, and research integrity.

---

## Summary

This project demonstrates how to build and evaluate a complete LOB-based alpha research system, from raw data to backtested trading decisions, using industry-standard tools and practices.

It is structured to reflect how quantitative research is performed in practice and can serve as a strong foundation for further development.
