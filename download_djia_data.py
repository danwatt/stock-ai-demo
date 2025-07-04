"""
Market Indices Historical Data Downloader

This script downloads historical closing price data for the Dow Jones Industrial Average (DJIA)
and S&P 500 from January 2000 to the present day and saves them to CSV files in the format 'date,closing_price'.

Requirements:
- yfinance
- pandas

Usage:
    python download_djia_data.py

Output:
    Creates files 'djia_closing_prices.csv' and 'sp500_closing_prices.csv' in the current directory
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Set date range (from January 1, 2000 to today)
end_date = datetime.now()
start_date = datetime(2000, 1, 1)  # January 1, 2000

# Format dates as strings for yfinance
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

print(f"Downloading market data from {start_date_str} to {end_date_str}...")

# Download DJIA data using the ticker symbol ^DJI
print("Downloading DJIA data...")
djia_data = yf.download('^DJI', start=start_date_str, end=end_date_str, auto_adjust=True)

# Extract the closing prices
djia_closing_data = djia_data['Close'].reset_index()
djia_closing_data.columns = ['date', 'closing']

# Format the date as string
djia_closing_data['date'] = djia_closing_data['date'].dt.strftime('%Y-%m-%d')

# Save to CSV with the required format
djia_output_file = 'djia_closing_prices.csv'
djia_closing_data.to_csv(djia_output_file, header=True, index=False)

print(f"DJIA data successfully saved to {djia_output_file}")
print(f"Total DJIA records: {len(djia_closing_data)}")

# Download S&P 500 data using the ticker symbol ^GSPC
print("\nDownloading S&P 500 data...")
sp500_data = yf.download('^GSPC', start=start_date_str, end=end_date_str, auto_adjust=True)

# Extract the closing prices
sp500_closing_data = sp500_data['Close'].reset_index()
sp500_closing_data.columns = ['date', 'closing']

# Format the date as string
sp500_closing_data['date'] = sp500_closing_data['date'].dt.strftime('%Y-%m-%d')

# Save to CSV with the required format
sp500_output_file = 'sp500_closing_prices.csv'
sp500_closing_data.to_csv(sp500_output_file, header=True, index=False)

print(f"S&P 500 data successfully saved to {sp500_output_file}")
print(f"Total S&P 500 records: {len(sp500_closing_data)}")
