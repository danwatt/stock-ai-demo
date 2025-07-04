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

# Download VV (Vanguard Large-Cap ETF) data
print("\nDownloading VV data...")
vv_data = yf.download('VV', start=start_date_str, end=end_date_str, auto_adjust=True)

# Extract the closing prices
vv_closing_data = vv_data['Close'].reset_index()
vv_closing_data.columns = ['date', 'closing']

# Format the date as string
vv_closing_data['date'] = vv_closing_data['date'].dt.strftime('%Y-%m-%d')

# Save to CSV with the required format
vv_output_file = 'vv_closing_prices.csv'
vv_closing_data.to_csv(vv_output_file, header=True, index=False)

print(f"VV data successfully saved to {vv_output_file}")
print(f"Total VV records: {len(vv_closing_data)}")

# Download VTSAX (Vanguard Total Stock Market Index Fund) data
print("\nDownloading VTSAX data...")
vtsax_data = yf.download('VTSAX', start=start_date_str, end=end_date_str, auto_adjust=True)

# Extract the closing prices
vtsax_closing_data = vtsax_data['Close'].reset_index()
vtsax_closing_data.columns = ['date', 'closing']

# Format the date as string
vtsax_closing_data['date'] = vtsax_closing_data['date'].dt.strftime('%Y-%m-%d')

# Save to CSV with the required format
vtsax_output_file = 'vtsax_closing_prices.csv'
vtsax_closing_data.to_csv(vtsax_output_file, header=True, index=False)

print(f"VTSAX data successfully saved to {vtsax_output_file}")
print(f"Total VTSAX records: {len(vtsax_closing_data)}")

# Download VFIAX (Vanguard 500 Index Fund) data
print("\nDownloading VFIAX data...")
vfiax_data = yf.download('VFIAX', start=start_date_str, end=end_date_str, auto_adjust=True)

# Extract the closing prices
vfiax_closing_data = vfiax_data['Close'].reset_index()
vfiax_closing_data.columns = ['date', 'closing']

# Format the date as string
vfiax_closing_data['date'] = vfiax_closing_data['date'].dt.strftime('%Y-%m-%d')

# Save to CSV with the required format
vfiax_output_file = 'vfiax_closing_prices.csv'
vfiax_closing_data.to_csv(vfiax_output_file, header=True, index=False)

print(f"VFIAX data successfully saved to {vfiax_output_file}")
print(f"Total VFIAX records: {len(vfiax_closing_data)}")
