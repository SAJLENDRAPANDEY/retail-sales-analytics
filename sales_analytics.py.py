"""
Sales Analytics Pipeline
========================
End-to-end retail sales analysis covering data ingestion, cleaning,
feature engineering, KPI reporting, and visualization.

Author  : <Your Name>
Date    : 2024
Dataset : Retail Sales (products · customers · stores · calendar)
"""

# ─────────────────────────────────────────────
# 0. IMPORTS
# ─────────────────────────────────────────────
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ─────────────────────────────────────────────
# 1. DATA LOADING
# ─────────────────────────────────────────────
DATA_DIR = r"C:\Data analytics project"

def load_data(data_dir: str) -> dict[str, pd.DataFrame]:
    """Load all source tables and return them in a dictionary."""
    files = {
        "sales"   : "reduced_sales_data.xlsx",
        "customer": "cutomer data.xlsx",
        "product" : "product data.xlsx",
        "store"   : "store data.xlsx",
        "calendar": "calendar.xlsx",
    }

    start = time.time()
    tables = {name: pd.read_excel(f"{data_dir}\\{file}") for name, file in files.items()}
    print(f"[INFO] All tables loaded in {time.time() - start:.2f}s")
    return tables


# ─────────────────────────────────────────────
# 2. DATA MERGING
# ─────────────────────────────────────────────
def merge_tables(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Join all dimension tables onto the sales fact table.

    Joins
    -----
    sales  ← product  on product_id
    sales  ← customer on customer_id
    sales  ← store    on store_id
    sales  ← calendar on order_date = date
    """
    df = (
        tables["sales"]
        .merge(tables["product"],  on="product_id",  how="left")
        .merge(tables["customer"], on="customer_id", how="left")
        .merge(tables["store"],    on="store_id",    how="left")
        .merge(tables["calendar"], left_on="order_date", right_on="date", how="left")
    )
    return df


# ─────────────────────────────────────────────
# 3. DATA CLEANING
# ─────────────────────────────────────────────
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and drop artefact columns."""
    df = df.drop_duplicates()
    artefact_cols = ["Unnamed: 5", "Unnamed: 6", "Unnamed: 7"]
    df = df.drop(columns=artefact_cols, errors="ignore")
    print(f"[INFO] Clean shape: {df.shape}")
    return df


# ─────────────────────────────────────────────
# 4. FEATURE ENGINEERING
# ─────────────────────────────────────────────
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Derive analytical columns.

    New columns
    -----------
    profit_flag    : 'profit' if profit > 0 else 'loss'
    profit_margin  : (profit / revenue) × 100  — 0 when revenue is zero
    month          : integer month extracted from order_date
    """
    df = df.copy()
    df["profit_flag"]   = np.where(df["profit"] > 0, "profit", "loss")
    df["profit_margin"] = np.where(
        df["revenue"] != 0,
        df["profit"] / df["revenue"] * 100,
        0,
    )
    df["month"] = pd.to_datetime(df["order_date"]).dt.month
    return df


# ─────────────────────────────────────────────
# 5. KPI SUMMARY
# ─────────────────────────────────────────────
def print_kpi_summary(df: pd.DataFrame) -> None:
    """Print high-level business KPIs to the console."""
    separator = "=" * 45

    print(f"\n{separator}")
    print("  KEY PERFORMANCE INDICATORS")
    print(separator)
    print(f"  Total Revenue          : ₹{df['revenue'].sum():>15,.2f}")
    print(f"  Total Profit           : ₹{df['profit'].sum():>15,.2f}")
    print(f"  Avg Profit per Order   : ₹{df['profit'].mean():>15,.2f}")
    print(f"  Avg Profit Margin      :  {df['profit_margin'].mean():>14.2f}%")
    print(f"  Unique Countries       :  {df['country'].nunique():>14}")
    print(f"  Loss-making Products   :  {(df['profit'] < 0).sum():>14}")
    print(separator)

    print("\n--- Top 5 Countries by Revenue ---")
    top_countries = (
        df.groupby("country")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    print(top_countries.to_string())

    print("\n--- Top 5 Products by Profit Margin ---")
    top_products = (
        df.groupby("product_name", as_index=False)
        .agg(total_profit=("profit", "sum"), total_revenue=("revenue", "sum"))
        .assign(profit_margin=lambda x: x["total_profit"] / x["total_revenue"] * 100)
        .sort_values("profit_margin", ascending=False)
        .head(5)[["product_name", "total_revenue", "total_profit", "profit_margin"]]
    )
    print(top_products.to_string(index=False))

    print("\n--- Store Performance Ranking (by Profit) ---")
    store_rank = (
        df.groupby("store_id")["profit"]
        .sum()
        .rank(ascending=False)
        .sort_values()
    )
    print(store_rank.head(5).to_string())

    print("\n--- Top Brand by Quantity Sold ---")
    print(f"  {df.groupby('brand')['quantity'].sum().idxmax()}")

    print("\n--- Highest Profit Country ---")
    print(f"  {df.groupby('country')['profit'].sum().idxmax()}")


# ─────────────────────────────────────────────
# 6. VISUALIZATIONS
# ─────────────────────────────────────────────
def plot_all(df: pd.DataFrame) -> None:
    """Generate and display all analytical charts."""
    sns.set_theme(style="whitegrid", palette="muted")

    # 6.1 Country-wise Revenue (bar)
    fig, ax = plt.subplots(figsize=(10, 5))
    country_rev = df.groupby("country")["revenue"].sum().sort_values(ascending=False)
    country_rev.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Revenue by Country", fontsize=14, fontweight="bold")
    ax.set_xlabel("Country")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # 6.2 Monthly Revenue Trend (line)
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("month")["revenue"].sum().plot(kind="line", marker="o", ax=ax, color="darkorange")
    ax.set_title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    plt.tight_layout()
    plt.show()

    # 6.3 Monthly Profit Trend (line)
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("month")["profit"].sum().plot(kind="line", marker="o", ax=ax, color="seagreen")
    ax.set_title("Monthly Profit Trend", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Profit")
    plt.tight_layout()
    plt.show()

    # 6.4 Category-wise Profit (bar)
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("category")["profit"].sum().sort_values().plot(kind="bar", ax=ax, color="mediumpurple")
    ax.set_title("Profit by Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Category")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # 6.5 Top 5 Products by Revenue (bar)
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("product_name")["revenue"].sum().nlargest(5).plot(kind="bar", ax=ax, color="tomato")
    ax.set_title("Top 5 Products by Revenue", fontsize=14, fontweight="bold")
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

    # 6.6 Store-type Revenue (bar)
    fig, ax = plt.subplots(figsize=(8, 5))
    df.groupby("store_type")["revenue"].sum().sort_values(ascending=False).plot(
        kind="bar", ax=ax, color="cadetblue"
    )
    ax.set_title("Revenue by Store Type", fontsize=14, fontweight="bold")
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # 6.7 Discount vs Profit (scatter)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x="discount", y="profit", data=df, alpha=0.5, ax=ax, color="coral")
    ax.set_title("Discount vs Profit", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # 6.8 Revenue vs Profit (scatter)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x="revenue", y="profit", data=df, alpha=0.4, ax=ax, color="dodgerblue")
    ax.set_title("Revenue vs Profit", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # 6.9 Discount vs Profit (box plot)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxenplot(x="discount", y="profit", data=df, ax=ax)
    ax.set_title("Profit Distribution across Discount Levels", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────
# 7. MAIN ENTRYPOINT
# ─────────────────────────────────────────────
def main():
    # Load
    tables = load_data(DATA_DIR)

    # Build master DataFrame
    df = merge_tables(tables)
    df = clean_data(df)
    df = engineer_features(df)

    # Insights
    print_kpi_summary(df)

    # Visualise
    plot_all(df)


    df.to_excel("final_output_new.xlsx", index=False)
    print("[INFO] Output saved to final_output.xlsx")


if __name__ == "__main__":
    main()

