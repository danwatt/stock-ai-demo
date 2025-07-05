# Market Indices Historical Data Downloader and Visualizer

This project provides a Python script that downloads historical closing price data for the Dow Jones Industrial Average (DJIA) and S&P 500 from January 2000 to the present day and saves them to CSV files. It also includes a web-based visualization of both indices using Chart.js.

## Features

- Downloads historical closing prices for multiple market indices using Yahoo Finance API:
  - Dow Jones Industrial Average (DJIA)
  - S&P 500
- Retrieves data from January 2000 to the present day
- Saves data in a simple CSV format: `date,closing_price` with headers
- Visualizes both indices as an interactive line chart in a web browser with different colors

## Requirements

- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`):
  - yfinance
  - pandas

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with Python:

```bash
python download_djia_data.py
```

The script will:
1. Download DJIA and S&P 500 data from January 2000 to the present day
2. Save them to files named `djia_closing_prices.csv` and `sp500_closing_prices.csv` in the current directory
3. Display the date range and number of records downloaded for each index

## Output Format

Each output CSV file contains two columns with headers:
1. date (YYYY-MM-DD)
2. closing (price in USD)

Example of DJIA data (`djia_closing_prices.csv`):
```
date,closing
2005-07-05,10371.7998046875
2005-07-06,10270.6796875
2005-07-07,10302.2900390625
...
```

Example of S&P 500 data (`sp500_closing_prices.csv`):
```
date,closing
2005-07-05,1219.4400634765625
2005-07-06,1194.9400634765625
2005-07-07,1197.8699951171875
...
```

## Visualization

To view the market indices data as an interactive chart:

### Method 1: Direct File Opening
1. Make sure you have run the script to generate both CSV files
2. Open the `index.html` file in a web browser:
   ```bash
   # On macOS
   open index.html

   # On Linux
   xdg-open index.html

   # On Windows
   start index.html
   ```

### Method 2: Using the Built-in Server (Recommended)
Some browsers restrict loading local files due to security policies (CORS issues). To avoid this:

1. Make sure you have run the script to generate both CSV files
2. Run the server script:
   ```bash
   python serve.py
   ```
3. A browser window will automatically open with the chart
4. To stop the server, press Ctrl+C in the terminal

The chart will display both DJIA and S&P 500 closing prices from January 2000 to the present day. Hover over the chart to see specific values for each date.

The project offers two visualization modes that can be toggled using navigation buttons at the top of the page:

### Absolute Prices View (Default)

This view shows the actual closing prices of both indices over time:

- Interactive line chart showing both indices with different colors:
  - DJIA in teal
  - S&P 500 in pink
- Date range selection with sliders and preset ranges:
  - Select specific time periods to zoom in on the data
  - Dual sliders for setting both start and end dates
  - Preset range buttons for common time periods (1 week, 1 month, YTD, 1 year)
  - Reset button to return to the full view from January 2000 to present
- Presidential term indicators:
  - Background color zones showing the terms of the past 5 presidents
  - Color-coded legend with president names and term dates
  - Visual context for market performance during different administrations
- Tooltips showing exact values when hovering
- Legend to distinguish between the indices
- Responsive design that works on different screen sizes
- Automatic scaling of the y-axis to show the data clearly

### Presidential Comparison View

This view normalizes the S&P 500 performance to allow direct comparison between presidential terms:

- Interactive line chart showing S&P 500 performance during each presidential term:
  - Each line represents a different presidential administration
  - All lines start at 100% (normalized to the first trading day of each term)
  - X-axis shows days from the start of each term, making it easy to compare performance at the same point in different administrations
  - Republican presidents shown in red/orange tones, Democratic presidents in blue/teal tones
- Tooltips showing:
  - Exact percentage gain/loss from the start of the term
  - The actual date and day number from the start of the term
- Legend showing each president's term with start and end dates
- Responsive design that works on different screen sizes

## Testing with Cypress

This project includes Cypress tests to validate the functionality of all three pages: index.html, funds.html, and presidential_comparison.html.

### Prerequisites

- Node.js (v14 or higher)
- npm (comes with Node.js)

### Installing Test Dependencies

1. Run the following command in the project directory to install the required dependencies:

```bash
npm install
```

2. This will install Cypress and other dependencies needed for testing.

### Running the Tests

You can run the tests in two ways:

#### Interactive Mode (with UI)

```bash
npm test
```

This will open the Cypress Test Runner where you can select which tests to run and watch them execute in real-time.

#### Headless Mode (for CI/CD)

```bash
npm run test:headless
```

This will run all tests in the terminal without opening a browser UI, which is useful for automated testing environments.

### What the Tests Validate

The Cypress tests verify:
- Each page loads successfully
- The correct page title appears
- Main headings and content are displayed
- Navigation between pages works
- Interactive elements like sliders and buttons are present
- Charts are rendered on the page

For the tests to work properly, make sure the local server is running:
```bash
python serve.py
```

## License

This project is open source and available for any use.
