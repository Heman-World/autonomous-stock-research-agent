from typing import Any


import logging
from config import DEFAULT_TICKER
from data_collector import get_stock_data
from analyzer import analyze_stock
from report_generator import generate_report
from fundamental_analyzer import get_fundamentals

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    results = run_analysis(DEFAULT_TICKER)
    if results is None:
        logging.error("Application stopped")

def run_analysis(ticker):
    df = get_stock_data(ticker)
    if df is None:
        logging.error("Application stopped")
        return
    logging.info(f"Downloaded data for {ticker}")
    results = analyze_stock(df)
    logging.info(f"Analyzed stock data for {ticker}")
    generate_report(ticker, results)
    logging.info(f"Generated report for {ticker}")
    fundamental_result = get_fundamentals(ticker)
    combined_result = {**results,**fundamental_result}
    return combined_result

if __name__ == "__main__":
    main()

