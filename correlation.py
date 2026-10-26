import pandas as pd

#Load your CSV files
files = [
    "prices_round_1_day_-2.csv", 
    "prices_round_1_day_-1.csv", 
    "prices_round_1_day_0.csv"
]

dfs = [pd.read_csv(f, sep=";") for f in files]

df = pd.concat(dfs, ignore_index=True)

df['unique_time'] = df['day'].astype(str) + "_" + df['timestamp'].astype(str)

pivot_df = df.pivot(index='unique_time', columns='product', values='mid_price')

price_corr = pivot_df['ASH_COATED_OSMIUM'].corr(pivot_df['INTARIAN_PEPPER_ROOT'])

print(f"Absolute Price Correlation: {price_corr:.4f}")

returns_df = pivot_df.diff().dropna()

returns_corr = returns_df['ASH_COATED_OSMIUM'].corr(returns_df['INTARIAN_PEPPER_ROOT'])

print(f"Tick-to-Tick Returns Correlation: {returns_corr:.4f}")