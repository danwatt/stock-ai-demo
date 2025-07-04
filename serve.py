"""
Simple HTTP Server for DJIA Visualization

This script starts a simple HTTP server to serve the HTML and CSV files,
which helps avoid CORS issues when loading the CSV file in some browsers.

Usage:
    python serve.py

Then open a browser and navigate to:
    http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
from urllib.parse import urlparse

# Define the port
PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect root to index.html
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def main():
    # Check if the CSV file exists
    if not os.path.exists('djia_closing_prices.csv'):
        print("Warning: djia_closing_prices.csv not found.")
        print("Run 'python download_djia_data.py' first to generate the data.")
        user_input = input("Do you want to continue anyway? (y/n): ")
        if user_input.lower() != 'y':
            print("Exiting. Please run 'python download_djia_data.py' first.")
            return

    # Create the server
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server")
        
        # Open the browser automatically
        webbrowser.open(f"http://localhost:{PORT}")
        
        # Keep the server running
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()