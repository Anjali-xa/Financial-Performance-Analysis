"""Financial Performance Analysis

Reproducible starter analysis for data/dataset.csv.
Current repository data is synthetic demo data; do not interpret findings as real-world facts.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "dataset.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}")
    df = pd.read_csv(DATA)
    print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")
    print("\nMissing values:\n", df.isna().sum())
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print("\nData types:\n", df.dtypes)

    # Validate the expected starter schema before analysis.
    required = [c.strip() for c in "month, business_unit, revenue, expenses, budget_revenue".split(",")]
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Expected columns are missing: {missing}")

    df["month"] = pd.to_datetime(df["month"], errors="coerce")
    for c in ["revenue", "expenses", "budget_revenue"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["profit"] = df["revenue"] - df["expenses"]
    df["profit_margin_pct"] = df["profit"].div(df["revenue"].replace(0, pd.NA)).mul(100)
    df["budget_variance"] = df["revenue"] - df["budget_revenue"]
    summary = df.groupby("business_unit")["profit"].sum().sort_values(ascending=False)
    trend = df.groupby(df["month"].dt.to_period("M"))["revenue"].sum()
    ylabel = "Profit"

    summary.to_csv(OUT / "segment_summary.csv", header=["value"])
    fig, ax = plt.subplots(figsize=(10, 5))
    summary.plot(kind="bar", ax=ax, title="Financial Performance Analysis: segment summary")
    ax.set_ylabel(ylabel)
    ax.set_xlabel("")
    fig.tight_layout()
    fig.savefig(OUT / "segment_summary.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    trend.plot(ax=ax, marker="o", title="Financial Performance Analysis: trend")
    ax.set_ylabel("Revenue")
    ax.set_xlabel("Period / segment")
    fig.tight_layout()
    fig.savefig(OUT / "trend.png", dpi=160)
    plt.close(fig)

    print("\nSegment summary:\n", summary)
    print(f"\nOutputs saved to: {OUT}")


if __name__ == "__main__":
    main()
