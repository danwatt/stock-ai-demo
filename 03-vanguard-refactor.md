# Vanguard Funds Integration & Code Refactoring

## Overview

In this session, we enhanced the DJIA visualization project in two significant ways:

1. Added support for tracking and visualizing three Vanguard funds:
   - VV (Vanguard Large-Cap ETF)
   - VTSAX (Vanguard Total Stock Market Index Fund)
   - VFIAX (Vanguard 500 Index Fund)

2. Refactored the data download script to remove code duplication

## Implementation Steps

### 1. Updated the Download Script to Include Vanguard Funds

First, we modified the `download_djia_data.py` script to download historical data for the three Vanguard funds in addition to the existing DJIA and S&P 500 indices.

The script connects to Yahoo Finance to retrieve the historical price data and saves it in CSV format for each fund.

### 2. Created a New Visualization Page

We created a new HTML page called `funds.html` specifically for visualizing the Vanguard funds. This page follows the same design pattern as the existing index.html, featuring:

- Interactive date range controls
- Presidential term overlays
- Line charts for price visualization
- Responsive design using Bootstrap

### 3. Updated Navigation

To create a cohesive user experience, we updated the navigation in all pages:
- `index.html` - Added link to the new funds page
- `presidential_comparison.html` - Added link to the new funds page
- `funds.html` - Added links to the other pages

### 4. Refactored the Download Script

After adding the Vanguard funds functionality, we observed significant code duplication in the download script. To improve maintainability, we refactored `download_djia_data.py` by:

1. Extracting a reusable function called `download_ticker_data()` that handles:
   - Downloading data for a specific ticker
   - Processing the data
   - Saving to CSV
   - Displaying progress information

2. Creating a simple list of ticker symbols and names

3. Using a loop to download data for each ticker by calling the extracted function

## Before & After Comparison

### Before: Repetitive Code

The original approach repeated the same code block for each ticker, with only minor differences in variable names and ticker symbols.

### After: DRY Implementation

The refactored code follows the "Don't Repeat Yourself" (DRY) principle, with a single function handling the download process for any ticker.

```python
def download_ticker_data(ticker, ticker_name, start_date_str, end_date_str):
    """
    Download historical closing price data for a given ticker symbol and save to CSV.
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

    # Save to CSV with the required format
    closing_data.to_csv(output_file, header=True, index=False)

    print(f"{ticker_name} data successfully saved to {output_file}")
    print(f"Total {ticker_name} records: {len(closing_data)}")

    return closing_data


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
```

## Benefits

1. **Enhanced Visualization**: Users can now analyze and compare the performance of three popular Vanguard funds alongside market indices.

2. **Improved Code Quality**: The refactored download script is more maintainable and easier to extend.

3. **Consistent User Experience**: Updated navigation provides a seamless experience across all visualization pages.

4. **Extensibility**: Adding new funds in the future will be much easier, requiring only an addition to the tickers list.