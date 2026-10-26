# Prosperity 2026 — Cross-Product Correlation Analysis

Analysis script from my IMC Prosperity 2026 Round 1 prep.

Measures the relationship between ASH_COATED_OSMIUM and INTARIAN_PEPPER_ROOT using round-1 order-book snapshots.

## What it computes
1. Absolute price correlation (Pearson on mid-prices)
2. Tick-to-tick return correlation (Pearson)

## Requirements
pip install pandas

## Data
No data is included. The price CSVs were distributed by IMC Prosperity and cannot be redistributed. Place them in this folder and run: python correlation.py

## License
MIT