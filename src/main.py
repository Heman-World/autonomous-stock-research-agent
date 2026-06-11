import logging
from data_collector import get_stock_data
from analyzer import analyze_stock
from report_generator import generate_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    ticker = "TCS.NS"
    get_stock_data(ticker)
    logging.info(f"Downloaded data for {ticker}")
    results = analyze_stock(ticker)
    logging.info(f"Analyzed stock data for {ticker}")
    generate_report(ticker, results)
    logging.info(f"Generated report for {ticker}")

if __name__ == "__main__":
    main()

