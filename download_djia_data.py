"""
Market Indices Historical Data Downloader

This script downloads historical closing price data for the Dow Jones Industrial Average (DJIA),
S&P 500, VV (Vanguard Large-Cap ETF), VTSAX (Vanguard Total Stock Market Index Fund),
and VFIAX (Vanguard 500 Index Fund) from January 2000 to the present day and saves them to CSV files
in the format 'date,closing_price'.

Requirements:
- yfinance
- pandas

Usage:
    python download_djia_data.py

Output:
    Creates files 'djia_closing_prices.csv', 'sp500_closing_prices.csv', 'vv_closing_prices.csv',
    'vtsax_closing_prices.csv', and 'vfiax_closing_prices.csv' in the current directory
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def download_ticker_data(ticker, ticker_name, start_date_str, end_date_str):
    """
    Download historical closing price data for a given ticker symbol and save to CSV.

    Args:
        ticker (str): The ticker symbol to download data for
        ticker_name (str): A user-friendly name for the ticker
        start_date_str (str): Start date in YYYY-MM-DD format
        end_date_str (str): End date in YYYY-MM-DD format

    Returns:
        None
    """
    # Generate the output filename
    output_file = f"{ticker_name.lower().replace(' ', '_')}_closing_prices.csv"

    # Download data
    print(f"\nDownloading {ticker_name} data...")
    data = yf.download(ticker, start=start_date_str, end=end_date_str, auto_adjust=True)

    # Extract the closing prices
    closing_data = data['Close'].reset_index()
    closing_data.columns = ['date', 'closing']

    # Format the date as string
    closing_data['date'] = closing_data['date'].dt.strftime('%Y-%m-%d')

    # Round closing prices to 4 decimal places
    closing_data['closing'] = closing_data['closing'].round(4)

    # Save to CSV with the required format
    closing_data.to_csv(output_file, header=True, index=False)

    print(f"{ticker_name} data successfully saved to {output_file}")
    print(f"Total {ticker_name} records: {len(closing_data)}")

    return closing_data


# Set date range (from January 1, 2000 to today)
end_date = datetime.now()
start_date = datetime(2000, 1, 1)  # January 1, 2000

# Format dates as strings for yfinance
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

print(f"Downloading market data from {start_date_str} to {end_date_str}...")

# Define the tickers to download
tickers = [
    ('^DJI', 'DJIA'),
    ('^GSPC', 'sp500'),
    ('VV', 'VV'),
    ('VTSAX', 'VTSAX'),
    ('VFIAX', 'VFIAX')
]

# Download data for each ticker
for ticker, name in tickers:
    download_ticker_data(ticker, name, start_date_str, end_date_str)
