from data_collector import get_stock_data
from analyzer import analyze_stock
from report_generator import generate_report

def main():
    ticker = "TCS.NS"
    get_stock_data(ticker)
    results = analyze_stock(ticker)
    print("Analyzed stock data")
    generate_report(ticker, results)
    print("Generated report")

if __name__ == "__main__":
    main()

