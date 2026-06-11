import yfinance as yf
import logging
def get_stock_data (company):
    logging.info(f"Downloading data for {company}")
    df = yf.download(company, period="1mo")
    df.to_csv(f"data/{company}.csv", index=False)

